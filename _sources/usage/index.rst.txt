:navigation: footer
:order: 1

Quickstart
==========

.. rubric:: Constructing & Analyzing Symbolic Geometry in Python

You can explore all GEOMETOR Book Codices and WebGL laboratories directly in your browser without installing anything, or install the symbolic Python libraries locally to construct models, verify invariants, and scan for golden sections.

.. toctree::
   :maxdepth: 2

   installation

Example: Vesica Piscis to the Golden Section
--------------------------------------------

Below is a complete, runnable Python script using ``SymPy`` and ``geometor.model`` to construct two starting points, sweep the **Vesica Piscis**, locate the **Equidistant Poles**, and verify exact rational spread :math:`s = \frac{3}{4}` and golden section ratios:

.. code-block:: python

   import sympy as sp
   from geometor.model import Model
   from geometor.model.invariants import quadrance, line_spread

   phi = (1 + sp.sqrt(5)) / 2

   # 1. Establish the planar field from two given points
   model = Model("vesica_quickstart")
   A = model.set_point(0, 0, classes=["given"], ID="A")
   B = model.set_point(1, 0, classes=["given"], ID="B")
   line_AB = model.construct_line(A, B)

   # 2. Construct the Vesica Piscis
   model.construct_circle(A, B)
   model.construct_circle(B, A)

   # 3. Inspect exact algebraic coordinates discovered by intersection
   for pt in model.points:
       print(f"{model[pt].ID}: ({pt.x}, {pt.y})")

   # 4. Verify exact rational quadrance and spread on equilateral side [ A C ]
   C = sp.Point2D(sp.Rational(1, 2), sp.sqrt(3) / 2)
   line_AC = sp.Line2D(A, C)
   assert quadrance(A, C) == 1
   assert line_spread(line_AB, line_AC) == sp.Rational(3, 4)

Interactive Workbench & Discovery
---------------------------------

* **Visual Exploration (`explorer`)**: Launch the interactive SVG workbench and CLI via `geometor/explorer <https://geometor.github.io/explorer/>`_.
* **Golden Ratio Scanning (`divine`)**: Pass any constructed ``Model`` into `geometor/divine <https://geometor.github.io/divine/>`_ to detect all collinear golden sections, golden chains, and harmonic quadruples automatically.
* **Publishing Book Codices (`publish`)**: All GEOMETOR documentation repositories build from ``docsrc/`` into ``docs/`` via ``publish build`` (`photon-platform/publish <https://github.com/photon-platform/publish>`_).
