# -*- coding: utf-8 -*-
import sys
import os
from datetime import datetime

sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('.'))

extensions = [
  'sphinx.ext.autodoc',
  'sphinx.ext.mathjax',
  'sphinx.ext.viewcode',
]
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

project = u'Sphinx Bulma Theme'
year = datetime.now().year
copyright = u'%d Augusto Goulart' % year

exclude_patterns = ['_build']

html_logo = 'static/logo.png'
html_favicon = 'static/favicon.ico'
html_theme = 'sphinx-bulma'
html_theme_options = {
  'display_git': True,
  'git_host': 'github.com',
  'git_user': 'oAGoulart',
  'git_repo': 'sphinx-bulma',
  'git_version': 'master/docs/',
  'git_icon': 'github-circled',
  'git_desc': 'Edit on GitHub'
}

html_theme_path = ["../src"]
