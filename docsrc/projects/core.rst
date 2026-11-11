I. The Symbolic Core & Discovery Engine
=======================================

.. rubric:: Exact Algebraic Modeling, Interactive Visualization & Automated Discovery

The symbolic core provides the mathematical substrate on which every GEOMETOR construction, verification script, and studio broadcast runs.

----

``model`` — The Symbolic Construction Engine
--------------------------------------------

* **Documentation**: `geometor.github.io/model <https://geometor.github.io/model/>`_
* **Repository**: `github.com/geometor/model <https://github.com/geometor/model>`_ · **PyPI**: `geometor-model <https://pypi.org/project/geometor-model/>`_

``geometor.model`` implements compass-and-straightedge geometry in pure symbolic algebra (`SymPy <https://www.sympy.org/>`_):

* **Exact Primitives & Closed-Form 2D Intersections**: Points, infinite lines ``[ A B ]``, circles ``( A B )``, segments ``/ A B /``, polygons ``< A B C >``, wedges, and polynomial loci—with fast closed-form algebraic intersection deduplication and scoped subconstructions.
* **Rational & Projective Invariants (`invariants.py`)**: Exact symbolic ``quadrance``, ``line_spread``, ``vertex_spread``, ``cross``, ``cross_ratio``, and ``is_harmonic`` verification without transcendental rounding error.
* **Constructive Proof & Ancestral DAGs (`proof.py`, `ancestors.py`)**: Every derived point records the exact ancestral chain of givens, lines, and circles required to construct it, plus JSON serialization for downstream rendering and analysis.

----

``explorer`` — Interactive SVG Workbench
----------------------------------------

* **Documentation**: `geometor.github.io/explorer <https://geometor.github.io/explorer/>`_
* **Repository**: `github.com/geometor/explorer <https://github.com/geometor/explorer>`_

``geometor.explorer`` unifies visual inspection, interactive construction, and print/video SVG export (superseding the earlier standalone ``render`` prototype):

* **Web Canvas & Symbolic CLI**: Construct and inspect ``geometor.model`` figures interactively in the browser with pan/zoom SVG viewports, KaTeX algebraic coordinate inspection, and ancestral highlighting.
* **Step-by-Step Timeline & Sheet Export**: Scrub through construction history step by step or export publication-grade vector figures for Sphinx Book Codices and QHD broadcasts.

----

``divine`` — Golden Ratio & Harmonic Discovery
----------------------------------------------

* **Documentation**: `geometor.github.io/divine <https://geometor.github.io/divine/>`_
* **Repository**: `github.com/geometor/divine <https://github.com/geometor/divine>`_ · **PyPI**: `geometor-divine <https://pypi.org/project/geometor-divine/>`_

Once a model is constructed, ``geometor.divine`` scans every collinear point set on every line in the field to uncover emergent proportional structures:

* **Exact Golden Sections**: Identifies collinear triples :math:`(A, B, C)` whose segment ratios simplify algebraically to :math:`\phi = \frac{1 + \sqrt{5}}{2}` or :math:`\frac{1}{\phi} = \phi - 1`.
* **Golden Chains & Harmonic Ranges**: Groups contiguous golden sections into self-similar geometric progressions (*golden chains*) and detects projective harmonic quadruples :math:`(A, B; C, D) = -1`.

----

``trees`` — Monotone Planar Tree Drawings
-----------------------------------------

* **Repository**: `github.com/geometor/trees <https://github.com/geometor/trees>`_

Investigates straight-line monotone planar drawings of arbitrary rooted trees on compact integer grids using **Stern–Brocot mediant trees** and **Farey rational sequences**—connecting discrete number-theoretic mediants directly to crossing-free geometric graph layouts.
