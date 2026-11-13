Medieval Transmission, Renaissance Proportion & Classical Triangle Statics
==========================================================================

.. rubric:: Fibonacci · Aquinas · Nicholas of Cusa · Pacioli & Leonardo · Dürer · Kepler · Pascal · Ceva · Euler & Feuerbach

----

Leonardo Pisano — Fibonacci (c. 1170 – c. 1250)
-----------------------------------------------

* **GEOMETOR Edition**: `fibonacci — Liber Abaci (1202) & Practica Geometriae (1220) <https://geometor.github.io/fibonacci/>`_ (`Repo <https://github.com/geometor/fibonacci>`_)

Pisan mathematician whose *Liber Abaci* introduced Hindu–Arabic positional arithmetic, unit-fraction decompositions, and the additive **Fibonacci recurrence** :math:`1, 1, 2, 3, 5, 8, 13, 21, \dots` to Latin Europe, while his *Practica Geometriae* transmitted exact Euclidean and Ptolemaic radical measurements of the regular pentagon, decagon, and icosahedron over :math:`\mathbb{Q}(\sqrt{5})`.

----

St. Thomas Aquinas (1225–1274)
------------------------------

* **GEOMETOR Edition**: `aquinas — Opera de Scientia Mathematica et Materia Intelligibili <https://geometor.github.io/aquinas/>`_ (`Repo <https://github.com/geometor/aquinas>`_)

In *Super Boetium De Trinitate* (Questions 5 and 6) and his commentaries on Aristotle's *Posterior Analytics*, *Physics*, *De Anima*, and *Metaphysics*, Aquinas articulated how mathematics stands uniquely poised between natural physics and pure metaphysics: mathematical judgment abstracts from sensible qualities while terminating in the imagination's **intelligible matter** (*materia intelligibilis*)—pure continuous extension in which geometric necessity is verified without empirical uncertainty.

----

Nicholas of Cusa (1401–1464)
----------------------------

* **GEOMETOR Edition**: `cusa — De Docta Ignorantia (1440) <https://geometor.github.io/cusa/>`_ (`Repo <https://github.com/geometor/cusa>`_)

German cardinal, jurist, and philosopher whose *De Docta Ignorantia* (*On Learned Ignorance*, Book I) employed exact **transsumptive mathematical symbolism** to contemplate the Infinite: as radius grows without bound, the curved circumference approaches coincidence with its straight tangent (*coincidentia oppositorum*)—inspiring Kepler (*"divinus mihi Cusanus"*), Desargues's points at infinity, and modern limiting geometry.

----

Fra Luca Pacioli (c. 1447–1517) & Leonardo da Vinci (1452–1519)
---------------------------------------------------------------

* **GEOMETOR Editions**: `pacioli — De Divina Proportione (1509) <https://geometor.github.io/pacioli/>`_ · `Summa de Arithmetica (1494) <https://geometor.github.io/pacioli/summa_1494/>`_ (`Repo <https://github.com/geometor/pacioli>`_)

Franciscan mathematician **Luca Pacioli**—steward of Piero della Francesca's polyhedral geometry and mathematical collaborator with **Leonardo da Vinci** at the court of Milan—published both the encyclopedic *Summa* (1494) and *De Divina Proportione* (1509). Celebrating Euclid's Extreme and Mean Ratio through its *thirteen admirable effects*, architectural proportions, Roman majuscule letterforms, and **Leonardo's 60 unprecedented solid (*solido*) and skeletal (*vacuo*) perspective woodcuts** of the Platonic, Archimedean, and stellated polyhedra, Pacioli gave the Golden Ratio its Renaissance name.

----

Albrecht Dürer (1471–1528)
--------------------------

* **GEOMETOR Edition**: `durer — Underweysung der Messung (1525) <https://geometor.github.io/durer/>`_ (`Repo <https://github.com/geometor/durer>`_)

