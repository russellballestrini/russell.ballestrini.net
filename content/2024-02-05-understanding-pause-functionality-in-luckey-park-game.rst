Understanding Pause Functionality in LucKey Park Built on Dry Engine
########################################################################

:author: Russell Ballestrini
:slug: understanding-pause-functionality-in-luckey-park-game
:date: 2024-02-05 08:57
:tags: Programming, Game Development, Dry, Park
:status: published
:summary: Dive deep into the pause functionality of LucKey Park built on the Dry engine, exploring how the game's status is managed and toggled end-to-end.


In today's post, we're examining the pause functionality of the `LucKey Park game code <https://gitlab.com/luckeyproductions/games/park>`_, which is built on the 'Dry' engine. We'll uncover how the game's status is managed and toggled, especially in response to the cancel button (ESC key), and provide insights into the game's input handling and state management.

* Check out `screenshots and videos of LucKey Park on itch.io <https://luckeyproductions.itch.io/park>`_

Understanding the Game's Status Management
===============================================

The 'Park' game uses an enumeration ``GameStatus`` with values like ``GS_MAIN``, ``GS_PLAY``, ``GS_PAUSED``, and ``GS_MODAL`` to represent the game's current state. The ``Game`` class in ``game.h`` maintains a ``status_`` variable to track this state.

.. code-block:: cpp

    enum GameStatus{ GS_MAIN, GS_PLAY, GS_PAUSED, GS_MODAL };

    class Game: public Object
    {
        // ...
        private:
            GameStatus status_;
    };

The ``Game`` class provides methods to get and set this status, as well as a ``TogglePause()`` method that switches between ``GS_PLAY`` and ``GS_PAUSED``.

Binding the Cancel Action
-------------------------

In ``inputmaster.cpp``, the ``InputMaster`` class binds the ``IA_CANCEL`` action to the ESC key. This setup is crucial for handling the pause functionality when the player presses ESC.

.. code-block:: cpp

    Bind(IA_CANCEL, KEY_ESCAPE);

Handling the Cancel Action
--------------------------

When the ``IA_CANCEL`` action is triggered, the ``HandleAction`` method in ``InputMaster`` responds accordingly. If no tool is active, it calls ``gui->ShowMainMenu()``, which indirectly pauses the game by changing the game's status.

.. code-block:: cpp

    case IA_CANCEL:
        if (tool) sceneCursor->SetTool(nullptr);
        else gui->ShowMainMenu();
        break;

Showing the Main Menu and Pausing the Game
------------------------------------------

The ``ShowMainMenu()`` method in ``gui.cpp`` is where the game's status is set to ``GS_MODAL``, effectively pausing the game when the main menu is displayed.

.. code-block:: cpp

    void GUI::ShowMainMenu()
    {
        mainMenu_->Show();
        Game* game{ GetSubsystem<Game>() };
        if (game->GetStatus() == GS_PLAY)
        {
            game->SetStatus(GS_MODAL);
            HideDash();
        }
    }

The Main Update Loop Controlled by Dry Engine
---------------------------------------------

The Dry engine, like its predecessor Urho3D, manages the main game loop internally. Developers hook into this loop by subscribing to the ``E_UPDATE`` event, which the engine dispatches every frame. This event allows developers to perform per-frame updates to their game logic.

While the main update loop is not explicitly shown in the provided snippets, it's typically where the game checks the ``status_`` variable each frame. If the status is ``GS_PAUSED`` or ``GS_MODAL``, the loop skips updating the game world, pausing the game's logic.

End-to-End Pause Functionality
------------------------------

From the moment the player presses the ESC key to the game entering a paused state, the flow is as follows:

1. The ESC key is pressed.
2. ``InputMaster`` detects the ``IA_CANCEL`` action.
3. ``HandleAction`` calls ``gui->ShowMainMenu()`` if no tool is active.
4. ``ShowMainMenu()`` sets the game's status to ``GS_MODAL``.
5. The main update loop, controlled by the Dry engine, respects this status and pauses the game.

This exploration has provided a clear understanding of how the pause functionality is implemented in Lucky Park using the Dry engine. It's a great example of how game state management and input handling work together to create responsive gameplay.

Stay tuned for more deep dives into game development.


