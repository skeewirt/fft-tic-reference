# CharaRender_PlaceSlotImage

- **Address:** `0x1400ED7CC`
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Prototype:** `void CharaRender_PlaceSlotImage(CharaRenderSlot *slot)`
- **Callers:** CharaRender_SetSlotRequest, CharaRender_RegisterSlot, sub_1400ED9C4 (all 256 slots)
- **Callees:** sub_14003E5D8 and sub_14003E604 (texture width/height), GUINode_SetPosition, sub_1403EF6B4, sub_1403EF704

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Points the slot's UI image node at the unit's render texture and sizes/positions it: size = texture size x (slot scale +60 / entry scale +12), offset from the entry's anchor.

## Behavior

- V: texture handle comes from renderer+70708 + 4*id into the engine texture table qword_143CD9F20; width/height from sub_14003E5D8/E604.
- V: the node gets the texture at node+208, position (GUINode_SetPosition) from the slot anchor + entry offsets - scaled anchor, size (sub_1403EF6B4) from the texture size and pivot (sub_1403EF704).
- V: scale s = slot+60 (default 1.5, set by sub_1400ED768) divided by the config scale (entry +12, 2.0); node width = texture width x s x dword_1407DC468, node height = texture height x s, pivot = (config x x s x dword_1407DC468, config y x s) (read from the assembly).
- V: dword_1407DC468 is the unit image's pixel aspect factor: 1.0 when dword_142E7FCA0 = 0, 1.1408199 when it is non-zero (sub_1401E7BA4 / sub_140255DEC); the default init sets dword_142E7FCA0 = 1, so in normal play the sprite is 14.08% wider than tall. Measured on retail: horizontal scale 1.10..1.15 of the vertical one.

## State touched

- Calls: [GUINode_SetPosition](GUINode_SetPosition.md)
- Reads: [g_CharaRenderer](../globals/g_CharaRenderer.md), [g_TextureTable](../globals/g_TextureTable.md), [g_UnitImageAspectX](../globals/g_UnitImageAspectX.md)

## Referenced by

- Called by: [CharaRender_RegisterSlot](CharaRender_RegisterSlot.md), [CharaRender_SetSlotRequest](CharaRender_SetSlotRequest.md)

## Notes

The tree's gadget image therefore shows the unit's render texture through the UI image sampler.

## Open questions

The exact k for the tree panels was not evaluated; the studio uses a measured 2.5 x 2.2 (docs/reference/sprites.md).
