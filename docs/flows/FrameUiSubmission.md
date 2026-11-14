# FrameUiSubmission

- **Kind:** flow
- **Area:** [Graphics](../areas/graphics.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

How one frame's UI reaches the GPU, and why the order matters: commands are packed on the CPU in one order and executed by sort key in another, and every pass inherits the context state it does not set.

## Steps

| Step | Where | Conf | What happens |
|---|---|---|---|
| <a id="1"></a>1 | [RenderContext_ResetFrame](../functions/RenderContext_ResetFrame.md) | V | Start of frame (from App_RunFrame): every render context is reset; all sampler words = the default word (0: point, wrap). |
| <a id="2"></a>2 | [UIRender_SubmitFrame](../functions/UIRender_SubmitFrame.md) | V | UI submission: UIRender_ResolveBase, UIRender_DrawOverlayQuads. |
| <a id="3"></a>3 | [GUILayer_Composite](../functions/GUILayer_Composite.md) | V | Once per layer: the layer effect passes (alpha copy, blur, drop shadow, glow, mask, final blit) are packed here, with the sampler words still at the default. |
| <a id="4"></a>4 | [UIContext_SortCommands](../functions/UIContext_SortCommands.md) | V | Commands sorted by key. |
| <a id="5"></a>5 | [UICommandRing_Flush](../functions/UICommandRing_Flush.md) | V | g_Sampler and g_Sampler_tMaskBuffer set to the default, then the UI draws are replayed. |
| <a id="6"></a>6 | [UIRender_ApplyDrawState](../functions/UIRender_ApplyDrawState.md) | V | Per UI draw: g_Sampler = the draw's word (0x2C0, linear) when textured, else the default. |
| <a id="7"></a>7 |  | V | GPU: commands execute in sort-key order (layer content, then its effects by pass number). |

## Behavior

- V (live traces 2026-10-30): at the program apply of every layer pass (glow, mask, alpha copy, shadow, final blit) g_Sampler and g_Sampler_tMaskBuffer hold 0.

## Referenced by

- Observed behaviours: [EffectPassesInheritDefaultSampler](../behaviors/EffectPassesInheritDefaultSampler.md)

## Open questions

None recorded.
