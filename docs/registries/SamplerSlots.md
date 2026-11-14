# SamplerSlots

- **Kind:** registry
- **Area:** [Graphics](../areas/graphics.md)
- **Resolved by:** [NameSlotTable_Lookup](../functions/NameSlotTable_Lookup.md)
- **Values stored in:** [RenderContext.sampler_words](../structs/RenderContext.md#sampler_words)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The sampler names of the render device (31 live) and their slot ids. A shader's sampler register is bound by name to one of these slots; the GPU sampler it gets is the word stored at RenderContext.sampler_words[slot] when the draw is packed.

## Entries

| Id | Name | Value | Conf | Meaning | Observed behaviours | Bound in shaders |
|---|---|---|---|---|---|---|
| <a id="s_none1"></a>0 | `s_none1` |  | V | Placeholder name. |  |  |
| <a id="s_none2"></a>1 | `s_none2` |  | V | Placeholder name. |  |  |
| <a id="s_none3"></a>2 | `s_none3` |  | V | Placeholder name. |  |  |
| <a id="s_none4"></a>3 | `s_none4` |  | V | Placeholder name. |  |  |
| <a id="s_none5"></a>4 | `s_none5` |  | V | Placeholder name. |  |  |
| <a id="s_none6"></a>5 | `s_none6` |  | V | Placeholder name. |  |  |
| <a id="s_none7"></a>6 | `s_none7` |  | V | Placeholder name. |  |  |
| <a id="s_none8"></a>7 | `s_none8` |  | V | Placeholder name. |  |  |
| <a id="s_none9"></a>8 | `s_none9` |  | V | Placeholder name. |  |  |
| <a id="s_none10"></a>9 | `s_none10` |  | V | Placeholder name. |  |  |
| <a id="s_none11"></a>10 | `s_none11` |  | V | Placeholder name. |  |  |
| <a id="s_none12"></a>11 | `s_none12` |  | V | Placeholder name. |  |  |
| <a id="ccc_ppn_sampler"></a>12 | `ccc_ppn_sampler` | `0x2A` | V | Clamp on all axes, point min / mag, nearest mip (name pattern: three address letters, min, mag, mip). Set by the UI blur passes. |  |  |
| <a id="ccc_lln_sampler"></a>13 | `ccc_lln_sampler` | `0x26A` | V | Clamp, linear min / mag, nearest mip. Technique default of the layer-effect selector and of the blur passes. |  |  |
| <a id="g_sampler"></a>14 | `g_Sampler` | `0x2C0 or default` | V | The generic UI sampler: UIRender_ApplyDrawState writes the draw's word (0x2C0, linear, wrap) for textured draws and the default word otherwise; the layer-effect passes do not write it and get the default (0, point). | [EffectPassesInheritDefaultSampler](../behaviors/EffectPassesInheritDefaultSampler.md) | [UIImage_PS](../shaders/UIImage_PS.md), [LayerShadow_PS](../shaders/LayerShadow_PS.md) |
| <a id="g_sampler_tmaskbuffer"></a>15 | `g_Sampler_tMaskBuffer` | `as g_Sampler` | V | Written together with g_Sampler. |  |  |
| <a id="ccc_lln_sampler_tmaskbuffer"></a>16 | `ccc_lln_sampler_tMaskBuffer` | `0x26A` | V | Clamp, linear, nearest mip; technique default of the layer-effect selector. |  |  |
| <a id="www_lln_sampler"></a>17 | `www_lln_sampler` |  | V | Wrap, linear, nearest mip (by name). |  |  |
| <a id="cwc_lln_sampler"></a>18 | `cwc_lln_sampler` |  | V | Clamp / wrap / clamp, linear, nearest mip (by name). |  |  |
| <a id="pointsampler"></a>19 | `PointSampler` |  | V |  |  |  |
| <a id="linearsampler"></a>20 | `LinearSampler` |  | V |  |  |  |
| <a id="linearsampler_esgetex"></a>21 | `LinearSampler_esgeTex` |  | V |  |  |  |
| <a id="linearsampler_areatex"></a>22 | `LinearSampler_areaTex` |  | V |  |  |  |
| <a id="linearsampler_searchtex"></a>23 | `LinearSampler_searchTex` |  | V |  |  |  |
| <a id="linearsampler_blendtex"></a>24 | `LinearSampler_blendTex` |  | V |  |  |  |
| <a id="www_lll_sampler"></a>25 | `www_lll_sampler` |  | V | Wrap, linear, linear mip (by name). |  |  |
| <a id="www_ppn_sampler"></a>26 | `www_ppn_sampler` |  | V | Wrap, point, nearest mip (by name). |  |  |
| <a id="ssampler0"></a>27 | `sSampler0` |  | V |  |  |  |
| <a id="ssampler1"></a>28 | `sSampler1` |  | V |  |  |  |
| <a id="ssampler2"></a>29 | `sSampler2` |  | V |  |  |  |
| <a id="ssampler3"></a>30 | `sSampler3` |  | V |  |  |  |

## Behavior

- V (live read 2026-10-30): names and ids from the device's sampler table; values of slots 12-16 from live traces of the context at the layer passes and at UI draws.
- I: the meaning of the three-letter prefixes (address modes) and the lln / ppn / lll suffixes (min, mag, mip filters) is read from the names and matches the live words of slots 12, 13 and 16.

## Open questions

None recorded.
