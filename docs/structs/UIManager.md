# UIManager

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The UI manager object at Renderer.ui_manager: the shader selectors of the UI technique and the shared layer quad buffers.

## Fields

| Offset | Field | Type | Conf | Meaning | Read by | Bound in shaders | Written by |
|---|---|---|---|---|---|---|---|
| <a id="selector_9"></a>`0x48` | selector_9 | `ptr` | V | Shader selector #9 (final layer blit, fitted post targets). | [GUILayer_BlitFinal](../functions/GUILayer_BlitFinal.md), [PostTarget_DrawFitted](../functions/PostTarget_DrawFitted.md) |  |  |
| <a id="selector_10"></a>`0x50` | selector_10 | `ptr` | V | Shader selector #10: program 0 the alpha copy, program 1 the drop shadow. | [GUILayer_BlurShadowPass](../functions/GUILayer_BlurShadowPass.md), [GUILayer_CopyToTarget](../functions/GUILayer_CopyToTarget.md) |  |  |
| <a id="slot_ttexture0"></a>`0x94` | slot_tTexture0 | `uint16` | V | Texture slot id of tTexture0 (UIRender_LoadShaders); +0x96 the constant-buffer slot id of cConstant0. |  |  |  |
| <a id="current_layer"></a>`0xD0` | current_layer | `ptr` | V | The layer being recorded (GUILayer_SetCurrent; read when commands are appended). |  |  |  |
| <a id="layers"></a>`0xD8` | layers | `ptr[512]` | V | Layer pointer table: 512 entries, the entry i is the record of slot i (the count at +0xAC belongs to the sorted layer list at +0x10D8, not to this table). |  |  |  |
| <a id="layer_list_count"></a>`0xAC` | layer_list_count | `uint32` | V | Number of entries of the sorted layer list at +0x10D8 (set by the collection in UIRender_PrepareLayers, cleared to 0 after the frame by UIRender_ClearLayerFlags). |  |  |  |
| <a id="layer_list"></a>`0x10D8` | layer_list | `ptr[512]` | V | The frame's used layers: filled in slot order, sorted by the layers' order (StdSort_LayersByOrder, a no-op) and then by the draw-order key +84 (StdSort_LayersByKey); GUILayer_PackAtlasRect runs over it in this order. Entries stay in memory after the frame. |  |  |  |
| <a id="atlas_primary"></a>`0x21A8` | atlas_primary | `AtlasShelf` | V | The primary layer atlas shelf (cursor x, row top, row height, page); see the behavior LayerAtlasPlacement. |  |  |  |
| <a id="atlas_secondary"></a>`0x21B8` | atlas_secondary | `AtlasShelf` | V | The secondary shelf used for masked layers (+487 only). |  |  |  |
| <a id="ui_render"></a>`0x20D8` | ui_render | `ptr` | V | The UIRender command ring (UIRender_LoadShaders). |  |  |  |
| <a id="effect_input_layout"></a>`0x2120` | effect_input_layout | `ptr` | V | Object the effect passes store at RenderContext.input_layout (element 1060); I: a vertex input layout (see that field). | [GUILayer_BlitFinal](../functions/GUILayer_BlitFinal.md), [GUILayer_BlurShadowPass](../functions/GUILayer_BlurShadowPass.md), [GUILayer_GlowPass](../functions/GUILayer_GlowPass.md), [sub_1403B5170](../functions/sub_1403B5170.md), [UIRender_DrawOverlayQuads](../functions/UIRender_DrawOverlayQuads.md) |  |  |
| <a id="layer_quad_buffer"></a>`0x2130` | layer_quad_buffer | `ptr` | V | Buffer of the layer quads used by the drop shadow and the final blit (element 1062): 64 bytes per layer, 16-byte vertices (position, uv). | [GUILayer_BlitFinal](../functions/GUILayer_BlitFinal.md), [GUILayer_BlurShadowPass](../functions/GUILayer_BlurShadowPass.md), [GUILayer_GlowPass](../functions/GUILayer_GlowPass.md), [UIRender_SubmitFrame](../functions/UIRender_SubmitFrame.md) | [LayerBlendNormal_PS](../shaders/LayerBlendNormal_PS.md), [LayerQuadOffset_VS](../shaders/LayerQuadOffset_VS.md) |  |
| <a id="layer_quad_mapped"></a>`0x2148` | layer_quad_mapped | `ptr` | V | CPU pointer of layer_quad_buffer while UIRender_SubmitFrame has it mapped (element 1065); GUILayer_FillQuadBuffers writes rect - atlas_offset, uv = position / target size. |  |  | [GUILayer_FillQuadBuffers](../functions/GUILayer_FillQuadBuffers.md), [UIRender_SubmitFrame](../functions/UIRender_SubmitFrame.md) |

## Referenced by

- Observed behaviours: [LayerAtlasPlacement](../behaviors/LayerAtlasPlacement.md)

## Notes

Detail and evidence: the function sheets linked from this page.

## Open questions

None recorded.
