# CharaRenderer_GlareChain

- **Address:** `0x1400D1018`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `void CharaRenderer_GlareChain(GlareState *g)`
- **Callers:** CharaRenderer_PostFrame
- **Callees:** shader table (qword_140D3AD60) methods, sub_140069A38, sub_1403CC7C0, sub_1403CC8E0, sub_1403D0694

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Runs the glare (bloom) passes on the unit renderer's scene target: bright-pass (shader id 1035 GLARE_BRIGHT), blur (1036 GLARE_BLUR) and the composite.

## Behavior

- V: sets the target from g+3840, viewport (g+4448 >> 2, g+4452 >> 2) = quarter resolution, selects shader 1035 with parameters {1.0, g+3868, g+3864} (v69[0..2]); a later part runs the blur chain and composite.
- V (shader, from the embedded DXBC): bright-pass keeps pixels above luminance threshold p.x * p.y, capped at p.x * p.z, hue-preserving; the composite pixel shader (post_effect_ps) adds the blurred texture (tTexture1) to the scene (tTexture0) with the tone formula in the post-effect pixel shader (embedded DXBC).

## State touched

- Reads: [RenderContext.target](../structs/RenderContext.md#target), [RenderContext.raster_word](../structs/RenderContext.md#raster_word), [g_TextureTable](../globals/g_TextureTable.md)
- Writes: [RenderContext.sort_key](../structs/RenderContext.md#sort_key), [RenderContext.target](../structs/RenderContext.md#target), [RenderContext.target_handle](../structs/RenderContext.md#target_handle), [RenderContext.raster_word](../structs/RenderContext.md#raster_word), [RenderContext.clip_rect](../structs/RenderContext.md#clip_rect), [RenderContext.blend_rt0](../structs/RenderContext.md#blend_rt0), [RenderContext.texture_handles](../structs/RenderContext.md#texture_handles), [RenderContext.sampler_words](../structs/RenderContext.md#sampler_words)

## Referenced by

- Called by: [CharaRenderer_PostFrame](CharaRenderer_PostFrame.md)

## Notes

Only the first ~120 lines of this 8.5 KB function were read; the blur and composite parts are not yet documented.

## Open questions

Parameter values at g+3864/+3868 and which target a UI draw ends up in (?).
