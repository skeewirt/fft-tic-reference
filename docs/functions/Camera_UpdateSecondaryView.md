# Camera_UpdateSecondaryView

- **Address:** `0x1403A5ECC`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `void Camera_UpdateSecondaryView(Camera *cam)`
- **Callers:** Camera_UpdateMatrices (0x1403A5E88), vtable data slot 0x143D40030 (CFG table)
- **Callees:** sub_1400AE0C0, sub_1400AF420, sub_1403BFEDC, sub_1400AD6E8, sub_1403BFFDC

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Tail of Camera_UpdateMatrices: builds the second view (the one belonging to the render target object at target+32), its view-projection and inverse, with the same epsilon dirty tracking.

## Behavior

- V: reads the target object (renderer +6584 index, table at +56), takes its node at target+32 (sub_1400AE0C0), negates the three translation floats (v67..69 * -1.0), multiplies it with the camera view cam+48 (sub_1400AF420) and stores the 12 floats at cam+656; compares with the previous copy (sub_1403BFEDC) and ORs the changed flag into cam+3343 when cam+3345 is set.
- V: cam+720 = sub_1400AD6E8(thatView, cam+656, proj cam+112) (view-projection of the second view); cam+784 = sub_1403BFFDC(cam+656) (its inverse), again compared with the previous values.

## State touched

- Reads: [g_Renderer](../globals/g_Renderer.md)

## Referenced by

- Called by: [Camera_UpdateMatrices](Camera_UpdateMatrices.md)

## Notes

The name is ours (IDB: sub_1403A5ECC). Every operation is whole-frame matrix maths, nothing per glyph.

## Open questions

? what the object at target+32 is (a second camera node, perhaps the previous-frame or the shadow view); sub_1400AF420 is read as a 4x3 multiply (I) but was not decompiled.
