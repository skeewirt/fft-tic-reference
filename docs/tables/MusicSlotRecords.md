# MusicSlotRecords

- **Kind:** table
- **Area:** [Event system](../areas/event-system.md)
- **Storage:** Executable
- **Address:** `0x14067FBB0`
- **Rows:** 101 rows of 12 bytes (extent of the object)
- **Keyed by:** sound id
- **Read by:** [EventCmd_ActivateSlotParam](../functions/EventCmd_ActivateSlotParam.md)
- **Row layout:** [MusicSlotRecordsRow](../structs/MusicSlotRecordsRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Per event sound id: an enable flag and two numbers loaded into the music state when the slot is activated. Verdict: designer-data.

## Behavior

- V: the slot activation function copies the id and the three dwords into the music state block, which the track loader reads
- I: the two numbers look like positions (multiples of 1024 less 64)

## Notes

Our names. Tags: V layout, I meaning, I count.

## Open questions

- ?: meaning of the two numbers
- ?: the exact row count
