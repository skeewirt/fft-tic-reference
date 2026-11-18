# AudioTableValueTypeNames

- **Kind:** table
- **Area:** [Resource](../areas/resource.md)
- **Storage:** Executable
- **Address:** `0x140782540`
- **Rows:** 13 rows of 8 bytes
- **Keyed by:** value type id 0..12 (I)
- **Row layout:** [TextPointerRow](../structs/TextPointerRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Names of the value types of the audio library data tables: signed and unsigned 8 / 16 / 32 / 64 bit integers, 32 and 64 bit floats, string, variable length data and chunk data. Verdict: text.

## Behavior

- V: slots 10 and 11 (the string and variable-length types) are the same two strings that slots 10 and 11 of AudioTableValueTypeNamesAlt point to: each of those strings has two pointers
- V: 13 string pointers; the table at 0x140782730 lists the same types with another spelling and a GUID instead of chunk data in the last slot

## Notes

Our names. Tags: V layout, I use.

## Open questions

None recorded.
