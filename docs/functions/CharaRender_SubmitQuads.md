# CharaRender_SubmitQuads

- **Address:** `0x1403CF370`
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Prototype:** `unsigned int CharaRender_SubmitQuads(__int64 rt, __int64 target, unsigned first, const void *verts, int count, unsigned atlasTexId, unsigned lutTexId, char outlinePass)`
- **Callers:** CharaRender_DrawFrame
- **Callees:** sub_14003E120, sub_14003E228, sub_1403D0694 (constants), sub_1403D0538 (draw), memmove, memset

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Binds the atlas (slot 0) and the LUT texture (slots 1..3), sets sampler words and pass constants, copies the quad vertices into the vertex ring and queues the draw.

## Behavior

- V: texture slots: t0 = atlas, t1..t3 = the LUT texture (arg a7).
- V: sampler words: slot 0 = default word with bits 6..9 cleared; slots 1..3 = default word with bits 6 and 9 set (0x240), top bit masked. (The bit meanings are not decoded: slot 0 looks like point sampling, which matches the retail crisp pixel blocks.)
- V: vertices are 80 bytes each, copied at ring offset first * 80.
- V: pass constants (a 176-byte block matching the shader's cbDrawPS layout): outline pass: m_uiShaderType = 1 and m_outlinesColor = 0xFF000000; colour pass: m_uiShaderType = 0 and m_lutBlendFactor = 0.0.

## State touched

- Reads: [RenderContext.blend_state](../structs/RenderContext.md#blend_state), [g_DefaultSamplerWord](../globals/g_DefaultSamplerWord.md), [g_TextureTable](../globals/g_TextureTable.md)
- Writes: [RenderContext.texture_handles](../structs/RenderContext.md#texture_handles), [RenderContext.sampler_words](../structs/RenderContext.md#sampler_words), [RenderContext.index_buffer](../structs/RenderContext.md#index_buffer), [RenderContext.blend_state](../structs/RenderContext.md#blend_state), [RenderContext.blend_rt0](../structs/RenderContext.md#blend_rt0)

## Referenced by

- Called by: [CharaRender_DrawFrame](CharaRender_DrawFrame.md)

## Open questions

Blend state of the two passes and the sampler bit meanings are not decoded (?).
