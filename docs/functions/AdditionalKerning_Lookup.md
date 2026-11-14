# AdditionalKerning_Lookup

- **Address:** `0x1403BA2D4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `float *AdditionalKerning_Lookup(AdditionalKerning *t, float out[3], unsigned __int16 leftGid, unsigned __int16 rightGid)`
- **Callers:** SDFFont_GetKerning
- **Callees:** sub_1403BA3A4 (builds the table)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Looks up the (left, right) glyph pair in the .ker table's std::map and returns its extra (x, y) kerning (0 when missing); builds the map first when it is dirty.

## Behavior

- V: when byte t+184 (dirty) is set: sub_1403BA3A4(t) builds the map and the byte is cleared.
- V: out+4 (qword) = 0; out[0] = out[1] = rightGid. Key = rightGid + (leftGid << 16). Walks the red-black tree rooted at t+208: nodes with byte +25 == 0 are real; dword +28 is the key; keys >= wanted go left, others right. When found (not the head and key not larger): out+4 += float at node+36 (x) and out+8 += float at node+40 (y).

## Referenced by

- Called by: [SDFFont_GetKerning](SDFFont_GetKerning.md)

## Notes

Name proposed (IDB: sub_1403BA2D4). Documented in fonts.md as table B; shipped .ker files are empty so the lookup always misses in retail data.

## Open questions

-
