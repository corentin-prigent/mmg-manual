#########
Tutorials
#########

Several tutorials and examples are provided within this section. Click on the
links below to access them. Examples are available for **mmg2d**, **mmgs**, 
**mmg3d**, as well as tutorials for using **mmg** as a library (available in C,
C++ and Fortran). Meshes and metric data files are downloadable by clicking on
their names at the beginning of each tutorial.

**mmg2d**

.. toctree::
    :maxdepth: 1

    Mesh generation <tutorials_mmg2d_mesh_generation.rst>
    Mesh adaption <tutorials_mmg2d_mesh_adaptation.rst>
    Implicit domain meshing <tutorials_mmg2d_implicit.rst>
    Lagrangian motion <tutorials_mmg2d_lagrangian.rst>

**mmgs**

.. toctree::
    :maxdepth: 1

    Mechanical piece remeshing <tutorials_mmgs_mesh_mechanical.rst>
    Smooth surface remeshing <tutorials_mmgs_mesh_smooth.rst>
    Implicit domain meshing <tutorials_mmgs_implicit.rst>

**mmg3d**

.. toctree::
    :maxdepth: 1

    Mesh quality improvement <tutorials_mmg3d_improvement.rst>
    Open boundary remeshing <tutorials_mmg3d_remeshing.rst>
    Mesh adaptation to a solution <tutorials_mmg3d_solution.rst>
    Implicit domain meshing <tutorials_mmg3d_implicit.rst>

**Libraries**

.. toctree::
    :maxdepth: 1

    Libraries <tutorials_libraries.rst>

*************
Prerequisites
*************

Once installed, **mmg** can be used as a command-line tool in any given shell.
Three different software are produced by the compilation, one for each given
configuration: **mmg2d**, **mmgs**, **mmg3d**.

A help message containing a summary of the main options may be printed::

    mmg3d_O3 -h

Input data
==========

Mesh data
---------

Input meshes may be provided in several different formats:

* ``.mesh``/``.meshb`` : ASCII/binary **Medit** file formats
* ``.msh``/``.mshb`` : ASCII/binary **gmsh** file formats
* ``.vtk``/``.vtp``/``.vtu`` : **Paraview** file formats

Input meshes must be conformal.
An input mesh name, which may be specified without the extension, 
is mandatory and is the only positional argument of **mmg**.

Using `gmsh <https://gmsh.info/>`_, it is possible to convert many different
file formats to medit file format ``.mesh``::

    Save As -> Mesh - INRIA Medit (*.mesh)    

For two-dimensional meshes, there is a non-compatibility between the ``.mesh``
format used by mmg2d (with coordinates in 2D) and **gmsh** output (with 
coordinates in 3D).

* To force **mmg2d** to produce a ``.mesh`` file readable by **gmsh**, run 
  **mmg2d** with the ``-3dMedit 1`` command line argument.
* To load a 2D ``.mesh`` file created with **gmsh**, run **mmg2d** with the 
  ``-3dMedit 2`` command line argument. In this case, the .mesh file produced 
  by mmg2d is a **gmsh** ``.mesh``.
* To load a 2D ``.mesh`` file created with **gmsh** and save it as a **Medit** 
  2D ``.mesh`` file, run **mmg2d** with the ``–3dMedit 3`` command line 
  argument.

Paraview file formats require access to the `VTK library <https://vtk.org/>`_.
It must be linked to **mmg** when compiling.
In `.vtk` file formats, domain references (resp. node references) 
can be provided using cell data (resp. point data) with the ``medit:ref`` 
array name.

Metric data
-----------

For mesh adaptation with respect to a given metric (or size map),
metric data should be provided according to mesh file format.

**Medit file format**

* metric data may be provided as a **Medit** solution file (``.sol`` extension).
  If the file has the same name as the mesh file, it is automatically opened
  and treated as metric data (assuming that level-set discretization mode is
  disabled).
* ``-met``/``-sol`` options may be indistinctly used to specify the file name 
  if it different from the mesh file name.
* In level-set discretization mode, metric files are ignored by default and
  must be loaded with the ``-met`` option.

**GMSH file format (.msh or .mshb)**: size map data should be provided in the 
mesh file as ``\$NodeData`` and flagged using a string tag with the ``:metric`` 
suffix.

**VTK file formats (.vtk or .vtu)**: a point data field should be given in the 
mesh file with the name ``:metric``.

Solution file for level-set discretization
------------------------------------------

For level-set discretization mode (``-ls`` option), solution data should be
provided. Similarly to metric data, its format depends on mesh file format.

**Medit file format**

* solution data may be provided as a **Medit** solution file (``.sol`` 
  extension). If the file has the same name as the mesh file, it is 
  automatically opened and treated as solution data.
* ``-sol`` options may be used to specify the file name if it different from 
  the mesh file name.

**GMSH file format (.msh or .mshb)**: level-set must be provided in the 
``.msh(b)`` file as ``$NodeData``

**VTK file formats (.vtk or .vtu)**: level-set must be provided in the mesh file
as point data with the ``:ls`` suffix.

Lagrangian displacement
-----------------------

To perform the lagrangian motion of an object, it is necessary to provide:

**Medit file format**: a displacement at **Medit** solution file format
(``.sol`` extension).

**GMSH file format (.msh or .mshb)**: displacement data must be provided in the 
``.msh(b)`` file as ``$NodeData``.

**VTK file formats (.vtk or .vtu)**: displacement data must be provided in the 
mesh file as point data.

Output data
===========

By default, 

Mesh visualization
==================

* `Medit <https://github.com/ISCDtoolbox/Medit>`_: for visualizing meshes at
  **Medit** file formats.
* `gmsh <https://gmsh.info/>`_: for visualizing meshes at
  **Medit** file formats without associated solution file or **gmsh** files
  with embedded solution data.
* `Paraview <https://www.paraview.org/>`_: for visualizing meshes at
  **VTK** file formats.