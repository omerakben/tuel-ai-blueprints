(() => {
  "use strict";

  const catalog = Array.isArray(window.BLUEPRINT_CATALOG) ? window.BLUEPRINT_CATALOG : [];
  const categoryNames = {
    food: "Food & drink",
    shops: "Shops & studios",
    care: "Care & coaching",
    trades: "Trades & crews",
  };
  const helloPrompt = "Please read START-HERE.md and ADOPT-AI.md in this folder, then help me set up my business here. Ask me one question at a time, with no tech talk. Help me choose one repeated job for an Assisted start, define what success and a stop signal look like, and save an adoption plan with my first useful draft. Show me every draft and every change before you save it. Never send, post, book, order, pay, file, sign, decide, or delete anything. I handle those actions myself.";

  const grid = document.getElementById("catalog-grid");
  const search = document.getElementById("business-search");
  const clearSearch = document.getElementById("clear-search");
  const resultStatus = document.getElementById("result-status");
  const emptyState = document.getElementById("empty-state");
  const resetFilters = document.getElementById("reset-filters");
  const copyStatus = document.getElementById("copy-status");
  const filterButtons = [...document.querySelectorAll("[data-category]")];
  let activeCategory = "all";

  const escapeHtml = (value) => String(value).replace(/[&<>"']/g, (character) => ({
    "&": "&amp;",
    "<": "&lt;",
    ">": "&gt;",
    "\"": "&quot;",
    "'": "&#39;",
  })[character]);

  const validSlug = (value) => /^[a-z][a-z0-9-]*$/.test(value);

  function cardMarkup(blueprint, index) {
    if (!validSlug(blueprint.slug)) return "";

    const titleId = `blueprint-title-${index}`;
    const category = categoryNames[blueprint.category] || "Business";
    const paddedIndex = String(index + 1).padStart(2, "0");
    const name = escapeHtml(blueprint.name);
    const slug = escapeHtml(blueprint.slug);
    const checksum = escapeHtml(blueprint.sha256);
    const tree = `${slug}/\n├── START-HERE.md\n├── ADOPT-AI.md\n├── CLAUDE.md\n├── UPGRADE.md\n├── adoption/\n├── business/\n├── inbox/\n├── operations/\n├── roles/\n├── skills/\n├── schedules/\n├── templates/\n├── workflows/\n└── reports/`;

    return `
      <article class="blueprint-card" aria-labelledby="${titleId}"
        data-category="${escapeHtml(blueprint.category)}"
        data-search="${escapeHtml(`${blueprint.name} ${blueprint.business_type} ${blueprint.keywords} ${blueprint.summary}`.toLowerCase())}">
        <div class="card-main">
          <div class="card-topline">
            <span class="category-label">${escapeHtml(category)}</span>
            <span class="card-index" aria-hidden="true">${paddedIndex}</span>
          </div>
          <div class="card-title-row">
            <span class="business-mark" aria-hidden="true">${escapeHtml(blueprint.emoji)}</span>
            <div>
              <h3 id="${titleId}">${name}</h3>
              <p class="business-type">For ${escapeHtml(blueprint.business_type)} owners</p>
            </div>
          </div>
          <p class="card-summary">${escapeHtml(blueprint.summary)}</p>
          <div class="first-win">
            <span>Your first useful draft</span>
            <strong>${escapeHtml(blueprint.first_win)}</strong>
          </div>
          <p class="artifact-facts">v${escapeHtml(blueprint.version)} · ${escapeHtml(blueprint.file_count)} files · ${escapeHtml(blueprint.zip_size)}</p>
          <div class="card-actions">
            <a class="button button-primary download-button" href="downloads/${slug}.zip" download aria-label="Download the ${name} blueprint ZIP">
              Download ZIP <span aria-hidden="true">↓</span>
            </a>
          </div>
        </div>
        <details class="card-preview">
          <summary>Preview what's inside</summary>
          <div class="preview-body">
            <p class="preview-intro">An ordinary working folder. Nothing installs when you download it.</p>
            <div class="mini-tree" aria-label="Folder preview for ${name}">${tree}</div>
            <div class="prompt-heading">
              <h4>Your hello prompt</h4>
              <button class="copy-button" type="button" data-blueprint-name="${name}" aria-label="Copy the hello prompt for ${name}">Copy prompt</button>
            </div>
            <p class="hello-prompt">${escapeHtml(helloPrompt)}</p>
            <p class="checksum"><code title="${checksum}" aria-label="SHA-256 checksum ${checksum}">SHA-256 ${checksum.slice(0, 16)}…</code><a href="downloads/${slug}.zip.sha256" download>Full hash</a></p>
          </div>
        </details>
      </article>`;
  }

  function buildCatalog() {
    grid.innerHTML = catalog.map(cardMarkup).join("");
    const count = document.getElementById("blueprint-count");
    if (count) count.textContent = String(catalog.length);
  }

  function normalizedSearch() {
    return search.value.trim().toLocaleLowerCase();
  }

  function applyFilters() {
    const query = normalizedSearch();
    const cards = [...grid.querySelectorAll(".blueprint-card")];
    let visibleCount = 0;

    cards.forEach((card) => {
      const categoryMatch = activeCategory === "all" || card.dataset.category === activeCategory;
      const searchMatch = !query || card.dataset.search.includes(query);
      const visible = categoryMatch && searchMatch;
      card.hidden = !visible;
      if (visible) visibleCount += 1;
    });

    clearSearch.hidden = search.value.length === 0;
    emptyState.hidden = visibleCount !== 0;
    const noun = visibleCount === 1 ? "blueprint" : "blueprints";
    resultStatus.textContent = `${visibleCount} ${noun} shown`;
  }

  function selectCategory(category) {
    activeCategory = category;
    filterButtons.forEach((button) => {
      button.setAttribute("aria-pressed", String(button.dataset.category === category));
    });
    applyFilters();
  }

  async function copyText(text) {
    if (navigator.clipboard && window.isSecureContext) {
      await navigator.clipboard.writeText(text);
      return;
    }

    const textArea = document.createElement("textarea");
    textArea.value = text;
    textArea.setAttribute("readonly", "");
    textArea.style.position = "fixed";
    textArea.style.opacity = "0";
    document.body.appendChild(textArea);
    textArea.select();
    const copied = document.execCommand("copy");
    textArea.remove();
    if (!copied) throw new Error("Copy command was not accepted");
  }

  async function handleCopy(button) {
    const name = button.dataset.blueprintName || "this blueprint";
    const originalLabel = button.textContent;
    button.disabled = true;

    try {
      await copyText(helloPrompt);
      button.textContent = "Copied ✓";
      copyStatus.textContent = `Hello prompt copied for ${name}.`;
    } catch {
      button.textContent = "Copy failed";
      copyStatus.textContent = "The prompt could not be copied. Select the prompt text and copy it manually.";
    }

    window.setTimeout(() => {
      button.textContent = originalLabel;
      button.disabled = false;
    }, 1800);
  }

  buildCatalog();
  applyFilters();

  search.addEventListener("input", applyFilters);
  clearSearch.addEventListener("click", () => {
    search.value = "";
    applyFilters();
    search.focus();
  });

  filterButtons.forEach((button) => {
    button.addEventListener("click", () => selectCategory(button.dataset.category));
  });

  resetFilters.addEventListener("click", () => {
    search.value = "";
    selectCategory("all");
    search.focus();
  });

  grid.addEventListener("click", (event) => {
    const button = event.target.closest(".copy-button");
    if (button) handleCopy(button);
  });
})();
