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
level-set function defined at the mesh nodes ``elephant.sol`` displayed figure 1.

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

Note that **mmg** impose the reference (or color) of the isosurface and the domains:

  * The isosurface corresponds to reference 10.
  * Interior volume has reference 3.
  * Exterior volume outside has reference 2.

.. figure:: /figures/user_guide/elephant-Final.png
    :align: center

    Figure 2: Final cube mesh: Implicit surface mesh (left) and cross-section
    view through the volume cube mesh (right).

*****************************************************
Preservation of one given subdomain and analysis mode
*****************************************************

Mmg allows to save a given subdomain of a mesh containing multiple subdomains using the -nsd option. You can for example run Mmg on your output mesh (cube.o.mesh file) save only the elephant mesh (domain of reference 3) with the following command line:

mmg3d_O3 cube.o.mesh -noinsert -noswap -nomove -nsd 3

Figure 3: Saving of only the subdomain of reference 3 using the -nsd option

The coupling of the -noinsert, -noswap and -nomove options forbid all the Mmg operators, thus the cube.o.mesh mesh is analyzed but not remeshed.

****************************
Boundary level-set splitting
****************************

With -lssurf option, it is possible to split only domain boundaries along the level-set while not splitting the interior of the mesh. Starting from the peninsula.mesh mesh file, the ls.sol level-set file and the peninsula.mmg3d reference mapping (provided after command line), we run the following command:

mmgs_O3 -lssurf peninsula.mesh

cat > peninsula.mmg3d <<EOF
LSReferences
5
1 10 11
2 3 4
38 5 6
37 7 8
0 nosplit
EOF

we obtain the figure 4:

    Mesh boundaries are splitted if ask and are assigned the wanted references
    internal domains (tetra) are not

Boundary splitting with lssurf option

Figure 4: Boundaries splitting using lssurf option

Note that if  a mapping is provided for one of the input boundary references, then the mapping for all boundary references has to be given too.