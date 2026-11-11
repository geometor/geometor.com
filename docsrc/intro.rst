GEOMETOR
========

.. rubric:: Exploring the Architecture of All That Is

**GEOMETOR** is an open-source research initiative, symbolic software engine, and digital scriptorium investigating **geometry as humanity's most concise language for documenting nature, proportion, and deductive truth**.

When we watch a botanical meristem pack florets at the golden angle, examine crystal lattices, or trace projective collineations, one foundational question recurs: *How do the simplest axiomatic relationships unfold into the full complexity of form and mind?*

Every repository in GEOMETOR lays a stone in that architecture—recasting 2,300 years of classical treatises, projective and rational geometry, natural morphogenesis, epistemological philosophy, and machine reasoning into **one consistent, exact symbolic grammar** so we can witness the whole edifice unfold step by step.

----

From Two Points in an Empty Field
---------------------------------

Every GEOMETOR construction begins on an unmarked planar field with the minimum possible information: **two given points**, :g:`A <vesica_to_phi:A>` and :g:`B <vesica_to_phi:B>`. Their separation establishes the unit measure (:math:`1`). Rather than approximating coordinates in floating-point arithmetic, we **project** continuous straight lines and circles from known points and **select** exact algebraic intersections.

Use the playback controls below the figure (or hover any highlighted symbol in the steps) to watch how two points unfold through the **Vesica Piscis** and **Equidistant Poles** into the **Divine Proportion**:

.. picture:: _static/svg/vesica_to_phi.svg
   :alt: Exact symbolic construction unfolding from two starting points A and B through the Vesica Piscis and Equidistant Poles to George Odom's Golden Section G = (phi, 0)

.. step:: given

   :g:`A <vesica_to_phi:A>`, :g:`B <vesica_to_phi:B>` — Two starting points at :math:`(0, 0)` and :math:`(1, 0)` establish the planar field, unit segment :g:`/ A B / <vesica_to_phi:/ A B />`, and infinite baseline :g:`[ A B ] <vesica_to_phi:[ A B ]>`.

.. step:: construct

   :fn:`circle <G.15>`\ (:g:`A <vesica_to_phi:A>`, :g:`B <vesica_to_phi:B>`) → :g:`( A B ) <vesica_to_phi:( A B )>`, :fn:`circle <G.15>`\ (:g:`B <vesica_to_phi:B>`, :g:`A <vesica_to_phi:A>`) → :g:`( B A ) <vesica_to_phi:( B A )>` — Sweeping two symmetric unit circles forms the **Vesica Piscis**.

.. step:: intersect

   :g:`( A B ) <vesica_to_phi:( A B )>` ∩ :g:`( B A ) <vesica_to_phi:( B A )>` → :g:`C <vesica_to_phi:C>`, :g:`C′ <vesica_to_phi:D>` — Their intersections select the **Equidistant Poles**, unfolding the equilateral triangle :g:`< A B C > <vesica_to_phi:< A B C >>` (:fn:`equilateral_triangle <G.17>`), rational spread :math:`s = \frac{3}{4}` (:math:`\sqrt{3}`), and the orthogonal axis :g:`[ C C′ ] <vesica_to_phi:[ C D ]>` bisecting :g:`/ A B / <vesica_to_phi:/ A B />` at midpoint :g:`M <vesica_to_phi:M>`.

.. step:: construct

   Extending rays :g:`[ C′ P ] <vesica_to_phi:[ D P ]>` and :g:`[ C′ Q ] <vesica_to_phi:[ D Q ]>` through :g:`A <vesica_to_phi:A>` and :g:`B <vesica_to_phi:B>` to the twin circles forms the enlarged side-:math:`2` equilateral frame :g:`< C′ P Q > <vesica_to_phi:< D P Q >>`; its medians :g:`[ A Q ] <vesica_to_phi:[ A Q ]>` and :g:`[ B P ] <vesica_to_phi:[ B P ]>` meet :g:`[ C C′ ] <vesica_to_phi:[ C D ]>` at circumcenter :g:`O <vesica_to_phi:O>`, from which we sweep the outer circumcircle :g:`( O C′ ) <vesica_to_phi:( O D )>`.

