"""Generate static JSON indexes for the interactive People and Media directories on geometor.com."""

from __future__ import annotations

import json
import pathlib
import re
from typing import Any

GEO_ROOT = pathlib.Path("/home/phi/PROJECTS/geometor")
COM_ROOT = GEO_ROOT / "geometor.com"
DOCSRC = COM_ROOT / "docsrc"
DATA_DIR = DOCSRC / "_static" / "data"

ERA_LABELS = {
    "antiquity.rst": "Classical Antiquity",
    "medieval_renaissance.rst": "Medieval & Renaissance",
    "axiomatics_noetics.rst": "Modern Axiomatics & Noetics",
    "nature_harmonics_modern.rst": "Natural Systems & Contemporary",
}

# Primary source languages per GEOMETOR repository slug
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
    "fundamentals": ["English"],
    "thompson": ["English"],
    "hambidge": ["English"],
    "russell": ["English"],
    "huntley": ["English"],
    "livio": ["English"],
    "posamentier": ["English"],
    "divine": ["English"],
    "phyllotaxis": ["English"],
    "knott": ["English"],
    "etc": ["English"],
    "wildberger": ["English"],
}

# Fallback death years for thinkers whose heading omits dates
KNOWN_DEATH_YEARS: dict[str, tuple[int, str]] = {
    "Euclid of Alexandria": (-270, "fl. c. 300 BC"),
    "Fred W. Seelig": (1995, "20th c."),
    "Roger V. Jean": (2015, "c. 2015"),
    "H. E. Huntley": (1978, "1978"),
    "Ron Knott": (9999, "Living"),
    "Clark Kimberling": (9999, "Living"),
    "Norman J. Wildberger": (9999, "Living"),
}


def _find_hero_path(repo_slug: str) -> str:
    local = "walter-russell" if repo_slug == "russell" else ("constructions" if repo_slug == "animations" else repo_slug)
    heroes_dir = DOCSRC / "_static" / "heroes"
    for ext in (".svg", ".png", ".jpg"):
        if (heroes_dir / f"{local}{ext}").is_file():
            return f"../_static/heroes/{local}{ext}"
    return ""


def _parse_death_year(heading: str) -> tuple[int, str, str]:
    """Return (numeric_death_year, death_label, lifespan_display)."""
    m_span = re.search(r"\(([^)]+)\)", heading)
    lifespan = m_span.group(1).strip() if m_span else ""
    is_bc = "BC" in heading or "BCE" in heading

    for k, (yr, lbl) in KNOWN_DEATH_YEARS.items():
        if k in heading:
            return yr, lbl, lifespan or lbl

    # Look for range like 1880–1961 or c. 240 – c. 190 BC or c. 427–347 BC
    m_years = re.findall(r"\b(\d{3,4})\b", lifespan)
    if len(m_years) >= 2:
        dy = int(m_years[-1])
        if is_bc:
            return -dy, f"{dy} BC", lifespan
        return dy, str(dy), lifespan
    if len(m_years) == 1:
        dy = int(m_years[0])
        if is_bc:
            return -dy, f"c. {dy} BC", lifespan
        return dy, str(dy), lifespan
    return 9999, "Contemporary", lifespan or "Contemporary"


def _clean_rst_text(txt: str) -> str:
    txt = re.sub(r":math:`[^`]+`", "", txt)
    txt = re.sub(r"`([^`<]+?)\s*<[^>]+>`_", r"\1", txt)
    txt = re.sub(r"``([^`]+)``", r"\1", txt)
    txt = re.sub(r"\*\*([^*]+)\*\*", r"\1", txt)
    txt = re.sub(r"\*([^*]+)\*", r"\1", txt)
    return re.sub(r"\s+", " ", txt).strip()


