from ablog.conf import *

org = 'geometor'
org_name = 'GEOMETOR'

repo = 'geometor.com'
repo_name = repo

blog_title = f'{org_name}'
project = blog_title
version = ''  # The short X.Y version.
release = ''  # The full version, including alpha/beta/rc tags.

copyright = f'{year}, {org_name}'
author = f'{org_name}'

# Base URL for the website, required for generating feeds.
# e.g. blog_baseurl = "http://example.com/"
blog_baseurl = f'https://{repo}'
html_base_url = blog_baseurl
html_baseurl = blog_baseurl

blog_authors = {
    "phi": ("phi ARCHITECT", None),
}

html_theme_options = {
    'logo': 'logo.png',
    'logo_name': True,
    'github_user': org,
    'github_repo': repo,
    'github_button': True,
}

