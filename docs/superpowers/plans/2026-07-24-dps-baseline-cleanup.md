# DPS Baseline Cleanup Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Remove internal-panel marketing/navigation clutter from the `24a9aa4` DPS theme and use the DPS palette for all remaining primary accents.

**Architecture:** `apply_design.py` already downloads `dps_design.css` and saves it as CyberPanel's custom CSS. The implementation therefore adds a narrowly scoped override layer to that CSS only; no CyberPanel templates or routes change.

**Tech Stack:** CSS custom properties, Python `pytest`, CyberPanel `CyberPanelCosmetic` installer.

---

### Task 1: Lock the styling contract

**Files:**
- Create: `tests/test_dps_design_contract.py`
- Test: `tests/test_dps_design_contract.py`

- [ ] **Step 1: Write failing assertions**

Assert that `dps_design.css` has selectors that hide `.dashboard-greeting`, `.cp-quick-actions`, the two internal sidebar routes, the Help header/links, and exposes `#32b561` / `#151577` DPS colour tokens.

- [ ] **Step 2: Run the contract test**

Run: `python -m pytest tests/test_dps_design_contract.py -q`

Expected: FAIL because the baseline CSS has none of the required cleanup selectors or DPS tokens.

### Task 2: Add the CSS-only cleanup layer

**Files:**
- Modify: `dps_design.css`
- Test: `tests/test_dps_design_contract.py`

- [ ] **Step 1: Add DPS tokens and targeted overrides**

Define DPS navy and green tokens, map CyberPanel primary/accent variables to navy, and override activity/dashboard primary treatments without changing layout or server behaviour.

- [ ] **Step 2: Hide only requested dashboard/navigation UI**

Hide the greeting/quick-action block and sidebar Email, Build Services, Help, Connect, and Community entries by their existing classes and rendered links.

- [ ] **Step 3: Run the contract test**

Run: `python -m pytest tests/test_dps_design_contract.py -q`

Expected: PASS.

### Task 3: Deploy and visually review

**Files:**
- Modify: `dps_design.css`

- [ ] **Step 1: Commit and push the CSS change**

Push the verified CSS change to `main` so the one-line installer fetches the same revision.

- [ ] **Step 2: Run the existing installer on the panel**

Run the documented `apply_design.sh` command as root. It must successfully update `CyberPanelCosmetic.MainDashboardCSS` and restart `lscpd`.

- [ ] **Step 3: Review the live dashboard**

Confirm the requested items are absent and the remaining purple accents are navy/green DPS accents.
