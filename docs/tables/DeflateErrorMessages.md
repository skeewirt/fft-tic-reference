# DeflateErrorMessages

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** Executable
- **Address:** `0x1406F7660`
- **Rows:** 10 rows of 8 bytes
- **Keyed by:** 2 - result code of the compression routines
- **Read by:** [Deflate_Init2](../functions/Deflate_Init2.md)
- **Row layout:** [StringPointerRow](../structs/StringPointerRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Result code messages of the embedded compression library in its usual order: need dictionary, stream end, (empty), file error, stream error, data error, insufficient memory, buffer error, incompatible version, (empty). Verdict: text.

## Behavior

- V: slots 2 and 9 point at the shared empty string of the executable (658 instructions and 5 other pointers address it); strings 4 and 7 are addressed by one further instruction each, the other strings by nothing else
- V: Deflate_Init2 stores the insufficient memory message (entry 6) into the stream when an allocation fails

## Notes

Our names. Tags: V layout, V reader, I count.

## Open questions

- ?: the inflate side readers
