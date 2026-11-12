:navigation: footer
:order: 2

Glossary
========

.. rubric:: Core Vocabulary of the GEOMETOR Architecture

.. glossary::
   :sorted:

   Point
      An indivisible location ``A`` on the planar field (`Euclid I, Def. 1 / G.1 <https://geometor.github.io/elements/elements2/G.1/>`_). In ``geometor.model``, a point represents exact algebraic *information* :math:`(x, y)`—either placed as one of the two initial givens or selected by the intersection of two constructed loci.

   Line
      An infinite straight projection ``[ A B ]`` determined symmetrically by two distinct points (`G.2 <https://geometor.github.io/elements/elements2/G.2/>`_). Expressed algebraically as :math:`ax + by + c = 0` with exact symbolic coefficients.

   Segment
      The bounded portion ``/ A B /`` of a line ``[ A B ]`` lying between extremities ``A`` and ``B`` (`G.4 <https://geometor.github.io/elements/elements2/G.4/>`_).

   Circle
      A closed planar projection ``( A B )`` swept by rotating radius point ``B`` perpendicularly around stationary center ``A`` (`G.10 <https://geometor.github.io/elements/elements2/G.10/>`_, `G.15 <https://geometor.github.io/elements/elements2/G.15/>`_). Unlike ``[ A B ]``, ``( A B )`` and ``( B A )`` are distinct loci.

   Vesica Piscis
      The symmetric lens formed by two congruent circles ``( A B )`` and ``( B A )`` each passing through the other's center. Their intersections select the **Equidistant Poles**, generating the equilateral triangle, perpendicular bisection, and :math:`\sqrt{3}`.

   Equidistant Poles
      The conjugate intersection points :math:`C` and :math:`C'` of two symmetric circles ``( A B )`` and ``( B A )``, each equidistant from ``A`` and ``B`` and defining the orthogonal axis ``[ C C′ ]`` perpendicular to ``[ A B ]``.

   Quadrance
      In Rational Trigonometry (`geometor/wildberger <https://geometor.github.io/wildberger/>`_), the exact algebraic square of separation between two points, :math:`Q(A_1, A_2) = (x_2 - x_1)^2 + (y_2 - y_1)^2`, avoiding unnecessary square roots.

   Spread
      In Rational Trigonometry, the exact rational measure of inclination between two lines, :math:`s(\ell_1, \ell_2) \in [0, 1]` (equivalent to :math:`\sin^2\theta` in Euclidean space), where :math:`s = 0` is parallel, :math:`s = \tfrac{1}{2}` is :math:`45^\circ`, :math:`s = \tfrac{3}{4}` is :math:`60^\circ`, and :math:`s = 1` is perpendicular.

   Cross-Ratio
      The fundamental four-point projective invariant :math:`(A, B; C, D) = \frac{(A - C)(B - D)}{(A - D)(B - C)}`, preserved under central projection (`geometor/pappus <https://geometor.github.io/pappus/>`_).

   Harmonic Range
      Four collinear points :math:`A, B, C, D` whose cross-ratio equals :math:`(A, B; C, D) = -1`, meaning :math:`C` and :math:`D` divide segment ``/ A B /`` internally and externally in the same ratio. Constructible by unmarked straightedge alone from a complete quadrangle.

   Extreme and Mean Ratio
      Euclid's classical name (*Book VI, Def. 3*) for the **Golden Ratio** or **Divine Proportion** :math:`\phi = \frac{1 + \sqrt{5}}{2}`, satisfying :math:`\frac{a}{b} = \frac{b}{a + b}` and :math:`\phi^2 - \phi - 1 = 0`.

   Golden Chain
      A sequence of collinear segments on a constructed line whose successive lengths form a geometric progression in powers of :math:`\phi` (:math:`\dots, \phi^{-1}, 1, \phi, \phi^2, \dots`) while simultaneously obeying the additive Fibonacci recurrence :math:`\phi^{n+1} = \phi^n + \phi^{n-1}`.

   Intelligible Matter
      *Materia intelligibilis* in Aristotle and Thomas Aquinas (`geometor/aquinas <https://geometor.github.io/aquinas/>`_): the pure continuum of spatial extension abstracted from sensible qualities, in which geometric figures are constructed and judged.

   Intuitive Formal Abstraction
      Fr. Petrus Hoenen's epistemological principle (`geometor/hoenen <https://geometor.github.io/hoenen/>`_) that universal geometric necessity is apprehended directly within concrete spatial construction prior to formal axiomatic codification.

   G-Index
      The 601-node topological dependency sequence (``G.1``–``G.601``) in `geometor/elements <https://geometor.github.io/elements/>`_ ordering Euclid's definitions, postulates, common notions, and propositions into a strict directed acyclic graph.

   Book Codex
      GEOMETOR's multi-track digital scholarly format powered by `photon-platform/publish <https://github.com/photon-platform/publish>`_, pairing synchronized source languages, formal pseudocode, executable Python, and interactive vector figures on every folio.
