# StatsPanelCellsLanguage0

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1408087B0`
- **Rows:** 18 rows of 12 bytes
- **Keyed by:** panel cell 0..17
- **Read by:** [StatsPanel_Build](../functions/StatsPanel_Build.md)
- **Row layout:** [UiSpriteCell](../structs/UiSpriteCell.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Sprite cells of the detailed stats panel (Move, Jump, weapon power, At / Def / Ar / Av), language 0. Verdict: designer-data.

## Behavior

- V: loop of 18; 0xD8 = 18 x 12
- V: sub_14022AC18 (detailed stats panel, display script 6): places 18 cells

## Notes

Our names. Tags: V.

## Open questions

None recorded.
