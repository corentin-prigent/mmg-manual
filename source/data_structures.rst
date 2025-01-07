###############
Data structures
###############

In **mmg**, several data structures are defined in order to represent and 
manipulate different entities such as tetrahedra, triangles, or meshes.

Mesh
----

The main data structure that is used throughout **mmg** is the mesh structure ``MMG5_Mesh``.
This structure contains the following fields:

.. c:struct:: MMG5_Mesh

    .. c:var:: size_t memMax

        Maximum memory available

    .. c:var:: size_t memCur

        Current memory used

    .. c:var:: double gap

        Gap for table reallocation

    .. c:var:: int ver

        Version of the mesh file

    .. c:var:: int dim

        Dimension of the mesh

    .. c:var:: int type

        Type of the mesh

    .. c:var:: MMG5_int npi

        Number of ??

    .. c:var:: MMG5_int nti

        Number of ??

    .. c:var:: MMG5_int nai

        Number of ??

    .. c:var:: MMG5_int nei

        Number of ??

    .. c:var:: MMG5_int np

        Number of ??

    .. c:var:: MMG5_int na

        Number of ??

    .. c:var:: MMG5_int nt

        Number of ??

    .. c:var:: MMG5_int ne

        Number of ??

    .. c:var:: MMG5_int npmax

        Number of ??

    .. c:var:: MMG5_int namax

        Number of ??

    .. c:var:: MMG5_int ntmax

        Number of ??

    .. c:var:: MMG5_int nemax

        Number of ??

    .. c:var:: MMG5_int xpmax

        Number of ??

    .. c:var:: MMG5_int xtmax

        Number of ??

    .. c:var:: MMG5_int nquad

        number of quadrangles

    .. c:var:: MMG5_int nprism

        number of prisms

    .. c:var:: int nsols

        number of solutions (metric excluded) in the solution file (lower than \a NSOLS_MAX)

    .. c:var:: MMG5_int nc1

        number of ??

    .. c:var:: MMG5_int base

        Used with \a flag to know if an entity has been treated

    .. c:var:: MMG5_int mark

        Flag for delaunay (to know if an entity has been treated)

    .. c:var:: MMG5_int xp

        Number of surface points

    .. c:var:: MMG5_int xt

        Number of triangles/tetrahedra

    .. c:var:: MMG5_int xpr

        Number of prisms

    .. c:var:: MMG5_int npnil

        Index of first unused point

    .. c:var:: MMG5_int nenil

        Index of first unused element

    .. c:var:: MMG5_int nanil

        Index of first unused edge (2D only)

    .. c:var:: MMG5_int *adja

        !< Table of tetrahedron adjacency: if
                    \f$adja[4*(i-1)+1+j]=4*k+l\f$ then the \f$i^{th}\f$ and
                    \f$k^th\f$ tetrahedra are adjacent and share their
                    faces \a j and \a l (resp.)

    .. c:var:: MMG5_int *adjt

        Table of triangles adjacency: if
                    \f$adjt[3*(i-1)+1+j]=3*k+l\f$ then the \f$i^{th}\f$ and
                    \f$k^th\f$ triangles are adjacent and share their
                    edges \a j and \a l (resp.)

    .. c:var:: MMG5_int *adjapr

        Table of prisms adjacency: if
                    \f$adjapr[5*(i-1)+1+j]=5*k+l\f$ then the \f$i^{th}\f$ and
                    \f$k^th\f$ prism are adjacent and share their
                    faces \a j and \a l (resp.) 

    .. c:var:: MMG5_int *adjq

        Table of quadrangles adjacency: if
                    \f$adjq[4*(i-1)+1+j]=4*k+l\f$ then the \f$i^{th}\f$ and
                    \f$k^th\f$ quadrilaterals are adjacent and share their
                    edges \a j and \a l (resp.)

    .. c:var:: int *ipar

        Store indices of the local parameters

    .. c:var:: MMG5_pPoint Point

        Pointer toward the :c:struct:`MMG5_Point` structure

    .. c:var:: MMG5_pxPoint xPoint

        Pointer toward the :c:struct:`MMG5_Point` structure

    .. c:var:: MMG5_pTetra tetra

        Pointer toward the :c:struct:`MMG5_Point` structure

    .. c:var:: MMG5_pxTetra xtetra

        Pointer toward the :c:struct:`MMG5_Point` structure

    .. c:var:: MMG5_pPrism prism

        Pointer toward the :c:struct:`MMG5_Point` structure

    .. c:var:: MMG5_pxPrism xprism

        Pointer toward the :c:struct:`MMG5_Point` structure

    .. c:var:: MMG5_pTria tria
        
        Pointer toward the :c:struct:`MMG5_Point` structure

    .. c:var:: MMG5_pQuad quadra

        Pointer toward the :c:struct:`MMG5_Point` structure

    .. c:var:: MMG5_pEdge edge

        Pointer toward the :c:struct:`MMG5_Point` structure

    .. c:var:: MMG5_HGeom htab

        :c:struct:`MMG5_Point` structure

    .. c:var:: MMG5_Info info

        :c:struct:`MMG5_Point` structure

    .. c:var:: char *namein

        Input mesh name

    .. c:var:: char *nameout

        Output mesh name


Tetrahedra are represented using the **MMG5_Tetra** structure:

.. c:struct:: MMG5_Tetra

    .. c:var:: double qual

        Quality of the element

    .. c:var:: MMG5_int v[4]

        Vertices of the tetrahedron

    .. c:var:: MMG5_int ref

        Reference of the tetrahedron

    .. c:var:: MMG5_int base

        Description

    .. c:var:: MMG5_int mark

        Used for delaunay

    .. c:var:: MMG5_int xt

        Index of the surface \ref MMG5_xTetra associated to the
                 tetrahedron (only for tetrahedra that are adjacent to
                 surfaces)

    .. c:var:: MMG5_int flag

        flag

    .. c:var:: uint16 tag

        tag
