Using **mmg**
*************

Once installed, **mmg** can be used a command-line tool in any given shell.
Three different software are produced by the compilation, one for each given configuration: **mmg2d**,
**mmgs**, **mmg3d**.

A help message containing a summary of the main options may be printed::

    mmg3d_O3 -h


Input data
==========

Mesh data
---------

Input meshes may be provided in several different formats:
medit (ASCII or binary), gmsh (ASCII or binary), vtk and vtu.
An input mesh name is mandatory and is the only positional argument of **mmg**.
The input mesh name may be specified without the extension.

Metric data
-----------

For mesh adaptation with respect to a given metric (or size map),
metric data should be provided according to mesh file format.

If Medit file formats (.mesh or .meshb) are used, metric data should be
given in a Medit solution file (.sol extension).
If the file has the same name as the mesh file, it is automatically opened and treated as metric data (assuming that level-set discretization mode is disabled).
If the file has a different name, it can be specified using ``-met`` or ``-sol`` options.
If level-set discretization mode is enabled, metric files are ignored by default and can be loaded with the ``-met`` option.

If GMSH file format (.msh or .mshb) is used, the size map should
be provided in the mesh file as \$NodeData and flagged using a string tag
with the ``:metric`` suffix.

If VTK file formats (.vtk or .vtu) are used, a point data field should
be given in the mesh file with the ``:metric`` name.

Solution file for level-set discretization
------------------------------------------

For level-set discretization, 

Lagrangian displacement
-----------------------

Main options for mesh adaptation
================================

Output data
===========