# HdSheetGroup_ClaimClutEntry

- **Address:** `0x14041E448`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `int HdSheetGroup_ClaimClutEntry(int group, int clut)`
- **Callers:** sub_140260CF0, EffectNxd_SelectPageTexture, sub_140311CB0, sub_14031DA24, sub_1403953D8
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the index (0..15) of the palette entry a battle HD sheet group keeps for a draw quad's CLUT word, claiming a free one when the word is new.

## Behavior

- V: the group is g_HdSheetGroups + 21144 x group; its 16 palette entries are 8-byte pairs at +2564 (the CLUT word, then a used flag).
- V: returns the index of the entry holding the word and sets its used flag; else takes the first entry whose word is -1, stores the word and sets the flag; returns 0 when all 16 hold other words.
- V: callers and the groups they pass: sub_140260CF0 (0 and 1 for sheet words 4 and 5, 18 and 19 for their alternates, 2 for word 9, 3 for word 11, word - 16 = 4..12 for words 20..28, 13 for word 17, 14 for word 30), EffectNxd_SelectPageTexture, sub_140311CB0 and sub_14031DA24 (14), sub_1403953D8.

## Referenced by

- Observed behaviours: [HdLayerUnitSheetsAreTenFixedGroups](../behaviors/HdLayerUnitSheetsAreTenFixedGroups.md)

## Notes

Behavior: HdLayerUnitSheetsAreTenFixedGroups.

## Open questions

None recorded.
