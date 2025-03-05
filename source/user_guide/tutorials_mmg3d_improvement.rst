############################################################
Mesh quality improvement with mean edge lengths preservation
############################################################

The mmg3d application allows to improve the quality of an input mesh 
while keeping the mean edge lengths of the mesh.

We consider the initial cube mesh displayed figure 1 (:download:`cube.mesh </meshes/cube.mesh>`)
This mesh is provided without any associated sizemap.

.. figure:: /figures/user_guide/cube_init.png
    :align: center

    Figure 1: Initial cube mesh

To improve your mesh quality while keeping the mean edge sizes, you just need to
run the application using the ``-optim`` option::

    mmg3d_O3 -optim cube.mesh -out optimMesh.mesh

* option ``-out`` allows to choose the ouput file name.
* option ``-optim`` enables mesh improvement with mean edge length preservation.

We obtain a mesh named ``optimMesh.mesh`` as well as the size map computed to preserve the 
edge sizes (see figure 2). This sizemap is saved in the ``optimMesh.sol`` file.

.. figure:: /figures/user_guide/cube_optim.png
    :align: center

    Figure 2: Final cube mesh using the -optim option and computed size map.

Remark:

By default, the Mmg applications try to coarsen the mesh with respect to:

* the geometric approximation
* the gradation control value
* the minimal and maximal edge sizes if specified by the user

For example, starting from our initial cube mesh, we run the application without any arguments::

    mmg3d_O3 cube.mesh

We obtain the cube.o.mesh mesh displayed figure 3. 
As the approximation of the cube boundaries is exact, the remesher can coarse the mesh.

.. figure:: /figures/user_guide/cube_default.png
    :align: center

    Figure 3: Default output mesh.