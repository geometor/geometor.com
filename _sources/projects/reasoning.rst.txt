V. Machine Reasoning & Program Synthesis
========================================

.. rubric:: Neuro-Symbolic Visual Induction & Verifiable Python Transformations

Can a machine reason like a geometer—observing only a handful of visual transformations, abstracting the underlying invariant law, and expressing it as an exact, verifiable program rather than a statistical pixel guess?

----

``seer`` — Multi-Agent Program Synthesis for Abstract Visual Reasoning
----------------------------------------------------------------------

* **Documentation**: `geometor.github.io/seer <https://geometor.github.io/seer/>`_
* **Repository**: `github.com/geometor/seer <https://github.com/geometor/seer>`_

Built for the **Abstraction and Reasoning Corpus (ARC-AGI)**, ``geometor.seer`` rejects direct matrix-to-matrix neural hallucination in favor of **neuro-symbolic program synthesis**:

* **The Dreamer**: Perceives input–output grid pairs as structured spatial objects, symmetries, enclosures, rays, and topological invariants, formulating natural-language geometric hypotheses.
* **The Coder**: Translates hypotheses into executable Python ``transform(grid)`` programs, testing them against every demonstration pair and iteratively refining the hypothesis from exact pixel-level discrepancies.

----

``seer_navigator`` — Terminal Trajectory Browser
------------------------------------------------

* **Documentation**: `geometor.github.io/seer_navigator <https://geometor.github.io/seer_navigator/>`_
* **Repository**: `github.com/geometor/seer_navigator <https://github.com/geometor/seer_navigator>`_

A fast ``Textual`` terminal user interface (TUI) for browsing multi-step ``seer`` reasoning trajectories, inspecting synthesized Python programs, comparing predicted vs. expected grids, and diagnosing failure modes across solver runs.

----

``seer_sessions`` — Longitudinal Reasoning Observatory
------------------------------------------------------

* **Live Observatory**: `geometor.github.io/seer_sessions <https://geometor.github.io/seer_sessions/>`_
* **Repository**: `github.com/geometor/seer_sessions <https://github.com/geometor/seer_sessions>`_

An empirical archive, mining suite, and static web observatory spanning **8,514 task runs**, **2,939 unique visual reasoning puzzles**, and **475 experimental sessions**—documenting how symbolic verification, iterative error feedback, and geometric priors govern machine abstraction.
