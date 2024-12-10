Downloading, compiling and installing **mmg**
=============================================

Required tools
==============

In order to obtain and compile **mmg**, the following tools are needed:

  * **Git**: to download source code, a git manager is necessary. 
    You can install a git manager from the link below but there are many other git clients that you can use:
    
    * `Official Git client <https://git=scm.com/download>`_ (command=line program)
    * `GitKraken <https://www.gitkraken.com/>`_
    * `SourceTree <https://www.sourcetreeapp.com/>`_

Note that if you use Microsoft Visual Studio (Windows OS), you can simply activate the Git Module of the application.

  * **CMake** : **mmg** uses the CMake building system that can be downloaded on the
    following `web page <https://cmake.org/download/>`_. On Windows OS,
    once CMake is installed, please do not forget to mark the option:: 
        
      Add CMake to the system PATH for all users


Download and compiling **mmg**
==============================

Unix=like OS (Linux, macOS...)
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

2. Fast installation::

      cd mmg
      mkdir build
      cd build
      cmake ..
      make
      make install

If the ``make install`` command fails, try to run the ``sudo make install`` command.

3. Advanced installation:
   
   You can customize the project configuration by passing arguments to the `cmake` command. The most useful variables that can be set are detailed here.

====================  =================================== ==========================================
**Variable name**     **Object**                          **Authorized values and effects**       
--------------------  ----------------------------------- ------------------------------------------
**CMAKE_BUILD_TYPE**  allow to choose the compiler flags  =============== ===========
                                                          .. raw::Release compilation
                                                          =============== ===========
                                                          Debug           compilation
                                                          =============== ===========
====================  =================================== ==========================================

+--------------------+-----------------------------------+------------------------------------------+
|**Variable name**   | **Object**                        | **Authorized values and effects**        |
+====================+===================================+==========================================+
|**CMAKE_BUILD_TYPE**| allow to choose the compiler flags|                                          |
|                    |                                   |                                          |
|                    |                                   |                                          |
|                    |                                   |                                          |
|                    |                                   |                                          |
+--------------------+-----------------------------------+------------------------------------------+


       


<table><tr><td>`Release`</td><td>compilation in release mode (add `=O3` flag): fast executable</td></tr><tr><td>`RelWithDebInfo`</td><td>release mode with debug informations (`=O3 =g` flags): a little slower executable</td></tr><tr><td>`Debug`</td><td>debug mode with (`=g` flag): very slow executable</td></tr><tr><td>`MinSizeRel`</td><td>minimum size mode (`=Os` flag): executable of small size</td></tr><tr><td>` `</td><td>empty mode (no flag): slow executable</td></tr></table> |
| **LIBMMG3D_STATIC** | enable or disable the static **mmg3d** library compilation | <table><tr><td>`ON`</td> <td>enabled</td></tr><tr><td> `OFF`</td><td> disabled </td></tr> </table> |
| **LIBMMG3D_SHARED** | enable or disable the shared **mmg3d** library compilation | <table><tr><td>`ON`</td> <td>enabled</td></tr><tr><td> `OFF`</td><td> disabled </td></tr> </table> |
| **LIBMMG2D_STATIC** | enable or disable the static **mmg2d** library compilation | <table><tr><td>`ON`</td> <td>enabled</td></tr><tr><td> `OFF`</td><td> disabled </td></tr> </table> |
| **LIBMMG2D_SHARED** | enable or disable the shared **mmg2d** library compilation | <table><tr><td>`ON`</td> <td>enabled</td></tr><tr><td> `OFF`</td><td> disabled </td></tr> </table> |
| **LIBMMGS_STATIC** | enable or disable the static **mmgs** library compilation | <table><tr><td>`ON`</td> <td>enabled</td></tr><tr><td> `OFF`</td><td> disabled </td></tr> </table> |
| **LIBMMGS_SHARED** | enable or disable the shared **mmgs** library compilation | <table><tr><td>`ON`</td> <td>enabled</td></tr><tr><td> `OFF`</td><td> disabled </td></tr> </table> |
| **LIBMMG_STATIC** | enable or disable the static **mmg** library compilation | <table><tr><td>`ON`</td> <td>enabled</td></tr><tr><td> `OFF`</td><td> disabled </td></tr> </table> |
| **LIBMMG_SHARED** | enable or disable the shared **mmg** library compilation | <table><tr><td>`ON`</td> <td>enabled</td></tr><tr><td> `OFF`</td><td> disabled </td></tr> </table> |
| **USE_SCOTCH**       | enable or disable the **SCOTCH** library link              | <table><tr><td>`ON`</td> <td>enabled</td></tr><tr><td> `OFF`</td><td> disabled </td></tr> </table> |
| **TEST_LIBMMG3D**    | enable or disable the compilation of examples of the **mmg3d** library usage | <table><tr><td>`ON`</td> <td>enabled</td></tr><tr><td> `OFF`</td><td> disabled </td></tr> </table> |
| **TEST_LIBMMG2D**    | enable or disable the compilation of examples of the **mmg2d** library usage | <table><tr><td>`ON`</td> <td>enabled</td></tr><tr><td> `OFF`</td><td> disabled </td></tr> </table> |
| **TEST_LIBMMGS**    | enable or disable the compilation of examples of the **mmgs** library usage | <table><tr><td>`ON`</td> <td>enabled</td></tr><tr><td> `OFF`</td><td> disabled </td></tr> </table> |
| **TEST_LIBMMG**    | enable or disable the compilation of examples of the **mmg** library usage | <table><tr><td>`ON`</td> <td>enabled</td></tr><tr><td> `OFF`</td><td> disabled </td></tr> </table> |

