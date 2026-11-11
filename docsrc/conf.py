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
html_title = "GEOMETOR"
blog_title = "GEOMETOR"
project = "GEOMETOR"

# Used for canonical URLs and the CNAME file created by sphinx.ext.githubpages
html_baseurl = "https://geometor.com/"
html_base_url = "https://geometor.com/"
blog_baseurl = "https://geometor.com/"
