"""Generate individual .rst record files in geometor.com/docsrc/{people,books,projects}/."""

from __future__ import annotations

import json
import pathlib
import re
from typing import Any

GEO_ROOT = pathlib.Path("/home/phi/PROJECTS/geometor")
COM_ROOT = GEO_ROOT / "geometor.com"
DOCSRC = COM_ROOT / "docsrc"

CATALOG_REPOS = {
    "elements",
    "etc",
    "wildberger",
    "fundamentals",
    "divine",
    "polyhedra",
    "knott",
    "huntley",
    "livio",
    "posamentier",
    "codes",
    "gibert",
    "heptadecagon",
    "levels",
}

REPO_LANGUAGES: dict[str, list[str]] = {
    "plato": ["Greek", "English"],
    "aristotle": ["Greek", "English"],
    "euclid": ["Greek", "English"],
    "elements": ["Greek", "English"],
    "archimedes": ["Greek", "English"],
    "apollonius": ["Greek", "English"],
    "heron": ["Greek", "English"],
    "menelaus": ["Latin", "Greek", "English"],
    "nicomachus": ["Greek", "English"],
    "ptolemy": ["Greek", "Latin", "English"],
    "pappus": ["Greek", "English"],
    "proclus": ["Greek", "English"],
    "fibonacci": ["Latin", "English"],
    "aquinas": ["Latin", "English"],
    "cusa": ["Latin", "English"],
    "piero": ["Latin", "English"],
    "pacioli": ["Italian", "English"],
    "durer": ["German", "English"],
    "kepler": ["Latin", "English"],
    "pascal": ["French", "English"],
    "ceva": ["Latin", "English"],
    "euler": ["Latin", "English"],
    "mascheroni": ["Italian", "English"],
    "feuerbach": ["German", "English"],
    "steiner": ["German", "English"],
    "byrne": ["English"],
    "staudt": ["German", "English"],
    "petersen": ["English"],
    "pasch": ["German", "English"],
    "casey": ["English"],
    "lemoine": ["French", "English"],
    "klein": ["German", "English"],
    "poincare": ["French", "English"],
    "hilbert": ["German", "English"],
    "bertrand-russell": ["English"],
    "altshiller-court": ["English"],
    "hoenen": ["Latin", "English"],
}

