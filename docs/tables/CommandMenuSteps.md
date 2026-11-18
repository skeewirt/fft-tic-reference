# CommandMenuSteps

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1408E64F0`
- **Rows:** 61 rows of 32 bytes
- **Keyed by:** step number
- **Read by:** [BattleCommand_BuildMenu](../functions/BattleCommand_BuildMenu.md)
- **Row layout:** [BattleMenuStepRow](../structs/BattleMenuStepRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The 61 rows of the stock battle menu step table with the task pointer of the command menu task. Verdict: code-table.

## Behavior

- V: 61 rows by the gap to the runtime state at 0x1408E6C90 and by the stock table
- V: bytes 16..18 of each row differ from the stock table; everything else is equal

## Notes

Our names. Tags: V relation, I fields.

## Open questions

None recorded.
