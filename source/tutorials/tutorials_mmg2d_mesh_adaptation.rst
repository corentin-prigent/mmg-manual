###############
Mesh adaptation
###############

In this section, some examples of mesh adaptation are presented. In all of them,
the following mesh (:download:`hole.mesh </meshes/hole.mesh>`) is used.

.. figure:: /figures/tutorials/hole-mesh-init.png
    :align: center

    Initial mesh

This mesh contains a hole and two domains with different references (yellow and
pink).

******************
Default parameters
******************

To run **mmg2d** with default parameters, run the following command::

    mmg2d_O3 hole.mesh

The output mesh, stored in a file called ``hole.o.mesh`` is displayed below:

.. figure:: /figures/tutorials/hole-mesh-out.png
    :align: center

    Output mesh with default parameters

**mmg** attempt to unrefine the mesh while preserving the maximal distance between the 
ideal geometry and its discretization (``-hausd`` parameter, 0.01 by default) and with 
respect to the prescribed gradation ( ``-hgrad`` option, 1.3 by default) that impose 
the maximal ratio between the lengths of two adjacent edges.

******************************
Boundary approximation control
******************************

The boundary approximation is controlled by the Hausdorff parameter.  
You can use the ``-hausd`` option to adapt the Hausdorff value to your needs.
We obtain the result displayed on Figure 3 by asking for a maximal Hausdorff 
distance of 0.1 (our mesh bounding box is [-5 ; 10]x[-5 ; 10] )::

    mmg2d_O3 -hausd 0.1 hole.mesh

.. figure:: /figures/user_guide/hole-mesh-out2.png
    :align: center

    Figure 3: Output mesh for a hausdorff parameter of 0.1 (the square is [-5 ; 10]x[-5 ; 10])

Here, the hole boundary and the interface between the 2 domains are degraded 
because the asked Hausdorff distance is large compared to the object sizes.

.. note:: 

    * The Hausdorff parameter leads to refine the mesh in areas with high curvature;
    * The Hausdorff parameter depends of your mesh/object sizes, thus, the default value will rarely fit your needs;
    * Knowing the mesh bounding box is very useful to fit the Hausdorff parameter: you can get this bounding box when you visualize your mesh with Medit;
    * The default value (0.01) suits for a circle with radius of 1.

*********
Gradation
*********

The ``-hgrad`` parameter control the mesh gradation, i.e. the ratio between the
lengths of two adjacent edges. By default, this parameter is set to 1.3.
You can disable the gradation using the -hgrad -1 value or customize the ratio
value using the -hgrad val option (see Figure 4). 
Note that disabling the gradation can lead to bad quality meshes.

.. figure:: /figures/user_guide/hole-mesh-gradation.png
    :align: center

    Figure 4: influence of the gradation parameter. Left, gradation is disabled (-hgrad -1), right, it is set to 2.3 (-hgrad 2.3)

******************
Constant mesh size
******************

You can prescribe a constant edge size using the ``-hsiz`` option::

    mmg2d_O3 hole.mesh -hsiz 0.25

In this case, Mmg will create a mesh that will respect the intersection between 
the size map prescribed by the hausdorff parameter and the constant size map 
(which means that we keep the smallest size asked). 
This intersected size map still respects the gradation parameter (see Figure 5).

.. figure:: /figures/user_guide/hole-mesh-constant.png
    :align: center

    Figure 5: Output mesh when asking for a constant mesh size of size 0.25 (-hsiz 0.25)

*******************************
Adaptation to an input size map
*******************************

A size map can be supplied to mmg in order to impose a desired size feature when
remeshing the input mesh (hole.mesh). 
This size map is a scalar / tensorial function defined at the mesh vertices.
At each vertex, it associates the desired size of the surrounding elements of the mesh.

Size maps must be encoded in:

* a ``.sol``  file if you use input mesh at Medit file format. Mmg automatically detects
  and use a ``.sol`` file with the same name than your input mesh file (``hole.sol`` in our example).
  Otherwise, you can specify another sol file using the ``-sol`` option (``-sol mysolfile.sol``)
* the ``NodeData`` field of your ``.msh`` file if you use Gmsh file format. 
  In this case, the string tag of the ``NodeData`` field must contains the ``:metric`` keyword.

For example, the hole.sol file contains a scalar size map that asks for edges of length 0.1
at vertices with abscissa between 1 and 3 and of size 1 outside this area (see Figure 6, left).
As the sol file has the same name than the mesh file, Mmg will automatically read it 
and the following command line will adapt the mesh to the wanted size map::

    mmg2d_O3 hole.mesh

.. figure:: /figures/user_guide/hole-mesh-size-map.png
    :align: center

    Figure 6: prescribed size map (left) and adapted output mesh (right).