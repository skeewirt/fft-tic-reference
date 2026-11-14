# CharaRender_FrameCacheUpdate

- **Address:** `0x1400CD22C`
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Prototype:** `__int64 CharaRender_FrameCacheUpdate(CharaRenderState *r, int *request)`
- **Callers:** CharaAnim_Step
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Keeps the 44-byte frame cache entry of a slot in step with the current request (shape, palettes, frame, flags): a changed request invalidates the atlases or the whole frame.

## Behavior

- V: entry = r + 47152 + 44 * id: flags (+0, bit 0 = valid, bit 1 = atlases built, bit 2 = drawn, bit 3 = LUT cell chosen), then copies of the request fields (shape +4, frame +8, flag word +12, shape id +16 ...).
- V: if the shape, frame, palette or flag fields differ, flag bits are reset (atlases kept when only the frame or flags changed: value 2 / 9 in the low flag bits); the request is copied into the entry and flag 1 is set.

## Open questions

Which request field each entry offset holds is only partly mapped (?).
