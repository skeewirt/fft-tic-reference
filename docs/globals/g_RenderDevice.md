# g_RenderDevice

- **Kind:** global
- **Address:** `0x140C696A8`
- **Area:** [Graphics](../areas/graphics.md)
- **Type:** `RenderDevice *`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The render device: name-to-slot tables for constant buffers (+5056), textures (+5064) and samplers (+5072), the render-context array (+4984, stride 6032, count +5088) and the command-memory pool counters (+5144..+5152).

## Referenced by

- Read by: [App_RunFrame](../functions/App_RunFrame.md), [FrequentUtilRenderer_CreateResources](../functions/FrequentUtilRenderer_CreateResources.md), [GUILayer_BlurEffect](../functions/GUILayer_BlurEffect.md), [GUILayer_Composite](../functions/GUILayer_Composite.md), [RenderPass_Build](../functions/RenderPass_Build.md), [RenderPass_Sort](../functions/RenderPass_Sort.md), [RenderState_PackCommand](../functions/RenderState_PackCommand.md), [RootSignature_CreateWithSampler](../functions/RootSignature_CreateWithSampler.md), [SDFFontRenderer_CreateResources](../functions/SDFFontRenderer_CreateResources.md), [ShaderProgram_ApplyState](../functions/ShaderProgram_ApplyState.md), [TextureLoadInfo_Free](../functions/TextureLoadInfo_Free.md), [TextureResourceHandle_RegisterImages](../functions/TextureResourceHandle_RegisterImages.md), [TextureResourceHandle_Unload](../functions/TextureResourceHandle_Unload.md), [UILayer_FillConstants](../functions/UILayer_FillConstants.md), [UIRender_CreateBuffers](../functions/UIRender_CreateBuffers.md), [UIRender_DrawLetterbox](../functions/UIRender_DrawLetterbox.md), [UIRender_GetThreadContext](../functions/UIRender_GetThreadContext.md), [UIRender_LoadShaders](../functions/UIRender_LoadShaders.md), [UIRender_ResolveBase](../functions/UIRender_ResolveBase.md), [UIRender_SubmitFrame](../functions/UIRender_SubmitFrame.md), [Video_OnResize](../functions/Video_OnResize.md)

## Open questions

None recorded.
