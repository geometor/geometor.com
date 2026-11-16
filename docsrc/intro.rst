.. container:: author-overline

   semantic digital archive • central portal

========
GEOMETOR
========

.. rubric:: Exploring the Architecture of All That Is

**GEOMETOR** is the central portal and gateway to the interconnected **semantic digital archive**, symbolic software engine, and digital scriptorium investigating **geometry as humanity's most concise language for documenting nature, proportion, and deductive truth**.

When we watch a botanical meristem pack florets at the golden angle, examine crystal lattices, or trace projective collineations, one foundational question recurs: *How do the simplest axiomatic relationships unfold into the full complexity of form and mind?*

Across **sixty-one interconnected repositories**, GEOMETOR recasts 2,400 years of classical treatises, projective and rational geometry, natural morphogenesis, epistemological philosophy, and machine reasoning into **one consistent, exact symbolic grammar**—uniting two complementary modes of work:

* **Scholarly Editions (*74 Book Codices · 39 Authors*)**: Multi-language critical editions of public-domain works (*Greek, Latin, Italian, German, French, and English*) paired with over **8,400 tracked primary-source folio scans** and calibrated ``.euclid-graphic`` SVGs.
* **Mathematical Catalogs (*11 Compendia*)**: One-item-per-page symbolic catalogs documenting the dependency graphs, golden constructions, triangle centers, polyhedra, rational trigonometry laws, Fibonacci identities, and proving engines of modern mathematics (``elements``, ``etc``, ``wildberger``, ``fundamentals``, ``divine``, ``polyhedra``, ``knott``, ``huntley``, ``livio``, ``posamentier``, ``codes``) with full scholarly citation.

.. admonition:: Browse the Complete Digital Scriptorium & Symbolic Catalogs
   :class: note

   Explore all **74 working Book Codices** (direct links to every treatise across all 39 authors) and **11 Mathematical Catalogs** in the :doc:`Books & Catalogs Directory <books/index>`, or view the full 61-repository architecture in :doc:`Projects <projects/index>`.

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
* **Earned Understanding (*Noetics of Geometry*)**: Grounded in Plato, Aristotle, Proclus, Thomas Aquinas (*materia intelligibilis*), Nicholas of Cusa, and Petrus Hoenen's *De Noetica Geometriae*, geometric necessity is neither empirical guesswork nor an uninterpreted game of marks—it is apprehended directly within concrete construction.
* **Scholarly Editions & Mathematical Catalogs**: Powered by `photon-platform/publish <https://github.com/photon-platform/publish>`_, GEOMETOR pairs multi-track Book Codices of historical public-domain sources with structured one-item-per-page Mathematical Catalogs for modern research works.

----

Key Projects Across Five Pillars
--------------------------------

*(See the complete list of all 74 historical treatises and 11 catalogs in* :doc:`Books & Catalogs <books/index>` *, or all 61 repositories in* :doc:`Projects <projects/index>` *.)*

I. The Symbolic Core, Discovery & Archive Architecture
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* `model <https://geometor.github.io/model/>`_ (`GitHub <https://github.com/geometor/model>`_ · `PyPI <https://pypi.org/project/geometor-model/>`_): Exact ``SymPy`` compass-and-straightedge construction engine with rational trigonometry invariants (``quadrance``, ``spread``, ``cross_ratio``), ``@proposition`` proof ledgers, and ancestral DAGs.
* `explorer <https://geometor.github.io/explorer/>`_ (`GitHub <https://github.com/geometor/explorer>`_): Interactive SVG workbench, symbolic CLI, scrubbable construction timeline, and publication sheet exporter.
* `divine <https://geometor.github.io/divine/>`_ (`GitHub <https://github.com/geometor/divine>`_ · `PyPI <https://pypi.org/project/geometor-divine/>`_): Automated golden-section & harmonic-range scanner paired with a **Catalog** of *Cut-the-Knot* golden ratio constructions (`constructions/ <https://geometor.github.io/divine/constructions/>`_).
* `polyhedra <https://geometor.github.io/polyhedra/>`_ (`GitHub <https://github.com/geometor/polyhedra>`_): Exact 3D symbolic **Catalog** of Platonic, Archimedean, Catalan, and Kepler–Poinsot solids alongside Leonardo da Vinci's 1509 polyhedral plates.
* `codes <https://geometor.github.io/codes/>`_ · `elementarium <https://geometor.github.io/elementarium/>`_ · `press <https://geometor.github.io/press/>`_ · `animations <https://geometor.github.io/animations/>`_ · `trees <https://geometor.github.io/trees/>`_: Theorem-proving engine **Catalog**, 100,000-year optical bootstrap archive, Digital Scriptorium Press shelf, proportional studies, and monotone planar tree layouts.

