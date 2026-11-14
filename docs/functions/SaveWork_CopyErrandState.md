# SaveWork_CopyErrandState

- **Address:** `0x14027966C`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void SaveWork_CopyErrandState(void *work, int direction)`
- **Callers:** Battle_SaveCapture, Battle_RestoreCapture
- **Callees:** none found

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Copies the party-wide status masks, the errand arrays and the active errand slot records between a save work block and the live globals, in the direction the second argument selects.

## Behavior

- V: the older index entry points at three int3 padding bytes; the body starts at 0x14027966C, which is the target of every call.
- V: the first argument is the base of the save work block and the second is the direction: 1 copies work to live, 0 copies live to work.
- V: the work block is read at fixed offsets (+0x114, +0x22C and later sub-blocks), each sub-block copied as a run of 16-byte units with a tail.
- V: the live side is the contiguous state region that begins at the party-wide status masks 0x1411A6A70; this body moves the errand part that follows the masks and never touches the masks themselves.
- V: the direction test is repeated in front of every sub-block, so the same routine serves the capture and the restore path.
- V: it returns without a value and calls no helper; it is a pure byte mover.
- I: the sub-blocks correspond to the errand and status state named in the save-layout records; the exact length of each was not counted here.
- ?: where the work block itself is allocated and whether it is cleared before a capture; this body only moves bytes.

## State touched

- Reads: [g_ErrandDelay](../globals/g_ErrandDelay.md), [g_ErrandActive](../globals/g_ErrandActive.md)
- Writes: [g_ErrandDelay](../globals/g_ErrandDelay.md), [g_ErrandActive](../globals/g_ErrandActive.md)

## Referenced by

- Called by: [Battle_RestoreCapture](Battle_RestoreCapture.md), [Battle_SaveCapture](Battle_SaveCapture.md)

## Notes

The older index entry is padding; the real body starts three bytes later at 0x14027966C. Direction and offsets read from the body; the block lengths belong to the save-format records.

## Open questions

None recorded.
