# Standard
from __future__ import annotations

import datetime

# ----------------------------------------------------------------------------
# General Settings
# ----------------------------------------------------------------------------
extensions = ["sphinx.ext.autodoc"]
templates_path = ["_templates"]
source_suffix = ".rst"
master_doc = "index"
project = "log_color"
copyright = f"2017 - {datetime.datetime.now().year}, Brant Watson"
version = "1.0.7"
release = "0"
exclude_patterns = []
pygments_style = "sphinx"

# ----------------------------------------------------------------------------
# HTML Settings
# ----------------------------------------------------------------------------
html_theme = "sphinx_rtd_theme"
html_show_copyright = True
htmlhelp_basename = "logcolordoc"
