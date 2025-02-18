##########################
Mechanical piece remeshing
##########################

We start from a mesh named linkrods.mesh (see figure 1).

.. figure:: /figures/user_guide/mechanical1.png
    :align: center

    Figure 1: Initial mesh of a connecting rod

*********
Example 1
*********

Control the surface approximation using the ``-hausd`` option::

    (1)  mmgs_O3 linkrods.mesh -hausd 0.01

    (2)  mmgs_O3 linkrods.mesh -hausd 0.001

The final mesh is saved in the linkrods.o.mesh file. 
The result of command (1) is displayed figure 2, and the result of command (2) is displayed figure 3.

.. figure:: /figures/user_guide/mechanical2.png
    :align: center

    Figure 2: Final mesh for a hausdorff parameter of 0.01

.. figure:: /figures/user_guide/mechanical3.png
    :align: center

    Figure 3: Final mesh for a hausdorff parameter of 0.001

*********
Example 2
*********

Bound the edge sizes using the -hmin and/or -hmax options::

    mmgs_O3 linkrods.mesh -hmax 0.05


.. figure:: /figures/user_guide/mechanical4.png
    :align: center

    Figure 4: Final mesh for edge truncation at a maximal size of 0.05
