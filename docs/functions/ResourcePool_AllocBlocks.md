# ResourcePool_AllocBlocks

- **Address:** `0x1402F3888`
- **Area:** [Resource](../areas/resource.md)
- **Prototype:** `char *__fastcall ResourcePool_AllocBlocks(unsigned __int64 size)`
- **Callers:** About 20 loaders, among them CharaPalette_LoadClassic, CharaRender_BuildAtlasTexture, EffectPalette_Step, EventSprite_LoadTask, JobChange_RunPreviewAnim
- **Callees:** memset

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Allocates a run of 2048-byte blocks from a fixed pool of 128 blocks and returns its address, or null.

## Behavior

- V: the block count is size/2048 rounded up.
- V: the owner map `byte_1418622F0` has 128 bytes; 0 is free. It scans for the first run of enough free bytes, remembering the highest non-zero tag seen plus 1 (starting at 1) as the new tag.
- V: the run is filled with that tag by memset and the result is `unk_141982E00 + 2048 * firstBlock`; null when no run is long enough.
- I: the pool holds file read buffers (rests on callers such as CharaRender_BuildAtlasTexture and EventSprite_LoadTask).

## Referenced by

- Called by: [EffectSequence_HitFlashSprites](EffectSequence_HitFlashSprites.md), [EffectSequence_ProjectileFlight](EffectSequence_ProjectileFlight.md)

## Notes

Whole body read.

## Open questions

How the tags are released.
