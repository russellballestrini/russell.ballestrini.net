Integrating OpenAI with Dry's Sample Chat Game
################################################################

:author: Russell Ballestrini
:slug: integrating-openai-with-dry-sample-chat-game
:date: 2024-02-17 14:11
:tags: C++, OpenAI, Dry, Chatbot
:status: published

This tutorial demonstrates enhancing `Dry's Sample Chat Game <https://gitlab.com/luckeyproductions/dry/-/blob/master/Source/Samples/16_Chat/Chat.cpp>`_ by integrating OpenAI's language models, enabling the game to provide intelligent, AI-driven responses to user queries. Dry, the successor to Urho3D, offers a comprehensive framework for developing 2D and 3D games. Leveraging LLMs within the Dry engine opens up new possibilities.

Background
----------

The Sample Chat game in Dry provides basic messaging functionality where multiple copies of the game client can connect to a server to communicate via text messages. Our aim is to extend this functionality to include responses from OpenAI's language models when messages contain specific triggers, such as "gpt-3".

Prerequisites
-------------

Ensure you have the following before starting:

- An OpenAI API key.
- A `configured Dry build environment <https://russell.ballestrini.net/building-dry-and-park-from-source-on-fedora-linux/>`_.
- Some familiarity with build tooling or at least the ability to copy and paste commands into the terminal.

Step-by-Step Integration
------------------------

Follow these steps to integrate OpenAI with the Sample Chat game:

1. **Obtain the OpenAI C++ Client**

   Before modifying the chat game, you need to download the necessary files from the OpenAI C++ client repository. Use the following commands to create a directory for these files and download them:

   .. code-block:: bash

       cd ~/git/dry
       mkdir -p Source/ThirdParty/openai
       mkdir -p Source/ThirdParty/openai/nlohmann
       cd Source/ThirdParty/openai
       wget https://raw.githubusercontent.com/olrea/openai-cpp/main/include/openai/openai.hpp
       cd nlohmann
       wget https://raw.githubusercontent.com/olrea/openai-cpp/main/include/openai/nlohmann/json.hpp

   I also found the need to modify the client to code slightly for the JSON import, pardon me if this is ignorant:

   .. code-block:: cpp

      // #include <nlohmann/json.hpp>  // nlohmann/json
      #include <Dry/ThirdParty/openai/nlohmann/json.hpp>

   The client requires cURL development files, on Fedora:

   .. code-block:: bash

      sudo dnf install libcurl-devel


2. **Update the CMake Configuration**

   Apply the following diff to `CMakeLists.txt` to include the OpenAI C++ client as well as cURL in your dry project:

   .. code-block:: diff

       diff --git a/CMakeLists.txt b/CMakeLists.txt
       index a1eff04..0f32bc7 100644
       --- a/CMakeLists.txt
       +++ b/CMakeLists.txt
       @@ -188,6 +188,20 @@ else ()
        endif ()
        file (MAKE_DIRECTORY ${THIRD_PARTY_INCLUDE_DIR})
        
       +# Find the cURL library
       +find_package(CURL REQUIRED)
       +
       +# Globally link cURL to all targets
       +link_libraries(${CURL_LIBRARIES})
       +
       +# Create a symbolic link for openai
       +execute_process(COMMAND ${CMAKE_COMMAND} -E create_symlink
       +                ${PROJECT_SOURCE_DIR}/Source/ThirdParty/openai
       +                ${CMAKE_BINARY_DIR}/include/Dry/ThirdParty/openai)
       +

