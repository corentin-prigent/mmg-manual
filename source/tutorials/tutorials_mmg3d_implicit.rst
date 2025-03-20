#######################
Implicit domain meshing
#######################

**mmg3d** allows to discretize and optimize an implicitly defined surface 
(i.e. a surface defined by a level-set function). 
More information about the level-set discretization algorithm is available here.

Since **mmg2d** and **mmg3d** have lot of options in common, it is possible to
refer to the 2d examples for:

  * isosurface discretization with mesh adaptation.
  * input materials preservation (multi-material mode).
  * bubble removal (small parasitic component deletion).

*********************************
Standard level-set discretization
*********************************

The starting point of this example is a mesh of a cube and the discrete 
level-set function defined at the mesh nodes ``elephant.sol`` 
displayed figure 1.

.. figure:: /figures/user_guide/elephant-ls.png
    :align: center

    Figure 1: Iso surfaces of the level-set function defined at the nodes 
    of the cube mesh

To split the domain on the 0 value of the level-set function, run the following
command::

    mmg3d_O3 cube -sol elephant.sol -ls -nr -hausd 0.001 -hgrad 1.3 -hmax 0.05

* ``.sol`` file name is specified using the :ref:`-sol <sol-option>` option.
* The ``-ls`` option states that the input ``.sol`` file is a level-set file 
  and that we want to discretize the implicit surface defined by the 0 level 
  of the level-set.
* A level-set function being a smooth function, we do not want to detect ridges
  so the ``-nr`` option is used.
* The cube mesh bounding box size is [1 x 1 x 1], then a hausdorff parameter 
  (:ref:`-hausd <hausd-option>` option) of 0.001 allows to have a good surface
  approximation.
* The authorized ratio between consecutive edges is increased using the 
  :ref:`-hgrad <hgrad-option>` option.
* The :ref:`-hmax <hmax-option>` option ensure that no edges longer than 0.05
  will be created.

The output of the execution consists in two domains separated by a surface that 
is an optimized mesh of the initial implicit surface (see figure 2).

Note that **mmg** impose the reference (or color) of the isosurface and domains:

  * The isosurface corresponds to reference 10.
  * Interior volume has reference 3.
  * Exterior volume outside has reference 2.

.. figure:: /figures/user_guide/elephant-Final.png
    :align: center

    Figure 2: Final cube mesh: Implicit surface mesh (left) and cross-section
    view through the volume cube mesh (right).

********************************************************
Preservation of one specific subdomain and analysis mode
********************************************************

**mmg** allows to save a given subdomain of a mesh containing multiple 
subdomains using the ``-nsd`` option. For example, running **mmg** with the 
following command will save the domain of reference 3 (the elephant part of the
mesh)::

  mmg3d_O3 cube.o.mesh -noinsert -noswap -nomove -nsd 3

The coupling of ``-noinsert``, ``-noswap`` and ``-nomove`` options deactivates
all remeshing operations, meaning that the mesh in ``cube.o.mesh`` is only 
analyzed, and is not modified. The output is displayed on figure 3.

.. figure:: /figures/user_guide/elephant-ls-nsd3.png
   :align: center

   Figure 3: Saving of only the subdomain of reference 3 using the ``-nsd`` 
   option

****************************
Boundary level-set splitting
****************************

With ``-lssurf`` option, it is possible to only split domain boundaries along 
the level-set while not splitting the interior of the mesh. Starting from the
``peninsula.mesh`` mesh file, the ``ls.sol`` level-set file and the 
``peninsula.mmg3d`` reference mapping (provided below), run the following 
command::

  mmgs_O3 -lssurf peninsula.mesh

In this example, the reference mapping is provided as follows::

  LSReferences
  5
  1 10 11
  2 3 4
  38 5 6
  37 7 8
  0 nosplit
  EOF

The result of this example is displayed on figure 4. With this option, mesh
boundaries are split and provided references are assigned. Internal tetrahedra
are not split. Note that all boundary references must be mapped.

.. figure:: /figures/user_guide/peninsula_lssurf.png
   :align: center

   Figure 4: Boundaries split using ``-lssurf`` option