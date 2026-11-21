# HdQuad_CopyFromDrawQuad

- **Address:** `0x14025DB94`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 HdQuad_CopyFromDrawQuad(const void *quad, void *hd_quad)`
- **Callers:** sub_14025B1C4
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Copies a draw quad's colour bytes and, with enhanced graphics, its HD draw id and palette words into the quad record the battle HD layer reads.

## Behavior

- V: hd +72..+75 = quad +59, +60, +63, +68; hd +64 (the draw id) and +68 start at 0.
- V: with g_GraphicsLevel >= 2: the face ids (11111, 11112..11879) are copied when the HD face mode dword is set; with the HD mode dword set, the draw id ranges 10000..10050, 10051..10066, 10067..10082, 10339..10354, 10355..10370, 10083..10098, 10099..10114, 10115..10258, 10259..10274 and 10275..10290 are copied to hd +64, most with the quad's palette words (+52, +54) to hd +68 / +70.
- V: an id in none of these ranges leaves hd +64 at 0 (the quad is not drawn from an HD sheet); the test of word 17's range (0x14025DF68) compares id - 10259 with 15.

## Referenced by

- Observed behaviours: [WordSeventeensArithmeticReachesNewSheetGroups](../behaviors/WordSeventeensArithmeticReachesNewSheetGroups.md)

## Open questions

None recorded.
