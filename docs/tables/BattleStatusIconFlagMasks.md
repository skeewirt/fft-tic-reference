# BattleStatusIconFlagMasks

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** Executable
- **Address:** `0x1406735D0`
- **Rows:** 40 rows of 4 bytes (42 to the next symbol)
- **Keyed by:** status id 0..39
- **Read by:** [sub_1401FB064](../functions/sub_1401FB064.md)
- **Row layout:** [StatusIconFlagMaskRow](../structs/StatusIconFlagMaskRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Per status id the bit mask that marks the status on the battle scene object (drawing side). Verdict: engine-data.

## Behavior

- V: sub_1401FB064 picks a flag group by status id and sets or clears the mask from this table
- V: status 16 (oil) writes bit 8 of the second group directly, so its mask is unused

## Notes

Our names. Tags: V layout, V reader, I mapping.

## Open questions

- ?: which flag group each status uses