II. The Unfolding Canon (*The Elementrium* & Constructive Geometry)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* `euclid <https://geometor.github.io/euclid/>`_ · `elements <https://geometor.github.io/elements/>`_ · `byrne <https://geometor.github.io/byrne/>`_: Heath's 13-Book *Elements* (**1,416 folios**, **831 calibrated SVGs**) & *Data*, the **601-node G-Index** (`elements2/ <https://geometor.github.io/elements/elements2/>`_), and Oliver Byrne's 1847 chromatic *Elements* (**339 RGB folios**).
* `archimedes <https://geometor.github.io/archimedes/>`_ · `apollonius <https://geometor.github.io/apollonius/>`_ · `heron <https://geometor.github.io/heron/>`_ · `menelaus <https://geometor.github.io/menelaus/>`_ · `ptolemy <https://geometor.github.io/ptolemy/>`_ · `pappus <https://geometor.github.io/pappus/>`_: Seven treatises of Archimedes, Apollonius's *Conics* & reconstructed works, four treatises of Heron (*Metrica*, *Definitiones*, *Catoptrica*, *Dioptra*), Menelaus's *Sphaerica*, Ptolemy's *Almagest* & *Planisphaerium* (**1,054 folios**), and Pappus's *Synagoge*.
* `pascal <https://geometor.github.io/pascal/>`_ · `ceva <https://geometor.github.io/ceva/>`_ · `euler <https://geometor.github.io/euler/>`_ · `mascheroni <https://geometor.github.io/mascheroni/>`_ · `feuerbach <https://geometor.github.io/feuerbach/>`_ · `steiner <https://geometor.github.io/steiner/>`_: Pascal's 1640 *Essay pour les Coniques*, Ceva's 1678 statical concurrency, Euler's 1765 *Solutio facilis* (*E325*), Mascheroni's 1797 compass-only geometry, Feuerbach's 1822 Nine-Point tangency, and Steiner's 1833 fixed-circle straightedge constructions.
* `staudt <https://geometor.github.io/staudt/>`_ · `petersen <https://geometor.github.io/petersen/>`_ · `casey <https://geometor.github.io/casey/>`_ · `klein <https://geometor.github.io/klein/>`_ · `lemoine <https://geometor.github.io/lemoine/>`_ · `altshiller-court <https://geometor.github.io/altshiller-court/>`_: von Staudt's *Geometrie der Lage* & *Beiträge*, Petersen's *Methods and Theories*, Casey's *Sequel to Euclid*, Klein's *Erlangen Program* & *Famous Problems*, Lemoine's *Géométrographie*, and Altshiller-Court's *College Geometry*.
* `etc <https://geometor.github.io/etc/>`_ · `wildberger <https://geometor.github.io/wildberger/>`_ · `fundamentals <https://geometor.github.io/fundamentals/>`_: **Catalogs** of Kimberling's *Encyclopedia of Triangle Centers* (4,000+ compiled centers, 16,000+ SVGs), Wildberger's *Divine Proportions* & Rational Trigonometry, and the 353-folio Fred W. Seelig Archive.