Master printmaker and geometer of Nuremberg whose *Underweysung der Messung mit dem Zirckel und Richtscheyt* (1525) founded German constructive geometry: introducing **parallel-projection conic sections** (anticipating Monge's descriptive geometry), **unfolded polyhedral paper nets** (*Netze*), the classic **fixed-compass pentagon**, modular Roman and Fraktur letterforms, and mechanical perspective frames.

----

Johannes Kepler (1571–1630)
---------------------------

* **GEOMETOR Edition**: `kepler — Mysterium (1596), Strena (1611) & Harmonices Mundi (1619) <https://geometor.github.io/kepler/>`_ (`Repo <https://github.com/geometor/kepler>`_) · `etc (Kepler Reference Triangle) <https://geometor.github.io/etc/>`_

In *Mysterium Cosmographicum* (1596), *Strena seu de Nive Sexangula* (1611), and *Harmonices Mundi* (1619), Kepler famously declared:

.. epigraph::

   *"Geometry has two great treasures: one is the Theorem of Pythagoras; the other, the division of a line into extreme and mean ratio. The first we may compare to a measure of gold; the second we may name a precious jewel."*

Kepler nested the five Platonic solids among the planetary spheres, discovered the **rhombic dodecahedron**, formulated the **sphere-packing conjecture** :math:`\pi/(3\sqrt{2})`, connected Fibonacci ratios to botanical phyllotaxis, classified the **11 Archimedean tilings** and star polyhedra, identified the **Kepler Right Triangle** :math:`(1, \sqrt{\phi}, \phi)`, and discovered the **Harmonic Third Law** :math:`T^2 \propto a^3`.

----

Blaise Pascal (1623–1662)
-------------------------

* **Featured in**: `pappus (Hexagrammum Mysticum) <https://geometor.github.io/pappus/>`_

At age sixteen, Pascal generalized Pappus's two-line hexagon theorem to any six points inscribed on a non-degenerate conic (*Essai pour les coniques*, 1640): opposite sides of an inscribed hexagon meet in three collinear points along a **Pascal line**. Permuting six vertices yields the **60 Pascal lines**, **20 Steiner points**, **60 Kirkman points**, and **15 Plücker lines** of the *Hexagrammum Mysticum*—verified symbolically in exact ``SymPy`` algebra inside ``geometor/pappus``.

----

Giovanni Ceva (1647–1734)
-------------------------

* **GEOMETOR Edition**: `ceva — De lineis rectis se invicem secantibus statica constructio (1678) <https://geometor.github.io/ceva/>`_ (`Repo <https://github.com/geometor/ceva>`_)

Milanese and Mantuan geometer who elevated Archimedes' Law of the Lever into pure incidence geometry: by placing virtual statical weights at the vertices of a triangle (and tetrahedron), Ceva proved **Ceva's Concurrency Theorem** (:math:`\frac{AF}{FB}\cdot\frac{BD}{DC}\cdot\frac{CE}{EA} = 1`) alongside Menelaus's dual—planting the direct conceptual seed of Möbius's **homogeneous barycentric coordinates** powering ``geometor/etc``.

----

Leonhard Euler (1707–1783) & Karl Wilhelm Feuerbach (1800–1834)
---------------------------------------------------------------

* **GEOMETOR Edition**: `feuerbach — Founding Trilogy of Triangle Geometry <https://geometor.github.io/feuerbach/>`_ (`Repo <https://github.com/geometor/feuerbach>`_)

In memoir *E325* (*Solutio facilis*, 1765), **Leonhard Euler** computed the exact algebraic distances among the four classical centers of any scalene triangle—discovering :math:`OI^2 = R^2 - 2Rr` and the **Euler Line** (:math:`X_4, X_2, X_3`). Fifty-seven years later in Nuremberg (*Eigenschaften*, 1822), **Karl Wilhelm Feuerbach** proved that the circle through the side-midpoints and altitude-feet (center :math:`X_5`, radius :math:`R/2`) **touches the incircle internally at the Feuerbach point** :math:`X_{11}` and all three excircles externally—inaugurating modern triangle geometry.
