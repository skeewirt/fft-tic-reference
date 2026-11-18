# GfxBitExpandTables

- **Kind:** table
- **Area:** [Graphics](../areas/graphics.md)
- **Storage:** Executable
- **Address:** `0x140906B70`
- **Rows:** 16 + 32 + 64 rows of 1 byte
- **Keyed by:** channel value
- **Row layout:** [ChannelExpandRow](../structs/ChannelExpandRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Lookup tables that expand 4, 5 and 6 bit colour channels to 8 bits in the texture format converters. Verdict: engine-data.

## Behavior

- V: the converters index the table with the packed nibbles and fields of 16-bit pixels

## Notes

Our names. Tags: V.

## Open questions

None recorded.
