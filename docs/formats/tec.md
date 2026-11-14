# tec

- **Kind:** file format
- **Extension:** `.tec`
- **Area:** [Graphics](../areas/graphics.md)
- **Read by:** [UIRender_CreateBuffers](../functions/UIRender_CreateBuffers.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Shader technique file (for example uirender.tec): the DXBC shader containers of a technique, its programs, sampler presets and the binding tables that tie each shader's registers to engine names.

## Layout

| Offset | Part | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="shader containers"></a>(per shader) | shader containers | `DXBC` | V | Complete DXBC containers at fixed offsets (the shader names on this site use the offset). |
| <a id="binding records"></a>(table) | binding records | `4 bytes` | I | One record per bound resource: register (byte), resource class (byte: 0 constant buffer or sampler, 0x54 texture, 0x14 UAV), name offset into the string pool (16-bit). Read from uirender.tec; the record layout is not confirmed by the loader code. |
| <a id="string pool"></a>(pool) | string pool | `char[]` | V | NUL-terminated names: sampler presets (ccc_lln_sampler, ...), constant buffers (cUIRender, cSDF, ...), textures (tTexture0, tTexture1), samplers (g_Sampler, g_Sampler_tMaskBuffer), uav, cCommon, cConstant0. |

## Open questions

? the header and the program / permutation tables; the loader that parses the binding records.
