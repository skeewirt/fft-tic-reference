# Camera_UpdateMatrices

- **Address:** `0x1403A5674`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 Camera_UpdateMatrices(Camera *cam)`
- **Callers:** vtable faith::Graphics::Object::Camera (slot 0x140720AF8), called each frame by the scene update
- **Callees:** sub_1400AE0C0, sub_1403BFCD4, sub_1403BFEDC, sub_1403BFFDC, sub_1400AD6E8, sub_1400AF784, sub_1403C2390, sub_1403C0994, tanf, Camera_UpdateSecondaryView

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Per-frame update of a render camera (vftable faith::Graphics::Object::Camera slot at 0x140720AF8): rebuilds its view matrix, projection matrix, view-projection matrix, inverses, and sets a 'changed' flag when anything moved.

## Behavior

- V: cam+16 is the camera's scene node (position / orientation read by sub_1400AE0C0 and sub_1403BFCD4); cam+24 selects the render target slot (renderer qword_143CDA098 + 6584 byte index, then the 4-entry table at +56) whose byte +4652 ('idle') drives the dirty logic: bytes cam+3343 (changed), +3344 (previous idle), +3345 (may-compare), +3339, +3732 (force-dirty request set by sub_1403A2774 from the frame update).
- V: every matrix is stored as 12 floats in 16-float slots (the 4th column is skipped when copying) and compared with the previous value by sub_1403BFEDC, which is true when |a - b| <= 1.1920929e-7 (FLT_EPSILON) for the 12 elements; any difference ORs 1 into cam+3343 (only when cam+3345 is set). The position (cam+32..40) is compared the same way.
- V (projection, cam+112..172, row-major 4x4 floats at idx 0, 5, 10, 11, 14, 15): fov = cam+3284 (radians), aspect = cam+3288, near = cam+3292, far = cam+3296, ortho size = cam+3300, flags cam+3332 (reverse depth), cam+3333 (orthographic), cam+3346 (finite far). Orthographic: m00 = 2 / (S * aspect), m11 = 2 / S (S = cam+3300), m22 = 1 / (far - near) (negated and m32 = -near / (far - near) when reverse depth), m33 = 1.0. Perspective: m11 = 1 / tan(fov / 2) (tanf), m00 = m11 / aspect, m23 = -1.0, depth terms from far / (far - near) when cam+3346 is set, else the infinite-far form m22 = 0 (or -1 reversed), m32 = -near.
- V: view = the 12-float block at cam+48 filled by sub_1403BFCD4 from a constant 4x3 identity template (dword_140906C60..C98) and the camera node; viewProj at cam+176 = sub_1400AD6E8(view, proj) ; inverse of the view at cam+240 (sub_1403BFFDC); cam+304 / cam+368 hold sub_1403C2390 results (4x4 copies of the view/proj, ?); cam+848 gets a third matrix built from the negated translation of cam+288 (the world-to-camera of the translation part only, I); cam+432 receives sub_1403C0994(cam+112) (the projection's extra form, ?). It finishes by calling Camera_UpdateSecondaryView (sub_1403A5ECC).
- I: the orthographic branch is what the UI layers use; nothing here rounds or snaps a value to pixels, so a UI text quad is placed by the projection exactly as the float matrices give it.

## State touched

- Calls: [Camera_UpdateSecondaryView](Camera_UpdateSecondaryView.md)
- Reads: [g_Renderer](../globals/g_Renderer.md)

## Notes

The name is ours (IDB: sub_1403A5674). Runs once per frame per camera, not per glyph. The flag meanings of +3332 / +3333 / +3346 are inferred from which maths branch they select (reverse depth, orthographic, finite far).

## Open questions

? which camera / which of the 4 render targets the Job Tree uses and its ortho size (S); ? the exact roles of cam+304 / +368 / +432 / +848; ? what sets +3732.
