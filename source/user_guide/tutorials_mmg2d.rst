#####
mmg2d
#####

You can generate a mesh from a set of points or from a set of edges.

***********************************
Mesh generation from a set of edges
***********************************

We start from a mesh containing only edges (the acdcBdy.mesh file)

.. figure:: /figures/user_guide/acdcEdg.png
    :align: center

    Initial set of edges

To generate a mesh containing these edges, we just need to run the mmg2d application. 
Because we don’t want to smooth the font used, we specify a sharp angle detection of 10° using the -ar option::

    mmg2d_O3 -ar 10 acdcBdy.mesh

We obtain the following mesh:

.. figure:: /figures/user_guide/acdcNoHmax.png
    :align: center

    Generated mesh with a sharp angle detection of 10°

Note that mmg meshes the internal subdomains created by the edges. 
By default, all subdomains are saved. You can choose to keep only one subdomain using the ``-nsd`` option.

*********************
Finer mesh generation
*********************

To generate a finer mesh we can specify a maximal edge size value using the -hmax option. 
The mesh bounding box is of size 500x200 thus we impose a maximal edge size of 10::

    mmg2d_O3 -ar 10 -hmax 10 acdcBdy.mesh

.. figure:: /figures/user_guide/acdcMesh.png
    :align: center

    Generated mesh for a maximal edge size of 10 and without the non wanted subdomains

************************************
Mesh generation from a set of points
************************************

In our example, our initial mesh file (the square.mesh file) contains only points (it is represented on figure 1).

.. figure:: /figures/user_guide/initPoints.png
    :align: center

    Figure 1: Set of points from which we want to generate a mesh

To generate a mesh of the convex hull of those points, you just need to run the **mmg2d** application::

    mmg2d_O3 square.mesh

We obtain the mesh represented on figure 2.

.. figure:: /figures/user_guide/squareDefault.png
    :align: center

    Figure 2: Mesh generation from a set of points

Here we have created a mesh containing all the initial vertices, then, 
the mesh has been optimized (as no option or size map is provided, we seek to have a high mesh quality with a minimal number of vertices).

**********************************
Preservation of the initial points
**********************************

You can keep your initial points using the ``-noinsert``, ``-noswap`` and ``-nomove`` arguments::

    mmg2d_O3 square.mesh -noinsert -nomove -noswap

The resulting mesh is represented figure 3.

.. figure:: /figures/user_guide/squareNoinsert.png
    :align: center

    Figure 3: Generation of a mesh from a set of points with preservation of points