# TitleMenu_SelectKind

- **Address:** `0x1401C4448`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void TitleMenu_SelectKind(UIAddonFFTOTitle *addon, uint8 kind)`
- **Callers:** TitleMenu_Build, TitleMenu_FocusCurrent
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sets the current row to the first row of a given kind (-1 when there is none).

## Behavior

- V: scans the rows in order and stores the index of the first row whose kind byte matches.

## Referenced by

- Called by: [TitleMenu_Build](TitleMenu_Build.md)

## Open questions

None recorded.
