Downloading, compiling and installing **mmg**
=============================================

Required tools
--------------

In order to obtain and compile **mmg**, the following tools are needed:

  * **Git**: to download the code you will have to use a git manager. You can install a git manager from the link below but there are many other git clients that you can use:
    
    * `Official Git client <https://git-scm.com/download>`_ (command-line program)
    * `GitKraken <https://www.gitkraken.com/>`_
    * `SourceTree <https://www.sourcetreeapp.com/>`_

Note that if you uses Microsoft Visual Studio (Windows OS), you can simply activate the Git Module of the application.

  * **CMake** : **mmg** uses the CMake building system that can be downloaded on the
    following `web page <https://cmake.org/download/>`_. On Windows OS,
    once CMake is installed, please do not forget to mark the option:: 
        
      Add CMake to the system PATH for all users


Download and compiling **mmg**
------------------------------

Unix-like OS (Linux, MacOS...)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Get the repository::

        wget https://github.com/MmgTools/mmg/archive/master.zip
    
  or::
  
        git clone https://github.com/MmgTools/mmg.git


  The project sources are available under the **src/** directory, see:
   * **src/mmg2d/**   for files related to the mmg2d application;
   * **src/mmgs/**   for files related to the mmgs application;
   * **src/mmg3d/**  for files related to the mmg3d application;
   * **src/common/** for files related to all three.

2. Fast compilation (build **mmg2d**, **mmgs**, **mmg3d**, the mmg2d static library (**libmmg3d.a**), the mmgs static library (**libmmgs.a**), the mmg3d static library (**libmmg3d.a**) and the mmg static library (**libmmg.a**)) all at once::

      cd mmg
      mkdir build
      cd build
      cmake ..
      make
      make install


If the ``make install`` command fails, try to run the ``sudo make install`` command.
If you don't have root access, please refer to the [Installation section](https://github.com/MmgTools/Mmg/wiki/Setup-guide#iii-installation) of the [setup guide](https://github.com/MmgTools/Mmg/wiki/Setup-guide#setup-guide).

The **mmg2d**, **mmgs** and **mmg3d** applications are available under the ``mmg2d_O3``, ``mmgs_O3`` and ``mmg3d_O3`` commands.

Note that if you use some specific options and want to set them easily, you can use a shell script to execute the previous commands. An example is provided [here](https://github.com/MmgTools/mmg/wiki/Configure-script-for-CMake-(UNIX-like-OS)).

Windows OS
^^^^^^^^^^

The following compilation can be performed in any modern version of *Windows*
(AKA 7, 8, 8.1 and 10). A basic knowledge of Windows is assumed (execute
commands in cmd, create directories, etc...).

Compile with VisualStudio
"""""""""""""""""""""""""

1. Get the **Visual Studio** software: it can be downloaded `here <https://www.visualstudio.com/downloads/>`_

2. if not done during the previous step, download **C/C++** compilers: in the Visual Studio searching zone, search **C compiler** and install the **Visual C++ compilers and libraries** (individual componant) and the MSBuild componant;

3. in the Visual Studio searching zone, search the **git** word and select the installation of the **GitHub extension for VisualStudio**;
   
4. stay in VisualStudio and clone the `Mmg repository <https://github.com/MmgTools/mmg.git>`_

5. Use **CMake** to configure and generate your project. It can be done either with the graphic mode of CMake (you have to select the "VisualStudio" generator) or with a command line. In this case, it is highly recommended to specify that you intent to build a VisualStudio project. 
   For example, if you are using VisualStudio 2017::
  
    cmake -G "Visual Studio 15 2017 Win64" ^
    configure
  

Note that you can use a script to make this step easier (an example of script is provided [here](https://github.com/MmgTools/mmg/wiki/Configure-script-for-CMake-(Windows-OS))).

Once the configuration script has finished without errors a `mmg.sln` file will be generated in the cmake_build directory.

6. Double click this file and the visual studio project will open. Then choose the project configuration (Release, Debug...) and make sure that the project is set to Win32 or x64.
   Finally, in order to compile Mmg, right click the `INSTALL` project and select the option `BUILD`.

Compile with MinGW
""""""""""""""""""

1. Get a **C Compiler**:
  * **MinGW** can be downloaded [here](http://mingw.org/). We recommand to install the *mingw-developer-tools*, *mingw32-base*, *mingw32-gcc-fortran*, *mingw32-gcc-g++* and *msys-base* packages;
  * Edit the environment variables and add MinGW in your **PATH** variable. It can be done in the **advanced system settings** panel. (note that you must modify the **PATH** variable, not **Path**);
  * **MinGW** binaries are probably in `C:\MinGW\bin`
  * the MinGW terminal is in `C:\MinGW\msys\1.0\msys`

2. Clone the Mmg repository from the following url: https://github.com/MmgTools/mmg.git;

3. Quit and restart the *CMake* application to take the PATH modification into account then use CMake to configure and generate your project (select the MinGW Makefiles generator of CMake). If you have installed the scotch libraries, you will need to set explicitely the libraries paths;
4. Build the Mmg applications: in the minGW prompt (`C:\MinGW\msys\1.0\msys`) run::

  mingw32-make


Again, if you use some specific options and want to make the CMake configuration step easier, you can use a batch script. An example script is provided [here](https://github.com/MmgTools/mmg/wiki/Configure-script-for-CMake-(Windows-OS)).
