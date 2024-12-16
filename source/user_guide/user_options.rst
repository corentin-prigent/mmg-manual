#####################
Options for remeshing
#####################

***************
Generic options
***************

``-d``
    Turn on debug mode.
``-h``
	Get help about available options.
``-m n``	
    Set the maximal memory size to n MBytes.
``-v n``	
    Set the verbosity level to n .
``-val``	
    Print the default parameters values.
``-debug``
    Save a default parameter file (extension .mmg<2d|s|3d>) that contains the parameters applied on different kind of entities.

*******************
File specifications
*******************

``-in input_mesh_file``
	Input triangulation.
``-out  output_mesh_file``
	Output triangulation.
``-sol  solution_file``
	Load metric, level-set or displacement file.
``-met  metric_file``
	Load metric file in level-set mode in order to discretize a level-set and to adapt the output mesh to a metric in one command.

**********
Parameters
**********

``-A``
	Force anisotropic mesh adaptation without metric.
``-ar x``
    Value for angle detection.
``-octree n``
	Maximum number of vertex per octree cell.
``-hausd x``
	Maximal Hausdorff distance for the boundaries approximation.
``-hgrad x``
	Gradation value.
``-hmax x``
	Maximal edge size.
``-hmin x``
	Minimal edge size.
``-hsiz x``
	Build a constant size map of size x.
``-lag [n]``
    Perform lagrangian movement of boundaries of ref 10. By default, n = 0.
``-ls [n]``
    Create mesh of isovalue n (0 if n is not provided).
``-lssurf [n]``
	Split mesh boundaries along isovalue n (0 if n is not provided).
``-3dMedit n``
    Save the 2D mesh in a 3d .mesh file if n=1. Read and save the mesh in a 3d .mesh file if n=2.
``-nofem``
	Allow the creation of elements with more than one boundary faces.
``-noinsert``
	No point insertion/deletion.
``-nomove``
	No point relocation.
``-nosurf``
	No surface modifications.
``-noswap``
	No edge flipping.
``-nr``
	No angle detection.
``-nreg n``
	Turn on (n=1) or off (n=0) normal regularization.
``-nsd n``
	Only save the subdomain of index n. Save all subdomains if n=0 (default).
``-optim``
	Mesh improvement without edge size modification.
``-optimLES``
    Strong isotropic mesh optimization for LES computations: tries to reduce the mesh skewness (available only in isotropic mode).
``-opnbdy``
	Preseve an open boundary inside a volume mesh (triangles at the interface between tetra of same references).
``-rmc [x]``
	Remove small parasitic componants embedded in the level-set (componants whose volume fraction is less than x of the mesh volume (1e-5 if x is not provided). Available only in ls mode.
``-rn``
	Turn on (n=1) or off (n=0) the renumbering using SCOTCH.
``-xreg``
	Smoothing/regularization of the position of boundary points using laplacian - anti-laplacian technic.