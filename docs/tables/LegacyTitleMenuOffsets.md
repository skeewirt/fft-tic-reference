# LegacyTitleMenuOffsets

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable
- **Address:** `0x140692FE0`
- **Rows:** 6 rows of 2 bytes
- **Keyed by:** slot 0..5
- **Row layout:** [LegacyTitleMenuOffsetsRow](../structs/LegacyTitleMenuOffsetsRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Six signed offsets applied to the opening menu slots; the same 0x30-byte object continues with a float (0.01), a list of cell ids and two 5-byte lists. Verdict: designer-data.

## Behavior

- V: reader indexes u16 [x]; the object is 0x2F bytes to the next candidate
- V: sub_14037BA34 (opening / title menu step): word [i] added as a per-slot offset

## Notes

Our names. Tags: V reader, ? meaning.

## Open questions

- ?: what the offset moves (x, tile or row)
- ?: the remaining constants after the six words
