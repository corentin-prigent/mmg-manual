###############
Mesh generation
###############

This section presents tutorials for using **mmg2d** for mesh generation from a
set of points or a set of edges.

***********************************
Mesh generation from a set of edges
***********************************

This first example shows how to generate a mesh from a set of edges. 
The input data (:download:`acdcBdy.mesh </meshes/acdcBdy.mesh>`) is displayed 
below:

.. figure:: /figures/tutorials/acdcEdg.png
    :align: center

    Initial set of edges

To generate a mesh containing these edges, run **mmg2d** with the input mesh
name as a argument. In order to prevent the font from being smoothed out,
specify a sharp angle detection of 10 degrees using the :ref:`-ar <ar-option>`
option. Sharp angles will be considered as a geometric property of the mesh and
hence will be preserved::

    mmg2d_O3 -ar 10 acdcBdy.mesh

The output mesh ``acdcBdy.o.mesh`` is displayed below:

.. figure:: /figures/tutorials/acdcNoHmax.png
    :align: center

    Generated mesh with a sharp angle detection of 10 degrees

Note that **mmg** creates a mesh for all the internal subdomains created by the 
edges, including the holes in the letters A and D. 
By default, all subdomains are saved in the output mesh file. It is possible to 
choose to keep only one subdomain using the ``-nsd`` option. For instance, the
following command will only keep the letter D (domain number 6) as the 
output mesh::

    mmg2d_O3 -ar 10 -nsd 6 acdcBdy.mesh

.. figure:: /figures/tutorials/acdc-nsd.png
    :align: center
    :height: 250 px

    Generated mesh with only one sub-domain

*********************
Finer mesh generation
*********************

To generate a finer mesh, it is possible to specify a maximal edge size value
using the ``-hmax`` option. In this example, since the bounding box size of the
mesh is 500x200, we can impose a maximal edge size of 10 by running the 
following command::

    mmg2d_O3 -ar 10 -hmax 10 acdcBdy.mesh

.. figure:: /figures/tutorials/acdcMesh.png
    :align: center

    Generated mesh for a maximal edge size of 10 (without unwanted subdomains)

************************************
Mesh generation from a set of points
************************************

In this example, let us take a look at mesh generation from a set of points.
The initial mesh (:download:`square.mesh </meshes/square.mesh>`) is represented
below.

.. figure:: /figures/tutorials/initPoints.png
    :align: center

    Initial set of points

To generate a mesh of the convex hull of these points, run **mmg2d**::

    mmg2d_O3 square.mesh

The output mesh ``square.o.mesh`` is represented below:

.. figure:: /figures/tutorials/squareDefault.png
    :align: center

    Generated mesh from a set of points

In this execution of **mmg**, a mesh containing all the initial vertices has
been created first. Then, the mesh has been optimized by a standard adaptation
procedure. Since no option or size map have been provided, **mmg** attempts to 
produce a high-quality mesh with a minimal number of vertices.

**********************************
Preservation of the initial points
**********************************

To keep the initial points, run **mmg** using the ``-noinsert``, ``-noswap``
and ``-nomove`` options in order to deactivate all remeshing operations and only
perform the mesh generation phase::

    mmg2d_O3 square.mesh -noinsert -nomove -noswap

.. figure:: /figures/tutorials/squareNoinsert.png
    :align: center

    Generation of a mesh with preservation of initial points