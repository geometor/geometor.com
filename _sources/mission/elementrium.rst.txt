The Elementrium: One Language of Form
=====================================

.. rubric:: Uniting 2,300 Years of Geometry in a Single Symbolic Grammar

Across twenty-three centuries, geometry has been rewritten in dozens of mutually isolated dialects:

* **Synthetic rhetorical prose** in Greek, Latin, and Renaissance Italian (Euclid, Pappus, Proclus, Pacioli);
* **Projective synthetic configurations** and harmonic cross-ratios (Pascal, Desargues, Poncelet, Altshiller-Court);
* **Homogeneous barycentric and trilinear coordinates** in modern triangle geometry (Clark Kimberling's *ETC*);
* **Rational algebraic quadrances and spreads** over arbitrary fields (Norman J. Wildberger);
* **Imperative algorithms and computer-assisted dependency graphs** in symbolic Python.

Because these dialects rarely share a common notation, a student reading Heath's translation of Euclid Book II, Pacioli's *De Divina Proportione*, and Kimberling's *Encyclopedia of Triangle Centers* can easily miss that they are describing **the exact same underlying geometric structures**.

The GEOMETOR Notation
---------------------

In **The Elementrium**, GEOMETOR establishes an unambiguous, ASCII-clean constructive grammar shared across prose `:g:` roles, SVG ``data-ref`` attributes, CLI commands, and ``geometor.model`` scripts:

.. list-table::
   :header-rows: 1
   :widths: 18 44 38

   * - Notation
     - Geometric Meaning
     - Constructive Role
   * - ``A``, ``B``, ``C′``
     - **Point** — an exact algebraic coordinate :math:`(x, y)`
     - *Information* on the planar field
   * - ``[ A B ]``
     - **Line** — infinite straight locus through ``A``, ``B``
     - *Linear projection* of two points' proportion
   * - ``/ A B /``
     - **Segment** — bounded span between ``A`` and ``B``
     - Finite magnitude / quadrance carrier
   * - ``( A B )``
     - **Circle** — center ``A``, radius point ``B``
     - *Rotational projection* (order-sensitive!)
   * - ``< B A C )``
     - **Angle / Spread** — inclination of rays from ``A``
     - Rational vertex spread :math:`s(\ell_1, \ell_2)`
   * - ``< A B C >``
     - **Polygon** — closed rectilineal figure
     - Bounded planar region and area carrier

Notice the deliberate distinction between ``( A B )`` and ``( B A )``: a line ``[ A B ]`` treats its two defining points symmetrically, whereas a circle ``( A B )`` distinguishes **center** ``A`` from **radius point** ``B``. Together, the twin circles ``( A B )`` and ``( B A )`` form the primordial **Vesica Piscis** (`G.17 <https://geometor.github.io/elements/elements2/G.17/>`_).

Multi-Track Book Codices
------------------------

Powered by `photon-platform/publish <https://github.com/photon-platform/publish>`_, GEOMETOR editions present primary historical sources alongside modern symbolic reconstructions as **synchronized companion tracks** on the same folio:

* **In** `elements <https://geometor.github.io/elements/>`_: Every node of the **601-node G-Index** (``G.1``–``G.601``) pairs **Formal Pseudocode**, **Executable Python**, **Sir Thomas Heath's English Text**, and **QHD Video**—linked directly to its upstream dependencies and downstream theorems.
* **In** `euclid <https://geometor.github.io/euclid/>`_ **and** `altshiller-court <https://geometor.github.io/altshiller-court/>`_: Every proposition binds `:g:` geometric references and `:just:` citations directly to recalibrated interactive vector diagrams.
* **In** `pacioli <https://geometor.github.io/pacioli/>`_, `proclus <https://geometor.github.io/proclus/>`_, `aquinas <https://geometor.github.io/aquinas/>`_, **and** `hoenen <https://geometor.github.io/hoenen/>`_: Diplomatic Greek, Latin, 1509 Venetian Italian, and 1889 German sources stand side by side with modern English translations and geometric commentary.

Nothing is flattened into a black box; every step remains human-readable, historically anchored, and machine-verifiable.
