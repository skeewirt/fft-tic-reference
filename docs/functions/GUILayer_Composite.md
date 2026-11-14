# GUILayer_Composite

- **Address:** `0x1403B59D4`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `char GUILayer_Composite(UILayer *layer, char first, __int64 a3, __int64 a4)`
- **Callers:** UIRender_SubmitFrame (once per used layer, the first call with flag 1)
- **Callees:** UILayer_FillConstants, GUILayer_FillQuadBuffers, LayerBinds_Replay, RenderCommand_Allocate, RenderCommand_Submit, GUILayer_CopyOffsetRegion, GUILayer_ApplyEffects, GUILayer_BlurEffect

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Packs the commands of one finished offscreen layer for the frame: the clears of its atlas page, the effect passes and the blit of the layer onto its parent target. Called once per used layer by UIRender_SubmitFrame.

## Behavior

- V (whole function read 2026-10-30): runs only when the layer's used byte +76 is set. Sets +491 = 1 unless the layer has +78, +487, +488 or a non-zero kind (+28), or the device byte at (*(g_RenderDevice + 88)) + 156 is 0; fills the layer's constants (UILayer_FillConstants) and, when that succeeded and the cull byte +79 is clear, the layer's quads (GUILayer_FillQuadBuffers).
- V: builds the clamp rectangle {(x + 0.5) / W, (y + 0.5) / H, (x + w - 0.5) / W, (y + h - 0.5) / H} from the float rectangle +208..+220 and the int rectangle {(int)x, (int)y, (int)(x + w), (int)(y + h)} (the packed atlas rectangle) and passes them to the effect passes.
- V: sort keys (the same layout in every use: (order & 0x1FF | ((page & 0x3F | target type << 18) << 15) | pass constant) << 10; a target type of 1 is written as 0): clear 0x6AC00200 (pass 1), copy 0x6AC00E00 (pass 7), final 0x6AC07E00 (pass 63) is left in the state at the end.
- V: clears: when the layer's atlas page (+16) differs from the last cleared page (dword_140906B5C, reset to -1 each frame by UIRender_PrepareLayers) it queues, for the layer's target type table (g_Renderer + 512 x type + 24224), clear commands (RenderCommand_Allocate type 0, 32 bytes: the +40 member of the slot's target in the second qword, 16 zero bytes of colour after it) for slots 26, 27, 28 and 29 (offsets 24432 .. 24456); a 24-byte type-1 command for g_Renderer + 20632 when +492 and +484 are set. A drop-shadow layer (+177, +486 clear) also clears slot 3 (24248) once per page (dword_140906B60) and a masked layer (+487) slot 30 (24464) (dword_140906B64).
- V: effects (when the byte +179 is set): the sort key becomes 0x6AC00E00; kind (+28) 1 runs GUILayer_BlurEffect (the whole-layer blur) and kind 0 runs GUILayer_CopyOffsetRegion (masked layers) or, when that returns 0, GUILayer_ApplyEffects, which draws the layer's effects and the layer blit (GUILayer_BlitFinal) and the glow pass.
- V: the layer's own draws are not queued here: UICommand_ExecuteBatches replays them (sort key pass 2, constant 0x6AC00400) into RT 26.

## State touched

- Calls: [UILayer_FillConstants](UILayer_FillConstants.md), [GUILayer_FillQuadBuffers](GUILayer_FillQuadBuffers.md), [LayerBinds_Replay](LayerBinds_Replay.md), [RenderCommand_Allocate](RenderCommand_Allocate.md), [RenderCommand_Submit](RenderCommand_Submit.md), [GUILayer_CopyOffsetRegion](GUILayer_CopyOffsetRegion.md), [GUILayer_ApplyEffects](GUILayer_ApplyEffects.md), [GUILayer_BlurEffect](GUILayer_BlurEffect.md)
- Reads: [GUILayer.rect](../structs/GUILayer.md#rect), [GUILayer.sort_lo](../structs/GUILayer.md#sort_lo), [GUILayer.sort_hi](../structs/GUILayer.md#sort_hi), [Renderer.ui_manager](../structs/Renderer.md#ui_manager), [Renderer.output_width](../structs/Renderer.md#output_width), [Renderer.output_height](../structs/Renderer.md#output_height), [g_RenderDevice](../globals/g_RenderDevice.md), [g_Renderer](../globals/g_Renderer.md), [GUILayer.used](../structs/GUILayer.md#used), [GUILayer.culled](../structs/GUILayer.md#culled), [GUILayer.composited](../structs/GUILayer.md#composited), [GUILayer.layer_kind](../structs/GUILayer.md#layer_kind), [GUILayer.packed](../structs/GUILayer.md#packed), [GUILayer.atlas_offset](../structs/GUILayer.md#atlas_offset)
- Writes: [RenderContext.sort_key](../structs/RenderContext.md#sort_key)

## Referenced by

- Appears in flows: [FrameUiSubmission](../flows/FrameUiSubmission.md)
- Called by: [UIRender_SubmitFrame](UIRender_SubmitFrame.md)
- Resolves registries: [LayerPassKeys](../registries/LayerPassKeys.md)

## Notes

Earlier versions of this sheet listed only the head. The glow strength / gain / mode 3 combine is in GUILayer_GlowPass and its shader (decoded elsewhere). The clears fire once per atlas page, before any draw of the page (pass order), so the layer content target is empty (0, 0, 0, 0) where no draw lands.

## Open questions

? the type-1 command's target (g_Renderer + 20632) and when +484 / +492 are both set.
