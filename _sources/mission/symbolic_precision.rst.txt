Symbolic Precision, Quadrance & Spread
======================================

.. rubric:: Why Exact Algebra Replaces Floating-Point Approximation

Most interactive geometry environments represent points as pairs of 64-bit IEEE-754 floating-point numbers. Within two or three nested circle-circle intersections, rounding error accumulates: three lines that ought to concur at a single Steiner or Kirkman point miss one another by :math:`10^{-15}`, and a ratio of segments can only be tested as ``abs(r - 1.618033988749895) < 1e-9``.

In **GEOMETOR**, decimal approximations belong to applied engineering—not to pure geometric inquiry.

Exact Algebraic Coordinates in ``SymPy``
----------------------------------------

Inside `geometor.model <https://geometor.github.io/model/>`_, every point, line coefficient, circle equation, and intersection is maintained as a closed-form algebraic expression in `SymPy <https://www.sympy.org/>`_:

.. math::

   C = \left(\frac{1}{2},\, \frac{\sqrt{3}}{2}\right), \qquad
   O = \left(\frac{1}{2},\, \frac{\sqrt{3}}{6}\right), \qquad
   G = \left(\frac{1 + \sqrt{5}}{2},\, 0\right)

When ``geometor.divine`` or ``geometor.pappus`` tests collinearity, concurrency, harmonic conjugacy, or Extreme and Mean Ratio, ``sp.simplify(expr) == 0`` proves **exact mathematical identity** across nested quadratic extensions such as :math:`\mathbb{Q}(\sqrt{3}, \sqrt{5})`.

Rational Trigonometry Invariants
--------------------------------

Following Norman J. Wildberger's *Divine Proportions: Rational Trigonometry to Universal Geometry* (explored in full in `geometor/wildberger <https://geometor.github.io/wildberger/>`_ and built directly into ``geometor.model.invariants``), GEOMETOR complements Euclidean distance and transcendental angle with purely algebraic quadratic invariants:

1. **Quadrance** :math:`Q(A_1, A_2)` — squared separation without square roots:

   .. math::

      Q(A_1, A_2) = (x_2 - x_1)^2 + (y_2 - y_1)^2

2. **Spread** :math:`s(\ell_1, \ell_2)` — rational separation of two lines :math:`a_1 x + b_1 y + c_1 = 0` and :math:`a_2 x + b_2 y + c_2 = 0` without inverse trigonometric functions:

   .. math::

      s(\ell_1, \ell_2) = \frac{(a_1 b_2 - a_2 b_1)^2}{(a_1^2 + b_1^2)(a_2^2 + b_2^2)} \in [0, 1]

   Parallel lines have spread :math:`s = 0`; perpendicular lines have spread :math:`s = 1`; the equilateral triangle of the Vesica Piscis has exact rational spread :math:`s = \frac{3}{4}`; and the regular pentagon is governed by the golden spread :math:`s = \frac{5 - \sqrt{5}}{8}`, satisfying the five-fold spread polynomial :math:`S_5(s) = s(16s^2 - 20s + 5)^2 = 0`.

3. **Projective Cross-Ratio** :math:`(A, B; C, D)` — the fundamental projective invariant preserved under central projection (`geometor/pappus <https://geometor.github.io/pappus/>`_):

   .. math::

      (A, B; C, D) = \frac{(A - C)(B - D)}{(A - D)(B - C)}

   When :math:`(A, B; C, D) = -1`, the four collinear points form a **harmonic range**, constructible by unmarked straightedge alone from a complete quadrangle.
