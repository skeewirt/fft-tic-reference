# SceneUnit_LoadExtraPage

- **Address:** `0x14026C2E8`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `int SceneUnit_LoadExtraPage(uint8_t *sceneUnit, int page, int slot)`
- **Callers:** sub_14026CAA4
- **Callees:** VramPage_CopyRect, sub_1400CB5B4, sub_14025FE14

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Gives a scene unit one of the two extra sprite pages for its second-sheet frames (special poses such as a punch) and points that page's HD sheet slot at the unit's second sheet entry.

## Behavior

- V: with graphics level 2.0 or more and the dword at 0x142E7FC88 non-zero: when the scene unit's sprite byte (+0xA) has an HD entry e (the HD entry table, not -1), slot 11 + page (0x142E7FE98) = 0 and slot 16 + page (0x142E7FEAC) and the dword at 0x142E7FEF4 + 4 * page = e + 1, the second sheet of the pair.
- V: otherwise (classic graphics) it copies the unit's classic frames into the page with VramPage_CopyRect.
- V: then the page owner (0x140CE3260 + 0x7CE8 * page) = scene unit byte +8 | 0x80, and the page's in-use words are set.
- V: caller sub_14026CAA4 (per frame) looks for a page whose owner's low 5 bits are the unit's; with none it takes a free page (owner 255).
- V (seen live 2026-11-17): a resumed battle restores slot 16 from the save (g_HdSheetEntryBySlot 13..28 come from the payload), so it names the second sheet of the unit that last used page 0 while every page owner reads 255.
- V (seen live 2026-11-17): the sprite byte decides the second sheet: a scene unit whose byte read 0 left slot 16 as it was (another unit's entry), and the HD layer drew that unit's second-sheet pieces in its colours.
- V (seen live 2026-11-24): a scene unit of sprite 50 (HD entry 910) whose byte read 0 took extra page 0 for a casting pose in a resumed battle while slot 16 held 1069, the second sheet of sprite 134 (HD entry 1068): the pose drew as a block of that sheet's pieces for the whole cast, and slot 16 still read 1069 afterwards. With the byte at 50 the same cast drew the unit's own frames. Sprite 0 has HD entry -1, so the three stores are skipped; with slot 16 at -1 instead, nothing is drawn for the pose.

## State touched

- Calls: [VramPage_CopyRect](VramPage_CopyRect.md)

## Referenced by

- Observed behaviours: [ClassicLookDataHasEightBufferPlaces](../behaviors/ClassicLookDataHasEightBufferPlaces.md)

## Notes

Slot 16 + page is read by the battle sprite draw (sub_140260CF0, the page-4 path) as the entry of the extra page; a draw that finds it -1 sets it lazily from the drawn object's sprite byte.

## Open questions

? what the dword at 0x142E7FC88 stands for (a video mode: 2 picks the copy branch too).
