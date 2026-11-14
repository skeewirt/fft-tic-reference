# UIImage_PS

- **Kind:** shader
- **Stage:** pixel
- **Area:** [Graphics](../areas/graphics.md)
- **Technique file:** uirender.tec
- **Offset in file:** `0x001E9C`
- **DXBC hash:** `edb866934daead99d5aa4a0a8b0bba4a`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The plain UI image pixel shader (UI technique program 0): every textured UI image (discs, the selection ring, the cursor glove, plates, floor tiles, line parts).

## Interface and bindings

| Slot | Name | Bound to | Conf | Use |
|---|---|---|---|---|
| <a id="ttexture0"></a>`t0` | `tTexture0` |  | V | The image's texture (straight alpha); its size and mip count are read in the shader. |
| <a id="g_sampler"></a>`s0` | `g_Sampler` | [SamplerSlots.g_Sampler](../registries/SamplerSlots.md#g_sampler) | V | The draw's sampler word (0x2C0: bilinear, wrap). |

## Behavior

- V: footprint F = max over u and v of max(ddx, ddy) of the texel coordinate (coarse derivatives, SIGNED: a mirrored cell's u counts as 0).
- V: when the texture has fewer than 2 mip levels and F > 2 (a pixel spans more than two texels) it takes four bilinear samples at +-0.5 texel in u and v and averages them; otherwise one sample.
- V: every sample's alpha is remapped before averaging: a' = saturate(a x 1.0101009607315063 - 0.010101010091602802), i.e. (a - 0.01) / 0.99; colour is not remapped.
- V: output = saturate(sample x vertex colour), premultiplied by the output alpha.
- V (mid-frame capture 2026-10-30, the selection ring's own draw into its layer, 2.7 texels per pixel): this fetch reproduces the draw to +-1 on 26 of 7700 values; a single bilinear sample misses by up to 24.

## Referenced by

- Observed behaviours: [BlendFactorUsesStoredSourceAlpha](../behaviors/BlendFactorUsesStoredSourceAlpha.md), [BlendTermsRoundedSeparately](../behaviors/BlendTermsRoundedSeparately.md), [CursorDrawnThroughLayerTarget](../behaviors/CursorDrawnThroughLayerTarget.md), [LayerContentDrawnIntoCleared8BitTarget](../behaviors/LayerContentDrawnIntoCleared8BitTarget.md), [RasterizerSnapsTo1_256Px](../behaviors/RasterizerSnapsTo1_256Px.md), [TexelWeights8Bit](../behaviors/TexelWeights8Bit.md), [VertexColourBytesTruncated](../behaviors/VertexColourBytesTruncated.md)
- Used in programs: [UIImage](../programs/UIImage.md)

## Open questions

None recorded.
