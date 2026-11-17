(function () {
  "use strict";

  function esc(str) {
    return String(str || "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function compareNatural(a, b) {
    return String(a || "").localeCompare(String(b || ""), undefined, {
      numeric: true,
      sensitivity: "base",
    });
  }

  function initDirectory(root) {
    var kind = root.getAttribute("data-kind");
    var dataUrl = root.getAttribute("data-src");
    if (!kind || !dataUrl) return;

    var params = new URLSearchParams(window.location.search);
    var state = {
      q: params.get("q") || "",
      lang: params.get("lang") || "All",
      series: params.get("series") || "All",
      format: params.get("format") || "All",
      sort: params.get("sort") || (kind === "people" ? "death_asc" : "pub_desc"),
    };

    var items = [];

    function syncUrl() {
      var p = new URLSearchParams();
      if (state.q) p.set("q", state.q);
      if (state.lang !== "All") p.set("lang", state.lang);
      if (state.series !== "All") p.set("series", state.series);
      if (state.format !== "All") p.set("format", state.format);
      if (state.sort) p.set("sort", state.sort);
      var qs = p.toString();
      var next = window.location.pathname + (qs ? "?" + qs : "");
      window.history.replaceState(null, "", next);
    }

    function render() {
      var qLow = state.q.trim().toLowerCase();
      var filtered = items.filter(function (it) {
        if (state.lang !== "All" && (it.languages || []).indexOf(state.lang) === -1) {
          return false;
        }
        if (kind === "media") {
          if (state.series !== "All" && it.series !== state.series) return false;
          if (state.format !== "All" && it.format !== state.format) return false;
        }
        if (qLow) {
          var hay = (
            (it.name || "") +
            " " +
            (it.title || "") +
            " " +
            (it.summary || "") +
            " " +
            (it.era || "") +
            " " +
            (it.series || "") +
            " " +
            (it.repo || "")
          ).toLowerCase();
          if (hay.indexOf(qLow) === -1) return false;
        }
        return true;
      });

      filtered.sort(function (a, b) {
        if (state.sort === "title_asc") return compareNatural(a.name || a.title, b.name || b.title);
        if (state.sort === "title_desc") return compareNatural(b.name || b.title, a.name || a.title);
        if (state.sort === "death_asc") {
          return (a.death_year - b.death_year) || compareNatural(a.name, b.name);
        }
        if (state.sort === "death_desc") {
          return (b.death_year - a.death_year) || compareNatural(a.name, b.name);
        }
        if (state.sort === "pub_desc") {
          return String(b.published_at || "").localeCompare(String(a.published_at || ""));
        }
        if (state.sort === "pub_asc") {
          return String(a.published_at || "").localeCompare(String(b.published_at || ""));
        }
        return 0;
      });

      var countEl = root.querySelector(".geom-dir-count");
      if (countEl) {
        countEl.textContent = filtered.length + " of " + items.length + (kind === "people" ? " people" : " videos");
      }

      var grid = root.querySelector(".geom-dir-grid");
      if (!grid) return;

      grid.innerHTML = filtered
        .map(function (it) {
          if (kind === "people") {
            var imgHtml = it.hero
              ? '<img class="geom-dir-thumb" src="' + esc(it.hero) + '" alt="' + esc(it.name) + '" loading="lazy">'
              : "";
            var langsHtml = (it.languages || [])
              .map(function (l) {
                return '<span class="geom-dir-tag">' + esc(l) + "</span>";
              })
              .join("");
            var linksHtml = "";
            if (it.site_url) linksHtml += '<a href="' + esc(it.site_url) + '">Codex Site</a>';
            if (it.github_url) linksHtml += '<a href="' + esc(it.github_url) + '">GitHub</a>';
            return (
              '<article class="geom-dir-card">' +
              imgHtml +
              '<div class="geom-dir-body">' +
              '<h3 class="geom-dir-title">' + esc(it.name) + "</h3>" +
              '<div class="geom-dir-meta">' +
              esc(it.lifespan || it.death_label) +
              " · Death: <strong>" + esc(it.death_label) + "</strong> · " +
              esc(it.era) +
              "</div>" +
              (it.summary ? '<p class="geom-dir-summary">' + esc(it.summary) + "</p>" : "") +
              '<div class="geom-dir-tags">' + langsHtml + "</div>" +
              (linksHtml ? '<div class="geom-dir-links">' + linksHtml + "</div>" : "") +
              "</div></article>"
            );
          }

          var mLangs = (it.languages || [])
            .map(function (l) {
              return '<span class="geom-dir-tag">' + esc(l) + "</span>";
            })
            .join("");
          return (
            '<article class="geom-dir-card">' +
            '<a href="' + esc(it.url) + '" target="_blank" rel="noopener">' +
            '<img class="geom-dir-thumb" src="' + esc(it.thumbnail) + '" alt="' + esc(it.title) + '" loading="lazy">' +
            "</a>" +
            '<div class="geom-dir-body">' +
            '<h3 class="geom-dir-title">' + esc(it.title) + "</h3>" +
            '<div class="geom-dir-meta">' +
            esc(it.published_date) + " · " + esc(it.format) + " · " + esc(it.series) +
            "</div>" +
            '<div class="geom-dir-tags">' + mLangs + "</div>" +
            '<div class="geom-dir-links">' +
            '<a href="' + esc(it.url) + '" target="_blank" rel="noopener">Watch on YouTube</a>' +
            (it.codex_url ? '<a href="' + esc(it.codex_url) + '">Interactive Codex</a>' : "") +
            "</div></div></article>"
          );
        })
        .join("");
    }

    function buildShell() {
      var sortOpts =
        kind === "people"
          ? '<option value="death_asc">Sort: Death Date (Ancient → Modern)</option>' +
            '<option value="death_desc">Sort: Death Date (Modern → Ancient)</option>' +
            '<option value="title_asc">Sort: Name (A → Z)</option>' +
            '<option value="title_desc">Sort: Name (Z → A)</option>'
          : '<option value="pub_desc">Sort: Publish Date (Newest First)</option>' +
            '<option value="pub_asc">Sort: Publish Date (Oldest First)</option>' +
            '<option value="title_asc">Sort: Title (A → Z)</option>' +
            '<option value="title_desc">Sort: Title (Z → A)</option>';

      var langSet = { All: true };
      var seriesSet = { All: true };
      var formatSet = { All: true };
      items.forEach(function (it) {
        (it.languages || []).forEach(function (l) {
          langSet[l] = true;
        });
        if (it.series) seriesSet[it.series] = true;
        if (it.format) formatSet[it.format] = true;
      });

      var langPills = Object.keys(langSet)
        .map(function (l) {
          var cls = "geom-dir-pill" + (state.lang === l ? " is-active" : "");
          return '<button type="button" class="' + cls + '" data-filter="lang" data-val="' + esc(l) + '">' + esc(l) + "</button>";
        })
        .join("");

      var extraMediaFilters = "";
      if (kind === "media") {
        var sPills = Object.keys(seriesSet)
          .map(function (s) {
            var cls = "geom-dir-pill" + (state.series === s ? " is-active" : "");
            return '<button type="button" class="' + cls + '" data-filter="series" data-val="' + esc(s) + '">' + esc(s) + "</button>";
          })
          .join("");
        var fPills = Object.keys(formatSet)
          .map(function (f) {
            var cls = "geom-dir-pill" + (state.format === f ? " is-active" : "");
            return '<button type="button" class="' + cls + '" data-filter="format" data-val="' + esc(f) + '">' + esc(f) + "</button>";
          })
          .join("");
        extraMediaFilters =
          '<div class="geom-dir-pills"><span class="geom-dir-label">Series:</span>' + sPills + "</div>" +
          '<div class="geom-dir-pills"><span class="geom-dir-label">Format:</span>' + fPills + "</div>";
      }

      root.innerHTML =
        '<div class="geom-dir-controls">' +
        '  <div class="geom-dir-row">' +
        '    <input type="search" class="geom-dir-search" placeholder="Search ' + esc(kind) + '..." value="' + esc(state.q) + '">' +
        '    <select class="geom-dir-select">' + sortOpts + "</select>" +
        '    <span class="geom-dir-count"></span>' +
        "  </div>" +
        '  <div class="geom-dir-pills"><span class="geom-dir-label">Language:</span>' + langPills + "</div>" +
        extraMediaFilters +
        "</div>" +
        '<div class="geom-dir-grid"></div>';

      var sel = root.querySelector(".geom-dir-select");
      sel.value = state.sort;
      sel.addEventListener("change", function () {
        state.sort = sel.value;
        syncUrl();
        render();
      });

      var inp = root.querySelector(".geom-dir-search");
      inp.addEventListener("input", function () {
        state.q = inp.value;
        syncUrl();
        render();
      });

      root.querySelectorAll(".geom-dir-pill").forEach(function (btn) {
        btn.addEventListener("click", function () {
          var fk = btn.getAttribute("data-filter");
          var fv = btn.getAttribute("data-val");
          state[fk] = fv;
          root.querySelectorAll('.geom-dir-pill[data-filter="' + fk + '"]').forEach(function (b) {
            b.classList.toggle("is-active", b.getAttribute("data-val") === fv);
          });
          syncUrl();
          render();
        });
      });
    }

    fetch(dataUrl)
      .then(function (res) {
        return res.json();
      })
      .then(function (data) {
        items = Array.isArray(data) ? data : [];
        buildShell();
        render();
      })
      .catch(function (err) {
        root.innerHTML = "<p>Unable to load directory data.</p>";
        if (window.console) console.error(err);
      });
  }

  document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".geometor-directory[data-kind]").forEach(initDirectory);
  });
})();
