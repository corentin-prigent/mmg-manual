##############
Usage examples
##############

Some library examples are provided in the **mmg** repository, under the 
`libexamples <https://github.com/MmgTools/mmg/tree/master/libexamples>`_ 
directory.
(see the projects source tree section of the wiki for the description 
of the libexamples directory).

* Basic examples with automatic parsing of ``.mesh`` files are provided in the 
  ``libexamples/mmg<X>/adaptation_example0/example0_a`` folder (<X> = <2d|3d|s>
  depending on the library that you want to use). Inputs/outputs are done using
  the API functions that read/write .mesh/.sol files.
* Basic examples with manual mesh setters and getters are provided in the 
  ``libexamples/mmg<X>/adaptation_example0/example0_b`` folder. Inputs/outputs 
  are done using setters and getters to transfer a mesh and a size map already 
  stored in arrays (in the solver structures for example) to **mmg** entities by 
  entities.
* Examples of Fortran calls can be found in the 
  ``libexamples/mmg<X>/adaptation_example0_fortran/example0_<a|b>`` folders. 
  These examples are similar to the previous ones. Usually, a Fortran subroutine
  similar to the C API is provided with an additional argument to store the 
  return value of the C function. Note that if the C API takes a string as 
  argument, the Fortran one will use another additional input argument for
  string length.
* An example of library call from a C++ code is provided in 
  ``libexamples/mmg/adaptation_example0_cpp``.
* ``libexamples/mmg3d/adaptation_example2`` shows how to customize some of the 
  parameters of Mmg;
* ``libexamples/mmg3d/IsosurfDiscretization_example0`` provides examples of 
  isovalue discretisation;
* ``libexamples/mmg3d/LagrangianMotion_example0`` shows examples of lagrangian 
  motion.
* Even if we try to preserve the API compatibility between **mmg** versions, 
  we can have small modifications. In this case, you can use predefined macro 
  (MMG_VERSION, MMG_VERSION_LE…) to detect the API version of Mmg in your code. 
  An example is provided in the 
  ``mmg/libexamples/mmg2d/adaptation_example0/example0_b/`` directory 
  (and its fortran version);

Since **mmg3d** library and API have been developped first, you will find more 
examples in the ``libexamples/mmg3d`` folder than in the other ones. 
Note that the APIs of the 3 codes works in the same way except that:

  * use suitable prefixes: ``MMG3D_`` for **mmg3d**, ``MMG2D_`` for **mmg2d** or
    ``MMGS_`` for **mmgs**.
  * in 2D, the ``MMG2D_Set_vertex`` function takes 2D coordinates while the 
    ``MMGS_Set_vertex`` and ``MMG3D_Set_vertex`` functions take 3D coordinates.

#############################
How to link **mmg** libraries
#############################

By default, the ``make install`` command installs the libraries into the 
``/usr/local/lib`` directory. The header files are located into the 
``/usr/local/include`` directory.

Link using **CMake**
====================

Several ``.cmake`` files may be used:

  * the ``FindMMG.cmake`` file to automatically find the **mmg** library.
  * the ``FindMMG2D.cmake`` file to automatically find the **mmg2d** library.
  * the ``FindMMGS.cmake`` file to automatically find the **mmgs** library.
  * the ``FindMMG3D.cmake`` file to automatically find the **mmg3d** library.

If the package fails, try:

  * setting the MMG_DIR environment variable to your mmg directory path::

        export MMG_DIR=<your_mmg_directory_path>

  * setting the MMG_DIR CMake variable to your mmg directory path::

        SET(MMG_DIR <your_mmg_directory_path>)

FindMMG.cmake package
---------------------

The ``FindMMG.cmake`` package defines the ``MMG_INCLUDE_DIRS`` and the 
``MMG_LIBRARIES`` variables.
To link a program named ``YOUR_TARGET`` with the **mmg** library using 
**CMake**, add the following lines in your ``CMakeLists.txt``::

    FIND_PACKAGE(MMG)
    INCLUDE_DIRECTORIES(${MMG_INCLUDE_DIRS})
    TARGET_LINK_LIBRARIES( ${YOUR_TARGET} ${MMG_LIBRARIES})

Do not forget to include the **mmg** library headers to your program::

    #include "mmg/libmmg.h"

FindMMG<X>.cmake package
------------------------

The ``FindMMG<X>.cmake`` packages, with <X> = <2d|3d|s>, define the 
``MMG_INCLUDE_DIRS`` and the ``MMG_LIBRARIES`` variables.
To link a program named ``YOUR_TARGET`` with the **mmg** library using 
**CMake**, add the following lines in your ``CMakeLists.txt``::

    INCLUDE(FindMMG<X>.cmake)
    INCLUDE_DIRECTORIES(${MMG<X>_INCLUDE_DIRS})
    TARGET_LINK_LIBRARIES( ${YOUR_TARGET} ${MMG<X>_LIBRARIES})

Do not forget to include the **mmg** library headers to your program::

    #include "mmg/mmg<X>/libmmg<X>.h"

Link using command lines
========================

In the following examples, it is assumed that:

  * a one-file program is compiled (``main.c``).
  * **mmg** libraries are installed in the ``<LIB_PATH>`` directory and the 
    header files in the ``<INCLUDE_PATH>`` one (which is the default 
    configuration).
  * the **scotch** library is installed in the ``<SCOTCH_PATH>`` directory.

To compile with the **mmg3d** library, it is necessary to specify:

  * the mmg3d include directory with the ``-I`` option.
  * the mmg3d library location with the ``-L`` option.
  * the mmg3d library name with the ``-l`` option.

in the following command::

    gcc main.c -I<INCLUDE_PATH> -L<LIB_PATH> -L<SCOTCH_PATH> -lmmg3d -lscotch -lscotcherr -lm

Note that **mmg** uses the math library and may require it be to linked as well 
(``-lm`` option). If **mmg** is built without **scotch**, variables related to
it may be removed::

    gcc main.c -I<INCLUDE_PATH> -L<LIB_PATH> -lmmg3d -lm

It may be needed to add the path toward the library directory to your 
``LD_LIBRARY_PATH`` environment variable::

    export LD_LIBRARY_PATH=<LIB_PATH>:$LD_LIBRARY_PATH

Finally, include the **mmg3d** library headers to your program::

    #include "mmg/mmg3d/libmmg3d.h"

Fortran users
-------------

Depending on the extension of Fortran files and on the compiler that is used,
it may be necessary to enable the preprocessing step to link with the **mmg** 
libraries.

For example, **gfortran** enables automatically the preprocessing for ``.F90``
files and not for ``.f90`` files. Thus, to compile the ``main.f90`` file that 
uses the **mmg** API functions, add the ``-cpp`` option to **gfortran**::

    gfortran -cpp main.f90 -lmmg3d -lscotch -lscotcherr -lm

Linking with dynamic library on macOS
-------------------------------------

To avoid trouble with the rpath under Mac OS X just add 
``-Wl,-rpath,<LIB_PATH>`` to your compilation command line::

    gcc main.c -I/usr/local/include/ -L/usr/local/lib -lmmg3d -lm -Wl,-rpath,<LIB_PATH>

Please refer to your compiler documentation for further information.


