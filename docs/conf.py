# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'PlumeIA-API'
copyright = '2026, PlumeIA Inc.'
author = 'PlumeIA Inc.'
release = '0.1.2'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
language = 'fr'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_permalinks = False 

html_theme_options = {
    "anchor_hover_bg" : "#2e7eed",
    "body_text": "#000",
    "caption_font_family": 'Open Sans , sans-serif', 
    "code_highlight":  "#2e7eed",
    "fixed_sidebar": True,          
    "font_family": 'Open Sans , sans-serif', 
    "head_font_family":'Open Sans , sans-serif', 
    "link":  "#2e7eed",      
    "link_hover":"#2e7eed",
    "logo": "plume-ia.png",              
    "narrow_sidebar_fg":"#000",
    "page_width": "95%",           
    "sidebar_hr" :  "#2e7eed",
    "sidebar_width": "300px",  
    "show_powered_by": False,
}

# Optional: add custom CSS
html_static_path = ['_static']
html_css_files = ['custom.css']

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.githubpages'
]