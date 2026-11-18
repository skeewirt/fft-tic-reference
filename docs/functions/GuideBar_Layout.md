# GuideBar_Layout

- **Address:** `0x14013D758`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 GuideBar_Layout(ButtonGuide *g)`
- **Callers:** sub_14013D064, sub_14013D4B0, sub_14013D590, GuideBar_SetPage, sub_14013DF84
- **Callees:** GUINode_UpdateColourAndMatrix, sub_1403DBC20, GuideBar_LayoutRow

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Rebuilds the guide bar: hides and resets all 8 slots, then lays out the visible rows of table 33 in two passes (left-aligned, then right-aligned).

## Behavior

- V: for the 8 slot nodes at g+280 (stride 272): if present set +144 = 0 (hidden) and GUINode_UpdateColourAndMatrix(node, 1); slot field +32 = -1 (no row).
- V: n = sub_1403DBC20(33, g+2224) rows. Pass 1: x cursor j = g+2232; for row i < n while used < 8: if GuideBar_LayoutRow(g, &j, used, i, 0) succeeded then used++ (rows whose flag byte +37 is 0).
- V: pass 2: j = 1920 - g+2232 (right edge of a 1920-wide screen); the same for rows with flag +37 == 1 (a5 = 1).
- V: returns the last call's result.

## State touched

- Calls: [GUINode_UpdateColourAndMatrix](GUINode_UpdateColourAndMatrix.md), [GuideBar_LayoutRow](GuideBar_LayoutRow.md)

## Referenced by

- Called by: [GuideBar_SetPage](GuideBar_SetPage.md)
- Observed behaviours: [GuideBarLayout](../behaviors/GuideBarLayout.md)

## Notes

The 1920 constant is V. Left group grows right from the left margin g+2232; right group is placed from the right margin leftwards (GuideBar_LayoutRow subtracts the width).

## Open questions

? row flag +37 semantics (left / right placement assumed).
