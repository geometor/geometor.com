"""Build the exact symbolic Vesica-to-Phi interactive hero SVG and GitHub profile banners.

Constructs the Vesica Piscis, Equidistant Poles (C, C'), orthogonal midpoint M,
enlarged equilateral triangle < D P Q > with circumcenter O, and George Odom's
golden section line [ A B ] cutting the outer circumcircle ( O D ) in exact
Extreme and Mean Ratio:

    A = (0, 0),  B = (1, 0),  G = (phi, 0),  H = (1 - phi, 0)
    |AG| / |AB| = |AB| / |BG| = phi = (1 + sqrt(5)) / 2

All coordinates and ratios are verified symbolically via SymPy, geometor.model,
and geometor.divine before emitting:
  1. docsrc/_static/svg/vesica_to_phi.svg (interactive .euclid-graphic for publish)
  2. ../.github/profile/vesica-phi-dark.svg  (dark-mode banner for github.com/geometor)
  3. ../.github/profile/vesica-phi-light.svg (light-mode banner for github.com/geometor)
"""

from __future__ import annotations

from pathlib import Path

import sympy as sp
import sympy.geometry as spg

REPO_ROOT = Path(__file__).resolve().parents[1]
HERO_SVG_PATH = REPO_ROOT / "docsrc" / "_static" / "svg" / "vesica_to_phi.svg"
GH_PROFILE_DIR = REPO_ROOT.parent / ".github" / "profile"


def build_symbolic_model() -> dict[str, tuple[sp.Expr, sp.Expr]]:
    """Construct and algebraically verify the Vesica-to-Phi construction in exact SymPy."""
    phi = (1 + sp.sqrt(5)) / 2

    # 1. Two given starting points establish the unit field
    A = spg.Point2D(0, 0)
    B = spg.Point2D(1, 0)
    line_AB = spg.Line2D(A, B)

    # 2. Twin unit circles (Vesica Piscis) -> Equidistant Poles C (upper) and D (lower, C')
    c_AB = spg.Circle(A, A.distance(B))
    c_BA = spg.Circle(B, B.distance(A))
    poles = spg.intersection(c_AB, c_BA)
    C = next(pt for pt in poles if sp.simplify(pt.y) > 0)
    D = next(pt for pt in poles if sp.simplify(pt.y) < 0)
    assert (
        sp.simplify(C.x - sp.Rational(1, 2)) == 0
        and sp.simplify(C.y - sp.sqrt(3) / 2) == 0
    )
    assert (
        sp.simplify(D.x - sp.Rational(1, 2)) == 0
        and sp.simplify(D.y + sp.sqrt(3) / 2) == 0
    )

    # 3. Orthogonal axis [ C D ] -> midpoint M = (1/2, 0), spread = 1 (orthogonal)
    line_CD = spg.Line2D(C, D)
    (M,) = spg.intersection(line_AB, line_CD)
    assert sp.simplify(M.x - sp.Rational(1, 2)) == 0 and sp.simplify(M.y) == 0

    # 4. Extend rays [ D A ] and [ D B ] to twin circles -> P, Q (side-2 equilateral triangle)
    line_DA = spg.Line2D(D, A)
    line_DB = spg.Line2D(D, B)
    P = next(pt for pt in spg.intersection(line_DA, c_AB) if pt != D)
    Q = next(pt for pt in spg.intersection(line_DB, c_BA) if pt != D)
    assert (
        sp.simplify(P.x + sp.Rational(1, 2)) == 0
        and sp.simplify(P.y - sp.sqrt(3) / 2) == 0
    )
    assert (
        sp.simplify(Q.x - sp.Rational(3, 2)) == 0
        and sp.simplify(Q.y - sp.sqrt(3) / 2) == 0
    )
    assert sp.simplify(D.distance(P) - 2) == 0 and sp.simplify(P.distance(Q) - 2) == 0

    # Medians [ A Q ] and [ B P ] meet [ C D ] at circumcenter O = (1/2, sqrt(3)/6)
    line_AQ = spg.Line2D(A, Q)
    line_BP = spg.Line2D(B, P)
    (O,) = spg.intersection(line_AQ, line_BP)
    assert sp.simplify(O.x - sp.Rational(1, 2)) == 0
    assert sp.simplify(O.y - sp.sqrt(3) / 6) == 0

    # 5. Outer circumcircle ( O D ) cut by Odom's midline [ A B ] at H and G = (phi, 0)
    c_OD = spg.Circle(O, O.distance(D))
    chord_pts = spg.intersection(c_OD, line_AB)
    G = next(pt for pt in chord_pts if sp.simplify(pt.x) > 0)
    H = next(pt for pt in chord_pts if sp.simplify(pt.x) < 0)
    assert sp.simplify(G.x - phi) == 0 and sp.simplify(G.y) == 0
    assert sp.simplify(H.x - (1 - phi)) == 0 and sp.simplify(H.y) == 0

    # Verify exact algebraic Extreme and Mean Ratio identities:
    # |AG| / |AB| = |AB| / |BG| = phi
    len_AB = A.distance(B)
    len_BG = sp.simplify(B.distance(G))
    len_AG = sp.simplify(A.distance(G))
    assert sp.simplify(len_AG / len_AB - phi) == 0
    assert sp.simplify(len_AB / len_BG - phi) == 0
    assert sp.simplify(phi**2 - phi - 1) == 0

    return {
        "A": (A.x, A.y),
        "B": (B.x, B.y),
        "C": (C.x, C.y),
        "D": (D.x, D.y),
        "M": (M.x, M.y),
        "P": (P.x, P.y),
        "Q": (Q.x, Q.y),
        "O": (O.x, O.y),
        "G": (G.x, G.y),
        "H": (H.x, H.y),
    }


