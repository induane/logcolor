# Standard
import datetime
import sphinx_rtd_theme

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
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_show_copyright = True
htmlhelp_basename = "logcolordoc"