.. step:: conclude

   :g:`( O C′ ) <vesica_to_phi:( O D )>` ∩ :g:`[ A B ] <vesica_to_phi:[ A B ]>` → :g:`H <vesica_to_phi:H>`, :g:`G <vesica_to_phi:G>` — By George Odom's midline theorem, :g:`/ A B / <vesica_to_phi:/ A B />` and :g:`/ B G / <vesica_to_phi:/ B G />` divide :g:`/ A G / <vesica_to_phi:/ A G />` in :eq:`Extreme and Mean Ratio <vesica_to_phi:/ A G / = vesica_to_phi:/ A B / = vesica_to_phi:/ B G />`:

   .. math::

      \frac{|AG|}{|AB|} = \frac{|AB|}{|BG|} = \phi = \frac{1 + \sqrt{5}}{2}

From this single unfolding emerge the regular pentagon and icosahedron, projective harmonic ranges, rational spread polynomials, Fibonacci parastichies in living plants, and formal constructive proofs.

----

One Language of Form: Method & Principles
-----------------------------------------

* **Exact Symbolic Algebra over Floating-Point Approximation**: Dynamic geometry tools built on IEEE-754 floats can only report that two segments look *numerically close* to :math:`1.6180339\dots` Powered by `SymPy <https://www.sympy.org/>`_, ``geometor.model`` preserves every coordinate, polynomial root, **quadrance**, **spread**, and **cross-ratio** in exact algebraic form—proving mathematical identity rather than decimal coincidence.
* **Projection & Selection**: Points hold *information*; lines ``[ A B ]`` and circles ``( A B )`` *project* infinite loci across the field; intersections ``∩`` *select* derived points carrying their complete ancestral dependency DAG back to the initial givens.
* **Earned Understanding (*Noetics of Geometry*)**: Grounded in Aristotle, Proclus, Thomas Aquinas (*materia intelligibilis*), and Petrus Hoenen's *De Noetica Geometriae*, geometric necessity is neither empirical guesswork nor an uninterpreted game of marks—it is apprehended directly within concrete construction.
* **The Elementrium & Multi-Track Book Codices**: Across millennia, geometry fractured into incompatible idioms—Greek synthetic prose, Renaissance perspective woodcuts, projective cross-ratios, homogeneous trilinears, and imperative code. Powered by `photon-platform/publish <https://github.com/photon-platform/publish>`_, GEOMETOR unites classical sources, symbolic pseudocode, interactive SVGs, and executable Python side by side.

----

The Five Pillars of Exploration
-------------------------------

I. The Symbolic Core & Discovery Engine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* `model <https://geometor.github.io/model/>`_ (`GitHub <https://github.com/geometor/model>`_ · `PyPI <https://pypi.org/project/geometor-model/>`_): Exact ``SymPy`` compass-and-straightedge construction engine with rational trigonometry invariants (`quadrance`, `spread`, `cross_ratio`) and ancestral DAGs.
* `explorer <https://geometor.github.io/explorer/>`_ (`GitHub <https://github.com/geometor/explorer>`_): Interactive SVG workbench, symbolic CLI, scrubbable construction timeline, and publication sheet exporter.
* `divine <https://geometor.github.io/divine/>`_ (`GitHub <https://github.com/geometor/divine>`_ · `PyPI <https://pypi.org/project/geometor-divine/>`_): Automated discovery engine scanning constructed models to uncover golden sections, golden chains, and harmonic ranges.
* `trees <https://github.com/geometor/trees>`_: Monotone planar tree drawing algorithms grounded in Stern–Brocot trees and Farey rational sequences.

