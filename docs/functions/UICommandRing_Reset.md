# UICommandRing_Reset

- **Address:** `0x1403ADE60`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 UICommandRing_Reset(__int64 ring)`
- **Callers:** UIRender_LoadShaders, UIRender_SubmitFrame
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Resets the per-frame UI command ring: clears the write counters and re-initialises the 32 UIContext slots (80 bytes each).

## Behavior

- V: zeroes the interlocked counters ring+156 / +160 / +164 / +168 (the last gets ring+148, the capacity, when ring+24 is 0), sets ring+184 = ring+24 (current write base).
- V: for each of 32 slots at (ring+200) + 80 * i: +16 = 0, +24 = 0, +32 = ring+184, +56 = slot+48, +64 = 2048, +68 = 1024, +72 = 1 (block size 2048 bytes, 1024 entries..., first block count 1).

## Referenced by

- Called by: [UIRender_LoadShaders](UIRender_LoadShaders.md), [UIRender_SubmitFrame](UIRender_SubmitFrame.md)

## Notes

The name is ours (IDB: sub_1403ADE60). The meaning of 2048 / 1024 / 1 inside a slot is inferred from how UIContext_SortCommands reads the same slot (+76 = block count, +48 = first block).

## Open questions

Exact slot layout (?).
