# HdQuad_SheetRect

- **Address:** `0x14041AC00`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `void HdQuad_SheetRect(uint16_t *quad, int rect[4])`
- **Callers:** HdLayer_ResolveQuadTexture
- **Callees:** log2f, floorf, powf

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Turns a battle HD draw quad's four UV pairs into the sheet rectangle its texture piece is cut from, and makes the quad's UVs relative to that piece.

## Behavior

- V: the UV pairs are the quad's u16 words 0/1, 8/9, 16/17 and 24/25; the rectangle is x = 2 x the smallest u, y = 2 x the smallest v (HD pixels, twice the classic coordinates), and the width and height are 2 x the spans rounded up to powers of two (at least 1).
- V: the quad's UVs are rewritten to 0 or the doubled span, keeping which corner is which (a mirrored quad stays mirrored).

## Referenced by

- Called by: [HdLayer_ResolveQuadTexture](HdLayer_ResolveQuadTexture.md)
- Observed behaviours: [HeldWeaponsDrawFromOneSheetPageByAByteRow](../behaviors/HeldWeaponsDrawFromOneSheetPageByAByteRow.md)

## Notes

Behavior: HeldWeaponsDrawFromOneSheetPageByAByteRow.

## Open questions

None recorded.
