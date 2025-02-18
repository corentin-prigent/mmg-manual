########################
Smooth surface remeshing
########################

Starting from a rough mesh representing the thinker of Rodin (:download:`rodin.mesh </meshes/rodin.mesh>`) 
we want to improve its surface representation.
The ``-hausd`` option can be used to control the surface approximation and 
the ``-nr`` option allows to specify that we don’t want to detect ridges along the surface:

* The Hausdorff value is related to the mesh bounding box. 
  The default value is of 0.01 and stands for a bounding box af size [1 x 1 x 1].
  Here, the size of the mesh bounding box is of  [0.6 x 0.4 x 1], 
  thus, a hausdorff value of 0.001 allows to have a good surface representation.
* The ``-nr`` option states that we don’t want to detect sharp edges during the
  initial analysis of the input triangulation, thus, the ideal reconstructed
  surface don’t contain ridges. Here the initial mesh is very poor and 
  the “thinker” is a smooth surface so the ``-nr`` option avoid to detect triangulation artefacts.

The initial and final meshes are displayed below:

.. figure:: /figures/user_guide/smooth.png
    :align: center

    Figure 1: Initial (left) and final (right) meshes of the thinker of Rodin
