###############
Mesh adaptation
###############

In this section, some examples of mesh adaptation are presented. In all of them,
the following mesh (:download:`hole.mesh </meshes/hole.mesh>`) is used.

.. figure:: /figures/tutorials/hole-mesh-init.png
    :align: center
    :height: 500 px

    Initial mesh: a square with a hole and two different domains (different
    references)

******************
Default parameters
******************

To run **mmg2d** with default parameters, run the following command::

    mmg2d_O3 hole.mesh

The output mesh, stored in a file called ``hole.o.mesh``, is displayed below:

.. figure:: /figures/tutorials/hole-mesh-out.png
    :align: center
    :height: 500 px

    Output mesh with default parameters

**mmg** attempt to unrefine the mesh while:
    * preserving the maximal distance between the ideal geometry and its 
      discretization (set with ``-hausd`` option, equal to 0.01 by default).
    * applying the prescribed gradation (set with ``-hgrad`` option, 1.3 by
      default) that enforces the maximal length ratio between two adjacent 
      edges.
    * preserving the subdomains.

******************************
Boundary approximation control
******************************

The boundary approximation is controlled by the Hausdorff parameter.  
The ``-hausd`` option allows to adapt the Hausdorff value.
The mesh bounding box of this example is [-5 ; 10]x[-5 ; 10]. To set a maximal
Hausdorff distance of 0.1, run the following command::

    mmg2d_O3 -hausd 0.1 hole.mesh

This produces the following output:

.. figure:: /figures/tutorials/hole-mesh-out2.png
    :align: center
    :height: 500 px

    Output mesh for a Hausdorff parameter of 0.1.

In this example, the hole boundary and the interface between the two domains are
degraded because the Hausdorff distance that has been set is large compared to
the object sizes.

In general, note that:

* decreasing the Hausdorff parameter leads to refine the mesh in areas 
  with high curvature.
* the ideal Hausdorff parameter depends of mesh size and the default value will
  rarely fit.
* knowing the mesh bounding box is very useful to fit the Hausdorff parameter.
  Visualizing a mesh with **Medit** is a good way to get the size of the
  bounding box.
* the default value of the Hausdorrf parameter is equal to 0.01 and is suitable
  for a circle of radius 1.

*********
Gradation
*********

The ``-hgrad`` parameter control the mesh gradation, i.e. the ratio between the
lengths of two adjacent edges. By default, this parameter is set to 1.3.

It is possible to:

  * customize the ratio value by passing it to the ``-hgrad`` option. 
  * disable the gradation by setting ``-hgrad -1``.
  
The two following meshes are obtained by running the following commands::

    mmg2d_O3 -hgrad 2.3 hole.mesh
    mmg2d_O3 -hgrad -1  hole.mesh

.. figure:: /figures/tutorials/hole-mesh-gradation2.png
    :align: center
    :height: 500 px

    Output mesh with gradation set to 2.3

.. figure:: /figures/tutorials/hole-mesh-gradation.png
    :align: center
    :height: 500 px

    Output mesh without gradation

Note that disabling the gradation can lead to bad quality meshes.

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