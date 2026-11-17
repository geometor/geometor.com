"""Generate individual .rst record files in geometor.com/docsrc/people/ and geometor.com/docsrc/books/."""

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


def _slugify(text: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return s or "record"


def _hero_for_repo(repo_local: str) -> str:
    heroes_dir = DOCSRC / "_static" / "heroes"
    for ext in (".svg", ".png", ".jpg"):
        if (heroes_dir / f"{repo_local}{ext}").is_file():
            return f"/_static/heroes/{repo_local}{ext}"
    return ""


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
    # Remove old generated records
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

        hero = p.get("hero", "")
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

    index_rst = """\
:navigation: header
:order: 7
:nav_title: People
:breadcrumb_title: People

.. _people-directory:

People
======

.. rubric:: Searchable Directory of Geometers, Philosophers & Mathematical Thinkers

Browse all **49 figures** across the GEOMETOR lineage—filter by **source language**, search by name or treatise, and sort by **death date** or **name**.

.. collection::
   :template: collection/directory.html
   :sort: death_year
"""
    (people_dir / "index.rst").write_text(index_rst, encoding="utf-8")
    return len(people)


def generate_book_records() -> int:
    books_dir = DOCSRC / "books"
    books_dir.mkdir(parents=True, exist_ok=True)
    for old in books_dir.glob("*.rst"):
        if old.name != "index.rst":
            old.unlink()

    records: list[dict[str, Any]] = []
    for d in sorted(GEO_ROOT.iterdir()):
        if not (d.is_dir() and (d / ".git").exists()) or d.name in {".config", ".github", "geometor.com"}:
            continue
        docsrc = d / "docsrc"
        if not docsrc.is_dir():
            continue
        gh_slug = "russell" if d.name == "walter-russell" else ("animations" if d.name == "constructions" else d.name)
        hero = _hero_for_repo(d.name)
        langs = REPO_LANGUAGES.get(d.name, ["English"])
        is_catalog = d.name in CATALOG_REPOS

        found_books = []
        for idx_rst in sorted(docsrc.glob("*/index.rst")):
            txt = idx_rst.read_text(encoding="utf-8", errors="ignore")
            meta = _parse_frontmatter(txt)
            if meta.get("type") != "book":
                continue
            found_books.append((idx_rst.parent.name, txt, meta))

        # Include polyhedra and codes catalogs even without :type: book
        if not found_books and d.name in {"polyhedra", "codes"}:
            root_txt = (docsrc / "index.rst").read_text(encoding="utf-8", errors="ignore")
            rmeta = _parse_frontmatter(root_txt)
            title = _extract_h1(root_txt) or d.name.title()
            records.append(
                {
                    "slug": f"{d.name}_catalog",
                    "title": title,
                    "author": rmeta.get("author", "GEOMETOR"),
                    "year": rmeta.get("year", "2026"),
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
            m_rubric = re.search(r"^\.\. rubric::\s*\*([^*]+)\*", txt, re.M)
            native = m_rubric.group(1).strip() if m_rubric else ""
            excerpt = meta.get("excerpt") or meta.get("description") or ""
            records.append(
                {
                    "slug": f"{d.name}_{sub_slug}",
                    "title": title,
                    "author": author,
                    "year": year,
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
            f":era: {rec['era']}",
            f":languages: {', '.join(rec['languages'])}",
            f":site_url: {rec['site_url']}",
            f":github_url: {rec['github_url']}",
        ]
        if rec["year"]:
            lines.append(f":year: {rec['year']}")
        if rec["native_title"]:
            lines.append(f":native_title: {rec['native_title']}")
        if rec["excerpt"]:
            lines.append(f":excerpt: {rec['excerpt']}")
        lines.extend(["", title, underline, ""])
        if rec["hero"]:
            lines.extend([f".. image:: {rec['hero']}", f"   :alt: {title}", ""])
        if rec["excerpt"]:
            lines.extend([rec["excerpt"], ""])
        lines.append(f"* **Read Online**: `{title} <{rec['site_url']}>`_")
        lines.append(f"* **GitHub Repository**: `{rec['github_url']} <{rec['github_url']}>`_")
        lines.append("")
        (books_dir / f"{rec['slug']}.rst").write_text("\n".join(lines), encoding="utf-8")

    books_index = """\
:navigation: header
:order: 2
:nav_title: Books & Catalogs
:breadcrumb_title: Books & Catalogs

.. _books-and-catalogs:

Books & Catalogs
================

.. rubric:: Searchable Directory of GEOMETOR Book Codices & Mathematical Catalogs

Browse all **83 Book Codices & Mathematical Catalogs** across **39 historical authors** and **11 constructive catalog archives**—filter by **language** or **group**, search by title or author, and sort dynamically by **title** or **year**.

.. collection::
   :template: collection/directory.html
   :sort: year
"""
    (books_dir / "index.rst").write_text(books_index, encoding="utf-8")
    return len(records)


def main() -> None:
    n_people = generate_people_records()
    n_books = generate_book_records()
    print(f"Generated {n_people} person records and {n_books} book/catalog records.")


if __name__ == "__main__":
    main()