3. **Modify Sample/16_Chat/chat.cpp file**

   Implement the changes outlined in the diffs below for ``chat.cpp``:

   .. code-block:: diff

       diff --git a/Source/Samples/16_Chat/Chat.cpp b/Source/Samples/16_Chat/Chat.cpp
       index ee7c2b7..9d0e454 100644
       --- a/Source/Samples/16_Chat/Chat.cpp
       +++ b/Source/Samples/16_Chat/Chat.cpp
       @@ -41,6 +41,7 @@
        #include <Dry/UI/Text.h>
        #include <Dry/UI/UI.h>
        #include <Dry/UI/UIEvents.h>
       +#include <Dry/ThirdParty/openai/openai.hpp>
        
        #include "Chat.h"
        
       @@ -201,16 +202,58 @@ void Chat::HandleSend(StringHash /*eventType*/, VariantMap& eventData)
        
            if (serverConnection)
            {
       -        // A VectorBuffer object is convenient for constructing a message to send
       -        VectorBuffer msg;
       -        msg.WriteString(text);
       -        // Send the chat message as in-order and reliable
       -        serverConnection->SendMessage(MSG_CHAT, true, true, msg);
       +        // Check if the message contains "gpt-3"
       +        if (text.Contains("gpt-3"))
       +        {
       +            // Initialize OpenAI
       +            openai::start();
       +
       +            // Correctly construct the JSON payload as a std::string
       +            std::string payload = std::string(R"({"model": "gpt-3.5-turbo", "messages":[{"role":"user", "content":")") + text.CString() + std::string(R"("}], "max_tokens": 600, "temperature": 0.5})");
       +            nlohmann::json gptResponse;
       +            try {
       +                // Parse the payload to JSON and make the API call
       +                gptResponse = openai::chat().create(nlohmann::json::parse(payload));
       +            } catch (const std::exception& e) {
       +                // Handle JSON parsing errors or API call failures
       +                std::cerr << "Error making API call or parsing response: " << e.what() << '\n';
       +                return;
       +            }
       +
       +            std::string responseText;
       +            try {
       +                // Extract the response text from the JSON response
       +                responseText = gptResponse["choices"][0]["message"]["content"].get<std::string>();
       +            } catch (const std::exception& e) {
       +                // Handle errors in accessing the response content
       +                std::cerr << "Error extracting response text: " << e.what() << '\n';
       +                return;
       +            }
       +
       +            // send the user's message to gpt-3 to the server.
       +            VectorBuffer msg1;
       +            msg1.WriteString(text);
       +            serverConnection->SendMessage(MSG_CHAT, true, true, msg1);
       +
       +            // send the gpt-3 completion to the server.
       +            VectorBuffer msg2;
       +            msg2.WriteString(String(responseText.c_str()));
       +            serverConnection->SendMessage(MSG_CHAT, true, true, msg2);
       +        }
       +        else
       +        {
       +            // Normal chat message handling
       +            VectorBuffer msg;
       +            msg.WriteString(text);
       +            serverConnection->SendMessage(MSG_CHAT, true, true, msg);
       +        }
       +
                // Empty the text edit after sending
                textEdit_->SetText(String::EMPTY);
            }
        }


4. **Prepare the Build Environment**

   Before running CMake, ensure that any previous build configurations are cleared to avoid conflicts. This might involve deleting the CMake cache file:

   .. code-block:: bash

       rm CMakeCache.txt # If exists

   Then, generate the build configuration:

   .. code-block:: bash

       cmake .. -DCMAKE_BUILD_TYPE=Debug -DRY_64BIT=1

5. **Build the Chat Game**

   Compile the Sample Chat game with the newly integrated OpenAI C++ client:

   .. code-block:: bash

       make 16_Chat/fast

Testing the Integration
-----------------------

After applying the changes and compiling the game, ensure your OpenAI API key is available to the game:

.. code-block:: bash

    export OPENAI_API_KEY='your_openai_api_key_here'

Run the Sample Chat game and try sending a message containing "gpt-3". You should see an intelligent response generated by OpenAI's language model.

.. code-block:: bash

    ./bin/16_Chat

Remember you'll need at least one instance of the game running as server mode before a client can interact with the LLM.

That means you need to run ``./bin/16_Chat`` at least twice in two different windows to see the experience.



What's Next?
------------

You've now integrated OpenAI into Dry's Sample Chat game, enhancing it with AI-driven conversational capabilities. Explore further by customizing triggers, integrating other models using the same OpenAI client, or expanding the game's features.

I think personally I will try to get the client communicating with vllm likely running openchat.

Happy coding, and enjoy bringing LLM capabilities to your Dry games!

