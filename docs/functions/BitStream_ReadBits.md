# BitStream_ReadBits

- **Address:** `0x140360A74`
- **Area:** [Job list and unlock](../areas/job-list.md)
- **Prototype:** `uint32_t BitStream_ReadBits(int n)`
- **Callers:** Job_IsLockedForParty, sub_14028B6B0
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

MSB-first bit reader over the stream at `qword_143C49BF8`; the bit cursor is `dword_140906AAC`. `byte_142FF3CA7 = 1` resets the cursor to bit 7 of the first byte.

## Behavior

- V: returns 0 if n == 0.
- V: consumed bits advance the global cursor.
- V: pattern 'bit k of a bitfield' = reset, read(k), then read(1) (used by Job_IsLockedForParty).

## State touched

- Reads: [g_BitReaderCursor](../globals/g_BitReaderCursor.md), [g_BitReaderPtr](../globals/g_BitReaderPtr.md), [g_BitReaderReset](../globals/g_BitReaderReset.md)
- Writes: [g_BitReaderCursor](../globals/g_BitReaderCursor.md), [g_BitReaderPtr](../globals/g_BitReaderPtr.md), [g_BitReaderReset](../globals/g_BitReaderReset.md)

## Referenced by

- Called by: [JobList_RecomputeAvailability](JobList_RecomputeAvailability.md), [Job_IsLockedForParty](Job_IsLockedForParty.md)

## Notes

Global state; not thread-safe.

## Open questions

None recorded.