def build_people() -> list[dict[str, Any]]:
    """Extract structured person records from geometor.com/docsrc/lineage/*.rst."""
    lineage_dir = DOCSRC / "lineage"
    people: list[dict[str, Any]] = []

    for p in sorted(lineage_dir.glob("*.rst")):
        if p.name == "index.rst":
            continue
        era = ERA_LABELS.get(p.name, p.stem.replace("_", " ").title())
        lines = p.read_text(encoding="utf-8").splitlines()

        # Find section boundaries
        headings: list[tuple[int, str]] = []
        for i in range(len(lines) - 1):
            if (
                lines[i].strip()
                and lines[i + 1].strip()
                and set(lines[i + 1].strip()) == {"-"}
                and len(lines[i + 1].strip()) >= len(lines[i].strip())
            ):
                headings.append((i, lines[i].strip()))

        for idx, (start_i, raw_head) in enumerate(headings):
            end_i = headings[idx + 1][0] if idx + 1 < len(headings) else len(lines)
            block = "\n".join(lines[start_i + 2 : end_i])

            # Extract first geometor.github.io/<repo>/ link
            m_site = re.search(r"https://geometor\.github\.io/([a-z0-9_.-]+)/", block)
            repo = m_site.group(1) if m_site else ""

            # Clean display name (remove parenthetical date span and italic markers)
            name = re.sub(r"\s*\([^)]+\)", "", raw_head)
            name = re.sub(r"\*([^*]+)\*", r"\1", name).strip()
            death_year, death_label, lifespan = _parse_death_year(raw_head)

            # Extract prose paragraph (skip bullet list lines and ----)
            prose_lines = [
                ln.strip()
                for ln in lines[start_i + 2 : end_i]
                if ln.strip() and not ln.lstrip().startswith("*") and set(ln.strip()) != {"-"}
            ]
            summary = _clean_rst_text(" ".join(prose_lines))
            if len(summary) > 220:
                summary = summary[:217].rsplit(" ", 1)[0] + "…"

            langs = REPO_LANGUAGES.get(repo, ["English"])
            if "German" not in langs and any(k in raw_head for k in ("Haeckel", "Kayser")):
                langs = ["German", "English"]

            people.append(
                {
                    "name": name,
                    "lifespan": lifespan,
                    "death_year": death_year,
                    "death_label": death_label,
                    "era": era,
                    "languages": langs,
                    "repo": repo,
                    "site_url": f"https://geometor.github.io/{repo}/" if repo else "",
                    "github_url": f"https://github.com/geometor/{repo}" if repo else "",
                    "hero": _find_hero_path(repo) if repo else "",
                    "summary": summary,
                }
            )

    people.sort(key=lambda item: (item["death_year"], item["name"]))
    return people


def build_media() -> list[dict[str, Any]]:
    """Scan all youtube.json manifests across GEOMETOR studio directories."""
    media: list[dict[str, Any]] = []
    for yp in sorted(GEO_ROOT.glob("*/videos/**/youtube.json")):
        repo = yp.relative_to(GEO_ROOT).parts[0]
        try:
            data = json.loads(yp.read_text(encoding="utf-8"))
        except Exception:
            continue

        if repo == "elements":
            series = "Euclid's Elements"
            langs = ["English", "Greek"]
        elif repo == "etc":
            series = "Encyclopedia of Triangle Centers"
            langs = ["English"]
        elif repo == "phyllotaxis":
            series = "Phyllotaxis"
            langs = ["English"]
        else:
            series = repo.title()
            langs = ["English"]

        codex_url = data.get("etc_url") or data.get("codex_url") or f"https://geometor.github.io/{repo}/"
        if repo == "elements" and not data.get("etc_url"):
            prop_id = data.get("g_id") or data.get("short_code") or ""
            m_g = re.search(r"G\.\d+", str(prop_id) + " " + str(yp))
            if m_g:
                codex_url = f"https://geometor.github.io/elements/elements2/{m_g.group(0)}/"

        uploads = data.get("uploads", {})
        for fmt_key, fmt_label, title_key in (
            ("wide_1080p", "Widescreen", "title_1080p"),
            ("short", "Short", "title_short"),
        ):
            up = uploads.get(fmt_key) or {}
            vid = up.get("video_id")
            if not vid:
                continue
            title = data.get(title_key) or data.get("title_1080p") or yp.parent.name
            pub = up.get("published_at") or up.get("uploaded_at") or ""
            media.append(
                {
                    "title": title,
                    "video_id": vid,
                    "url": up.get("url") or f"https://youtu.be/{vid}",
                    "thumbnail": f"https://i.ytimg.com/vi/{vid}/hqdefault.jpg",
                    "published_at": pub,
                    "published_date": pub[:10] if pub else "",
                    "format": fmt_label,
                    "series": series,
                    "repo": repo,
                    "languages": langs,
                    "codex_url": codex_url,
                }
            )

    media.sort(key=lambda item: item["published_at"], reverse=True)
    return media


def main() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    people = build_people()
    media = build_media()
    (DATA_DIR / "people.json").write_text(json.dumps(people, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (DATA_DIR / "media.json").write_text(json.dumps(media, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(people)} people and {len(media)} media items to {DATA_DIR}")


if __name__ == "__main__":
    main()
