# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
import sys  # noqa: I001
# sys.path.insert(0, os.path.abspath('.'))
from sphinx.locale import _


# -- Project information -----------------------------------------------------

project = 'UMS Stack'
copyright = '2024, Univention GmbH'
author = 'Team openDesk Dev'

# The full version, including alpha/beta/rc tags
release = '0.0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.intersphinx",
    "sphinx_copybutton",
    "sphinx_inline_tabs",
    "sphinx_last_updated_by_git",
    "sphinxcontrib.inkscapeconverter",
    "sphinxcontrib.mermaid",
    "sphinxcontrib.spelling",
    "sphinxcontrib.video",
    "univention_sphinx_extension",
    'myst_parser',
    'sphinx.ext.ifconfig',
    'sphinx.ext.todo',
]

intersphinx_mapping = {
    # TODO: SSL Error, needs likely a certificate in the container to be installed
    # "uv-team-souvap-docs": (
    #     "https://univention.gitpages.knut.univention.de/internal/team-souvap-docs", None),
    # "uv-quickstart": ("https://docs.software-univention.de/quickstart/5.0/en/", None),
    # "uv-manual": ("https://docs.software-univention.de/manual/5.0/en/", None),
}

copybutton_prompt_text = r"\$ |> |.+# "
copybutton_prompt_is_regexp = True
copybutton_line_continuation_character = "\\"
copybutton_here_doc_delimiter = "EOT"

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

html_title = f'{project} Documentation'

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# See https://git.knut.univention.de/univention/documentation/univention_sphinx_book_theme
html_theme = 'univention_sphinx_book_theme'


# The following parts are inspired from the dev-onboarding document.
# See https://git.knut.univention.de/univention/internal/dev-onboarding

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = [
    # Not yet in use.
    # '_static',
]
html_last_updated_fmt = "%a, %d. %b %Y at %H:%M (UTC%z)"

# https://github.com/mgeier/sphinx-last-updated-by-git
git_last_updated_timezone = 'Europe/Berlin'
numfig = True
numfig_format = {
    "figure": _("Figure %s:"),
    "table": _("Table %s:"),
    "code-block": _("Listing %s:"),
    "section": _("Section %s:"),
}

suppress_warnings = ['git.too_shallow']

if "spelling" in sys.argv:
    extensions.append("univention_sphinx_extension")
    spelling_lang = "en_US"
    spelling_show_suggestions = True
    spelling_word_list_filename = ["spelling_wordlist"]

tls_cacerts = {
}

linkcheck_allowed_redirects = {
    r"https://git\.knut\.univention\.de/.*": r"https://git\.knut\.univention\.de/users/sign_in",
}

linkcheck_ignore = [
]

root_doc = "index"
pdf_doc_base = "ums-stack"

html_context = {
    # Not generating a PDF at the moment
    # "pdf_download_filename": f"{pdf_doc_base}.pdf",
}

html_theme_options = {
    "path_to_docs": "docs/",
    "repository_branch": "main",
    "repository_provider": "gitlab",
    "repository_url": "https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack",
    "use_edit_page_button": True,
    "use_repository_button": True,
}

latex_engine = 'lualatex'
latex_show_pagerefs = True
latex_show_urls = "footnote"
latex_documents = [
    (root_doc, f'{pdf_doc_base}.tex', project, author, "manual", False)]
latex_elements = {
    "papersize": "a4paper",
}

univention_doc_basename = ""
