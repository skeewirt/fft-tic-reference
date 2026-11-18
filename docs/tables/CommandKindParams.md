# CommandKindParams

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1408E64B0`
- **Rows:** 16 rows of 4 bytes
- **Keyed by:** battle command kind
- **Read by:** [BattleCommand_BuildMenu](../functions/BattleCommand_BuildMenu.md)
- **Row layout:** [CommandKindParam](../structs/CommandKindParam.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Two small values for each battle command kind; the same 16 rows sit in front of the stock menu step table. Verdict: designer-data.

## Behavior

- V: BattleCommand_BuildMenu reads the flag of the row for the unit's command kind (1 selects another message when the command byte is 20)
- I: 16 rows by the 64 bytes before the 61-row step table

## Notes

Our names. Found beside the table at 0x1408E64B0; tags V flag, I value.

## Open questions

None recorded.
