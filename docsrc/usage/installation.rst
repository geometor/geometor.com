Installation & Workspace Setup
==============================

.. rubric:: Python 3.13 & ``uv`` Environment Guide

GEOMETOR packages target modern **Python 3.13+** and recommend `uv <https://docs.astral.sh/uv/>`_ for fast, reproducible virtual environments.

Installing Release Packages from PyPI
-------------------------------------

To install the core symbolic engine and golden-section analyzer into a fresh environment:

.. code-block:: bash

   uv venv --python 3.13
   source .venv/bin/activate
   uv pip install geometor-model geometor-divine

Working from Source Repositories
--------------------------------

Every repository under `github.com/geometor <https://github.com/geometor>`_ follows a clean ``src/geometor/<repo_name>/`` namespace package layout and can be cloned and synced directly with ``uv``:

.. code-block:: bash

   git clone https://github.com/geometor/model.git
   cd model
   uv sync
   uv run pytest

Building Book Codices Locally
-----------------------------

GEOMETOR's multi-track Book Codices use Sphinx with the ``foundation`` Scriptorium theme from `photon-platform/publish <https://github.com/photon-platform/publish>`_:

.. code-block:: bash

   uv tool install git+https://github.com/photon-platform/publish.git
   publish build
