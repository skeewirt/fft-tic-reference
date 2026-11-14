# Renderer

- **Kind:** structure
- **Area:** [Graphics](../areas/graphics.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The renderer object (global g_Renderer): output size, the render-target table and the per-type target slot tables, and the UI manager.

## Fields

| Offset | Field | Type | Conf | Meaning | Read by |
|---|---|---|---|---|---|
| <a id="output_width"></a>`0x19A8` | output_width | `uint32` | V | Width of the UI target in pixels (1280 at 720p). | [GUILayer_Composite](../functions/GUILayer_Composite.md), [GUILayer_FillQuadBuffers](../functions/GUILayer_FillQuadBuffers.md), [RenderFrame_FillLayerConstants](../functions/RenderFrame_FillLayerConstants.md), [RenderFrame_Update](../functions/RenderFrame_Update.md), [UIBlur_DownsampleDispatch](../functions/UIBlur_DownsampleDispatch.md), [UIRender_LoadShaders](../functions/UIRender_LoadShaders.md), [UIRender_ResolveBase](../functions/UIRender_ResolveBase.md) |
| <a id="output_height"></a>`0x19AC` | output_height | `uint32` | V | Height of the UI target in pixels. | [GUILayer_Composite](../functions/GUILayer_Composite.md), [GUILayer_FillQuadBuffers](../functions/GUILayer_FillQuadBuffers.md), [RenderFrame_FillLayerConstants](../functions/RenderFrame_FillLayerConstants.md), [RenderFrame_Update](../functions/RenderFrame_Update.md), [UIBlur_DownsampleDispatch](../functions/UIBlur_DownsampleDispatch.md), [UIRender_LoadShaders](../functions/UIRender_LoadShaders.md), [UIRender_ResolveBase](../functions/UIRender_ResolveBase.md) |
| <a id="render_targets"></a>`0x5160` | render_targets | `{...}[40 B]` | V | Render-target table: entry k at +0x5160 + 40k, its +40 member the view object (render targets RT k). | [GUILayer_BlitFinal](../functions/GUILayer_BlitFinal.md), [GUILayer_CopyToTarget](../functions/GUILayer_CopyToTarget.md), [GUILayer_EffectPass0](../functions/GUILayer_EffectPass0.md), [GUILayer_GlowPass](../functions/GUILayer_GlowPass.md), [sub_1403B5170](../functions/sub_1403B5170.md), [UIBlur_BlurPassOrCopy](../functions/UIBlur_BlurPassOrCopy.md), [UIBlur_BlurPassSingle](../functions/UIBlur_BlurPassSingle.md), [UIBlur_CopyTarget](../functions/UIBlur_CopyTarget.md), [UIBlur_DownsampleDispatch](../functions/UIBlur_DownsampleDispatch.md), [UIBlur_Pass](../functions/UIBlur_Pass.md) |
| <a id="targets_by_type"></a>`0x5CB8` | targets_by_type | `{...}[800 B]` | V | Target table per target type (byte +86 of a target), stride 800. | [GUILayer_BlitFinal](../functions/GUILayer_BlitFinal.md), [GUILayer_BlurEffect](../functions/GUILayer_BlurEffect.md), [GUILayer_BlurShadowPass](../functions/GUILayer_BlurShadowPass.md), [GUILayer_GlowPass](../functions/GUILayer_GlowPass.md), [UIRender_SubmitFrame](../functions/UIRender_SubmitFrame.md) |
| <a id="slots_by_type"></a>`0x5EA0` | slots_by_type | `ptr[64][...]` | V | Per target type slot table (stride 512, 8-byte slots); slot 3 is the target the alpha copy writes (mid-frame capture: RT 3). | [GUILayer_EffectPass0](../functions/GUILayer_EffectPass0.md), [sub_1403B5170](../functions/sub_1403B5170.md), [UIBlur_BlurPassOrCopy](../functions/UIBlur_BlurPassOrCopy.md), [UIBlur_BlurPassSingle](../functions/UIBlur_BlurPassSingle.md), [UIBlur_CopyTarget](../functions/UIBlur_CopyTarget.md), [UIBlur_Pass](../functions/UIBlur_Pass.md) |
| <a id="ui_manager"></a>`0x9430` | ui_manager | `ptr` | V | The UI manager (UIManager). | [GUICore_DrawOutsideBars](../functions/GUICore_DrawOutsideBars.md), [GUILayer_ApplyEffects](../functions/GUILayer_ApplyEffects.md), [GUILayer_BlitFinal](../functions/GUILayer_BlitFinal.md), [GUILayer_BlurShadowPass](../functions/GUILayer_BlurShadowPass.md), [GUILayer_Composite](../functions/GUILayer_Composite.md), [GUILayer_CopyToTarget](../functions/GUILayer_CopyToTarget.md), [GUILayer_EffectPass0](../functions/GUILayer_EffectPass0.md), [GUILayer_FillQuadBuffers](../functions/GUILayer_FillQuadBuffers.md), [GUILayer_GlowPass](../functions/GUILayer_GlowPass.md), [GUILayer_PackAtlasRect](../functions/GUILayer_PackAtlasRect.md), [GUILayer_SetCurrent](../functions/GUILayer_SetCurrent.md), [GUIQuad_EmitGouraud](../functions/GUIQuad_EmitGouraud.md), [GUIRenderer_ResetFrame](../functions/GUIRenderer_ResetFrame.md), [PostTarget_DrawFitted](../functions/PostTarget_DrawFitted.md), [RenderFrame_Update](../functions/RenderFrame_Update.md), [sub_1403B5170](../functions/sub_1403B5170.md), [UIBlur_DownsampleDispatch](../functions/UIBlur_DownsampleDispatch.md), [UIBlur_DownsampleRegion](../functions/UIBlur_DownsampleRegion.md), [UICommand_ExecuteBatches](../functions/UICommand_ExecuteBatches.md), [UIDraw_QuadTransformed](../functions/UIDraw_QuadTransformed.md), [UIImage_DrawTiled](../functions/UIImage_DrawTiled.md), [UILayer_FillConstants](../functions/UILayer_FillConstants.md), [UIPartRef_GetResource](../functions/UIPartRef_GetResource.md), [UIRender_AppendCommand](../functions/UIRender_AppendCommand.md), [UIRender_ApplyDrawState](../functions/UIRender_ApplyDrawState.md), [UIRender_QueueImageDraw](../functions/UIRender_QueueImageDraw.md) |

## Referenced by

- Global instances: [g_Renderer](../globals/g_Renderer.md)

## Notes

Detail and evidence: the function sheets linked from this page.

## Open questions

? a pointer table at +6560 + 8 x (byte +13754) overlaps output_width (+6568): seven functions read +6568 as the width, so either the index is always 0 or one of the two readings is wrong.
