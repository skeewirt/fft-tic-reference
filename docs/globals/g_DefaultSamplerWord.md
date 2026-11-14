# g_DefaultSamplerWord

- **Kind:** global
- **Address:** `0x141D8BC7C`
- **Area:** [Graphics](../areas/graphics.md)
- **Type:** `uint32`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Default sampler word every render context is reset to (masked with 0x7FFFFFFF). Holds 0xFFFFFFFF in the database image but 0 at runtime (live read 2026-10-30): point filter, wrap. No static writer found.

## Referenced by

- Read by: [CharaRender_SubmitQuads](../functions/CharaRender_SubmitQuads.md), [PostTarget_DrawFitted](../functions/PostTarget_DrawFitted.md), [RenderContext_ResetFrame](../functions/RenderContext_ResetFrame.md), [UICommandRing_Flush](../functions/UICommandRing_Flush.md), [UIRender_ApplyDrawState](../functions/UIRender_ApplyDrawState.md)

## Open questions

None recorded.
