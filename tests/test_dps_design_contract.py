from pathlib import Path
import unittest


CSS = (Path(__file__).resolve().parents[1] / "dps_design.css").read_text(
    encoding="utf-8"
)


class DPSDesignContractTests(unittest.TestCase):
    def test_hides_non_operational_dashboard_and_sidebar_entries(self):
        required_selectors = (
            ".dashboard-greeting",
            ".cp-quick-actions",
            ".domain-hero",
            ".quick-actions",
            'a[href="/base/hub/email"]',
            'a[href="/base/buildServices"]',
            'a[href^="https://platform.cyberpersons.com/"]',
            'a[href^="https://cyberpanel.net/KnowledgeBase/"]',
            ".section-header:has(+ a[href^=\"https://platform.cyberpersons.com/\"])",
        )

        for selector in required_selectors:
            self.assertIn(selector, CSS)

    def test_uses_dps_navy_and_green_for_primary_accents(self):
        self.assertIn("--dps-navy: #151577;", CSS)
        self.assertIn("--dps-green: #32b561;", CSS)
        self.assertIn("--accent-color: var(--dps-navy);", CSS)
        self.assertIn(".activity-table thead", CSS)
        self.assertIn(".fa-chevron-down,", CSS)
        self.assertIn(".install-btn,", CSS)

    def test_overrides_late_legacy_purple_tokens_with_dps_surfaces(self):
        self.assertIn("html:root {", CSS)
        self.assertIn("--bg-primary: #f7f9fb;", CSS)
        self.assertIn("--bg-hover: #f0f6f2;", CSS)
        self.assertIn("--table-head-bg: var(--dps-navy);", CSS)
        self.assertIn("#main-content .btn-primary,", CSS)
        self.assertIn("#main-content .btn-info", CSS)
        self.assertIn("#main-content .btn-success,", CSS)
        self.assertIn(".cp-build-btn.ghost", CSS)
        self.assertIn("#cp-site-tabs .cp-tab.active", CSS)
        self.assertIn(".cp-tile .cp-tile-ic", CSS)

    def test_provides_2k_high_dpi_responsive_scaling(self):
        self.assertIn("@media screen and (min-width: 2200px)", CSS)
        self.assertIn("/* 2K / 1440p Displays (2200px+ viewport): ~1.5x font & UI scaling */", CSS)
        self.assertIn("font-size: 19.5px !important;", CSS)
        self.assertIn("height: 52px !important;", CSS)
        self.assertIn("width: 300px !important;", CSS)

    def test_hides_website_screenshot_and_compacts_metadata_grid(self):
        self.assertIn(".website-screenshot,", CSS)
        self.assertIn("display: none !important;", CSS)
        self.assertIn(".info-cell {", CSS)
        self.assertIn("padding: 10px 16px !important;", CSS)

    def test_redesigns_file_manager_with_dps_theme(self):
        self.assertIn("#navBar .nav-link:hover", CSS)
        self.assertIn("#treeView .content-box", CSS)
        self.assertIn(".col-sm-9 table thead", CSS)
        self.assertIn("background: var(--dps-navy, #151577) !important;", CSS)


if __name__ == "__main__":
    unittest.main()


