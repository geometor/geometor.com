The Golden Ratio (:math:`\phi`)
===============================

.. rubric:: Extreme and Mean Ratio, Algebraic Self-Similarity & Fibonacci Growth

Euclid defines **division in extreme and mean ratio** (*Book VI, Def. 3*) with austere precision: *A straight line is said to have been cut in extreme and mean ratio when, as the whole line is to the greater segment, so is the greater to the less.*

Equivalently, for lesser magnitude :math:`a` and greater magnitude :math:`b` whose whole is :math:`c = a + b`:

.. math::

   \frac{a}{b} = \frac{b}{a + b}

Unlike an ordinary **geometric mean** :math:`\frac{a}{b} = \frac{b}{c}` (which relates three independent magnitudes) or an **arithmetic progression** (which preserves additive differences), the **Golden Mean** requires *both simultaneously*: the geometric third term :math:`c` *is* the arithmetic sum :math:`a + b`.

.. picture:: ../_static/svg/quadratic.svg
   :alt: Quadratic parabola x^2 - x - 1 = 0 and golden roots phi and 1 - phi

The Defining Quadratic & Conjugate Roots
----------------------------------------

Setting :math:`\phi = \frac{b}{a} = \frac{a + b}{b} = 1 + \frac{1}{\phi}` and multiplying by :math:`\phi` yields the minimal polynomial over :math:`\mathbb{Q}`:

.. math::

   \phi^2 - \phi - 1 = 0

Applying the quadratic formula to :math:`x^2 - x - 1 = 0` selects the two algebraic conjugates in :math:`\mathbb{Q}(\sqrt{5})`:

.. math::

   \phi = \frac{1 + \sqrt{5}}{2} \approx 1.618033988749895\dots, \qquad
   \overline{\phi} = 1 - \phi = -\frac{1}{\phi} = \frac{1 - \sqrt{5}}{2} \approx -0.618033988749895\dots

Fundamental Algebraic Identities
--------------------------------

Because :math:`\phi^2 = \phi + 1` and :math:`\frac{1}{\phi} = \phi - 1`, **powers of** :math:`\phi` **bridge multiplication and addition**:

.. math::

   \begin{aligned}
   \phi^{-2} &= 2 - \phi \\
   \phi^{-1} &= \phi - 1 \\
   \phi^{0}  &= 1 \\
   \phi^{1}  &= \phi \\
   \phi^{2}  &= \phi + 1 \\
   \phi^{3}  &= 2\phi + 1 \\
   \phi^{4}  &= 3\phi + 2 \\
   \phi^{n}  &= F_n \phi + F_{n-1}
   \end{aligned}

Every golden chain :math:`\dots, \phi^{-2}, \phi^{-1}, 1, \phi, \phi^2, \phi^3, \dots` is simultaneously a **geometric progression** (each term multiplied by :math:`\phi`) and an **additive Fibonacci recurrence** (each term equal to the sum of the two before it: :math:`\phi^{n+1} = \phi^n + \phi^{n-1}`)!

Continued Fraction, Fibonacci & Lucas Sequences
-----------------------------------------------

* **Simplest Continued Fraction & Nested Radical**:

  .. math::

     \phi = 1 + \cfrac{1}{1 + \cfrac{1}{1 + \cfrac{1}{1 + \cdots}}}, \qquad
     \phi = \sqrt{1 + \sqrt{1 + \sqrt{1 + \cdots}}}

  Because all partial quotients equal :math:`1` (the smallest possible positive integer), :math:`\phi` is Hurwitz's extremal irrational—explaining why living plant meristems adopt the golden divergence angle :math:`2\pi/\phi^2` in `geometor/phyllotaxis <https://geometor.github.io/phyllotaxis/>`_.

* **Fibonacci (:math:`F_n`) and Lucas (:math:`L_n`) Numbers via Binet's Exact Formulas**:

  .. math::

     F_n = \frac{\phi^n - \overline{\phi}^{\,n}}{\sqrt{5}} \;\; (0, 1, 1, 2, 3, 5, 8, 13, 21, \dots), \qquad
     L_n = \phi^n + \overline{\phi}^{\,n} \;\; (2, 1, 3, 4, 7, 11, 18, 29, \dots)

Where to Explore Further in GEOMETOR
------------------------------------

* **Classical Proofs**: Euclid *Elements* `Book II, Prop. 11 <https://geometor.github.io/euclid/heath/volume_I/book_ii/propositions/11/>`_, `Book VI, Prop. 30 <https://geometor.github.io/euclid/heath/volume_II/book_vi/propositions/30/>`_, and `Book XIII <https://geometor.github.io/euclid/heath/volume_III/book_xiii/>`_ (the five Platonic solids).
* **Renaissance Polyhedra**: Luca Pacioli's thirteen divine effects and Leonardo's icosahedron/dodecahedron plates in `pacioli <https://geometor.github.io/pacioli/>`_.
* **Automated Discovery**: Scanning constructions for golden sections and golden chains in `divine <https://geometor.github.io/divine/>`_.
