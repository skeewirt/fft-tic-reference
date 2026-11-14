# LayerBlendNormal_PS

- **Kind:** shader
- **Stage:** pixel
- **Area:** [Graphics](../areas/graphics.md)
- **Technique file:** uirender.tec
- **Offset in file:** `0x006E60`
- **DXBC hash:** `89efc7496d5aea8df8ec2e9ffc7bafdc`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The layer blit pixel shader for blend type 0 (normal), offset variant 0: composites one layer's premultiplied pixels over the frame target by a read-modify-write of an unsigned-normalised UAV. It is the first of the 36 layer-blend pixel shaders (18 blend types x 2 offset variants) of selector #9; the blend arithmetic is in the shader, not in the fixed-function blend state.

## Interface and bindings

| Slot | Name | Bound to | Conf | Use |
|---|---|---|---|---|
| <a id="texcoord"></a>`in0` | `TEXCOORD` | [UIManager.layer_quad_buffer](../structs/UIManager.md#layer_quad_buffer) | V | Layer quad uv (position / target size). |
| <a id="sv_position"></a>`in1` | `SV_Position` |  | V | The pixel being written; its integer part addresses the UAV. |
| <a id="cuirender"></a>`cb0` | `cUIRender` |  | V | Row 34.zw = atlas offset / target size (added to the uv); rows 9 / 10 = colour multiply / add of the layer; row 8.z = brightness factor on rgb; rows 15, 18-19, 28-30 and 20-27 = the clip / distance-mask groups (off for a plain layer). |
| <a id="layer"></a>`t0` | `layer` | [RT26_LayerContent](../render-targets/RT26_LayerContent.md) | I | The layer's pixels (premultiplied RGBA); read through g_Sampler, which holds the default word (point), at the integer atlas offset, so the read is the texel. |
| <a id="mask source"></a>`t1` | `mask source` |  | V | Second source, sampled only when the clip group (row 15.w) is on; alpha scales the result. |
| <a id="target"></a>`u0` | `target` | [UITarget_Frame](../render-targets/UITarget_Frame.md) | V | The frame target (typed UNORM UAV), read and written in place. |

## Behavior

- V: S = sample(t0, uv + cb34.zw) x cb9 + cb10 per channel (rgba, premultiplied): with the default layer constants (multiply 1, add 0) S is the layer pixel.
- V: the clip / distance-mask groups (row 15.w, row 20.x and rows 24-27) only scale S further when enabled; a plain layer takes none of those branches.
- V: S.rgb is multiplied by cb8.z (1.0 in the Job Tree: the float at UI manager + 144, live read 1.0); S.a is not.
- V: when S.rgb x cb8.z and S.a are all exactly 0 the pixel is left alone (no load, no store).
- V: otherwise D = load(u0 at the pixel) and store(u0) = (D.rgb x (1 - S.a) + S.rgb x cb8.z, D.a x (1 - S.a) + S.a), a premultiplied 'over' in float, written to an 8-bit UNORM UAV.
- I: this is the pixel shader of selector #9 with digit 0 = 0 (blend type, GUILayer_BlitFinal) and digit 1 = 0 (no offset vectors): the 36 shaders at 0x006E60 .. 0x031B80 pair up as 3-sample / 5-sample variants, blend type k = shaders 2k and 2k + 1; blend type 2 (0x00BB20) computes a multiply (rgb = dst x (S + 1 - S.a)). Basis: the shader family layout and the arithmetic; the permutation table of the technique file was not parsed.

## Referenced by

- Observed behaviours: [LayerBlitOverFrameTarget](../behaviors/LayerBlitOverFrameTarget.md)
- Used in programs: [LayerBlit](../programs/LayerBlit.md)

## Notes

Blend type 0 is the type every Job Tree layer reads except the name tag Lv boards (type 2, multiply) and one layer with type 7 on the screen that was running when this was read.

## Open questions

? the vertex shader paired with it; the file's permutation table (which digit varies fastest) was inferred from the shader order, not parsed.
