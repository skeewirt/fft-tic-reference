# GuideBar_SetPage

- **Address:** `0x14013D5F4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 GuideBar_SetPage(ButtonGuide *g, int tableKey, int enabledMask)`
- **Callers:** sub_1400EB65C, sub_14013C740
- **Callees:** GuideBar_Layout, sub_1401CC2D8

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Selects the page of the button-guide bar: sets table key (+2224) and enabled-row bitmask (+2228) and rebuilds it with GuideBar_Layout.

## Behavior

- V: if g+2224 == tableKey and g+2228 == enabledMask returns (nothing changes). If the key differs: clears the override-string map at g+2280 (red-black tree walk with node size 296, each node freed through the map allocator).
- V: stores g+2224 = tableKey, g+2228 = enabledMask, calls GuideBar_Layout(g), clears byte g+2268.

## State touched

- Calls: [GuideBar_Layout](GuideBar_Layout.md)

## Referenced by

- Called by: [UIGuide_Set](UIGuide_Set.md)
- Observed behaviours: [GuideBarLayout](../behaviors/GuideBarLayout.md)

## Notes

Proposed ButtonGuide_SetPage. The 'guide bar' reading is I: the table is UI table 33 (the button-hint table), up to 8 slots of 272 bytes at g+48.

## Open questions

? the owning class name (ButtonGuide is a placeholder).
