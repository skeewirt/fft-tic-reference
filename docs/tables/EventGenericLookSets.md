# EventGenericLookSets

- **Kind:** table
- **Area:** [Event system](../areas/event-system.md)
- **Storage:** Executable
- **Address:** `0x1407141E0`
- **Rows:** 8 rows of 32 bytes
- **Keyed by:** look set id 0..7 (event script argument)
- **Read by:** [EventLookSet_Select](../functions/EventLookSet_Select.md)
- **Row layout:** [EventGenericLookSet](../structs/EventGenericLookSet.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Eight sets of generic sprite sheets that event scenes give to their placeholder actors. Verdict: designer-data.

## Behavior

- V: 8 x 32 bytes = 0x100 to the next symbol; guard id <= 7
- V: sub_1402459E0 (from EventScript_Run): copies row id into the active look pool 0x1437A1348 (id > 7: a default row)
- V: sub_140221798 / sub_14021FA50: an event actor with look code < 10 takes its sheet from the active pool

## Notes

Our names. Tags: V layout, I meaning.

## Open questions

- ?: which opcode selects the set
- ?: pool slots 8 and 9 (the reader allows < 10)