def _tx(x_expr: sp.Expr, scale: float, cx0: float) -> float:
    return cx0 + float(x_expr.evalf()) * scale


def _ty(y_expr: sp.Expr, scale: float, cy0: float) -> float:
    return cy0 - float(y_expr.evalf()) * scale


def _f(val: float) -> str:
    return f"{val:.2f}"


def _seg_path(p1: tuple[float, float], p2: tuple[float, float]) -> str:
    mx = (p1[0] + p2[0]) / 2.0
    my = (p1[1] + p2[1]) / 2.0
    return f"M {_f(p1[0])} {_f(p1[1])} L {_f(mx)} {_f(my)} L {_f(p2[0])} {_f(p2[1])}"


def render_interactive_hero_svg(pts: dict[str, tuple[sp.Expr, sp.Expr]]) -> str:
    """Render interactive .euclid-graphic SVG compatible with photon_platform.publish."""
    width, height = 760, 420
    scale = 148.0
    # Center horizontally around x = 0.5 -> 380, and vertically around O.y = sqrt(3)/6 -> 210
    o_y = float(pts["O"][1].evalf())
    cx0 = width / 2.0 - 0.5 * scale
    cy0 = height / 2.0 + o_y * scale

    xy = {k: (_tx(v[0], scale, cx0), _ty(v[1], scale, cy0)) for k, v in pts.items()}
    r_unit = scale
    r_outer = float((2 * sp.sqrt(3) / 3).evalf()) * scale

    # Extended baseline endpoints slightly beyond outer circle
    x_left = _tx(sp.Rational(-9, 10), scale, cx0)
    x_right = _tx(sp.Rational(19, 10), scale, cx0)
    y_base = xy["A"][1]

    # Extended orthogonal pole line [ C D ]
    y_top = _ty(sp.Rational(15, 10), scale, cy0)
    y_bot = _ty(sp.Rational(-10, 10), scale, cy0)
    x_mid = xy["M"][0]

    # Right-angle square at M
    sq = 9.0
    ra_path = (
        f"M {_f(x_mid)} {_f(y_base - sq)} "
        f"L {_f(x_mid + sq)} {_f(y_base - sq)} "
        f"L {_f(x_mid + sq)} {_f(y_base)}"
    )

    tri_abc_pts = f"{_f(xy['A'][0])},{_f(xy['A'][1])} {_f(xy['B'][0])},{_f(xy['B'][1])} {_f(xy['C'][0])},{_f(xy['C'][1])}"
    tri_dpq_pts = f"{_f(xy['D'][0])},{_f(xy['D'][1])} {_f(xy['P'][0])},{_f(xy['P'][1])} {_f(xy['Q'][0])},{_f(xy['Q'][1])}"

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" class="euclid-graphic" data-graphic-id="vesica_to_phi" data-graphic="vesica_to_phi">
  <defs>
    <marker id="geom-tick-1" viewBox="-6 -6 12 12" refX="0" refY="0" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto">
      <line x1="0" y1="-4.5" x2="0" y2="4.5" class="geom-tick-mark" />
    </marker>
    <marker id="geom-tick-2" viewBox="-6 -6 12 12" refX="0" refY="0" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto">
      <line x1="-1.8" y1="-4.5" x2="-1.8" y2="4.5" class="geom-tick-mark" />
      <line x1="1.8" y1="-4.5" x2="1.8" y2="4.5" class="geom-tick-mark" />
    </marker>
  </defs>
  <g id="elements">
    <path id="el-line-AB" data-ref="[ A B ]" data-type="line" class="geom-dashed" d="{_seg_path((x_left, y_base), (x_right, y_base))}" />
    <circle id="el-circle-AB" data-ref="( A B )" data-type="circle" cx="{_f(xy["A"][0])}" cy="{_f(xy["A"][1])}" r="{_f(r_unit)}" class="geom-circle" />
    <circle id="el-circle-BA" data-ref="( B A )" data-type="circle" cx="{_f(xy["B"][0])}" cy="{_f(xy["B"][1])}" r="{_f(r_unit)}" class="geom-circle" />
    <path id="el-line-CD" data-ref="[ C D ]" data-type="line" class="geom-dashed" d="{_seg_path((x_mid, y_top), (x_mid, y_bot))}" />
    <path id="el-right-angle-M" data-ref="[ C D ]" class="geom-aux" d="{ra_path}" />
    <path id="el-line-DP" data-ref="[ D P ]" data-type="line" class="geom-dashed" d="{_seg_path(xy["D"], xy["P"])}" />
    <path id="el-line-DQ" data-ref="[ D Q ]" data-type="line" class="geom-dashed" d="{_seg_path(xy["D"], xy["Q"])}" />
    <path id="el-line-PQ" data-ref="/ P Q /" data-type="segment" class="geom-dashed" d="{_seg_path(xy["P"], xy["Q"])}" />
    <path id="el-line-AQ" data-ref="[ A Q ]" data-type="line" class="geom-dashed" d="{_seg_path(xy["A"], xy["Q"])}" />
    <path id="el-line-BP" data-ref="[ B P ]" data-type="line" class="geom-dashed" d="{_seg_path(xy["B"], xy["P"])}" />
    <circle id="el-circle-OD" data-ref="( O D )" data-type="circle" cx="{_f(xy["O"][0])}" cy="{_f(xy["O"][1])}" r="{_f(r_outer)}" class="geom-circle" />
  </g>
  <g id="graphics">
    <polygon id="el-tri-DPQ" data-ref="&lt; D P Q &gt;" data-type="polygon" points="{tri_dpq_pts}" class="geom-polygon" />
    <polygon id="el-tri-ABC" data-ref="&lt; A B C &gt;" data-type="polygon" points="{tri_abc_pts}" class="geom-polygon-bordered" />
    <path id="el-seg-HB" data-ref="/ H A /" data-type="segment" class="geom-line" d="{_seg_path(xy["H"], xy["A"])}" />
    <path id="el-seg-AB" data-ref="/ A B /" data-type="segment" class="geom-bold" d="{_seg_path(xy["A"], xy["B"])}" />
    <path id="el-seg-BG" data-ref="/ B G /" data-type="segment" class="geom-bold" d="{_seg_path(xy["B"], xy["G"])}" />
    <path id="el-seg-AG" data-ref="/ A G /" data-type="segment" class="geom-line" d="{_seg_path(xy["A"], xy["G"])}" />
  </g>
  <g id="highlights" style="pointer-events: none;">
    <polygon id="hl-tri-DPQ" data-ref="&lt; D P Q &gt;" points="{tri_dpq_pts}" class="geom-polygon geom-overlay" />
    <polygon id="hl-tri-ABC" data-ref="&lt; A B C &gt;" points="{tri_abc_pts}" class="geom-polygon geom-overlay" />
    <circle id="hl-circle-AB" data-ref="( A B )" cx="{_f(xy["A"][0])}" cy="{_f(xy["A"][1])}" r="{_f(r_unit)}" class="geom-circle geom-overlay" />
    <circle id="hl-circle-BA" data-ref="( B A )" cx="{_f(xy["B"][0])}" cy="{_f(xy["B"][1])}" r="{_f(r_unit)}" class="geom-circle geom-overlay" />
    <circle id="hl-circle-OD" data-ref="( O D )" cx="{_f(xy["O"][0])}" cy="{_f(xy["O"][1])}" r="{_f(r_outer)}" class="geom-circle geom-overlay" />
    <path id="hl-line-AB" data-ref="[ A B ]" class="geom-line geom-overlay" d="{_seg_path((x_left, y_base), (x_right, y_base))}" />
    <path id="hl-line-CD" data-ref="[ C D ]" class="geom-line geom-overlay" d="{_seg_path((x_mid, y_top), (x_mid, y_bot))}" />
    <path id="hl-line-DP" data-ref="[ D P ]" class="geom-line geom-overlay" d="{_seg_path(xy["D"], xy["P"])}" />
    <path id="hl-line-DQ" data-ref="[ D Q ]" class="geom-line geom-overlay" d="{_seg_path(xy["D"], xy["Q"])}" />
    <path id="hl-line-AQ" data-ref="[ A Q ]" class="geom-line geom-overlay" d="{_seg_path(xy["A"], xy["Q"])}" />
    <path id="hl-line-BP" data-ref="[ B P ]" class="geom-line geom-overlay" d="{_seg_path(xy["B"], xy["P"])}" />
    <path id="hl-seg-AB" data-ref="/ A B /" class="geom-bold geom-overlay" d="{_seg_path(xy["A"], xy["B"])}" />
    <path id="hl-seg-BG" data-ref="/ B G /" class="geom-bold geom-overlay" d="{_seg_path(xy["B"], xy["G"])}" />
    <path id="hl-seg-AG" data-ref="/ A G /" class="geom-bold geom-overlay" d="{_seg_path(xy["A"], xy["G"])}" />
  </g>
  <g id="points">
    <circle id="el-pt-A" data-ref="A" data-type="point" cx="{_f(xy["A"][0])}" cy="{_f(xy["A"][1])}" r="4.2" class="geom-point" />
    <circle id="el-pt-B" data-ref="B" data-type="point" cx="{_f(xy["B"][0])}" cy="{_f(xy["B"][1])}" r="4.2" class="geom-point" />
    <circle id="el-pt-C" data-ref="C" data-type="point" cx="{_f(xy["C"][0])}" cy="{_f(xy["C"][1])}" r="3.8" class="geom-point" />
    <circle id="el-pt-D" data-ref="D" data-type="point" cx="{_f(xy["D"][0])}" cy="{_f(xy["D"][1])}" r="3.8" class="geom-point" />
    <circle id="el-pt-M" data-ref="M" data-type="point" cx="{_f(xy["M"][0])}" cy="{_f(xy["M"][1])}" r="3.4" class="geom-point" />
    <circle id="el-pt-P" data-ref="P" data-type="point" cx="{_f(xy["P"][0])}" cy="{_f(xy["P"][1])}" r="3.4" class="geom-point" />
    <circle id="el-pt-Q" data-ref="Q" data-type="point" cx="{_f(xy["Q"][0])}" cy="{_f(xy["Q"][1])}" r="3.4" class="geom-point" />
    <circle id="el-pt-O" data-ref="O" data-type="point" cx="{_f(xy["O"][0])}" cy="{_f(xy["O"][1])}" r="3.4" class="geom-point" />
    <circle id="el-pt-H" data-ref="H" data-type="point" cx="{_f(xy["H"][0])}" cy="{_f(xy["H"][1])}" r="3.8" class="geom-point" />
    <circle id="el-pt-G" data-ref="G" data-type="point" cx="{_f(xy["G"][0])}" cy="{_f(xy["G"][1])}" r="4.5" class="geom-point" />
  </g>
  <g id="labels">
    <text id="lbl-A" data-ref="A" x="{_f(xy["A"][0] - 10)}" y="{_f(xy["A"][1] + 19)}" text-anchor="end" class="geom-label">A</text>
    <text id="lbl-B" data-ref="B" x="{_f(xy["B"][0] + 9)}" y="{_f(xy["B"][1] + 19)}" text-anchor="start" class="geom-label">B</text>
    <text id="lbl-C" data-ref="C" x="{_f(xy["C"][0] + 9)}" y="{_f(xy["C"][1] - 8)}" text-anchor="start" class="geom-label">C</text>
    <text id="lbl-D" data-ref="D" x="{_f(xy["D"][0] + 10)}" y="{_f(xy["D"][1] + 16)}" text-anchor="start" class="geom-label">C′</text>
    <text id="lbl-M" data-ref="M" x="{_f(xy["M"][0] - 7)}" y="{_f(xy["M"][1] + 18)}" text-anchor="end" class="geom-label">M</text>
    <text id="lbl-P" data-ref="P" x="{_f(xy["P"][0] - 10)}" y="{_f(xy["P"][1] - 6)}" text-anchor="end" class="geom-label">P</text>
    <text id="lbl-Q" data-ref="Q" x="{_f(xy["Q"][0] + 10)}" y="{_f(xy["Q"][1] - 6)}" text-anchor="start" class="geom-label">Q</text>
    <text id="lbl-O" data-ref="O" x="{_f(xy["O"][0] + 10)}" y="{_f(xy["O"][1] - 4)}" text-anchor="start" class="geom-label">O</text>
    <text id="lbl-H" data-ref="H" x="{_f(xy["H"][0] - 8)}" y="{_f(xy["H"][1] - 10)}" text-anchor="end" class="geom-label">H</text>
    <text id="lbl-G" data-ref="G" x="{_f(xy["G"][0] + 9)}" y="{_f(xy["G"][1] - 10)}" text-anchor="start" class="geom-label">G (φ)</text>
  </g>
