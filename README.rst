GEOMETOR
========

*Exploring the architecture of all that is.*

Overview
--------

This repository hosts the narrative source, symbolic hero diagram generator, and Sphinx configuration for `geometor.com <https://geometor.com>`_, the central threshold of the **GEOMETOR** initiative.

GEOMETOR investigates geometry as humanity's most concise language for documenting nature, proportion, and deductive truth—grounding every construction in **exact symbolic algebra** (`SymPy <https://www.sympy.org/>`_) rather than floating-point approximation, and recasting 2,300 years of mathematical heritage into multi-track **Book Codices**, interactive laboratories, and visual broadcasts.

The Five Pillars
----------------

1. **The Symbolic Core & Discovery Engine**
   - `model <https://github.com/geometor/model>`_ (`Docs <https://geometor.github.io/model/>`_): Exact ``SymPy`` compass-and-straightedge algebra, rational trigonometry invariants (quadrance, spread, cross-ratio), and ancestral dependency DAGs.
   - `explorer <https://github.com/geometor/explorer>`_ (`Docs <https://geometor.github.io/explorer/>`_): Interactive SVG workbench, symbolic CLI, and animation exporter.
   - `divine <https://github.com/geometor/divine>`_ (`Docs <https://geometor.github.io/divine/>`_): Automated golden ratio (:math:`\phi`), golden chain, and harmonic range discovery.
   - `trees <https://github.com/geometor/trees>`_: Monotone planar tree drawing via Stern–Brocot trees and Farey sequences.

2. **The Unfolding Canon (The Elementrium)**
   - `euclid <https://geometor.github.io/euclid/>`_ (`Repo <https://github.com/geometor/euclid>`_): Sir Thomas L. Heath's 13-Book *Elements* (1,416 folios, 465 propositions, 831 SVGs, 2-Track Codex).
   - `elements <https://geometor.github.io/elements/>`_ (`Repo <https://github.com/geometor/elements>`_): 601-node topological G-Index (``G.1``–``G.601``) in a 3-Track Codex (*Pseudocode*, *Python*, *Heath*).
   - `fundamentals <https://geometor.github.io/fundamentals/>`_ (`Repo <https://github.com/geometor/fundamentals>`_): Fred W. Seelig Archive (55 topics ``F.1``–``F.55``, 353 manuscript folios).
   - `altshiller-court <https://geometor.github.io/altshiller-court/>`_ (`Repo <https://github.com/geometor/altshiller-court>`_): Nathan Altshiller-Court's *College Geometry* (334 folios, 699 articles on modern triangle and circle synthesis).
   - `etc <https://geometor.github.io/etc/>`_ (`Repo <https://github.com/geometor/etc>`_): Clark Kimberling's *Encyclopedia of Triangle Centers* (:math:`X_1`–:math:`X_{53144}`, 4,000+ compiled centers, 16,000+ SVGs).
   - `pappus <https://geometor.github.io/pappus/>`_ (`Repo <https://github.com/geometor/pappus>`_): Exact projective theorems, Pascal's *Hexagrammum Mysticum*, harmonic conjugates, and golden conics.
   - `wildberger <https://geometor.github.io/wildberger/>`_ (`Repo <https://github.com/geometor/wildberger>`_): Norman J. Wildberger's *Divine Proportions: Rational Trigonometry to Universal Geometry*.

3. **Historical, Epistemological & Axiomatic Scriptorium**
   - `aristotle <https://geometor.github.io/aristotle/>`_ (`Repo <https://github.com/geometor/aristotle>`_): *Loci Geometrici et Noetici* in Bekker Greek, English, and commentary.
   - `proclus <https://geometor.github.io/proclus/>`_ (`Repo <https://github.com/geometor/proclus>`_): *Commentary on Book I of Euclid's Elements* (4-Track Codex + 164-locus concordance).
   - `aquinas <https://geometor.github.io/aquinas/>`_ (`Repo <https://github.com/geometor/aquinas>`_): *Opera de Scientia Mathematica et Materia Intelligibili* (4-Track Codex + Hoenen concordance).
   - `pacioli <https://geometor.github.io/pacioli/>`_ (`Repo <https://github.com/geometor/pacioli>`_): Fra Luca Pacioli's *De Divina Proportione* (1509) 5-Track Codex with Leonardo da Vinci's 60 polyhedra plates.
   - `hilbert <https://geometor.github.io/hilbert/>`_ (`Repo <https://github.com/geometor/hilbert>`_): David Hilbert's *Grundlagen der Geometrie / Foundations of Geometry* (1899/1902).
   - `bertrand-russell <https://geometor.github.io/bertrand-russell/>`_ (`Repo <https://github.com/geometor/bertrand-russell>`_): Bertrand Russell's *Foundations of Geometry* (1897) & *Principles of Mathematics* Part VI *Space* (1903).
   - `hoenen <https://geometor.github.io/hoenen/>`_ (`Repo <https://github.com/geometor/hoenen>`_): Petrus Hoenen, S.J.'s *De Noetica Geometriae* (1954) in facing Latin and English.
   - `russell <https://geometor.github.io/russell/>`_ (`Repo <https://github.com/geometor/russell>`_): Walter & Lao Russell's 48-lesson *Home Study Course* with 180 vector figures and 3D wave-field geometry.

4. **Living Geometry & Morphogenesis**
   - `phyllotaxis <https://geometor.github.io/phyllotaxis/>`_ (`Repo <https://github.com/geometor/phyllotaxis>`_): Golden divergence, Fibonacci parastichies, and interactive 2D Canvas & 3D WebGL meristem studios.

5. **Machine Reasoning & Program Synthesis**
   - `seer <https://geometor.github.io/seer/>`_ (`Repo <https://github.com/geometor/seer>`_): Neuro-symbolic Python program synthesis (*Dreamer* + *Coder*) for ARC-AGI.
   - `seer_navigator <https://geometor.github.io/seer_navigator/>`_ (`Repo <https://github.com/geometor/seer_navigator>`_): ``Textual`` TUI trajectory browser.
   - `seer_sessions <https://geometor.github.io/seer_sessions/>`_ (`Repo <https://github.com/geometor/seer_sessions>`_): Longitudinal reasoning observatory across 8,514 task runs.

Build & Development
-------------------

This site is built with Sphinx using `photon-platform/publish <https://github.com/photon-platform/publish>`_ (the ``foundation`` Scriptorium theme).

To regenerate the symbolic hero SVG and build the HTML portal into ``docs/``:

.. code-block:: bash

   uv run python scripts/build_hero_svg.py
   publish build

Links
-----

- **Portal**: https://geometor.com
- **YouTube Broadcasts**: https://www.youtube.com/@geometor
- **GitHub Organization**: https://github.com/geometor
- **Discussions**: https://github.com/orgs/geometor/discussions