III. Philosophical, Renaissance, Harmonic & Axiomatic Scriptorium
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* `plato <https://geometor.github.io/plato/>`_ · `aristotle <https://geometor.github.io/aristotle/>`_ · `nicomachus <https://geometor.github.io/nicomachus/>`_ · `proclus <https://geometor.github.io/proclus/>`_: Five Platonic mathematical dialogues, five Aristotelian geometric/noetic treatises, Nicomachus's *Introductio Arithmetica* (**572 folios**), and Proclus's *Commentary on Euclid Book I*.
* `fibonacci <https://geometor.github.io/fibonacci/>`_ · `aquinas <https://geometor.github.io/aquinas/>`_ · `cusa <https://geometor.github.io/cusa/>`_: Fibonacci's *Liber Abbaci* & *Practica Geometriae* (**762 folios**), six Thomistic treatises on *materia intelligibilis*, and Nicholas of Cusa's *De Docta Ignorantia* & *De Mathematicis Complementis*.
* `piero <https://geometor.github.io/piero/>`_ · `pacioli <https://geometor.github.io/pacioli/>`_ · `durer <https://geometor.github.io/durer/>`_ · `kepler <https://geometor.github.io/kepler/>`_: Piero della Francesca's *Libellus de Quinque Corporibus Regularibus*, Pacioli's *De Divina Proportione* (Leonardo's 60 woodcuts) & *Summa* (1494), Dürer's *Underweysung der Messung* (1525), and Kepler's *Mysterium*, *Strena*, & *Harmonices Mundi*.
* `pasch <https://geometor.github.io/pasch/>`_ · `hilbert <https://geometor.github.io/hilbert/>`_ · `poincare <https://geometor.github.io/poincare/>`_ · `bertrand-russell <https://geometor.github.io/bertrand-russell/>`_ · `hoenen <https://geometor.github.io/hoenen/>`_ · `russell <https://geometor.github.io/russell/>`_: Pasch's *Vorlesungen* (1882), Hilbert's *Grundlagen* (1899), Poincaré's *Science and Hypothesis*, Bertrand Russell's *Foundations* & *Principles*, Hoenen's *De Noetica Geometriae* (1954), and Walter & Lao Russell's *Home Study Course* (**519 folios**) & *Wave-Field Cosmogony*.

IV. Living Geometry, Dynamic Symmetry & Golden Ratio Catalogs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* `phyllotaxis <https://geometor.github.io/phyllotaxis/>`_ (`GitHub <https://github.com/geometor/phyllotaxis>`_): Symbolic golden-angle divergence (:math:`\Phi = 2\pi/\phi^2 \approx 137.50776^\circ`), Fibonacci parastichy curves, and live `2D Apical Meristem <https://geometor.github.io/phyllotaxis/demos/meristem_2d.html>`_ & `3D Recursive Propagation <https://geometor.github.io/phyllotaxis/demos/propagation_3d.html>`_ WebGL laboratories.
* `thompson <https://geometor.github.io/thompson/>`_ · `hambidge <https://geometor.github.io/hambidge/>`_: D'Arcy Wentworth Thompson's *On Growth and Form* (1917) and Jay Hambidge's *The Elements of Dynamic Symmetry* (1920, **174 folios**).
* `knott <https://geometor.github.io/knott/>`_ · `huntley <https://geometor.github.io/huntley/>`_ · `livio <https://geometor.github.io/livio/>`_ · `posamentier <https://geometor.github.io/posamentier/>`_: Modern **Mathematical Catalogs** of Fibonacci numbers, Wythoff geometry, aesthetic Golden Ratio constructions, and primary-source historical myth triage.

V. Machine Reasoning & Program Synthesis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* `seer <https://geometor.github.io/seer/>`_ · `seer_navigator <https://geometor.github.io/seer_navigator/>`_ · `seer_sessions <https://geometor.github.io/seer_sessions/>`_: Multi-agent neuro-symbolic ARC-AGI Python program synthesis (*Dreamer* + *Coder*), ``Textual`` trajectory TUI, and longitudinal observatory indexing **8,514 task runs** across **2,939 puzzles** and **475 sessions**.

----

Start Exploring
---------------

1. **Walk the Genesis Spine**: Open `G.17 (Book I, Prop. 1 — Construct an Equilateral Triangle) <https://geometor.github.io/elements/elements2/G.17/>`_ in ``elements`` or compare Oliver Byrne's chromatic pseudocode in `byrne <https://geometor.github.io/byrne/>`_.
2. **Test Invariance Across Four Triangles**: Browse `X₁ through X₄₀₀₀+ <https://geometor.github.io/etc/>`_ in ``etc`` across Acute ``(5,6,7)``, Egyptian Right ``(3,4,5)``, Kepler Golden ``(1,√φ,φ)``, and Kimberling ``(6,9,13)`` reference triangles.
3. **Explore Projective, Classical & Rational Canons**: Trace Ptolemy's single-circle pentagon in `ptolemy <https://geometor.github.io/ptolemy/>`_, Pascal's 60-line *Hexagrammum Mysticum* in `pappus <https://geometor.github.io/pappus/>`_, and algebraic quadrance/spread laws in `wildberger <https://geometor.github.io/wildberger/>`_.
4. **Grow a Living Meristem in 2D & 3D**: Launch the interactive `2D Meristem Studio <https://geometor.github.io/phyllotaxis/demos/meristem_2d.html>`_ and `3D Propagation WebGL Lab <https://geometor.github.io/phyllotaxis/demos/propagation_3d.html>`_ in ``phyllotaxis``, paired with D'Arcy Thompson's `On Growth and Form <https://geometor.github.io/thompson/>`_.
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
