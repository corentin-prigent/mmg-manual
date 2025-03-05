#############################
Mesh adaptation to a solution
#############################

We want to adapt a M6 wing mesh (named aileM6.mesh) 
to an isotropic size map given in the aileM6-met.sol file 
(see figure 1 for the mesh and the metric representation).

Figure 1: Initial mesh of the M6 wing and associated metric : surface of the wing (left) and cut through the volume mesh (right)

Note that our metric is obtained from the density solution using the mshmet software (thanks to C. Dapogny, C.Dobrzynski and P. Frey).
You can adapt the mesh with the following command:

mmg3d_O3 aileM6.mesh -sol aileM6-met.sol -hgrad 2.3 -v 3

    The metric file name is specified using the -sol option.
    More infos about the -sol option

    The -hgrad option controls the ratio between two adjacent edges.
    More infos about the -hgrad option
     
    Last, the -v option to change the application verbosity.
    More infos about the -v option

The final mesh is displayed figure 2.


Figure 2: Final mesh of the M6 wing: surface of the wing (left) and cut through the volume mesh (right)