Data structures
===============

In **mmg**, several data structures are defined in order to represent and 
manipulate different entities such as tetrahedra, triangles, or meshes.

Mesh
----

The main data structure that is used throughout **mmg** is the mesh structure ``MMG5_Mesh``.
This structure contains the following fields:

``dim``   : integer mesh dimension
``memMax``: size t Maximum memory available
``memCur``: size t Current memory used
``gap``   : double Gap for table reallocation
``ver``   : integer Version of the mesh file
