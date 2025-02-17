# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import sys
import pathlib
import subprocess, os

project = 'mmg'
copyright = '2024, Prigent'
author = 'Prigent'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

read_the_docs_build = os.environ.get('READTHEDOCS', None) == 'True'

# if read_the_docs_build:

#      subprocess.call('cd ../../build/doc; doxygen', shell=True)

#sys.path.append(pathlib.Path('/Users/corentin/python/lib/python3.13/site-packages/breathe'))

extensions = ['sphinx_math_dollar','sphinx.ext.mathjax']

templates_path = ['_templates']
exclude_patterns = []

#breathe_projects = {"mmg-doxy": "/Users/corentin/Apps/mmg/build/doc/xml"}
#breathe_projects = {"mmg-doxy": "../../build/doc/xml"}
#breathe_default_project = "mmg-doxy"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = "mmg documentation"
html_theme = 'furo'
html_logo  = 'figures/logo-Mmg.png'
html_static_path = ['_static']

html_context = {
    "display_github": True, # Integrate GitHub
    "github_user": "corentin-prigent", # Username
    "github_repo": "mmgTools/mmg", # Repo name
    "github_version": "master", # Version
    "conf_py_path": "/source/", # Path in the checkout to the docs root
}