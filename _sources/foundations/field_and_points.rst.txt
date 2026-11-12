The Planar Field & Two Starting Points
======================================

.. rubric:: Beginning from Nothing Save Minimal Distinction

Classical compass-and-straightedge geometry operates on a pure planar continuum using only two ideal instruments: an **unmarked straightedge** and a **compass**. Crucially, *neither* instrument can operate on a single isolated point—both require **two points** to project a locus.

Two Givens Establish Unit Measure
---------------------------------

Every GEOMETOR construction begins on a blank slate. The only unconstructed *givens* are the first **two starting points** placed on the field—conventionally :math:`A = (0, 0)` and :math:`B = (1, 0)` (or symmetrically :math:`(-\tfrac{1}{2}, 0)` and :math:`(\tfrac{1}{2}, 0)` around the midpoint origin).

* Their separation defines the **unit measure** (:math:`1`) and **unit quadrance** (:math:`Q = 1`) of the entire model.
* No ruler ticks, protractor degrees, or arbitrary floating-point coordinates are imported from outside. Every subsequent magnitude—:math:`\frac{1}{2}`, :math:`\sqrt{2}`, :math:`\sqrt{3}`, :math:`\sqrt{5}`, :math:`\phi`—must be **earned constructively** through the intersection of lines and circles.

Continuous Loci vs. Graphical Segments
--------------------------------------

In `geometor.model <https://geometor.github.io/model/>`_ and `geometor.explorer <https://geometor.github.io/explorer/>`_:

* **Lines** ``[ A B ]`` and **circles** ``( A B )`` are *infinite or closed continuous proportions* projected across the entire plane. Extending lines beyond the local figure and drawing circles in full exposes remote intersections, harmonic conjugates, and symmetry axes that truncated textbook strokes conceal.
* **Segments** ``/ A B /``, **polygons** ``< A B C >``, and **wedges** are bounded *graphical and metric witnesses* highlighted atop the underlying projections once their endpoint vertices have been constructively selected.

Cartesian Algebra Without Decimal Drift
---------------------------------------

While faithful to Euclid's constructive postulates (`G.14 <https://geometor.github.io/elements/elements2/G.14/>`_–`G.15 <https://geometor.github.io/elements/elements2/G.15/>`_), GEOMETOR unites synthetic geometry with Descartes' coordinate plane and `SymPy <https://www.sympy.org/>`_ symbolic algebra:

.. code-block:: python

   from geometor.model import Model

   model = Model("unit_field")
   A = model.set_point(0, 0, classes=["given"], ID="A")
   B = model.set_point(1, 0, classes=["given"], ID="B")

   # Project baseline and Vesica Piscis
   model.construct_line(A, B)
   model.construct_circle(A, B)
   model.construct_circle(B, A)

   # Every derived point carries exact SymPy coordinates and full ancestry
   for pt in model.points:
       print(f"{model[pt].ID}: ({pt.x}, {pt.y})")

Decimal approximations belong to applied measurement; inside the field, every point preserves its exact algebraic identity back to :math:`A` and :math:`B`.
