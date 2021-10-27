![Sphinx Bulma Theme](banner.png)
#
[![Build Sass](https://github.com/oAGoulart/sphinx-bulma/actions/workflows/sass.yml/badge.svg)](https://github.com/oAGoulart/sphinx-bulma/actions/workflows/sass.yml)
[![CodeQL](https://github.com/oAGoulart/sphinx-bulma/actions/workflows/codeql-analysis.yml/badge.svg?branch=master)](https://github.com/oAGoulart/sphinx-bulma/actions/workflows/codeql-analysis.yml)
[![GitHub Pages deploy](https://github.com/oAGoulart/sphinx-bulma/actions/workflows/gh-pages.yml/badge.svg)](https://github.com/oAGoulart/sphinx-bulma/actions/workflows/gh-pages.yml)

> Currently updating major changes and updates from [AccentDesign/karma_sphinx_theme](https://github.com/AccentDesign/karma_sphinx_theme)
> 
> Check [todo] list for planned features to be included on release version **v0.1.0**

### A simple responsive theme for sphinx using **[Bulma]** featuring:
  1.  Has built-in dark/light color themes using native _CSS_ and _JavaScript_
  2.  Sphinx built-in text search engine
  3.  Extended _Sass_ rulesets from bulma
  4.  Support for user-defined favicon and logo from sphinx config
  5.  Custom icon font made with [Fontello]
  6.  Theme user-defined documentation repository reference

### Yet to be done a.k.a todo
  - [ ] Support user-defined colors (at least primary)
  - [ ] Enable custom _Sass_ rules on docs build
  - [ ] Examples of use with [breathe] for **C++** docs

## Installing

Using pip to install from this repository:

```sh
pip install git+https://github.com/oAGoulart/sphinx-bulma.git@v0.0.10
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
  'sidebar': True                  # if true sidebar will be rendered
}
```

[Bulma]: https://bulma.io/
[Fontello]: https://fontello.com/
[todo]: /#L19
[breathe]: https://github.com/michaeljones/breathe
