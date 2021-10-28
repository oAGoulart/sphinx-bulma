.. Sphinx Bulma Theme documentation master file.

Sphinx Bulma Theme
==================

A simple responsive theme for sphinx using **Bulma** featuring:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
1.  Has built-in dark/light color themes using native CSS and JavaScript
2.  Sphinx built-in text search engine
3.  Extended Sass rulesets from bulma
4.  Support for user-defined favicon and logo from sphinx config
5.  Custom icon font made with [Fontello]
6.  Theme user-defined documentation repository reference

Installing
----------

Using pip to install from this repository:

.. code-block:: shell

   pip install git+https://github.com/oAGoulart/sphinx-bulma.git@v0.0.10

Configuration
-------------

| The theme's project-wide options are defined in the `sphinx_bulma/theme.conf`
| file, and can be defined in your project's `conf.py` via
| `html_theme_options`. For example:

.. code-block:: python

    html_theme_options = {
      'navigation_depth': 2,           # maximum depth of tree
      'includehidden': True,           # if true sidebar may include toctrees marked with hidden option
      'titles_only': False,            # if true removes headers within a page from the sidebar
      'display_git': False,            # if true options below must be set
      'git_host': 'github.com',        # git host url
      'git_user': 'gh-user',           # your git host username
      'git_repo': 'doc-repo',          # doc repository
      'git_blob': 'blob',              # default for github
      'git_version': 'master/docs/',   # docs folder
      'git_icon': 'github',            # icon to show on docs
      'git_desc': 'Check the sources', # link description
      'default_palette': 'dark',       # default color palette (dark or light)
      'sidebar': True                  # if true sidebar will be rendered
    }

Contents
--------

.. toctree::
   :maxdepth: 1

   admonitions
   demo
   lists
   structure
   tables
   api
   changelog
