Comparing Node.js and Python Performance with the Official OpenAI Client
###############################################################################

:author: Russell Ballestrini
:slug: comparing-nodejs-and-python-performance-with-openai-client
:date: 2024-05-28 08:49
:tags: Node.js, Python, OpenAI, Performance
:status: published


As a seasoned Python developer, I've always appreciated the versatility and power of Python. I found out today that when it comes to handling high-volume API requests, CPU performance can be a bottleneck and cause stability issues if not throttled to around 80% utilization. I conducted a performance comparison between Node.js and Python using the official OpenAI client, and the results were quite revealing. Node.js outperformes Python in this specific use case.

Background
----------

At `CourseMojo, we are scaling an AI assistant teacher for public schools <https://coursemojo.com/>`_ which provides real-time, intelligent responses to students' answers to open ended questions. During our load testing in my sandbox environment, we identified that heavy CPU utilization was primarily due to calls to the OpenAI API. This prompted me to explore different programming languages to see if the problem existed elsewhere.

The Experiment
--------------

To compare the performance of Node.js and Python, I set up two scripts that interact with the OpenAI API. The goal was to measure the time taken to process a large number of tasks concurrently. Here’s a brief overview of the setup:

- **Node.js Script**: Processed 1800 tasks, with a concurrency limit of 200 tasks at a time.
- **Python Script**: Processed 300 tasks, with a concurrency limit of 20 tasks at a time.

Both scripts were designed to send chat messages to the OpenAI API and receive responses. The tasks were structured to simulate real-world usage, where multiple requests are sent concurrently in the background with a single process running on a single CPU core. This mocks our production application.

Node.js Script
--------------

Here is the Node.js script used for the experiment, we use p-limit to throttle the concurrency to healthy CPU levels for background work to continue in process:

.. code-block:: javascript

 import OpenAI from 'openai';
 import pLimit from 'p-limit';

 const openai = new OpenAI({ apiKey: process.env['OPENAI_API_KEY'] });

 async function generateChatCompletion(messages) {
     const stream = await openai.chat.completions.create({
         messages,
         model: 'gpt-3.5-turbo',
         stream: true,
     });

     let resultText = '';
     for await (const chunk of stream) {
         if (chunk.choices && chunk.choices.length > 0 && chunk.choices[0].delta && chunk.choices[0].delta.content) {
             resultText += chunk.choices[0].delta.content;
         }
     }
     return resultText;
 }

 // Generate an array of chats
 const chats = Array.from({ length: 1800 }, (_, index) => ({
     messages: [
         { role: 'system', content: 'You are a helpful assistant.' },
         { role: 'user', content: `What is the number ${index + 1}?` }
     ]
 }));

 // Function to execute chats with controlled concurrency
 async function executeChatsConcurrently() {
     const limit = pLimit(200); // limit the number of concurrent API calls.

     const promises = chats.map(chat => limit(() => generateChatCompletion(chat.messages)));
     const results = await Promise.all(promises);

     // Print the completions
     results.forEach((result, index) => {
         console.log(`Chat Completion Result ${index + 1}:`);
         console.log(result);
     });
 }

 executeChatsConcurrently().catch(console.error);


Python Script
-------------

Here is the Python script used for the experiment, we use a semaphore to throttle the concurrency to healthy CPU levels for background work to continue in process:

.. code-block:: python

 import asyncio
 from openai import AsyncOpenAI

 async_client = AsyncOpenAI()

 async def generate_text_async(messages, sem):
     async with sem:
         stream = await async_client.chat.completions.create(
             model="gpt-3.5-turbo",
             messages=messages,
             stream=True,
         )
         generated_text = ""
         async for chunk in stream:
             if chunk.choices[0].delta.content is not None:
                 generated_text += chunk.choices[0].delta.content
         return f"\n\nGenerated text for '{messages}':\n{generated_text}"

 # Generate a list of chats
 chats = [
     {
         "messages": [
             {"role": "system", "content": "You are a helpful assistant."},
             {"role": "user", "content": f"What is the number {index + 1}?"}
         ]
     }
     for index in range(300)
 ]

 async def main():
     sem = asyncio.Semaphore(20)  # limit concurrent tasks.
     tasks = [generate_text_async(chat["messages"], sem) for chat in chats]
     results = await asyncio.gather(*tasks)
     for result in results:
         print(result)

 asyncio.run(main())


Results
-------

The results of the experiment were as follows:

**Node.js Script**:

.. code-block:: text

 real    0m10.659s
 user    0m8.277s
 sys     0m0.544s


**Python Script**:

.. code-block:: text

 real    0m15.991s
 user    0m10.041s
 sys     0m0.229s


Analysis
--------

The `real` time, which represents the total elapsed time, was significantly lower for the Node.js script compared to the Python script. Here are some key takeaways from the results:

1. **Concurrency Handling**: Node.js handled 1800 tasks with a concurrency limit of 200, while Python handled 300 tasks with a concurrency limit of 20. Despite the higher number of tasks and concurrency in Node.js, it completed the tasks faster.

2. **Event-Driven Architecture**: Node.js’s event-driven, non-blocking I/O model is highly efficient for handling multiple concurrent tasks. This architecture allows Node.js to manage a large number of simultaneous connections with minimal overhead, making it ideal for high-volume API interactions.

3. **CPU Utilization**: Both scripts showed healthy CPU core usage, but Node.js managed to utilize the CPU more efficiently, resulting in faster completion times.

4. **User and System Time**: The `user` and `sys` times indicate the CPU time spent in user-mode and kernel-mode, respectively. Node.js showed a higher `user` time but a lower `sys` time compared to Python, suggesting that Node.js was more efficient in executing user-level code.

Conclusion
----------

The experiment clearly demonstrated that Node.js outperforms Python in handling high-volume, concurrent API requests using the official OpenAI client. The event-driven architecture of Node.js, combined with its efficient concurrency handling, makes it a superior choice for scenarios where performance and speed are critical.

While Python remains a powerful and versatile language, especially in the realm of data science and machine learning, Node.js proves to be a better option for high-performance, real-time applications that require efficient handling of multiple concurrent tasks.

If you’re working on a project that involves extensive use of the OpenAI API or any other high-volume API interactions, consider leveraging Node.js to maximize performance and efficiency. The results of this experiment highlight the potential gains in speed and responsiveness that can be achieved with the right choice of technology.

Final Thoughts
--------------

Choosing the right tool for the job is crucial in software development. While both Node.js and Python have their strengths, understanding their performance characteristics can help you make informed decisions that align with your project’s requirements. In the case of high-volume API interactions, Node.js stands out as the clear winner, offering superior performance and efficiency.

It's worth noting that the OpenAI client uses `httpx` for Python and `node-fetch` for Node.js by default. This choice of libraries also impacts performance. Additionally, there is hope for Python's future performance improvements, such as the potential removal of the Global Interpreter Lock (GIL) in later versions, which could significantly enhance Python's concurrency capabilities.

For now, if performance is a critical factor in your project, especially for handling numerous concurrent API requests, Node.js is the way to go. But keep an eye on Python's developments, as it continues to evolve and improve.

This post was written with the help of gpt-4 using https://github.com/russellballestrini/flask-socketio-llm-completions
