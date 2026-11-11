Lines, Proportions & Spreads
============================

.. rubric:: A Line Is a Proportion Derived from the Relationship of Two Points

We are often taught to picture a line as an "infinite string of points." Constructively, the truth is sharper:

.. epigraph::

   *A point on a line cannot be known unless that line intersects another element. Anything else is speculation.*

When two distinct points :math:`P_1 = (x_1, y_1)` and :math:`P_2 = (x_2, y_2)` are given (`G.2 <https://geometor.github.io/elements/elements2/G.2/>`_), aligning the unmarked straightedge projects a **constant linear proportion** ``[ P₁ P₂ ]`` across the field:

.. math::

   a x + b y + c = 0, \qquad
   a = y_1 - y_2, \quad
   b = x_2 - x_1, \quad
   c = x_1 y_2 - x_2 y_1

Notice the symmetry: interchanging :math:`P_1` and :math:`P_2` negates :math:`(a, b, c)` simultaneously, leaving the locus ``[ P₁ P₂ ] = [ P₂ P₁ ]`` invariant.

Exact Line–Line Selection
-------------------------

Two non-parallel lines :math:`a_1 x + b_1 y + c_1 = 0` and :math:`a_2 x + b_2 y + c_2 = 0` with non-vanishing determinant :math:`\Delta = a_1 b_2 - a_2 b_1 \neq 0` select a unique rational point in the same algebraic number field as their coefficients:

.. math::

   x = \frac{b_1 c_2 - b_2 c_1}{a_1 b_2 - a_2 b_1}, \qquad
   y = \frac{c_1 a_2 - c_2 a_1}{a_1 b_2 - a_2 b_1}

Pure straightedge operations (*projective incidence*) never introduce square roots! Because of this algebraic closure, theorems of pure collinearity and concurrency—such as **Pappus's Hexagon Theorem** and the **Complete Quadrangle construction of the Harmonic Fourth** (`geometor/pappus <https://geometor.github.io/pappus/>`_)—hold over any commutative field.

Inclination Without Transcendental Angles: Spread
-------------------------------------------------

Rather than measuring the inclination of two lines with transcendental ``arccos`` angles, `geometor.model <https://geometor.github.io/model/>`_ and `geometor/wildberger <https://geometor.github.io/wildberger/>`_ compute their exact **rational spread**:

.. math::

   s(\ell_1, \ell_2) = \frac{(a_1 b_2 - a_2 b_1)^2}{(a_1^2 + b_1^2)(a_2^2 + b_2^2)}

* :math:`s = 0` — parallel or coincident lines (:math:`0^\circ`);
* :math:`s = \frac{1}{4}` — :math:`30^\circ` / :math:`150^\circ` inclination;
* :math:`s = \frac{1}{2}` — diagonal :math:`45^\circ` inclination (:math:`\sqrt{2}` square diagonal);
* :math:`s = \frac{3}{4}` — equilateral :math:`60^\circ` / :math:`120^\circ` inclination (:math:`\sqrt{3}` Vesica Piscis);
* :math:`s = 1` — perpendicularity (:math:`90^\circ` orthogonal poles);
* :math:`s = \frac{5 \mp \sqrt{5}}{8}` — pentagonal / decagonal golden inclinations (:math:`36^\circ` and :math:`72^\circ`).

.. code-block:: python

   import sympy as sp
   import sympy.geometry as spg
   from geometor.model.invariants import line_spread

   l_base = spg.Line2D((0, 0), (1, 0))
   l_vesica = spg.Line2D((0, 0), (sp.Rational(1, 2), sp.sqrt(3) / 2))
   assert line_spread(l_base, l_vesica) == sp.Rational(3, 4)