II. The Unfolding Canon (*The Elementrium*)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* `euclid <https://geometor.github.io/euclid/>`_ (`GitHub <https://github.com/geometor/euclid>`_): Complete 13-Book critical edition of Sir Thomas L. Heath's *Euclid's Elements*—**465 propositions**, **1,416 archival folios**, and **831 recalibrated SVGs** in a synchronized 2-Track Book Codex.
* `elements <https://geometor.github.io/elements/>`_ (`GitHub <https://github.com/geometor/elements>`_): Topological codification of Euclid into the **601-node G-Index** (``G.1``–``G.601``) in a 3-Track Book Codex (*Pseudocode*, *Executable Python*, and *Heath Prose*).
* `fundamentals <https://geometor.github.io/fundamentals/>`_ (`GitHub <https://github.com/geometor/fundamentals>`_): The **Fred W. Seelig Archive**—**55 foundational topics** (``F.1``–``F.55``) and **353 manuscript folios** uniting triangle synthesis, harmonic duality, Conway notation, and sacred proportions.
* `altshiller-court <https://geometor.github.io/altshiller-court/>`_ (`GitHub <https://github.com/geometor/altshiller-court>`_): Nathan Altshiller-Court's *College Geometry* (1952)—**334 folios** and **699 articles** bridging Euclid to modern triangle and circle synthesis (Method of Loci, Similitude, Nine-Point & Feuerbach, Simson, Ceva/Menelaus, Harmonic Division, Inversion, Lemoine & Brocard).
* `etc <https://geometor.github.io/etc/>`_ (`GitHub <https://github.com/geometor/etc>`_): Semantic transformation of Clark Kimberling's *Encyclopedia of Triangle Centers* (**53,144 centers parsed**; **4,000+ centers compiled** across **62 collections** with **16,000+ interactive SVGs** across Acute, Egyptian Right, Kepler Golden, and Kimberling triangles).
* `pappus <https://geometor.github.io/pappus/>`_ (`GitHub <https://github.com/geometor/pappus>`_): Exact ``SymPy`` projective geometry—all six :math:`S_3` Pappus hexagon configurations, Steiner star points, Pascal's *Hexagrammum Mysticum* (60 Pascal lines, 20 Steiner points, 60 Kirkman points, 15 Plücker lines), straightedge harmonic fourths, and Golden Conics over :math:`\mathbb{Q}(\phi)`.
* `wildberger <https://geometor.github.io/wildberger/>`_ (`GitHub <https://github.com/geometor/wildberger>`_): Constructive companion to Norman J. Wildberger's *Divine Proportions: Rational Trigonometry to Universal Geometry*—exact ``SymPy`` proofs for Quadrance, Spread, pentagonal/golden Spread Polynomials, Triple Quad/Spread/Cross Laws, and Chromogeometry.

III. Historical, Epistemological & Axiomatic Scriptorium
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* `aristotle <https://geometor.github.io/aristotle/>`_ (`GitHub <https://github.com/geometor/aristotle>`_): *Loci Geometrici et Noetici*—critical selections from *Posterior Analytics*, *Physics*, *Metaphysics*, *De Anima*, and *De Caelo* in Bekker Greek, English, and geometric commentary.
* `proclus <https://geometor.github.io/proclus/>`_ (`GitHub <https://github.com/geometor/proclus>`_): *Commentary on the First Book of Euclid's Elements* (c. 470 AD)—4-Track Codex (*English*, *Friedlein Greek 1873*, *Summary*, *Notes*) with a 164-locus concordance on the Eudemian history, *phantasia*, and geometric projection (*probole*).
* `aquinas <https://geometor.github.io/aquinas/>`_ (`GitHub <https://github.com/geometor/aquinas>`_): *Opera de Scientia Mathematica et Materia Intelligibili*—4-Track Codex across 37 sections (*Super Boetium De Trinitate* qq. 5–6, *In Post. Anal.*, *In De Anima*, *In Phys.*, *In Metaph.*) with a 78-locus Hoenen concordance.
* `pacioli <https://geometor.github.io/pacioli/>`_ (`GitHub <https://github.com/geometor/pacioli>`_): 5-Track Book Codex of Fra Luca Pacioli's *De Divina Proportione* (Venice, 1509 / Vienna, 1889)—**318 folios** and **482 woodcuts** including **Leonardo da Vinci's 60 polyhedra plates**.
* `hilbert <https://geometor.github.io/hilbert/>`_ (`GitHub <https://github.com/geometor/hilbert>`_): David Hilbert's *Grundlagen der Geometrie / Foundations of Geometry* (1899/1902)—German text, Townsend English translation, and metamathematical independence models.
* `bertrand-russell <https://geometor.github.io/bertrand-russell/>`_ (`GitHub <https://github.com/geometor/bertrand-russell>`_): Bertrand Russell's *An Essay on the Foundations of Geometry* (1897) and *The Principles of Mathematics* Part VI *Space* (1903) tracing projective vs. metrical foundations.
* `hoenen <https://geometor.github.io/hoenen/>`_ (`GitHub <https://github.com/geometor/hoenen>`_): Facing Latin–English edition of Petrus Hoenen, S.J.'s *De Noetica Geometriae* (1954) on *intuitive formal abstraction* and the origin of geometric certainty.
* `russell <https://geometor.github.io/russell/>`_ (`GitHub <https://github.com/geometor/russell>`_): Digital edition and 3D cube-sphere wave-field reconstruction of Walter & Lao Russell's 48-lesson *Home Study Course* (180 vector figures).

