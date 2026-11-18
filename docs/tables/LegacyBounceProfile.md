# LegacyBounceProfile

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable
- **Address:** `0x1406931E6`
- **Rows:** 11 rows of 2 bytes
- **Keyed by:** frame
- **Row layout:** [LegacyBounceProfileRow](../structs/LegacyBounceProfileRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Symmetric 11-sample arc used to animate a cursor or row; the rest of the 0xBA-byte object holds small cell records. Verdict: engine-data.

## Behavior

- V: the reader addresses it as base + 6 of the object 0x1406931E0
- V: sub_1403980AC (0x1403980AC): word [frame] stored as a cursor offset (two sites, one per mode)

## Notes

Our names. Tags: V reader, I meaning.

## Open questions

- ?: the cell records after the arc (not read by this reader)
