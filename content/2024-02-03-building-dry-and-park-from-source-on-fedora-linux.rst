Building 'Dry' and 'Park' from Source on Fedora Linux
=====================================================

:date: 2024-02-03 09:19
:author: Russell Ballestrini
:tags: Programming, Game Development, Fedora, Dry, Park
:slug: building-dry-and-park-from-source-on-fedora-linux
:status: published
:summary: Learn how to compile the 'Dry' game engine and the 'Park' game from source on Fedora Linux with debugging enabled, and how to analyze core dumps for debugging.

In this guide, we'll explore how to compile the 'Dry' game engine and the 'Park' game from source on Fedora Linux with debugging enabled. This process will give you a deeper understanding of the inner workings of game development and the satisfaction of running a game you built yourself.

For Ubuntu, go here for pre-compiled game:

* https://luckeyproductions.itch.io/park

Prerequisites
-------------

Before diving in, ensure you have the necessary tools and libraries installed:

- Git
- CMake
- GNU Make
- GCC or Clang
- X11 and audio system development libraries

Install these on Fedora with:

.. code-block:: bash

    sudo dnf groupinstall "Development Tools"
    sudo dnf install cmake git gcc-c++ libX11-devel libXcursor-devel libXinerama-devel libXi-devel libXrandr-devel libXrender-devel libXScrnSaver-devel libXxf86vm-devel pulseaudio-libs-devel nas-libs-devel qt5-qtbase-devel

Cloning the Repositories
------------------------

Clone the 'Dry' and 'Park' repositories using Git:

.. code-block:: bash

    cd ~/git
    git clone https://gitlab.com/luckeyproductions/dry.git
    git clone https://gitlab.com/luckeyproductions/games/park.git

Building Dry with Debugging Enabled
-----------------------------------

Navigate to the 'dry' directory and prepare the build environment:

.. code-block:: bash

    cd dry
    mkdir build && cd build

Configure the build with CMake and enable debugging:

.. code-block:: bash

    cmake .. -DCMAKE_BUILD_TYPE=Debug -DRY_64BIT=1

Compile the Dry library with debug symbols:

.. code-block:: bash

    make

Building Park with Debugging Enabled
------------------------------------

In the 'Park' project, modify the ``Park.pro`` file to add the ``-g -O0`` flags for debugging, for example:

.. code-block:: bash

    QMAKE_CXXFLAGS += -std=c++17 -g -O0

Then set the ``DRY_HOME`` environment variable to the path of your compiled Dry library:

.. code-block:: bash

    export DRY_HOME=/home/fox/git/dry/build

Navigate to the 'park' directory and compile the game:

.. code-block:: bash

    cd /home/fox/git/park
    mkdir build && cd build
    qmake ../Park.pro
    make
    cp -r ../Resources .

Running Park
------------

After a successful build, run the Park executable located in the ``build`` directory:

.. code-block:: bash

    ./park

Analyzing Core Dumps on Fedora
------------------------------

If your application crashes, Fedora can generate core dumps, which are snapshots of the program's state at the time of the crash. These can be invaluable for debugging.

List recent core dumps with:

.. code-block:: bash

    coredumpctl list

To analyze a specific core dump, use ``gdb``:

.. code-block:: bash

    gdb /path/to/executable /path/to/coredump

For example:

.. code-block:: bash

    gdb /home/fox/git/park/Park/park core.291993

Once in ``gdb``, use the ``bt`` command to print a backtrace:

.. code-block:: gdb

    (gdb) bt

This will show you the call stack at the time of the crash, which can help pinpoint the source of the problem.

Happy building and debugging!

