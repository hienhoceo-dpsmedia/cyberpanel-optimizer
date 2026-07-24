# DPS baseline cleanup design

## Goal

Keep the established `24a9aa4` DPS theme while removing dashboard marketing and internal-only navigation that is not used in this panel.

## Scope

- Hide the dashboard greeting and five quick-action cards as one visual block.
- Hide sidebar links for Email and Build Services, plus the Help heading and its Connect and Community links.
- Replace the remaining purple accent treatment with the DPS palette: navy `#151577` for primary controls and green `#32b561` for success/brand detail.

## Implementation

The installer continues to inject `dps_design.css` through `CyberPanelCosmetic.MainDashboardCSS`. The change is CSS-only: it does not alter Django templates, routes, permissions, or service behaviour. Selectors are scoped to the existing dashboard and sidebar classes/links so the standard CyberPanel update path remains intact.

## Verification

- A static CSS contract test asserts the required suppression selectors and DPS tokens.
- The installer is run on the panel and the logged-in dashboard is visually reviewed: no greeting/quick actions, no Email/Build Services/Help navigation, and no purple primary accents.
