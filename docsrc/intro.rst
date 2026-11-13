GEOMETOR
========

.. rubric:: Exploring the Architecture of All That Is

**GEOMETOR** is an open-source research initiative, symbolic software engine, and digital scriptorium investigating **geometry as humanity's most concise language for documenting nature, proportion, and deductive truth**.

When we watch a botanical meristem pack florets at the golden angle, examine crystal lattices, or trace projective collineations, one foundational question recurs: *How do the simplest axiomatic relationships unfold into the full complexity of form and mind?*

Across **forty-six interconnected repositories**, GEOMETOR recasts 2,400 years of classical treatises, projective and rational geometry, natural morphogenesis, epistemological philosophy, and machine reasoning into **one consistent, exact symbolic grammar**—uniting two complementary modes of work:

* **Scholarly Editions (*Book Codices*)**: Multi-language critical editions of public-domain works (*Greek, Latin, Italian, German, French, and English*) paired with calibrated `.euclid-graphic` SVGs and runnable ``geometor.model`` constructions.
* **Mathematical Catalogs**: One-item-per-page symbolic catalogs documenting the theorems, golden constructions, triangle centers, rational trigonometry laws, and open-source proving engines of modern mathematics (`etc`, `wildberger`, `divine`, `knott`, `codes`) with full scholarly citation.

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

The Five Pillars of Exploration
-------------------------------

I. The Symbolic Core, Discovery & Software Catalog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* `model <https://geometor.github.io/model/>`_ (`GitHub <https://github.com/geometor/model>`_ · `PyPI <https://pypi.org/project/geometor-model/>`_): Exact ``SymPy`` compass-and-straightedge construction engine with rational trigonometry invariants (``quadrance``, ``spread``, ``cross_ratio``), ``@proposition`` proof ledgers, and ancestral DAGs.
* `explorer <https://geometor.github.io/explorer/>`_ (`GitHub <https://github.com/geometor/explorer>`_): Interactive SVG workbench, symbolic CLI, scrubbable construction timeline, and publication sheet exporter.
* `divine <https://geometor.github.io/divine/>`_ (`GitHub <https://github.com/geometor/divine>`_ · `PyPI <https://pypi.org/project/geometor-divine/>`_): Automated golden-section & harmonic-range scanner paired with a **Catalog** of *Cut-the-Knot* golden ratio constructions (Odom, Hofstetter, Bogomolny).
* `codes <https://geometor.github.io/codes/>`_ (`GitHub <https://github.com/geometor/codes>`_): **Catalog** of open-source geometric computing and theorem-proving engines (*GeoCoq*, *JGEX / Area Method*, *GeoGebra Discovery*, *SymPy Geometry*, *CGAL*).
* `trees <https://github.com/geometor/trees>`_: Monotone planar tree drawing algorithms grounded in Stern–Brocot trees and Farey rational sequences.

