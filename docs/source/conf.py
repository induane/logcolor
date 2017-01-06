# -*- coding: utf-8 -*-
#
# logcolor documentation build configuration file, created by
# sphinx-quickstart on Tue Jan 27 12:04:31 2015.
import datetime
import sphinx_rtd_theme

extensions = [
    'sphinx.ext.autodoc',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'logcolor'
copyright = u'2017 - %s, Brant Watson' % datetime.datetime.now().year

version = '1.0.1'
# The full version, including alpha/beta/rc tags.
release = '0'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True

# Output file base name for HTML help builder.
htmlhelp_basename = 'logcolordoc'
