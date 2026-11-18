# StatsPanel_Build

- **Address:** `0x14022AC18`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void StatsPanel_Build(void)`
- **Callers:** sub_14022AFEC; the battle action display program table (script 6)
- **Callees:** NumberFields_Draw, VramPage_CopyRect, GradientWindow_ColourFromPaletteA, GradientWindow_ColourFromPaletteB

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the detailed stats panel (display script 6): draws its numbers into VRAM and places its sprite cells.

## Behavior

- V: draws three number groups with NumberFields_Draw: Move / Jump / Wt (0x140808B30, 3 fields), weapon powers (0x140808B90, 4) and the attack / defence / evasion pairs (0x140808C10, 8), each copied to VRAM.
- V: places 18 sprite cells from the language's stats panel cell table (0x1408087B0 language 0, 0x140808890 default, 0x140808970 language 2, 0x140808A50 language 3).

## State touched

- Calls: [NumberFields_Draw](NumberFields_Draw.md), [VramPage_CopyRect](VramPage_CopyRect.md), [GradientWindow_ColourFromPaletteA](GradientWindow_ColourFromPaletteA.md), [GradientWindow_ColourFromPaletteB](GradientWindow_ColourFromPaletteB.md)

## Referenced by

- Reads tables: [StatsPanelCellsDefault](../tables/StatsPanelCellsDefault.md), [StatsPanelCellsLanguage0](../tables/StatsPanelCellsLanguage0.md), [StatsPanelCellsLanguage2](../tables/StatsPanelCellsLanguage2.md), [StatsPanelCellsLanguage3](../tables/StatsPanelCellsLanguage3.md), [StatsPanelNumbers](../tables/StatsPanelNumbers.md)

## Notes

Read: the head (number groups and cell placement).

## Open questions

None recorded.
