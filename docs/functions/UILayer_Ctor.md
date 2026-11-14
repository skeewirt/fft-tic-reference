# UILayer_Ctor

- **Address:** `0x1403B0494`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 UILayer_Ctor(UILayer *a1)`
- **Callers:** UIRenderer setup
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Initialises a 592-byte UI layer object (the offscreen-layer record) to its defaults.

## Behavior

- V: sets the UILayer vtable, ids -1, colour multiplier +88..+100 = 1, effect flag bytes +176 / +177 / +178 and the effect floats to their defaults (+180 = 1.0, +204 = 1.0, +464 = 0, colour +468..+476 = 1.0, mode dword +480 = 3), opacity +552 = 1.0.
- V: the layer record offsets quoted for GUILayer_BuildRecord are relative to this object + 24 (object base = r + 303480 + 592 * i): glow enable +178, strength +200, radius +204, colour +468..+476, mode +480.

## State touched

- Writes: [GUILayer.index](../structs/GUILayer.md#index), [GUILayer.sort_lo](../structs/GUILayer.md#sort_lo), [GUILayer.sort_hi](../structs/GUILayer.md#sort_hi), [GUILayer.blend_mode](../structs/GUILayer.md#blend_mode), [GUILayer.tex_slot_a](../structs/GUILayer.md#tex_slot_a), [GUILayer.tex_slot_b](../structs/GUILayer.md#tex_slot_b), [GUILayer.offset_vectors](../structs/GUILayer.md#offset_vectors), [GUILayer.shadow_strength](../structs/GUILayer.md#shadow_strength), [GUILayer.shadow_radius](../structs/GUILayer.md#shadow_radius), [GUILayer.shadow_offset](../structs/GUILayer.md#shadow_offset), [GUILayer.glow_strength](../structs/GUILayer.md#glow_strength), [GUILayer.glow_radius](../structs/GUILayer.md#glow_radius), [GUILayer.rect](../structs/GUILayer.md#rect), [GUILayer.atlas_offset](../structs/GUILayer.md#atlas_offset), [GUILayer.shadow_colour](../structs/GUILayer.md#shadow_colour), [GUILayer.glow_mode](../structs/GUILayer.md#glow_mode)

## Notes

Constant delta 24 between the BuildRecord page offsets and the object offsets (154 -> 178, 176 -> 200, 180 -> 204, 444 -> 468, 456 -> 480).

## Open questions

None recorded.
