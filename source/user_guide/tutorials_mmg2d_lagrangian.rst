#################
Lagrangian motion
#################

You can apply a motion to an object using Mmg. For this, there are some prerequisites:

* build Mmg with the lagrangian option enabled:
   * as Mmg propagates the movement of the boundary inside the mesh using a linear elasticity solver,
     you will need to build and install the `Linear Elasticity <https://github.com/ISCDtoolbox/LinearElasticity>`_ 
     solver of the ISCD (thanks to  C.Dapogny and P. Frey);
   * Mmg must detect the LinearElasticity library at CMake configuration step. 
     If not, you can help Mmg by giving the LinearElasticity directory using the ELAS_DIR CMake variable::

        cmake -DELAS_DIR=$PATH_TO_ELAS
   * You can then build Mmg. If everything works fine, the -lag option will be available. You can check it by calling the Mmg help::

        mmg2d_O3 -h
* apply the motion to your mesh:
   * Mmg will move the boundaries of references 10 only;
   * Mmg will forbid the movements of the boundaries of the embedded box. As consequences:
       * if a surface of reference 10 intersect the embedded box, the surface will not move at the intersection;
       * an object can’t go out of the embedded box (Mmg will stop the movement of the object when the quality of the elements between the object and the box will become too bad).
   * The lagrangian motion in Mmg works in the context of the small deformations. 
     Thus, the prescribed displacement must be small enough. If not, it is very probable that Mmg will stop before applying the entire movement.
     The proportion of the displacement realized is printed in the standard output and updated at each iteration (1 being the entire prescribed displacement)::

        —> Realized displacement: 0.187272

   * Mmg provide 3 different modes:
       * -lag 0: the object is moved inside the mesh using point relocation only (constant connectivity);
       * -lag 1: edge swapping is allowed but there is no point insertion/collapse;
       * -lag 2: all operators of the remsher are allowed (point insertion/collapse, edge swapping, point relocation).


*********************************************
Lagrangian movement of a ball inside a tunnel
*********************************************

We start from a mesh containing a circle whose boundary has reference 10 (the :download:`lag-mot2D.mesh </meshes/lag-mot2D.mesh>` file). 
Mmg allows to provide a displacement at mesh nodes (you must specified one displacement vector per node) in a Medit solution file. 
Here, we provide a displacement of 20 at circle nodes and 0 at other nodes in the :download:`lag-mot2D.sol </meshes/lag-mot2D.sol>` file 
(note that Mmg will automatically propagates the displacement in a given number of layers around the circle).

.. figure:: /figures/user_guide/lagmotion1.png
    :align: center

    Figure 1: Initial mesh. The red arrow represent the vector displacement applied to the circle boundary. 
    The tunnel is of size 30 and we ask for a displacement of 20.

To apply the displacement, you just need to run the mmg2d application with the -lag option and the wanted lagrangian mode
 (the solution file has the same name than the mesh so it is automatically detected).

Displacement at constant connectivity
#####################################

Using the following command::

    mmg2d_O3 -lag 0 lag-mot2D.mesh

we obtain the following mesh:

.. figure:: /figures/user_guide/lagmotion2.png
    :align: center

    Figure 2: output mesh obtaining using point relocation only (-lag 0)

Note that mmg can’t achieve the entire displacement as the mesh become too bad and edge swap and point insertion/collapse are forbidden.
Mmg output shows that we perform near 15.5% of the wanted displacement and that the worst element quality is of 0.000003 
(see the following extract of the standard output of Mmg)::

    ** Cumulative time: 0.001s sec. ---> Realized displacement: 0.155372 -- PHASE 2 COMPLETED. 0.018s -- MESH QUALITY 270 BEST 0.991985 AVRG. 0.528540 WRST. 0.000003 (157) HISTOGRAMM: 93.33 % > 0.12

Displacement with constant number of nodes
##########################################

Using the following command::

    mmg2d_O3 -lag 1 lag-mot2D.mesh

We obtain the following mesh:

.. figure::/figures/user_guide/lagmotion3.png
    :align: center

    Figure 3: output mesh obtaining using point relocation and edge swap (-lag 1)

This time, the entire movement has been applied and the output mesh quality is better::

    ** Cumulative time: 0.003s sec. ---> Realized displacement: 1.000000 -- GRADATION : 1.300000 (2.300000) -- PHASE 2 COMPLETED. 0.081s -- MESH QUALITY 270 BEST 0.999292 AVRG. 0.807426 WRST. 0.184979 (141) HISTOGRAMM: 100.00 % > 0.12

Displacement with point insertion, collapse, relocation and edge swap
#####################################################################

Using the following command::

    mmg2d_O3 -lag 2 lag-mot2D.mesh

We obtain the following mesh:

.. figure:: /figures/user_guide/lagmotion4.png
    :align: center

    Figure 4: output mesh obtaining using all the remesher operators (-lag 2)

The process is slower but the output quality much better::

    -- MESH QUALITY 301 BEST 0.999723 AVRG. 0.921515 WRST. 0.654973 (284)

Remark: The applied displacement is very large. As Mmg propagates the displacement in a given number 
of layers of elements around the object, the number of layers may constrain the movement.
By default, Mmg takes 20 layers of elements to propagate the displacement.
In this example it is enough to move the circle but in other cases (if the initial mesh is very fine for example) it can impose a smaller displacement.