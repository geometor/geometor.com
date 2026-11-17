from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from photon_platform.publish.global_conf import *
import geometor.com as module

version = module.__version__

org = "geometor"
org_name = "GEOMETOR"

repo = "geometor.com"
repo_name = "geometor.com"

setup_globals(org, org_name, repo, repo_name)

if "autoapi.extension" in extensions:
    extensions.remove("autoapi.extension")

exclude_patterns.append("intro.rst")

# Portal does not build Python/SymPy API autodocs; keep only sister GEOMETOR inventories
intersphinx_mapping.pop("python", None)
intersphinx_mapping.pop("sympy", None)

html_theme = "foundation"
site_title = "GEOMETOR"
project = site_title
html_title = site_title
blog_title = site_title

# Used for canonical URLs and the CNAME file created by sphinx.ext.githubpages
html_baseurl = "https://geometor.com/"
html_base_url = "https://geometor.com/"
blog_baseurl = "https://geometor.com/"

html_css_files = list(globals().get("html_css_files", [])) + ["css/directory.css"]
html_js_files = list(globals().get("html_js_files", [])) + ["js/directory.js"]