# Pillar classification + concise catalog metadata for all 64 GEOMETOR repositories
PROJECT_SPECS: list[tuple[str, str, str, str]] = [
    # (local_repo, display_title, pillar, summary)
    # 1. Core & Symbolic Engine
    ("geometor.com", "geometor.com", "Core & Symbolic Engine", "Central GEOMETOR portal, interactive Vesica-to-phi hero, Books, Projects & People directories."),
    ("model", "GEOMETOR Model", "Core & Symbolic Engine", "Exact SymPy constructive geometry kernel: points, lines, circles, quadrance, spread, and proof DAGs."),
    ("explorer", "GEOMETOR Explorer", "Core & Symbolic Engine", "Interactive SVG geometric workbench, symbolic CLI renderer, and constructive timeline."),
    ("divine", "GEOMETOR Divine", "Core & Symbolic Engine", "Automated golden-section scanner and catalog of exact golden-ratio geometric constructions."),
    ("polyhedra", "GEOMETOR Polyhedra", "Core & Symbolic Engine", "Exact 3D symbolic catalog of Platonic, Archimedean, and Leonardo's 1509 solid polyhedra."),
    ("codes", "GEOMETOR Codes", "Core & Symbolic Engine", "Catalog of open-source geometric theorem provers, constructive kernels, and formal geometry engines."),
    ("elementarium", "GEOMETOR Elementarium", "Core & Symbolic Engine", "Passive optical archive and zero-context universal geometric bootstrap architecture."),
    ("press", "GEOMETOR Press", "Core & Symbolic Engine", "Digital Scriptorium Press master shelf, cover system, and 69 compass-and-straightedge medallions."),
    ("constructions", "GEOMETOR Animations", "Core & Symbolic Engine", "Proportional golden-section studies, dynamic root grids, and star-polygon motion sequences."),
    ("trees", "GEOMETOR Trees", "Core & Symbolic Engine", "Stern–Brocot Farey trees, Ford tangent circles, and monotone planar dependency drawings."),
    ("levels", "GEOMETOR Levels", "Core & Symbolic Engine", "Constructive depth stratification, compass-and-straightedge generation layers, and complexity analysis."),
    # 2. Constructive & Projective Geometry
    ("euclid", "Euclid of Alexandria", "Constructive & Projective Geometry", "Heath's 13-Book Elements (1,416 folios, 831 calibrated SVGs) and Euclid's Data."),
    ("elements", "Euclid's Elements (G-Index)", "Constructive & Projective Geometry", "Computable 601-node G-Index 3-Track Codex uniting formal pseudocode, SymPy code, and Heath."),
    ("byrne", "Oliver Byrne", "Constructive & Projective Geometry", "Oliver Byrne's iconic chromatic Elements (1847, 339 RGB folios and vector color proofs)."),
    ("archimedes", "Archimedes of Syracuse", "Constructive & Projective Geometry", "Seven treatises of Archimedes and The Method (Heath 1897/1912) with calibrated diagrams."),
    ("apollonius", "Apollonius of Perga", "Constructive & Projective Geometry", "Conics (Books I–VII) and Reconstructed Analytic Works (Heath 1896) with conic constructions."),
    ("heron", "Heron of Alexandria", "Constructive & Projective Geometry", "Metrica, Definitiones, Catoptrica, and Dioptra (Schöne 1903) with optical & area proofs."),
    ("menelaus", "Menelaus of Alexandria", "Constructive & Projective Geometry", "Sphaerica (Books I–III, 482 folios: Halley 1758 & Bjørnbo 1902) on spherical triangles."),
    ("ptolemy", "Claudius Ptolemy", "Constructive & Projective Geometry", "Almagest (Book I chord geometry) and Planisphaerium (1,054 folios: Heiberg 1898/1907)."),
    ("pappus", "Pappus of Alexandria", "Constructive & Projective Geometry", "Synagoge (Books III–VIII, 445 folios), Pappus Hexagon Theorem, and Arbelos chains."),
    ("pascal", "Blaise Pascal", "Constructive & Projective Geometry", "Essay pour les Coniques (1640) and exact projective Hexagrammum Mysticum constructions."),
    ("ceva", "Giovanni Ceva", "Constructive & Projective Geometry", "De lineis rectis (1678, 126 folios) establishing statical lever concurrency and trilinear polars."),
    ("euler", "Leonhard Euler", "Constructive & Projective Geometry", "Solutio facilis (E325, 1765, 38 folios) discovering the Euler Line O–G–H and Nine-Point Circle."),
    ("mascheroni", "Lorenzo Mascheroni", "Constructive & Projective Geometry", "La Geometria del Compasso (1797, 181 folios) proving compass-only geometric equivalence."),
    ("heptadecagon", "Gauss's Heptadecagon", "Constructive & Projective Geometry", "Constructive catalog of the regular 17-gon (1796), Carlyle circles, and quadratic radical towers."),
    ("feuerbach", "Karl Wilhelm Feuerbach", "Constructive & Projective Geometry", "Eigenschaften (1822, 76 folios) proving Nine-Point Circle tangency to incircle & excircles."),
    ("steiner", "Jakob Steiner", "Constructive & Projective Geometry", "Die geometrischen Constructionen (1833, 94 folios) with straightedge and a single fixed circle."),
    ("staudt", "Karl G. C. von Staudt", "Constructive & Projective Geometry", "Geometrie der Lage (1847) and Beiträge (1857): pure synthetic projective Algebra of Throws."),
    ("petersen", "Julius Petersen", "Constructive & Projective Geometry", "Methods and Theories for Geometrical Constructions (1879, 136 folios) and loci synthesis."),
    ("casey", "John Casey", "Constructive & Projective Geometry", "A Sequel to the First Six Books of Euclid (1888, 324 folios) and Casey's Four-Circle Theorem."),
    ("klein", "Felix Klein", "Constructive & Projective Geometry", "Erlangen Program (1872) and Famous Problems of Elementary Geometry (1895)."),
    ("lemoine", "Émile Lemoine", "Constructive & Projective Geometry", "La Géométrographie (1902, 108 folios): construction simplicity calculus and symmedian point X(6)."),
    ("altshiller-court", "Nathan Altshiller-Court", "Constructive & Projective Geometry", "College Geometry (1952, 330 folios): modern Euclidean orthocentric and harmonic synthesis."),
    ("fundamentals", "GEOMETOR Fundamentals", "Constructive & Projective Geometry", "Foundational compass-and-straightedge primer and Fred W. Seelig Archive (F.1–F.55)."),
    ("etc", "Encyclopedia of Triangle Centers", "Constructive & Projective Geometry", "Clark Kimberling's ETC symbolic index (53,144 parsed centers; exact SymPy constructors)."),
    ("gibert", "Catalogue of Triangle Cubics", "Constructive & Projective Geometry", "Bernard Gibert's Catalogue of Triangle Cubics (CTC: Neuberg, Thomson, Darboux cubics)."),
    ("wildberger", "Norman J. Wildberger", "Constructive & Projective Geometry", "Divine Proportions & Rational Trigonometry formalized via exact quadrance and spread laws."),
    # 3. Digital Scriptorium & Noetics
    ("plato", "Plato of Athens", "Digital Scriptorium & Noetics", "Five dialogues (Meno, Theaetetus, Republic, Timaeus, Foundations) in Greek & English."),
    ("aristotle", "Aristotle of Stagira", "Digital Scriptorium & Noetics", "Five treatises (Organon, Post. Anal., Physica, De Anima, Metaphysica) on mathematical science."),
    ("nicomachus", "Nicomachus of Gerasa", "Digital Scriptorium & Noetics", "Introductio Arithmetica (572 folios: Hoche 1866 & D'Ooge 1926) on figurate number theory."),
    ("proclus", "Proclus Lycius", "Digital Scriptorium & Noetics", "Commentary on Euclid Book I (Friedlein 1873 Greek + English) on geometric imagination."),
    ("fibonacci", "Leonardo Pisano (Fibonacci)", "Digital Scriptorium & Noetics", "Liber Abbaci (1202) and Practica Geometriae (1220, 762 folios) in Latin & English."),
    ("aquinas", "St. Thomas Aquinas", "Digital Scriptorium & Noetics", "Six treatises on Scientia Mathematica, abstraction, and materia intelligibilis."),
    ("cusa", "Nicholas of Cusa", "Digital Scriptorium & Noetics", "De Docta Ignorantia (1440) and De Mathematicis Complementis (1453) on infinite polygons."),
    ("piero", "Piero della Francesca", "Digital Scriptorium & Noetics", "Libellus de Quinque Corporibus Regularibus (166 folios) on Platonic & truncated solids."),
    ("pacioli", "Fra Luca Pacioli", "Digital Scriptorium & Noetics", "De Divina Proportione (1509, 318 folios) with Leonardo's plates & Summa de Arithmetica."),
    ("durer", "Albrecht Dürer", "Digital Scriptorium & Noetics", "Underweysung der Messung (Nuremberg, 1525, Books I–IV) on constructive geometry & typography."),
    ("kepler", "Johannes Kepler", "Digital Scriptorium & Noetics", "Mysterium Cosmographicum, Strena Sexangula, and Harmonices Mundi (3 Latin/English codices)."),
    ("pasch", "Moritz Pasch", "Digital Scriptorium & Noetics", "Vorlesungen über neuere Geometrie (1882, 212 folios) establishing rigorous order axioms."),
    ("hilbert", "David Hilbert", "Digital Scriptorium & Noetics", "Grundlagen der Geometrie / Foundations of Geometry (1899/1902) bilingual axiomatic codex."),
    ("poincare", "Henri Poincaré", "Digital Scriptorium & Noetics", "Science and Hypothesis (1902/1905) on geometric conventionalism and hyperbolic space."),
    ("bertrand-russell", "Bertrand Russell", "Digital Scriptorium & Noetics", "Foundations of Geometry (1897) and Principles of Mathematics Part VI (1903)."),
    ("hoenen", "Petrus Hoenen, S.J.", "Digital Scriptorium & Noetics", "De Noetica Geometriae (1954, 300 folios: facing Latin & English Thomistic geometry)."),
    ("walter-russell", "Walter & Lao Russell", "Digital Scriptorium & Noetics", "Home Study Course (519 folios) and Cosmogony paired with parametric 2D/3D wave models."),
    # 4. Living Geometry & Proportion
    ("phyllotaxis", "GEOMETOR Phyllotaxis", "Living Geometry & Proportion", "Golden-angle divergence, parastichy lattices, and interactive 2D/3D botanical meristem studios."),
    ("thompson", "D'Arcy Wentworth Thompson", "Living Geometry & Proportion", "On Growth and Form (1917): logarithmic gnomons and coordinate transformation grids."),
    ("hambidge", "Jay Hambidge", "Living Geometry & Proportion", "The Elements of Dynamic Symmetry (1920, 174 folios): root rectangles & whirling squares."),
    ("knott", "Ron Knott", "Living Geometry & Proportion", "Catalog of Fibonacci Numbers, Golden Section identities, and Wythoff constructions."),
    ("huntley", "H. E. Huntley", "Living Geometry & Proportion", "Catalog of The Divine Proportion (1970): 3–4–5 golden section and Lemoine simplicity."),
    ("livio", "Mario Livio", "Living Geometry & Proportion", "Catalog of The Golden Ratio (2002): mathematical proofs, Penrose tilings, and myth triage."),
    ("posamentier", "Posamentier & Lehmann", "Living Geometry & Proportion", "Catalog of The Glorious Golden Ratio (2011): pentagon, decagon, and golden constructions."),
    # 5. Machine Reasoning & ARC
    ("seer", "GEOMETOR Seer", "Machine Reasoning & ARC", "Multi-agent neuro-symbolic Python program synthesis engine for ARC-AGI visual reasoning."),
    ("seer_navigator", "Seer Navigator", "Machine Reasoning & ARC", "Textual TUI browser for inspecting Seer reasoning trajectories, trees, and solver metrics."),
    ("seer_sessions", "Seer Sessions", "Machine Reasoning & ARC", "Longitudinal empirical archive and mining toolkit across 8,514 reasoning trials."),
]

