# LayerBlitOverFrameTarget

- **Kind:** observed behaviour
- **Scope:** every layer of blend type 0 (normal)
- **Area:** [Graphics](../areas/graphics.md)
- **Affects:** [UiLayerComposite](../flows/UiLayerComposite.md), [GUILayer_BlitFinal](../functions/GUILayer_BlitFinal.md), [LayerBlit](../programs/LayerBlit.md), [LayerBlendNormal_PS](../shaders/LayerBlendNormal_PS.md), [UITarget_Frame](../render-targets/UITarget_Frame.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Store 2: the layer is blended onto the frame target by a pixel shader that reads the frame pixel through a UAV and writes it back: frame = layer + frame x (1 - layer alpha) in premultiplied form, per channel, from the layer's 8-bit pixel, stored again at 8 bits. The blend factors are in the shader arithmetic (ONE / INV_SRC_ALPHA written out), not in the output-merger state.

## Behavior

- V: pixel shader 0x006E60 (blend type 0, no offsets): S = layer pixel x cb9 + cb10 (default 1 and 0); out.rgb = frame.rgb x (1 - S.a) + S.rgb x cb8.z; out.a = frame.a x (1 - S.a) + S.a; skipped when S.rgb x cb8.z and S.a are all zero; cb8.z = 1.0 (live read of the UI manager float at +144; GUILayer_FillConstants writes it).
- V: the layer pixel is read at uv + cb34.zw with the default sampler word (point) where uv = position / target size and cb34.zw = atlas offset / target size, the atlas offset being integral (GUILayer_PackAtlasRect), so the read is exactly texel (pixel + atlas offset).
- V: the quad is the layer's integer screen rectangle (rect - atlas offset: x0 = (int)x, y0 = (int)y, x1 = (int)(x + w), y1 = (int)(y + h) of the unpacked rectangle); only those pixels are visited.
- V: the store is a typed UNORM UAV store, so the float result is converted to 8 bits; on the test GPU an exact half stores the lower value (see UnormStoreRoundsHalfDown).
- I: formula for a renderer, with Lp = the layer's stored 8-bit premultiplied pixel / 255 and Fp = the frame pixel / 255: F'.rgb = floor-half-down(255 x (Fp.rgb x (1 - Lp.a) + Lp.rgb)) / 255, F'.a likewise with alpha; layers are applied in the order of LayerCompositeOrder; the result is exact only when the layer pixels are the 8-bit values of store 1.
- V: other blend types (digit 0 = 1..17) are other shaders of the same family; blend type 2 is a multiply (rgb = frame x (S + 1 - S.a)); the Job Tree uses type 2 for the Lv chips of the name tags.

## Notes

This record and LayerContentDrawnIntoCleared8BitTarget give the two stores; the second is exact only if the first is.

## Open questions

? the blend types other than 0 and 2 were not read formula by formula.
