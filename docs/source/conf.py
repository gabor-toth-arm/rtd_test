# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'asdasd'
copyright = '2021, Graziella'
author = 'Graziella'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = ['sphinx.ext.autosectionlabel', 'sphinxcontrib.plantuml' ]


templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