For example, the following command turns the project in debug mode, enables the compilation of the shared **mmg3d** library and disables the use of the **SCOTCH** library:  
```CMake
cmake =D CMAKE_BUILD_TYPE=Debug =D LIBMMG3D_SHARED=ON =D USE__SCOTCH=OFF ..
```

### Default configuration options
By default:
  * the project is configured in release mode;
  * it uses **SCOTCH** library if it is found;
  * it builds the static **mmg3d** library (but not the shared one and the examples). 



The **mmg2d**, **mmgs** and **mmg3d** applications are available under the ``mmg2d_O3``, ``mmgs_O3`` and ``mmg3d_O3`` commands.

Note that if you use some specific options and want to set them easily, you can use a shell script to execute the previous commands. An example is provided in  section :ref:`installation_examples`.

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
  
    cmake =G "Visual Studio 15 2017 Win64" ^
    configure
  

Note that you can use a script to make this step easier (an example of script is provided [here](https://github.com/MmgTools/mmg/wiki/Configure=script=for=CMake=(Windows=OS))).

Once the configuration script has finished without errors a `mmg.sln` file will be generated in the cmake_build directory.

6. Double click this file and the visual studio project will open. Then choose the project configuration (Release, Debug...) and make sure that the project is set to Win32 or x64.
   Finally, in order to compile Mmg, right click the `INSTALL` project and select the option `BUILD`.

Compile with MinGW
""""""""""""""""""

1. Get a **C Compiler**:

  * **MinGW** can be downloaded `here <https://www.mingw=w64.org/>`_. We recommand to install the *mingw=developer=tools*, *mingw32=base*, *mingw32=gcc=fortran*, *mingw32=gcc=g++* and *msys=base* packages;
  * Edit the environment variables and add MinGW in your **PATH** variable. It can be done in the **advanced system settings** panel. (note that you must modify the **PATH** variable, not **Path**);
  * **MinGW** binaries are probably in ``C:\MinGW\bin``
  * the MinGW terminal is in ``C:\MinGW\msys\1.0\msys``

2. Clone the **mmg** `repository <https://github.com/MmgTools/mmg.git>`_

3. Quit and restart the *CMake* application to take the PATH modification into account
   then use CMake to configure and generate your project (select the MinGW Makefiles generator of CMake). 
   If you have installed the scotch libraries, you will need to set explicitely the libraries paths;

4. Build the **mmg** applications: in the minGW prompt (``C:\MinGW\msys\1.0\msys``) run::

    mingw32=make


Again, if you use some specific options and want to make the CMake configuration step easier, you can use a batch script. An example script is provided in section :ref:`installation_examples`.

.. _installation_examples:

Examples of installation scripts
================================

The following shell script ``configure.sh`` can be used to build the project on UNIX=like OS. It is possible to personalize the compilation flags and library paths::

  cmake ..
  =DCMAKE_BUILD_TYPE=Release \
  =DCMAKE_CXX_FLAGS="=O3" \
  =DCMAKE_C_FLAGS="=O3" \
  =DUSE_SCOTCH=ON \
  =DSCOTCH_INCLUDE_DIR="/usr/include/scotch/" \
  =DSCOTCH_LIBRARY="libscotch=5.2.so" \
  =DSCOTCHERR_LIBRARY="libscotcherr=5.2.so"

  # uncomment next line for verbose output
  # make VERBOSE=1 =j
  make =j
  sudo make install

The following bash script ``configure.bat`` can be used to build the project on Windows OS. It is also possible to personalize the compilation flags and library paths::

  del CMakeCache.txt

  cls

  cmake =G "Visual Studio 15 2017 Win64"      ^
  =DCMAKE_BUILD_TYPE=Release                  ^
  =DCMAKE_CXX_FLAGS="=O3"                     ^
  =DCMAKE_C_FLAGS="=O3"                       ^
  =DUSE_SCOTCH=OFF                            ^
  ..

