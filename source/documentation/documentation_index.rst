#############
Documentation
#############

.. toctree::

    Options for remeshing <documentation_options.rst>
    Detailed options <documentation_detailed_options.rst>
    Algorithm overview <developer_overview.rst>
    Remeshing process <remeshing_process.rst>
    Data structures <data_structures.rst>

*************
Documentation
*************

Forum
=====

Share your comments and issues with other members of the Mmg community on the `mmg forum <https://forum.mmgtools.org/>`_.

GitHub Wiki
===========

More detailed information about the compilation and configuration of Mmg applications is available on the project `wiki <https://github.com/MmgTools/mmg/wiki>`_.

Man pages
=========

Man pages are available inside the **doc/man** directory:
  * To see the **mmg2d** man page, just run ``man ./doc/man/mmg2d.1.gz``
  * To see the **mmgs** man page, run ``man ./doc/man/mmgs.1.gz``
  * To see the **mmg3d** man page, run ``man ./doc/man/mmg3d.1.gz``

Code documentation
==================

Run the ``make doc`` command to build the Doxygen documentation, after running ``cmake``
  with the option ``-DBUILD_DOC=yes`` if you did not already do so.
  You may wish to adapt ``build/Doxyfile`` to your liking.
  * To see the **mmg** documentation, open the file ``<build>/doc/index.html``.