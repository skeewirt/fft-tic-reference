# RenderFrame_FillLayerConstants

- **Address:** `0x1403A7E48`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `char RenderFrame_FillLayerConstants(LayerBinder *b, __int64 unused)`
- **Callers:** sub_1403A2774 (renderer frame update, at 0x1403A28FE)
- **Callees:** sub_14003E120 (map), sub_14003E228 (unmap)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Once per frame (called from the frame update sub_1403A2774 on renderer+24760): for each render layer target, maps its per-layer constant buffer and fills it with the layer pixel size, 1/size, ratios to the back buffer, time and delta time.

## Behavior

- V: loops i over the layer count (u16 renderer+13734, layer ids at renderer+7262); layer record = *(renderer + 8*id + 88); skipped unless the record's +40 resource exists. w = u16 layer+20, h = u16 layer+22, slot = byte layer+86; the render target state is renderer+8*(byte at renderer+6584+layer+87)+56 (u8 < 4 else null).
- V (buffer layout, mapped with sub_14003E120(buf, 2): from b+8+8*slot, so one buffer per layer slot): +128 / +144 = (w, h) as the two u32 pairs; +136 / +152 = (1/w, 1/h); +160 = back buffer size (qword renderer+6568: two u32); +168 = (1 / targetW, 1 / targetH); +176 = ((w / targetW) * (w / w), (h / targetH) * (h / h)) = (w / targetW, h / targetH); +184 = reciprocals of +176; +192 = the previous layer's +176 pair (kept at b+40+8*i and replaced by the new pair) and +200 its reciprocal.
- V (time terms from the target state t): +208 = 0x44800000 (1024.0f); +212 = (u32 t+4608 & 0x1FFFFF) * 1/1024 (time seconds, 21-bit wrap); +556 = (t+4612 & 0x1FFFFF) / 1024 (the previous time); +216 = t+4604 (delta time, float); +236 = 1 / dt (0 when dt <= 0); +220 = slot; +224 = t+4608 (raw time); +228 = (int)(dt * 1024); +308 = 1; +612 = (slot != 0); +0..+27 = t+4624..4647 (24 bytes of camera / world parameters, ?); +268 = 1 / layer+96 when |layer+96| > FLT_EPSILON else 1.0.
- V: the byte b+99 is decremented if non-zero; byte b+110 is cleared at the end. Unmaps with sub_14003E228.

## State touched

- Reads: [Renderer.output_width](../structs/Renderer.md#output_width), [Renderer.output_height](../structs/Renderer.md#output_height), [g_Renderer](../globals/g_Renderer.md)

## Notes

The name is ours (IDB: sub_1403A7E48). Gives the shaders 1 / size terms of every render target; the SDF text shader derives its screen-space UV derivatives itself so this is not in the glyph path. The time fields (+4608 in 1/1024 s) are advanced in sub_1403A2774 with (int)(dt * 1024).

## Open questions

? which shader reads each field (only the layer pixel size and 1/size were matched by their formulas); ? what +4624..4647 of the target state hold.
