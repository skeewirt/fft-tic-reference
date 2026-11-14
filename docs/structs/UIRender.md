# UIRender

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The UI render object (the command ring): the slot ids it resolved by name when it was created, used by every UI draw.

## Fields

| Offset | Field | Type | Conf | Meaning | Read by | Written by |
|---|---|---|---|---|---|---|
| <a id="slot_cuirenderremap"></a>`0x40` | slot_cUIRenderRemap | `uint16` | V | Constant-buffer slot id of cUIRenderRemap. | [UICommandRing_Flush](../functions/UICommandRing_Flush.md) | [UIRender_CreateBuffers](../functions/UIRender_CreateBuffers.md), [UIRender_LoadShaders](../functions/UIRender_LoadShaders.md) |
| <a id="slot_cuirender"></a>`0x42` | slot_cUIRender | `uint16` | V | Constant-buffer slot id of cUIRender. | [UICommand_ExecuteBatches](../functions/UICommand_ExecuteBatches.md) | [UIRender_CreateBuffers](../functions/UIRender_CreateBuffers.md), [UIRender_LoadShaders](../functions/UIRender_LoadShaders.md) |
| <a id="slot_csdf"></a>`0x44` | slot_cSDF | `uint16` | V | Constant-buffer slot id of cSDF. | [UIRender_ApplyDrawState](../functions/UIRender_ApplyDrawState.md) | [UIRender_CreateBuffers](../functions/UIRender_CreateBuffers.md), [UIRender_LoadShaders](../functions/UIRender_LoadShaders.md) |
| <a id="slot_g_sampler"></a>`0x46` | slot_g_Sampler | `uint16` | V | Sampler slot id of g_Sampler (14 live). | [UICommandRing_Flush](../functions/UICommandRing_Flush.md), [UIRender_ApplyDrawState](../functions/UIRender_ApplyDrawState.md) | [UIRender_CreateBuffers](../functions/UIRender_CreateBuffers.md), [UIRender_LoadShaders](../functions/UIRender_LoadShaders.md) |
| <a id="slot_ttexture0"></a>`0x48` | slot_tTexture0 | `uint16` | V | Texture slot id of tTexture0. | [UICommandRing_Flush](../functions/UICommandRing_Flush.md), [UIRender_ApplyDrawState](../functions/UIRender_ApplyDrawState.md) | [UIRender_CreateBuffers](../functions/UIRender_CreateBuffers.md), [UIRender_LoadShaders](../functions/UIRender_LoadShaders.md) |
| <a id="slot_g_sampler_tmaskbuffer"></a>`0x4A` | slot_g_Sampler_tMaskBuffer | `uint16` | V | Sampler slot id of g_Sampler_tMaskBuffer (15 live). | [UICommandRing_Flush](../functions/UICommandRing_Flush.md), [UIRender_ApplyDrawState](../functions/UIRender_ApplyDrawState.md) | [UIRender_CreateBuffers](../functions/UIRender_CreateBuffers.md), [UIRender_LoadShaders](../functions/UIRender_LoadShaders.md) |

## Notes

Detail and evidence: the function sheets linked from this page.

## Open questions

None recorded.
