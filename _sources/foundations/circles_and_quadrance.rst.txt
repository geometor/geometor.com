Circles, Rotation & Quadrance
=============================

.. rubric:: A Circle Is a Perpendicular Relationship Between Two Points

If a straight line projects linear extension, **a circle is the locus of continuous perpendicular rotation of one point about another** (`G.10 <https://geometor.github.io/elements/elements2/G.10/>`_, `G.15 <https://geometor.github.io/elements/elements2/G.15/>`_).

Center vs. Radius Point: Directional Asymmetry
----------------------------------------------

Like a line, a circle is instantiated from two points—yet unlike a line, **those two points are not interchangeable**:

* ``( A B )`` places the stationary **center** at :math:`A = (h, k)` and sweeps through the **radius point** :math:`B`;
* ``( B A )`` reverses their roles, centering at :math:`B` and sweeping through :math:`A`.

Their shared radius squared is the **quadrance** :math:`Q(A, B)`:

.. math::

   Q(A, B) = (x_B - x_A)^2 + (y_B - y_A)^2 = r^2

and the algebraic locus of ``( A B )`` is purely quadratic in :math:`(x, y)` without a single square root in its defining polynomial:

.. math::

   (x - h)^2 + (y - k)^2 - Q(A, B) = 0

Quadratic Extensions & The Equidistant Poles
--------------------------------------------

Whereas intersecting two lines stays inside the current rational field, intersecting a circle with a line or a second circle solves a **quadratic equation**—introducing quadratic surds (:math:`\sqrt{\Delta}`) that unlock higher symmetries:

1. **First Compass Symmetry (`( A B ) ∩ ( B A )`)**: Intersecting the twin unit circles centered at :math:`(0, 0)` and :math:`(1, 0)` solves :math:`x = \frac{1}{2}` and :math:`\left(\frac{1}{2}\right)^2 + y^2 = 1`, selecting the **Equidistant Poles**:

   .. math::

      C = \left(\frac{1}{2},\, \frac{\sqrt{3}}{2}\right), \qquad
      C' = \left(\frac{1}{2},\, -\frac{\sqrt{3}}{2}\right)

   In a single symmetric act, the Vesica Piscis generates the **equilateral triangle** (`I.1 / G.17 <https://geometor.github.io/elements/elements2/G.17/>`_), **perpendicularity** (:math:`[A B] \perp [C C']`), **bisection** (:math:`M = (\tfrac{1}{2}, 0)`), and the quadratic field :math:`\mathbb{Q}(\sqrt{3})`.

2. **Orthogonal Symmetry (`√2`)**: Sweeping a circle centered at midpoint :math:`M` through :math:`A` and :math:`B` cuts the perpendicular pole line :math:`[C C']` at :math:`\left(\frac{1}{2}, \pm \frac{1}{2}\right)`, unfolding the **square**, right triangles, and :math:`\mathbb{Q}(\sqrt{2})`.

3. **Pentagonal & Golden Symmetry (`√5` and `φ`)**: Coupling the unit radius (:math:`1`) with the bisected half-unit (:math:`\frac{1}{2}`) along orthogonal axes produces hypotenuse quadrance :math:`Q = 1^2 + \left(\frac{1}{2}\right)^2 = \frac{5}{4}`, whose rotation onto the baseline yields :math:`\frac{1}{2} + \frac{\sqrt{5}}{2} = \phi` (`II.11 <https://geometor.github.io/euclid/heath/volume_I/book_ii/propositions/11/>`_, `IV.10–11 <https://geometor.github.io/euclid/heath/volume_II/book_iv/propositions/11/>`_).
