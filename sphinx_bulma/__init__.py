import os

from sphinx_bulma import _version as version

def get_path():
  """
  Shortcut for users whose theme is next to their conf.py.
  """
  return os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

def update_context(app, pagename, templatename, context, doctree):
  context['sphinx-bulma-version'] = version.__version__

def setup(app):
  theme_path = os.path.abspath(os.path.dirname(__file__))
  app.add_html_theme('sphinx_bulma', theme_path)
  app.connect('html-page-context', update_context)

  return {
    'version': version.__version__,
    'parallel_read_safe': True
  }
