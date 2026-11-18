# AudioTableValueTypeNamesAlt

- **Kind:** table
- **Area:** [Resource](../areas/resource.md)
- **Storage:** Executable
- **Address:** `0x140782730`
- **Rows:** 13 rows of 8 bytes
- **Keyed by:** value type id 0..12 (I)
- **Row layout:** [TextPointerRow](../structs/TextPointerRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The same value types as AudioTableValueTypeNames in the audio library own spelling; slot 12 is a GUID. Verdict: text.

## Behavior

- V: slots 10 and 11 point at strings that belong to AudioTableValueTypeNames; only 11 of its 13 slots own a string
- V: 13 string pointers, no direct instruction reference found (computed index)

## Notes

Our names. Tags: V layout, I use.

## Open questions

None recorded.
