# Camera_UploadSceneConstants

- **Address:** `0x1403A6240`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `_OWORD *Camera_UploadSceneConstants(Camera *cam, RenderTargetState *target)`
- **Callers:** vtable faith::Graphics::Object::Camera (slot 0x140720B00)
- **Callees:** sub_1400AE0C0, sub_1400AF420, sub_1400AD6E8, sub_1403BFEDC, sub_1403BFFDC, sub_1403C043C, sub_1403C19A8, sub_1403C1E1C, sub_1403C00F4, sub_1403C0E70, sub_1403C2390, sub_140028B10, sub_14003E120, sub_14003E228, memmove

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Second camera vtable function (0x140720B00): updates the camera-relative origin, the double-buffered matrix history, and writes the 1040-byte scene constant block (matrices current and previous) into a mapped GPU constant buffer.

## Behavior

- V: copies 12 floats from target+848.. (dwords a2[212..226]) to cam+3544 and flags a change (FLT_EPSILON compare, sub_1403BFEDC) when different; the same compare is done for the origin triple at cam+3672 (from *(rdx+288..296)) and the camera node position cam+16 +64..72.
- V (camera-relative translation): d = nodePos(+64,+68,+72) - cam+3672 (origin offset); the translation columns written to cam+3656.. are d (float subtraction), so rendering is done relative to a re-based origin (keeps float precision).
- V: the byte pair cam+3340 / +3341 / +3342 is a double buffer (current / previous matrix set): when the target is not idle (target+4652 == 0), anything changed, or cam+3733 is set, the index is toggled (3341 = old 3340, 3340 ^= 1, 3342 = new). Matrices are stored in 1040-byte records at cam+1168 + 1040 * index (view, viewProj, projection, their inverses, previous-frame forms, light / shadow direction from cam+80..88 via sub_140028B10 (a vector normalise, I) and the extra 128-byte block from sub_1403C0E70 at +2000).
- V: finally maps the camera's constant buffer (sub_14003E120(*(cam+3248), mode 2) = write-discard map), copies both 1040-byte records (current at +0, previous at +520), appends sub_1403C043C-transposed 4x4s at +2080 / +2144 (cam+3352 and cam+3480 matrices), and unmaps (sub_14003E228).
- I: the transposes (sub_1403C043C) are the row-major to HLSL column-major conversion for the matrices uploaded to the shader.

## State touched

- Reads: [g_Renderer](../globals/g_Renderer.md)

## Notes

The name is ours (IDB: sub_1403A6240). Pure per-frame camera upload; the ~900 line decompile was read for structure and the constants above, the matrix algebra of each 4x4 (which order, which transpose) was not followed element by element.

## Open questions

? the layout of the 1040-byte scene record (which offset is view, projection, jitter); ? whether any jitter / sub-pixel offset is added to the projection (none was seen in these functions); ? the Job Tree camera's origin offset.
