# Rgb555ToRgba8888

- **Address:** `0x14041DC34`
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Prototype:** `_UNKNOWN **Rgb555ToRgba8888(const unsigned short *src, int keepSemi, int zeroFirst, unsigned int *dst, int count)`
- **Callers:** CharaRender_BuildAtlasTexture, sub_140415D30
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Converts PSX RGB555 palette entries to RGBA8888 the way the engine does: each 5-bit channel times 8 (max 248, NOT 255), alpha 0xFF (0x80 for a set bit 15 when keepSemi).

## Behavior

- V: R = (c & 31) * 8, G = ((c >> 5) & 31) * 8, B = ((c >> 10) & 31) * 8; alpha 0xFF000000 or 0x80000000; when zeroFirst is set dst[0] = 0 (colour 0 transparent).

## Referenced by

- Called by: [CharaRender_BuildAtlasTexture](CharaRender_BuildAtlasTexture.md), [HdLayer_BuildTextures](HdLayer_BuildTextures.md)
- Observed behaviours: [SixteenColourLimitIsTwoCpuBuilders](../behaviors/SixteenColourLimitIsTwoCpuBuilders.md)

## Notes

Tree Studio's extract_sprites uses this exact conversion (8 * c).

## Open questions

None recorded.
