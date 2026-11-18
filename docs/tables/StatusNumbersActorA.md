# StatusNumbersActorA

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** Executable (initialised data, written at run time)
- **Address:** `0x140808200`
- **Rows:** 7 rows of 32 bytes
- **Keyed by:** field
- **Row layout:** [UiNumberField](../structs/UiNumberField.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Number fields of the acting unit's status panel (variant A). Verdict: designer-data.

## Behavior

- V: 7 records; the next symbol (0x1408082D0) is a field inside record 6
- V: BattleTask_Slot13Entry: draws the acting unit's HP, max HP, MP, max MP, CT (wt), max CT and AT

## Notes

Our names. Tags: V.

## Open questions

- ?: style bits