II. The Unfolding Canon (*The Elementrium* & Constructive Geometry)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* `euclid <https://geometor.github.io/euclid/>`_ (`GitHub <https://github.com/geometor/euclid>`_): Sir Thomas L. Heath's 13-Book *Elements* (**465 propositions**, **1,416 folios**, **831 calibrated SVGs**) plus Euclid's *Data* (*Δεδομένα*, **94 propositions** of geometric analysis in Greek & English).
* `elements <https://geometor.github.io/elements/>`_ (`GitHub <https://github.com/geometor/elements>`_): Topological codification of Euclid into the **601-node G-Index** (``G.1``–``G.601``) in a 3-Track Book Codex (*Pseudocode*, *Executable Python*, and *Heath Prose*).
* `byrne <https://geometor.github.io/byrne/>`_ (`GitHub <https://github.com/geometor/byrne>`_): Oliver Byrne's chromatic *First Six Books of the Elements of Euclid* (1847) analyzed as **visual geometric pseudocode** with a Rougeux/G-Index concordance.
* `archimedes <https://geometor.github.io/archimedes/>`_ (`GitHub <https://github.com/geometor/archimedes>`_): *Works of Archimedes* & *The Mechanical Method* (Heath 1897/1912)—circle measurement, quadrature of the parabola, spirals, sphere & cylinder, and the *Arbelos*/*Salinon* lemmas.
* `apollonius <https://geometor.github.io/apollonius/>`_ (`GitHub <https://github.com/geometor/apollonius>`_): Apollonius of Perga's *Treatise on Conic Sections* (Heath 1896, Books I–VII) on cone symptomata, conjugate diameters, poles/polars, normals, and analytical loci.
* `heron <https://geometor.github.io/heron/>`_ (`GitHub <https://github.com/geometor/heron>`_): Heron of Alexandria's *Metrica* & *Dioptra* (Schöne 1903 Greek + English)—Heron's Area Formula, iterative root extraction, Platonic/Archimedean volumes, and land-division problems.
* `menelaus <https://geometor.github.io/menelaus/>`_ (`GitHub <https://github.com/geometor/menelaus>`_): Menelaus of Alexandria's *Sphaerica* (Books I–III)—spherical congruence without parallels, Menelaus's planar & spherical transversal theorems, and cross-ratio invariance.
* `ptolemy <https://geometor.github.io/ptolemy/>`_ (`GitHub <https://github.com/geometor/ptolemy>`_): Claudius Ptolemy's *Almagest* (Book I) & *Planisphaerium* (Heiberg 1898/1907)—single-circle Golden Pentagon–Decagon construction, Ptolemy's Cyclic Quadrilateral Theorem, base-60 chords, and stereographic projection.
* `pappus <https://geometor.github.io/pappus/>`_ (`GitHub <https://github.com/geometor/pappus>`_): Pappus of Alexandria's *Synagoge* (Hultsch Greek + English: Three Means, Arbelos Chain, Honeycomb Isoperimetry, *Domain of Analysis*, Hexagon Theorem) alongside 6 :math:`S_3` Steiner lines and Pascal's 60-line *Hexagrammum Mysticum*.
* `ceva <https://geometor.github.io/ceva/>`_ (`GitHub <https://github.com/geometor/ceva>`_): Giovanni Ceva's *De lineis rectis se invicem secantibus statica constructio* (1678 Latin + English)—Archimedean barycentric-lever concurrency, Menelaus duality, :math:`(2n+1)`-gons, and 3D tetrahedra.
* `feuerbach <https://geometor.github.io/feuerbach/>`_ (`GitHub <https://github.com/geometor/feuerbach>`_): Leonhard Euler (*E325*, 1765 Latin) & Karl Wilhelm Feuerbach (*Eigenschaften*, 1822 German)—the Euler Line, center quadrances, Nine-Point Circle, and Feuerbach's Tangency Theorem (:math:`X_{11}`).
* `staudt <https://geometor.github.io/staudt/>`_ (`GitHub <https://github.com/geometor/staudt>`_): Karl Georg Christian von Staudt's *Geometrie der Lage* (1847) & *Beiträge* (1856–60)—metric-free projective geometry, harmonic nets, the Algebra of Throws (*Würfe*), and the projective regular 17-gon.
* `petersen <https://geometor.github.io/petersen/>`_ (`GitHub <https://github.com/geometor/petersen>`_): Julius Petersen's *Methods and Theories for Geometrical Constructions* (1879)—intersection of two loci, parallel translation, rotation/spiral similarity, and circular inversion.
* `casey <https://geometor.github.io/casey/>`_ (`GitHub <https://github.com/geometor/casey>`_): John Casey's *A Sequel to the First Six Books of Euclid* (1888)—coaxial circles, inversion, Casey's Generalized Ptolemy Bitangent Theorem, and Brocard–Neuberg triangle geometry.
* `lemoine <https://geometor.github.io/lemoine/>`_ (`GitHub <https://github.com/geometor/lemoine>`_): Émile Lemoine's *Géométrographie* (1902 French + English)—operational Simplicity (:math:`S`) and Exactness (:math:`E`) of compass-and-straightedge constructions plus Symmedian (:math:`X_6`) geometry.
* `klein <https://geometor.github.io/klein/>`_ (`GitHub <https://github.com/geometor/klein>`_): Felix Klein's *Erlangen Program* (1872) & *Famous Problems of Elementary Geometry* (1895)—transformation groups, quadratic-radical constructibility, Gauss's 17-gon, and the transcendence of :math:`e` and :math:`\pi`.
* `altshiller-court <https://geometor.github.io/altshiller-court/>`_ (`GitHub <https://github.com/geometor/altshiller-court>`_): Nathan Altshiller-Court's *College Geometry*—one-item-per-page proposition codex with calibrated and hero SVGs across 10 chapters.
* `fundamentals <https://geometor.github.io/fundamentals/>`_ (`GitHub <https://github.com/geometor/fundamentals>`_): The **Fred W. Seelig Archive**—**55 foundational topics** (``F.1``–``F.55``) and **353 manuscript folios** uniting triangle synthesis, harmonic duality, Conway notation, and sacred proportions.
* `etc <https://geometor.github.io/etc/>`_ (`GitHub <https://github.com/geometor/etc>`_): **Catalog** of Clark Kimberling's *Encyclopedia of Triangle Centers* (**53,144 centers parsed**; **4,000+ centers compiled** across **62 collections** with **16,000+ interactive SVGs**).
* `wildberger <https://geometor.github.io/wildberger/>`_ (`GitHub <https://github.com/geometor/wildberger>`_): **Catalog** of Norman J. Wildberger's *Divine Proportions*—exact ``SymPy`` proofs for Quadrance, Spread, pentagonal/golden Spread Polynomials, Triple Quad/Spread/Cross Laws, and Chromogeometry.

III. Philosophical, Renaissance, Harmonic & Axiomatic Scriptorium
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* `plato <https://geometor.github.io/plato/>`_ (`GitHub <https://github.com/geometor/plato>`_): *Geometric & Mathematical Dialogues* (Burnet Greek + Jowett English)—*Meno* diagonal square-doubling, *Republic* Divided Line & Quadrivium, and *Timaeus* World-Soul ratios & elemental triangles/solids.
* `aristotle <https://geometor.github.io/aristotle/>`_ (`GitHub <https://github.com/geometor/aristotle>`_): *Loci Geometrici et Noetici*—critical selections from *Posterior Analytics*, *Physics*, *Metaphysics* IX.9, *De Anima*, and *De Caelo* in Bekker Greek, English, and geometric commentary.
* `nicomachus <https://geometor.github.io/nicomachus/>`_ (`GitHub <https://github.com/geometor/nicomachus>`_): Nicomachus of Gerasa's *Introduction to Arithmetic* (Hoche 1866 Greek + D'Ooge 1926 English)—the Quadrivium, Three-Term Unfolding from Equality :math:`(1,1,1)`, polygonal gnomons, 10 means, and :math:`6:8::9:12` Cube Harmony.
* `proclus <https://geometor.github.io/proclus/>`_ (`GitHub <https://github.com/geometor/proclus>`_): *Commentary on the First Book of Euclid's Elements* (c. 470 AD)—4-Track Codex (*English*, *Friedlein Greek 1873*, *Summary*, *Notes*) with a 164-locus concordance on *phantasia* and *probole*.
* `fibonacci <https://geometor.github.io/fibonacci/>`_ (`GitHub <https://github.com/geometor/fibonacci>`_): Leonardo Pisano (Fibonacci)'s *Liber Abaci* (1202) & *Practica Geometriae* (1220)—Boncompagni Latin + English on the rabbit recurrence :math:`F_n`, continued fractions, and golden pentagon/decagon measurement.
* `aquinas <https://geometor.github.io/aquinas/>`_ (`GitHub <https://github.com/geometor/aquinas>`_): *Opera de Scientia Mathematica et Materia Intelligibili*—4-Track Codex across 37 sections (*Super Boetium De Trinitate* qq. 5–6, *In Post. Anal.*, *In De Anima*, *In Phys.*, *In Metaph.*) with a 78-locus Hoenen concordance.
* `cusa <https://geometor.github.io/cusa/>`_ (`GitHub <https://github.com/geometor/cusa>`_): Nicholas of Cusa's *De Docta Ignorantia* (*On Learned Ignorance*, 1440 Latin + English)—the *coincidentia oppositorum* of infinite line, triangle, circle, and sphere.
* `pacioli <https://geometor.github.io/pacioli/>`_ (`GitHub <https://github.com/geometor/pacioli>`_): Fra Luca Pacioli's *De Divina Proportione* (1509, **Leonardo da Vinci's 60 polyhedra woodcuts**) & geometric *Distinctio* of the *Summa de Arithmetica* (1494).
* `durer <https://geometor.github.io/durer/>`_ (`GitHub <https://github.com/geometor/durer>`_): Albrecht Dürer's *Underweysung der Messung* (Nuremberg, 1525 German + English)—spirals, projective conics, single-compass pentagon, unfolded polyhedral nets, letterforms, and perspective.
* `kepler <https://geometor.github.io/kepler/>`_ (`GitHub <https://github.com/geometor/kepler>`_): Johannes Kepler's *Mysterium Cosmographicum* (1596), *Strena* (1611), & *Harmonices Mundi* (1619)—nested Platonic solids, 6-cornered snowflake & rhombic dodecahedron, *Scibilia* polygons, Kepler Triangle :math:`(1,\sqrt{\phi},\phi)`, and Harmonic Third Law.
* `hilbert <https://geometor.github.io/hilbert/>`_ (`GitHub <https://github.com/geometor/hilbert>`_): David Hilbert's *Grundlagen der Geometrie / Foundations of Geometry* (1899/1902)—German text, Townsend English translation, and metamathematical independence models.
* `poincare <https://geometor.github.io/poincare/>`_ (`GitHub <https://github.com/geometor/poincare>`_): Henri Poincaré's *Science and Hypothesis* (1902/1905 French + English)—conventionalism, transformation groups, and the conformal Poincaré disk model of hyperbolic geometry.
* `bertrand-russell <https://geometor.github.io/bertrand-russell/>`_ (`GitHub <https://github.com/geometor/bertrand-russell>`_): Bertrand Russell's *An Essay on the Foundations of Geometry* (1897) and *The Principles of Mathematics* Part VI *Space* (1903) tracing projective vs. metrical foundations.
* `hoenen <https://geometor.github.io/hoenen/>`_ (`GitHub <https://github.com/geometor/hoenen>`_): Facing Latin–English edition of Petrus Hoenen, S.J.'s *De Noetica Geometriae* (1954) on *intuitive formal abstraction* and the origin of geometric certainty.
* `russell <https://geometor.github.io/russell/>`_ (`GitHub <https://github.com/geometor/russell>`_): Digital edition and 3D cube-sphere wave-field reconstruction of Walter & Lao Russell's 48-lesson *Home Study Course* (180 vector figures).

IV. Living Geometry & Morphogenesis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* `phyllotaxis <https://geometor.github.io/phyllotaxis/>`_ (`GitHub <https://github.com/geometor/phyllotaxis>`_): Symbolic golden-angle divergence (:math:`\Phi = 2\pi(1 - 1/\phi) \approx 137.50776^\circ`), opposing Fibonacci parastichy curves, and live `2D Apical Meristem <https://geometor.github.io/phyllotaxis/demos/meristem_2d.html>`_ & `3D Recursive Propagation <https://geometor.github.io/phyllotaxis/demos/propagation_3d.html>`_ WebGL laboratories.
* `thompson <https://geometor.github.io/thompson/>`_ (`GitHub <https://github.com/geometor/thompson>`_): Sir D'Arcy Wentworth Thompson's *On Growth and Form* (1917 Cambridge 1st ed.)—Plateau soap-film angles, Maraldi honeycomb rhombic apex, gnomonic logarithmic shells, and Cartesian transformation grids.
* `knott <https://geometor.github.io/knott/>`_ (`GitHub <https://github.com/geometor/knott>`_): **Catalog** of Ron Knott's *Fibonacci Numbers, the Golden Section & Wythoff Geometry*—Pisano periods, Zeckendorf representations, golden gnomons, continued fractions, and Wythoff's Nim.

V. Machine Reasoning & Program Synthesis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* `seer <https://geometor.github.io/seer/>`_ (`GitHub <https://github.com/geometor/seer>`_): Multi-agent neuro-symbolic architecture (*Dreamer* + *Coder*) synthesizing verifiable Python ``transform()`` programs for abstract spatial reasoning benchmarks (ARC-AGI).
* `seer_navigator <https://geometor.github.io/seer_navigator/>`_ (`GitHub <https://github.com/geometor/seer_navigator>`_) & `seer_sessions <https://geometor.github.io/seer_sessions/>`_ (`GitHub <https://github.com/geometor/seer_sessions>`_): ``Textual`` terminal trajectory browser and static observatory indexing **8,514 task runs** across **2,939 puzzles** and **475 sessions**.

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
