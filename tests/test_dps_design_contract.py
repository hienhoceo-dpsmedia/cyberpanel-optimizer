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

    def test_overrides_late_legacy_purple_tokens_with_dps_surfaces(self):
        self.assertIn("html:root {", CSS)
        self.assertIn("--bg-primary: #f7f9fb;", CSS)
        self.assertIn("--bg-hover: #f0f6f2;", CSS)
        self.assertIn("--table-head-bg: var(--dps-navy);", CSS)
        self.assertIn("#main-content .btn-primary,", CSS)
        self.assertIn("#main-content .btn-info", CSS)


if __name__ == "__main__":
    unittest.main()
