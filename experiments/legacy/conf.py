extensions = []
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = 'CrossCompute'
copyright = '2017, CrossCompute Inc.'
author = 'CrossCompute Inc.'
version = '1.5'
release = '1.5.0'
language = None
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'
todo_include_todos = False
html_theme = 'alabaster'
html_static_path = ['_static']
html_sidebars = {
    '**': [
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
    ]
}
htmlhelp_basename = 'CrossComputedoc'
