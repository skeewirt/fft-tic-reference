# JobTree_ReleaseCharaSlots

- **Address:** `0x140133EB8`
- **Area:** [Job tree](../areas/job-tree.md)
- **Prototype:** `void JobTree_ReleaseCharaSlots(void)`
- **Callers:** UI system (addon close)
- **Callees:** sub_1400ED768, sub_1400CC52C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Releases the unit-preview render slots used by the tree panels (CharaRender slot ids 80..98).

## Behavior

- V: loop of 19: slot id 80+i; clears the 112-byte slot at CharaRenderMgr+14920+8960+112*i (sub_1400ED768) and releases it from the renderer (sub_1400CC52C).
- V: the loop count is 19, not 20: the panel at index 19 (slot 99) is not released here, and the extra panels (slots 100+) are not either.

## State touched

- Reads: [g_CharaRenderer](../globals/g_CharaRenderer.md), [g_CharaRenderMgr](../globals/g_CharaRenderMgr.md)

## Notes

None.

## Open questions

Whether the unreleased slots leak or are reused.
