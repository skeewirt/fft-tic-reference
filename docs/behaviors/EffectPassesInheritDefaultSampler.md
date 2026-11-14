# EffectPassesInheritDefaultSampler

- **Kind:** observed behaviour
- **Scope:** engine
- **Area:** [Graphics](../areas/graphics.md)
- **Affects:** [SamplerSlots.g_Sampler](../registries/SamplerSlots.md#g_sampler), [LayerShadow](../programs/LayerShadow.md), [FrameUiSubmission](../flows/FrameUiSubmission.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Layer effect passes read their textures through g_Sampler without setting it; because they are packed before the UI draws that set it, they always get the default word (point filter, wrap).

## Behavior

- V (live traces 2026-10-30): slots 14 and 15 hold 0 at the program apply of the glow, mask, alpha copy, shadow and final blit passes.
- V (mid-frame capture): the drop shadow lands whole pixels away (offset 1.6 -> 2 px, 1.333 -> 1 px), as a point read predicts and a bilinear read does not.

## Open questions

? which other effect shaders sample at fractional positions (the glow's half-size path is the first candidate).