PERSON_MEDALLION_OVERRIDES: dict[str, str] = {
    "russell": "walter-russell",
    "thomas-little-heath": "heath",
    "sir-thomas-little-heath": "heath",
    "leonardo-da-vinci": "leonardo",
    "ernst-haeckel": "ernst-haeckel",
    "hans-kayser": "hans-kayser",
    "george-odom": "odom",
    "clark-kimberling": "kimberling",
}


def _slugify(text: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return s or "record"


def _medallion_for_slug(slug: str) -> str:
    med_dir = DOCSRC / "_static" / "medallions"
    cand = PERSON_MEDALLION_OVERRIDES.get(slug, slug)
    if (med_dir / f"{cand}.svg").is_file():
        return f"/_static/medallions/{cand}.svg"
    if (med_dir / f"{slug}.svg").is_file():
        return f"/_static/medallions/{slug}.svg"
    return ""


def _hero_for_repo(repo_local: str) -> str:
    heroes_dir = DOCSRC / "_static" / "heroes"
    for ext in (".svg", ".png", ".jpg"):
        if (heroes_dir / f"{repo_local}{ext}").is_file():
            return f"/_static/heroes/{repo_local}{ext}"
    return _medallion_for_slug(repo_local)


def _parse_frontmatter(txt: str) -> dict[str, str]:
    meta: dict[str, str] = {}
    for line in txt.splitlines():
        m = re.match(r"^:([A-Za-z0-9_.-]+):\s*(.*)$", line)
        if m:
            meta[m.group(1)] = m.group(2).strip()
        elif line.strip() and not line.startswith(" "):
            break
    return meta


def _extract_h1(txt: str) -> str:
    lines = txt.splitlines()
    for i in range(len(lines) - 1):
        l1 = lines[i].strip()
        l2 = lines[i + 1].strip()
        if l1 and l2 and set(l2) <= {"=", "-", "~"} and len(l2) >= len(l1):
            return l1
    return ""


def generate_people_records() -> int:
    people_dir = DOCSRC / "people"
    people_dir.mkdir(parents=True, exist_ok=True)
    for old in people_dir.glob("*.rst"):
        if old.name != "index.rst":
            old.unlink()

    people = json.loads((DOCSRC / "_static" / "data" / "people.json").read_text(encoding="utf-8"))
    used_slugs: set[str] = set()
    for p in people:
        base = p.get("repo") or _slugify(p["name"])
        slug = base
        idx = 2
        while slug in used_slugs:
            slug = f"{base}-{idx}"
            idx += 1
        used_slugs.add(slug)

        # Prefer our canonical compass-and-straightedge medallion coin when available
        med = _medallion_for_slug(slug) or _medallion_for_slug(_slugify(p["name"]))
        hero = med or p.get("hero", "")
        if hero.startswith("../"):
            hero = "/" + hero[3:]
        langs = ", ".join(p.get("languages", ["English"]))
        title = p["name"]
        underline = "=" * len(title)

        lines = [
            ":type: person",
            f":death_year: {p['death_year']}",
            f":death_label: {p['death_label']}",
            f":lifespan: {p['lifespan']}",
            f":era: {p['era']}",
            f":languages: {langs}",
        ]
        if p.get("site_url"):
            lines.append(f":site_url: {p['site_url']}")
        if p.get("github_url"):
            lines.append(f":github_url: {p['github_url']}")
        if p.get("summary"):
            lines.append(f":excerpt: {p['summary']}")
        lines.extend(["", title, underline, ""])
        if hero:
            lines.extend([f".. image:: {hero}", f"   :alt: {title}", ""])
        if p.get("summary"):
            lines.extend([p["summary"], ""])
        if p.get("site_url"):
            lines.append(f"* **GEOMETOR Website**: `{title} <{p['site_url']}>`_")
        if p.get("github_url"):
            lines.append(f"* **GitHub Repository**: `github.com/geometor/{p['repo']} <{p['github_url']}>`_")
        lines.append("")

        (people_dir / f"{slug}.rst").write_text("\n".join(lines), encoding="utf-8")

    index_rst = f"""\
:navigation: header
:order: 7
:nav_title: People
:breadcrumb_title: People

.. _people-directory:

People
======

.. rubric:: Searchable Directory of Geometers, Philosophers & Mathematical Thinkers

Browse all **{len(people)} figures** across the GEOMETOR lineage—filter by **source language** or **era**, search by name or treatise, and sort by **death date** or **name**.

.. people-directory::
   :sort: death_year
"""
    (people_dir / "index.rst").write_text(index_rst, encoding="utf-8")
    return len(people)


def _author_doc_for_repo(repo_local: str) -> str:
    overrides = {
        "elements": "euclid",
        "walter-russell": "russell",
    }
    slug = overrides.get(repo_local, repo_local)
    if (DOCSRC / "people" / f"{slug}.rst").is_file():
        return f"people/{slug}"
    return ""


def generate_book_records() -> int:
    books_dir = DOCSRC / "books"
    books_dir.mkdir(parents=True, exist_ok=True)
    for old in books_dir.glob("*.rst"):
        if old.name != "index.rst":
            old.unlink()

    records: list[dict[str, Any]] = []
    for d in sorted(GEO_ROOT.iterdir()):
        if not (d.is_dir() and (d / ".git").exists()) or d.name in {
            ".config",
            ".github",
            "geometor.com",
            "seer",
            "seer_navigator",
            "seer_sessions",
        }:
            continue
        docsrc = d / "docsrc"
        if not docsrc.is_dir():
            continue
        gh_slug = "russell" if d.name == "walter-russell" else ("animations" if d.name == "constructions" else d.name)
        hero = _hero_for_repo(d.name)
        langs = REPO_LANGUAGES.get(d.name, ["English"])
        is_catalog = d.name in CATALOG_REPOS
        author_doc = _author_doc_for_repo(d.name)

        found_books = []
        for idx_rst in sorted(docsrc.glob("*/index.rst")):
            txt = idx_rst.read_text(encoding="utf-8", errors="ignore")
            meta = _parse_frontmatter(txt)
            if meta.get("type") != "book":
                continue
            found_books.append((idx_rst.parent.name, txt, meta))

        if not found_books and d.name in {"polyhedra", "codes"}:
            root_txt = (docsrc / "index.rst").read_text(encoding="utf-8", errors="ignore")
            rmeta = _parse_frontmatter(root_txt)
            title = _extract_h1(root_txt) or d.name.title()
            records.append(
                {
                    "slug": f"{d.name}_catalog",
                    "title": title,
                    "author": rmeta.get("author", "GEOMETOR"),
                    "author_doc": author_doc,
                    "year": rmeta.get("year", "2026"),
                    "year_label": rmeta.get("year_label", ""),
                    "edition_year": rmeta.get("edition_year", ""),
                    "native_title": "",
                    "era": "Mathematical Catalogs",
                    "languages": langs,
                    "site_url": f"https://geometor.github.io/{gh_slug}/",
                    "github_url": f"https://github.com/geometor/{gh_slug}",
                    "hero": hero,
                    "excerpt": rmeta.get("description", rmeta.get("excerpt", f"Interactive symbolic catalog in geometor/{gh_slug}.")),
                }
            )
            continue

        for sub_slug, txt, meta in found_books:
            title = meta.get("book_title") or _extract_h1(txt) or sub_slug.replace("_", " ").title()
            author = meta.get("author") or d.name.replace("-", " ").title()
            year = meta.get("year") or ""
            year_label = meta.get("year_label") or ""
            edition_year = meta.get("edition_year") or ""
            m_rubric = re.search(r"^\.\. rubric::\s*\*([^*]+)\*", txt, re.M)
            native = m_rubric.group(1).strip() if m_rubric else ""
            excerpt = meta.get("excerpt") or meta.get("description") or ""
            records.append(
                {
                    "slug": f"{d.name}_{sub_slug}",
                    "title": title,
                    "author": author,
                    "author_doc": author_doc,
                    "year": year,
                    "year_label": year_label,
                    "edition_year": edition_year,
                    "native_title": native,
                    "era": "Mathematical Catalogs" if is_catalog else "Book Codices",
                    "languages": langs,
                    "site_url": f"https://geometor.github.io/{gh_slug}/{sub_slug}/",
                    "github_url": f"https://github.com/geometor/{gh_slug}",
                    "hero": hero,
                    "excerpt": excerpt,
                }
            )

    for rec in records:
        title = rec["title"]
        underline = "=" * len(title)
        lines = [
            ":type: book_record",
            f":author: {rec['author']}",
        ]
        if rec["author_doc"]:
            lines.append(f":author_doc: {rec['author_doc']}")
        lines.extend(
            [
                f":era: {rec['era']}",
                f":languages: {', '.join(rec['languages'])}",
                f":site_url: {rec['site_url']}",
                f":github_url: {rec['github_url']}",
            ]
        )
        if rec["year"]:
            lines.append(f":year: {rec['year']}")
        if rec["year_label"]:
            lines.append(f":year_label: {rec['year_label']}")
        if rec["edition_year"]:
            lines.append(f":edition_year: {rec['edition_year']}")
        if rec["native_title"]:
            lines.append(f":native_title: {rec['native_title']}")
        if rec["excerpt"]:
            lines.append(f":excerpt: {rec['excerpt']}")
        lines.extend(["", title, underline, ""])
        if rec["hero"]:
            lines.extend([f".. image:: {rec['hero']}", f"   :alt: {title}", ""])
        if rec["excerpt"]:
            lines.extend([rec["excerpt"], ""])
        pub_disp = rec["year_label"] or rec["year"]
        if pub_disp:
            ed_suffix = f" *(Edition: {rec['edition_year']})*" if rec["edition_year"] else ""
            lines.append(f"* **Published**: {pub_disp}{ed_suffix}")
        lines.append(f"* **Read Online**: `{title} <{rec['site_url']}>`_")
        lines.append(f"* **GitHub Repository**: `{rec['github_url']} <{rec['github_url']}>`_")
        lines.append("")
        (books_dir / f"{rec['slug']}.rst").write_text("\n".join(lines), encoding="utf-8")

    books_index = f"""\
:navigation: header
:order: 2
:nav_title: Books & Catalogs
:breadcrumb_title: Books & Catalogs

.. _books-and-catalogs:

Books & Catalogs
================

.. rubric:: Searchable Directory of GEOMETOR Book Codices & Mathematical Catalogs

Browse all **{len(records)} Book Codices & Mathematical Catalogs** across **39 historical authors** and **{len(CATALOG_REPOS)} constructive catalog archives**—filter by **language** or **group**, search by title or author, and sort dynamically by **year** or **title**.

.. reference-directory::
   :sort: year
"""
    (books_dir / "index.rst").write_text(books_index, encoding="utf-8")
    return len(records)


def generate_project_records() -> int:
    """Generate searchable project record cards using circular medallions in geometor.com/docsrc/projects/."""
    projects_dir = DOCSRC / "projects"
    projects_dir.mkdir(parents=True, exist_ok=True)
    preserved_dossiers = {"index.rst", "core.rst", "elementrium.rst", "scriptorium.rst", "living_geometry.rst", "reasoning.rst"}
    for old in projects_dir.glob("*.rst"):
        if old.name not in preserved_dossiers:
            old.unlink()

    for repo_local, title, pillar, summary in PROJECT_SPECS:
        gh_slug = (
            "russell"
            if repo_local == "walter-russell"
            else ("animations" if repo_local == "constructions" else repo_local)
        )
        site_url = "https://geometor.com/" if repo_local == "geometor.com" else f"https://geometor.github.io/{gh_slug}/"
        github_url = f"https://github.com/geometor/{gh_slug}"
        med_path = _medallion_for_slug(repo_local) or _hero_for_repo(repo_local)
        langs = REPO_LANGUAGES.get(repo_local, ["English"])
        rec_slug = f"repo_{repo_local.replace('.', '_').replace('-', '_')}"

        underline = "=" * len(title)
        lines = [
            ":type: project_record",
            f":era: {pillar}",
            f":native_title: geometor/{gh_slug}",
            f":languages: {', '.join(langs)}",
            f":site_url: {site_url}",
            f":github_url: {github_url}",
            f":excerpt: {summary}",
            "",
            title,
            underline,
            "",
        ]
        if med_path:
            lines.extend([f".. image:: {med_path}", f"   :alt: {title} Medallion", ""])
        lines.extend(
            [
                summary,
                "",
                f"* **Live Site**: `{title} <{site_url}>`_",
                f"* **GitHub Repository**: `github.com/geometor/{gh_slug} <{github_url}>`_",
                "",
            ]
        )
        (projects_dir / f"{rec_slug}.rst").write_text("\n".join(lines), encoding="utf-8")

    projects_index = f"""\
:navigation: header
:order: 3
:nav_title: Projects
:breadcrumb_title: Projects

.. _projects-directory:

Projects
========

.. rubric:: Searchable Medallion Directory of All {len(PROJECT_SPECS)} GEOMETOR Repositories

Explore all **{len(PROJECT_SPECS)} public GEOMETOR repositories** across our five architectural pillars—each represented by its own **compass-and-straightedge medallion** (zero Bézier curves). Filter by **pillar** or **language**, search by name or topic, and switch between card, banner, or list views.

.. tip::

   Looking directly for a specific treatise or catalog? Visit the :doc:`Books & Catalogs Directory <../books/index>` or the :doc:`People Directory <../people/index>`.

.. collection::
   :type: project_record
   :template: collection/directory.html
   :sort: title

Pillar Dossiers
---------------

.. toctree::
   :maxdepth: 1

   core
   elementrium
   scriptorium
   living_geometry
   reasoning
"""
    (projects_dir / "index.rst").write_text(projects_index, encoding="utf-8")
    return len(PROJECT_SPECS)


def main() -> None:
    n_people = generate_people_records()
    n_books = generate_book_records()
    n_projects = generate_project_records()
    print(f"Generated {n_people} person records, {n_books} book/catalog records, and {n_projects} project records.")


if __name__ == "__main__":
    main()
