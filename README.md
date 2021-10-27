![Sphinx Bulma Theme](banner.png)

[![CodeQL](https://github.com/oAGoulart/sphinx-bulma/actions/workflows/codeql-analysis.yml/badge.svg?branch=master)](https://github.com/oAGoulart/sphinx-bulma/actions/workflows/codeql-analysis.yml)
[![GitHub Pages deploy](https://github.com/oAGoulart/sphinx-bulma/actions/workflows/gh-pages.yml/badge.svg)](https://github.com/oAGoulart/sphinx-bulma/actions/workflows/gh-pages.yml)

A simple responsive theme for sphinx. This theme is in it's early stage of development so only 
contains limited options.

## Installing

```sh
pip install sphinx_bulma
```

## Configuration

The theme's project-wide options are defined in the `sphinx_bulma/theme.conf`
file, and can be defined in your project's `conf.py` via
`html_theme_options`. For example:

```py
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
  'sidebar': 'True'                # if true sidebar will be rendered
}
```
