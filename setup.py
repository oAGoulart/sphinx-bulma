#!/usr/bin/env python

import codecs
from setuptools import setup

# Version info -- read without importing
_locals = {}
with open('sphinx_bulma/_version.py') as fp:
  exec(fp.read(), None, _locals)
version = _locals['__version__']
name = _locals['__name__']

# README into long description
with codecs.open('README.md', encoding='utf-8') as f:
  readme = f.read()

setup(
  name=name,
  version=version,
  description='A Sphinx theme using Bulma',
  long_description=readme,
  long_description_content_type='text/markdown',
  url='https://github.com/oAGoulart/sphinx-bulma',
  author='Augusto Goulart',
  author_email='josegoulart.aluno@unipampa.edu.br',
  classifiers=[
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Developers',
    'Framework :: Sphinx :: Theme',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
  ],
  keywords='html sphinx theme',
  packages=['sphinx_bulma'],
  include_package_data=True,
  entry_points={
    'sphinx.html_themes': [
      'sphinx_bulma = sphinx_bulma',
    ]
  },
  project_urls={
    'Bug Reports': 'https://github.com/oAGoulart/sphinx-bulma/issues',
    'Source': 'https://github.com/oAGoulart/sphinx-bulma',
  },
)
