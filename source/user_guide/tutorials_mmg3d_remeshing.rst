#######################
Open boundary remeshing
#######################

By default, mmg considers only boundaries that are delimiting the mesh 
(external boundaries) or that are at the interface between two different 
domains (internal boundaries). Thus, if the user provides a portion of surface 
that is not at the interface between two domains with different references 
(see figure 1, mesh island.mesh), by default, this surface is deleted.

.. figure:: /figures/user_guide/opnbdy1.png
    :align: center

    Figure 1: Example of open boundary: the yellow surface does not share the sphere into domains with different references (colors)

If you want to preserve an open boundary, you have to run mmg in `opnbdy` mode. 
You can see on figure 2 the result of the remeshing of the previous mesh using the following command line::

    mmg3d_debug -opnbdy island.mesh

We can see that the open boundary is not deleted and is remeshed at the same time as the volume mesh.

.. figure:: /figures/user_guide/opnbdy2.png
    :align: center

    Figure 2: remeshing in `opnbdy` mode

Note that it slows down the code so when a boundary shares a domain into 2 distinct domains, 
it is better to assign different references to each domain and to run mmg as usually than to use the `-opnbdy` option.