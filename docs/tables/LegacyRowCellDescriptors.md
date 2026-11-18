# LegacyRowCellDescriptors

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable
- **Address:** `0x140811718`
- **Rows:** 9 rows of 24 bytes (from this address)
- **Keyed by:** descriptor index
- **Row layout:** [LegacyRowCellDescriptorsRow](../structs/LegacyRowCellDescriptorsRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Sprite cell descriptors of the item list row drawer, 24 bytes each. Verdict: designer-data.

## Behavior

- V: sub_1402BF9A8 selects descriptors by address according to the row type and passes them to the sprite queue
- I: bytes 4..15 hold two rectangles (the second equals the first)

## Notes

Our names. Tags: V reader, I layout.

## Open questions

- ?: field meanings
- ?: the descriptor count
