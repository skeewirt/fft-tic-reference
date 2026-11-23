# EventWorkBufferPointers

- **Kind:** table
- **Area:** [Event system](../areas/event-system.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x14080C5D0`
- **Rows:** 8 rows of 8 bytes
- **Keyed by:** buffer index
- **Row layout:** [BufferPointer](../structs/BufferPointer.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Descriptor {flags, count, 8 buffer pointers} of event work buffers. Verdict: pointer-table.

## Behavior

- V: 8 relocated pointers between two count dwords
- V: EventWork_RunCommand: clears count (dword_14080C5C0 = 9) words of the first buffer; a second descriptor follows at 0x14080C610

## Notes

Our names. Tags: V layout, ? meaning.

## Open questions

- ?: what the buffers hold