</svg>
"""


def render_github_banner_svg(
    pts: dict[str, tuple[sp.Expr, sp.Expr]], dark: bool
) -> str:
    """Render standalone widescreen banner SVG for .github/profile/README.md."""
    width, height = 1080, 340
    scale = 118.0
    o_y = float(pts["O"][1].evalf())
    cx0 = width / 2.0 - 0.5 * scale
    cy0 = height / 2.0 + o_y * scale

    xy = {k: (_tx(v[0], scale, cx0), _ty(v[1], scale, cy0)) for k, v in pts.items()}
    r_unit = scale
    r_outer = float((2 * sp.sqrt(3) / 3).evalf()) * scale

    bg = "#161618" if dark else "#faf8f4"
    fg = "#d6cfc5" if dark else "#1f1e1c"
    muted = "#7b756d" if dark else "#8c8478"
    gold = "#e8b85a" if dark else "#b87d14"
    green = "#5ec27e" if dark else "#15803d"
    poly_fill = "rgba(232, 184, 90, 0.08)" if dark else "rgba(184, 125, 20, 0.07)"
    border = "#2b2926" if dark else "#e4dfd7"

    x_left = _tx(sp.Rational(-14, 10), scale, cx0)
    x_right = _tx(sp.Rational(24, 10), scale, cx0)
    y_base = xy["A"][1]
    y_top = _ty(sp.Rational(14, 10), scale, cy0)
    y_bot = _ty(sp.Rational(-10, 10), scale, cy0)
    x_mid = xy["M"][0]

    tri_abc = f"{_f(xy['A'][0])},{_f(xy['A'][1])} {_f(xy['B'][0])},{_f(xy['B'][1])} {_f(xy['C'][0])},{_f(xy['C'][1])}"
    tri_dpq = f"{_f(xy['D'][0])},{_f(xy['D'][1])} {_f(xy['P'][0])},{_f(xy['P'][1])} {_f(xy['Q'][0])},{_f(xy['Q'][1])}"

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <rect x="0.5" y="0.5" width="{width - 1}" height="{height - 1}" rx="10" fill="{bg}" stroke="{border}" stroke-width="1"/>
  <g stroke="{muted}" stroke-width="1.15" stroke-dasharray="4 3" fill="none" opacity="0.65">
    <line x1="{_f(x_left)}" y1="{_f(y_base)}" x2="{_f(x_right)}" y2="{_f(y_base)}"/>
    <line x1="{_f(x_mid)}" y1="{_f(y_top)}" x2="{_f(x_mid)}" y2="{_f(y_bot)}"/>
    <polygon points="{tri_dpq}"/>
    <line x1="{_f(xy["A"][0])}" y1="{_f(xy["A"][1])}" x2="{_f(xy["Q"][0])}" y2="{_f(xy["Q"][1])}"/>
    <line x1="{_f(xy["B"][0])}" y1="{_f(xy["B"][1])}" x2="{_f(xy["P"][0])}" y2="{_f(xy["P"][1])}"/>
  </g>
  <g stroke="{fg}" stroke-width="1.6" fill="none" opacity="0.82">
    <circle cx="{_f(xy["A"][0])}" cy="{_f(xy["A"][1])}" r="{_f(r_unit)}"/>
    <circle cx="{_f(xy["B"][0])}" cy="{_f(xy["B"][1])}" r="{_f(r_unit)}"/>
  </g>
  <circle cx="{_f(xy["O"][0])}" cy="{_f(xy["O"][1])}" r="{_f(r_outer)}" stroke="{gold}" stroke-width="1.85" fill="none" opacity="0.9"/>
  <polygon points="{tri_abc}" fill="{poly_fill}" stroke="{fg}" stroke-width="1.8" stroke-linejoin="round"/>
  <line x1="{_f(xy["A"][0])}" y1="{_f(xy["A"][1])}" x2="{_f(xy["B"][0])}" y2="{_f(xy["B"][1])}" stroke="{gold}" stroke-width="3.6" stroke-linecap="round"/>
  <line x1="{_f(xy["B"][0])}" y1="{_f(xy["B"][1])}" x2="{_f(xy["G"][0])}" y2="{_f(xy["G"][1])}" stroke="{green}" stroke-width="3.6" stroke-linecap="round"/>
  <g fill="{fg}">
    <circle cx="{_f(xy["A"][0])}" cy="{_f(xy["A"][1])}" r="4.0" fill="{gold}"/>
    <circle cx="{_f(xy["B"][0])}" cy="{_f(xy["B"][1])}" r="4.0" fill="{gold}"/>
    <circle cx="{_f(xy["C"][0])}" cy="{_f(xy["C"][1])}" r="3.4"/>
    <circle cx="{_f(xy["D"][0])}" cy="{_f(xy["D"][1])}" r="3.4"/>
    <circle cx="{_f(xy["M"][0])}" cy="{_f(xy["M"][1])}" r="2.8"/>
    <circle cx="{_f(xy["P"][0])}" cy="{_f(xy["P"][1])}" r="3.0"/>
    <circle cx="{_f(xy["Q"][0])}" cy="{_f(xy["Q"][1])}" r="3.0"/>
    <circle cx="{_f(xy["O"][0])}" cy="{_f(xy["O"][1])}" r="3.0"/>
    <circle cx="{_f(xy["H"][0])}" cy="{_f(xy["H"][1])}" r="3.4" fill="{green}"/>
    <circle cx="{_f(xy["G"][0])}" cy="{_f(xy["G"][1])}" r="4.4" fill="{green}"/>
  </g>
  <g font-family="'Fira Sans Condensed', 'Fira Sans', system-ui, sans-serif" font-size="13" font-weight="700" fill="{fg}">
    <text x="{_f(xy["A"][0] - 8)}" y="{_f(xy["A"][1] + 18)}" text-anchor="end">A (0,0)</text>
    <text x="{_f(xy["B"][0] + 6)}" y="{_f(xy["B"][1] + 18)}" text-anchor="start">B (1,0)</text>
    <text x="{_f(xy["C"][0] + 8)}" y="{_f(xy["C"][1] - 6)}" text-anchor="start">C</text>
    <text x="{_f(xy["D"][0] + 8)}" y="{_f(xy["D"][1] + 14)}" text-anchor="start">C′</text>
    <text x="{_f(xy["G"][0] + 8)}" y="{_f(xy["G"][1] - 9)}" text-anchor="start" fill="{gold}">G (φ, 0)</text>
  </g>
</svg>
"""


def main() -> None:
    """Verify symbolic geometry and generate hero & GitHub profile SVGs."""
    pts = build_symbolic_model()

    HERO_SVG_PATH.parent.mkdir(parents=True, exist_ok=True)
    HERO_SVG_PATH.write_text(render_interactive_hero_svg(pts), encoding="utf-8")
    print(f"Wrote {HERO_SVG_PATH}")

    if GH_PROFILE_DIR.is_dir():
        dark_path = GH_PROFILE_DIR / "vesica-phi-dark.svg"
        light_path = GH_PROFILE_DIR / "vesica-phi-light.svg"
        dark_path.write_text(render_github_banner_svg(pts, dark=True), encoding="utf-8")
        light_path.write_text(
            render_github_banner_svg(pts, dark=False), encoding="utf-8"
        )
        print(f"Wrote {dark_path}")
        print(f"Wrote {light_path}")


if __name__ == "__main__":
    main()
