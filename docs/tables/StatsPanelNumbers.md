# StatsPanelNumbers

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x140808C10`
- **Rows:** 8 rows of 32 bytes
- **Keyed by:** field
- **Read by:** [StatsPanel_Build](../functions/StatsPanel_Build.md), [NumberFields_Draw](../functions/NumberFields_Draw.md)
- **Row layout:** [UiNumberField](../structs/UiNumberField.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Number fields of the detailed stats panel (attack, defence, evasion pairs). Verdict: designer-data.

## Behavior

- V: 8 records = 0x100
- V: sub_14022AC18: At, Atmagic, Def, Defmgc, Ar, Armagic, Av, Avmagic numbers (two smaller groups at 0x140808B30: Move, Jump, Wt; 0x140808B90: weapon powers)

## Notes

Our names. Tags: V.

## Open questions

None recorded.
