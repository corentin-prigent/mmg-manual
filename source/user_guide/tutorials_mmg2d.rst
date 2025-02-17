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

#############################
Mesh adaptation to a solution
#############################

We start from the :download:`hole.mesh </meshes/hole.mesh>` mesh (see Figure 1).

.. figure:: /figures/user_guide/hole-mesh-init.png
    :align: center

    Figure 1: Initial mesh (hole.mesh)

This mesh contains a hole and 2 domains with different references, the yellow domain and the pink one.
Default paramteters

To run Mmg2d, you only have to run the application followed by the mesh name:

mmg2d_O3 hole.mesh

We obtain an output file named hole.o.mesh (depicted Figure 2): Mmg tries to unrefine the mesh while preserving the maximal distance between the ideal geometry and its discretisation (-hausd parameter, 0.01 by default) and with respect to the prescribed gradation ( -hgrad option, 1.3 by default) that impose the maximal ratio between the lengths of two adjacent edges. You will find more informations about this options below.

Figure 2: Output mesh without parameters
Boundary approximation control

The boundary approximation is controlled by the Hausdorff parameter.  You can use the -hausd option to adapt the Hausdorff value to your needs (more infos about the -hausd option).  We obtain the result displayed Figure 3 by asking for a maximal Hausdorff distance of 0.1 (our mesh bounding box is [-5 ; 10]x[-5 ; 10] ):
mmg2d_O3 -hausd 0.1 hole.mesh

Figure 3: Output mesh for a hausdorff parameter of 0.1 (the square is [-5 ; 10]x[-5 ; 10])
Here, the hole boundary and the interface between the 2 domains are degraded because the asked hausdorff distance is large comparing to the object sizes.

Remarks:

    The Hausdorff parameter leads to refine the mesh in areas with high curvature;
    The Hausdorff parameter depends of your mesh/object sizes, thus, the default value will rarely fit your needs;
    Knowing the mesh bounding box is very useful to fit the Hausdorff parameter: you can get this bounding box when you visualize your mesh with Medit;
    The default value (0.01) suits for a circle with radius of 1.

Gradation

The -hgrad parameter control the mesh gradation (i.e. the ration between the lengths of two adjacent edges, more infos about the -hgrad option). By default this parameter is setted to 1.3. You can disable the gradation using the -hgrad -1 value or customize the ratio value using the -hgrad val option (see Figure 4). Note that disabling the gradation can lead to meshes with bad qualities.

Figure 4: influence of the gradation parameter. Left, the gradation is disabled (-hgrad -1), right, it is setted to 2.3 (-hgrad 2.3)
Constant mesh size

You can prescribe a constant edge size using the -hsiz option:

mmg2d_O3 hole.mesh -hsiz 0.25

In this case, Mmg will create a mesh that will respect the intersection between the size map prescribed by the hausdorff parameter and the constant size map (which means that we keep the smallest size asked). This intersected size map still respects the gradation parameter (see Figure 5).

Figure 5: Output mesh when asking for a constant mesh size of size 0.25 (-hsiz 0.25)
Adaptation to an input size map

A size map can be supplied to mmg in order to impose a desired size feature when remeshing the input mesh (hole.mesh). This size map is a scalar / tensorial function defined at the mesh vertices. At each vertex, it associates the desired size of the surrounding elements of the mesh.

Size maps must be encoded in:

    a .sol  file if you use input mesh at Medit file format. Mmg automatically detects and use a sol file with the same name than your input mesh file (hole.sol  in our example), otherwise, you can specify another sol file using the -sol option (-sol mysolfile.sol)
    the NodeData field of your .msh  file if you use Gmsh file format. In this case, the string tag of the NodeData field must contains the :metric keyword.

For example, the hole.sol file contains a scalar size map that asks for edges of length 0.1 at vertices with abscissa between 1 and 3 and of size 1 outside this area (see Figure 6, left). As the sol file has the same name than the mesh file, Mmg will automatically read it and the following command line will adapt the mesh to the wanted size map :

mmg2d_O3 hole.mesh

Figure 6: prescirbed size map (left) and adapted output mesh (right).