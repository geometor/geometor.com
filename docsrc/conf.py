from photon_platform.publish.global_conf import *

version = ""

org = "geometor"
org_name = "geometor"

repo = "geometor.com"
repo_name = "geometor.com"

setup_globals(org, org_name, repo, repo_name)

if 'autoapi.extension' in extensions:
    extensions.remove('autoapi.extension')

html_title = "GEOMETOR"
blog_title = "GEOMETOR"

html_baseurl = 'https://geometor.com/'
