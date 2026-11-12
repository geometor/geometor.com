Squaring the Circle, Kepler's Triangle & the Pyramids
=====================================================

.. rubric:: Circle–Square Harmonics and the :math:`(1, \sqrt{\phi}, \phi)` Right Triangle

Since Egyptian rope-stretchers and Greek geometers first sought a square equal in perimeter or area to a given circle, **squaring the circle** has stood at the threshold between algebraic constructibility and transcendental measure.

Exact Impossibility vs. Remarkable Harmonic Resonance
-----------------------------------------------------

By Lindemann's theorem (1882), :math:`\pi` is **transcendental** over :math:`\mathbb{Q}`: no finite sequence of unmarked straightedge and compass intersections (`geometor.model`) can construct a segment of exact length :math:`\sqrt{\pi}` or :math:`\frac{\pi}{4}`.

Yet when we examine the **Kepler Right Triangle**—the unique right triangle whose side lengths are in **geometric progression**—an extraordinary near-resonance between :math:`\phi` and :math:`\pi` appears:

The Kepler Golden Right Triangle :math:`(1, \sqrt{\phi}, \phi)`
---------------------------------------------------------------

Suppose a right triangle has legs :math:`1` and :math:`x` and hypotenuse :math:`x^2` in geometric progression :math:`1 : x : x^2`. By the Pythagorean theorem (or rational quadrance law :math:`Q_1 + Q_2 = Q_3`):

.. math::

   1 + x^2 = x^4 \implies (x^2)^2 - x^2 - 1 = 0 \implies x^2 = \phi, \quad x = \sqrt{\phi}

Thus the **quadrances** of the Kepler triangle are :math:`(1,\, \phi,\, \phi^2 = \phi + 1)`—the Golden Ratio itself embodied as a right triangle!

* In `geometor/etc <https://geometor.github.io/etc/>`_, the **Kepler Golden Right Triangle** ``(1, √φ, φ)`` serves as one of our four canonical reference triangles alongside Acute ``(5,6,7)``, Egyptian Right ``(3,4,5)``, and Kimberling ``(6,9,13)``.
* Rotating two Kepler triangles back-to-back along their :math:`\sqrt{\phi}` altitude forms the meridian cross-section traditionally associated with the **Great Pyramid of Giza**: base :math:`2`, apothem (slant height) :math:`\phi`, and altitude :math:`\sqrt{\phi}` (slope angle :math:`\arctan(\sqrt{\phi}) \approx 51^\circ 49' 38''`).

Perimeter and Area Circle–Square Proportions
--------------------------------------------

Consider a circle of radius :math:`r = \sqrt{\phi}` (altitude of the pyramid) and a square of side :math:`s = 2` (base of the pyramid):

* **Square perimeter**: :math:`P_{\square} = 4 \times 2 = 8`.
* **Circle circumference** with radius :math:`\sqrt{\phi}`: :math:`C_{\bigcirc} = 2\pi\sqrt{\phi} \approx 7.9923\dots` — agreeing with :math:`P_{\square}` to **within** :math:`0.096\%` (reflecting the classic algebraic approximation :math:`\pi \approx \frac{4}{\sqrt{\phi}} \approx 3.1446055\dots`)!

Because GEOMETOR works in **exact symbolic algebra**, we never confuse :math:`\frac{4}{\sqrt{\phi}}` with transcendental :math:`\pi`—instead, we can quantify the exact algebraic geometry of the Kepler triangle alongside the full archival analysis of circle–square and pyramid proportions preserved in **Fred W. Seelig's notebooks** (`geometor/fundamentals <https://geometor.github.io/fundamentals/>`_, Topics ``F.18``–``F.49``).