IV. Living Geometry & Morphogenesis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* `phyllotaxis <https://geometor.github.io/phyllotaxis/>`_ (`GitHub <https://github.com/geometor/phyllotaxis>`_): Symbolic golden-angle divergence (:math:`\Phi = 2\pi(1 - 1/\phi) \approx 137.50776^\circ`), opposing Fibonacci parastichy curves, and live `2D Apical Meristem <https://geometor.github.io/phyllotaxis/demos/meristem_2d.html>`_ & `3D Recursive Propagation <https://geometor.github.io/phyllotaxis/demos/propagation_3d.html>`_ WebGL laboratories.

V. Machine Reasoning & Program Synthesis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* `seer <https://geometor.github.io/seer/>`_ (`GitHub <https://github.com/geometor/seer>`_): Multi-agent neuro-symbolic architecture (*Dreamer* + *Coder*) synthesizing verifiable Python ``transform()`` programs for abstract spatial reasoning benchmarks (ARC-AGI).
* `seer_navigator <https://geometor.github.io/seer_navigator/>`_ (`GitHub <https://github.com/geometor/seer_navigator>`_) & `seer_sessions <https://geometor.github.io/seer_sessions/>`_ (`GitHub <https://github.com/geometor/seer_sessions>`_): ``Textual`` terminal trajectory browser and static observatory indexing **8,514 task runs** across **2,939 puzzles** and **475 sessions**.

----

Start Exploring
---------------

1. **Walk the Genesis Spine**: Open `G.17 (Book I, Prop. 1 — Construct an Equilateral Triangle) <https://geometor.github.io/elements/elements2/G.17/>`_ in ``elements`` and step through the interactive construction, Python script, and Heath commentary.
2. **Test Invariance Across Four Triangles**: Browse `X₁ through X₄₀₀₀+ <https://geometor.github.io/etc/>`_ in ``etc`` across Acute ``(5,6,7)``, Egyptian Right ``(3,4,5)``, Kepler Golden ``(1,√φ,φ)``, and Kimberling ``(6,9,13)`` reference triangles.
3. **Explore Projective & Rational Geometry**: Trace Pascal's 60-line *Hexagrammum Mysticum* in `pappus <https://geometor.github.io/pappus/>`_ and algebraic quadrance/spread laws in `wildberger <https://geometor.github.io/wildberger/>`_.
4. **Grow a Living Meristem in 2D & 3D**: Launch the interactive `2D Meristem Studio <https://geometor.github.io/phyllotaxis/demos/meristem_2d.html>`_ and `3D Propagation WebGL Lab <https://geometor.github.io/phyllotaxis/demos/propagation_3d.html>`_ in ``phyllotaxis``.
5. **Watch Visual Broadcasts on YouTube (`@geometor`)**: Experience 135+ dual-format QHD propositions and vertical Shorts across `Euclid's Elements <https://www.youtube.com/playlist?list=PLUXlBs_QySgw>`_ and the `Encyclopedia of Triangle Centers <https://www.youtube.com/playlist?list=PLKVZJpKGr5zc>`_ on `@geometor <https://www.youtube.com/@geometor>`_, or visit our :doc:`broadcasts/index` showcase.
6. **Construct in Exact Symbolic Python**:

   .. code-block:: python

      from geometor.model import Model

      model = Model("vesica")
      A = model.set_point(0, 0, classes=["given"], ID="A")
      B = model.set_point(1, 0, classes=["given"], ID="B")
      model.construct_line(A, B)
      model.construct_circle(A, B)
      model.construct_circle(B, A)

      for pt in model.points:
          print(f"{model[pt].ID}: ({pt.x}, {pt.y})")
