# UIContext_SortCommands

- **Address:** `0x1403AE508`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__m128i *UIContext_SortCommands(__int64 ctx, signed int *outCount)`
- **Callers:** UIRender_SubmitFrame
- **Callees:** UICommand_MergeSortRange

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Collects the 16-byte command records of one UIContext slot into a contiguous region of the command ring and stable-sorts them by the 64-bit key in the first qword.

## Behavior

- V: *outCount = 0 and returns 0 when ctx+76 (block count) is 0. Reserves 2 * blocks * 1024 bytes from the ring with an interlocked add on (ring+164) and fails (returns 0) when it does not fit.
- V: copies each 1024-byte block (a chain: next pointer at block +1008) with 16-byte moves, then duplicates the region once and computes count = bytes / 16 - ctx+72.
- V: sorts the records by unsigned 64-bit key (record +0): insertion sort for <= 7 entries, otherwise merge sort via UICommand_MergeSortRange on the two halves and a manual merge. Equal keys keep their order (stable).

## State touched

- Calls: [UICommand_MergeSortRange](UICommand_MergeSortRange.md)

## Referenced by

- Appears in flows: [FrameUiSubmission](../flows/FrameUiSubmission.md)
- Called by: [UIRender_SubmitFrame](UIRender_SubmitFrame.md)

## Notes

The name is ours (IDB: sub_1403AE508). The key is the value the draw helpers store at state+8 (see UIRender_SubmitFrame notes for its bit layout).

## Open questions

None recorded.
