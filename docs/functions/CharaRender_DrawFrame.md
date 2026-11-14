# CharaRender_DrawFrame

- **Address:** `0x1400CD458`
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Prototype:** `__int64 CharaRender_DrawFrame(CharaRenderer *r, __int64 unused, int slot)`
- **Callers:** sub_1400D4CB0 (per-frame renderer update)
- **Callees:** CharaRender_BuildAtlasTexture, CharaRender_LookupLutParams, CharaRender_LutUvForQuad, CharaRender_SubmitQuads, sub_1403CC7C0 (set shader), sub_1403CCF24 (viewport), sub_14003F794

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Renders one unit slot's current animation frame into its 256 x 256 target: builds the atlas textures and LUT cell on demand, turns the frame's rectangles into quads and submits them twice (outline pass, then colour pass).

## Behavior

- V: the frame cache entry is renderer+47152 + 44*slot; it must have flag 1 (frame loaded). Flag 2 = atlases built (CharaRender_BuildAtlasTexture for which = 0 and 1), flag 8 = LUT cell chosen, flag 4 = drawn this frame.
- V: LUT cell (stored per slot at renderer+58424 + 40*slot): x = request byte +28 (a negative value means 2), y = request byte +29 (negative means 2); the entry's flag word (+47164) adds 5 (bit 2), 15 (bit 8) or 10 (bit 4) to x. The tree's flag word is 0, so its cell is (2, 2).
- V: LUT parameters (region size floats, offset shorts) come from CharaRender_LookupLutParams; the per-quad LUT UVs from CharaRender_LutUvForQuad.
- V: quad scale = target config scale (2.0) x 512 / 256 = 4 target px per classic px; ground point = config (128, 192); quad UVs are classic sheet px / 256 (corner + 0.5), clamped to 1.0.
- V: the frame index is the value from CharaAnim_ReadStep (entry +47160); frame records come from the pre-parsed SHP tables (one table per shape class, class stride 1668 words, 8-byte frame pointers, up to 208 frames); each 7-byte rectangle record gives x, y, w/h bytes, source u/v and mirror flags (bit 2 mirrors x about the ground, bit 4 mirrors y).
- V: vertices (80 bytes, 6 per rectangle) get vertex colour 1.0; the pass uses shader id 1014 (SHADER_ID_REFINED_CHARA_PARTS) and a 256 x 256 viewport (set from renderer+75832).
- V: two CharaRender_SubmitQuads calls follow: the first with the outline flag, the second without.

## State touched

- Calls: [CharaRender_BuildAtlasTexture](CharaRender_BuildAtlasTexture.md), [CharaRender_LookupLutParams](CharaRender_LookupLutParams.md), [CharaRender_LutUvForQuad](CharaRender_LutUvForQuad.md), [CharaRender_SubmitQuads](CharaRender_SubmitQuads.md)
- Reads: [g_CharaRenderer](../globals/g_CharaRenderer.md)
- Writes: [RenderContext.target](../structs/RenderContext.md#target), [RenderContext.target_handle](../structs/RenderContext.md#target_handle)

## Referenced by

- Called by: [CharaRenderer_Update](CharaRenderer_Update.md)

## Notes

Constants: docs/reference/sprite-pipeline.md. The studio carries a software model of this draw path.

## Open questions

The 8-bit frame-record fields (size code to w/h, mirror semantics) were matched to the classic SHP format rather than traced byte by byte (?).
