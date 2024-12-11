Introduction
************

About **mmg**
=============



**mmg** is an open-source software for bidimensional and tridimensional
surface and volume remeshing. 
**mmg** source code is available on `github.com <https://github.com/MmgTools/mmg>`_.

It is compatible with most operating systems (Linux, macOS, Windows).

**mmg** provides 3 applications and 4 libraries:
  * the **mmg2d** application and library: mesh generation from a set of edges, adaptation and optimization of a bidimensional triangulation, and isovalue discretization;
  * the **mmgs** application and library: adaptation and optimization of a surface triangulation and isovalue discretization;
  * the **mmg3d** application and library: adaptation and optimization of a tetrahedral mesh, isovalue discretization and lagrangian movement;
  * the **mmg** library gathering the **mmg2d**, **mmgs** and **mmg3d** libraries.

Downloading and installing **mmg**
==================================

For the download and installation of **mmg**, please refer to the :doc:`installation` section.

Documentation
=============

Project web page
----------------

Actualities of the project and software tutorials can be found on the [mmgtools](http://www.mmgtools.org) web page.

Forum
-----

Share your comments and issues with other members of the Mmg community on the [Mmg forum](https://forum.mmgtools.org/).

GitHub Wiki
-----------

More detailed information about the compilation and configuration of Mmg applications is available on the project [wiki](https://github.com/MmgTools/mmg/wiki).

Man pages
---------

Man pages are available inside the **doc/man** directory:
  * To see the **mmg2d** man page, just run ``man ./doc/man/mmg2d.1.gz``
  * To see the **mmgs** man page, run ``man ./doc/man/mmgs.1.gz``
  * To see the **mmg3d** man page, run ``man ./doc/man/mmg3d.1.gz``

Code documentation
------------------

Run the ``make doc`` command to build the Doxygen documentation, after running ``cmake``
  with the option ``-DBUILD_DOC=yes`` if you did not already do so.
  You may wish to adapt ``build/Doxyfile`` to your liking.
  * To see the **mmg** documentation, open the file ``<build>/doc/index.html``.

Platforms
=========

The **mmg** applications are tested on macOS and on most of the Linux platforms.

Contributing
============

Your contributions to the **mmg** project are welcome. You can help us to improve
our code by many means:
  * pull requests: please follow the [guidelines on the wiki](https://github.com/MmgTools/Mmg/wiki/Developers-wiki#pull-requests);
  * feature requests: please use the [Mmg forum](https://forum.mmgtools.org/);
  * bug reports: please use the [GitHub issue tracker](https://github.com/MmgTools/mmg/issues/new);

About the team
==============

Mmg's current developers and maintainers are Charles Dapogny, Cécile Dobrzynski, Pascal Frey and Algiane Froehly.

Contact: contact@mmgtools.org

License and copyright
=====================

Code is under the [terms of the GNU Lesser General Public License](https://raw.githubusercontent.com/MmgTools/mmg/master/LICENSE).

Copyright © Bx INP/Inria/UBordeaux/UPMC, 2004- .

Reference
=========

[Tetrahedral remeshing in the context of large-scale numerical simulation and high performance computing - _G. Balarac, F. Basile, P. Bénard, F. Bordeu, J.-B. Chapelier, L. Cirrottola, G. Caumon, C. Dapogny, P. Frey, A. Froehly, G. Ghigliotti, R. Laraufie, G. Lartigue, C. Legentil, R. Mercier, V. Moureau, C. Nardoni, S. Pertant and M. Zakari_ - submitted, (2021)](https://membres-ljk.imag.fr/Charles.Dapogny/publis/mmgapp2.pdf)

[Three-dimensional adaptive domain remeshing, implicit domain meshing, and applications to free and moving boundary problems - _C. Dapogny, C. Dobrzynski and P. Frey_ - April 1, 2014 - _JCP_](http://www.sciencedirect.com/science/article/pii/S0021999114000266)


