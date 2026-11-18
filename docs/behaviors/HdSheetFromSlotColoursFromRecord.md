# HdSheetFromSlotColoursFromRecord

- **Kind:** observed behaviour
- **Scope:** engine (Enhanced battle sprite)
- **Area:** [Graphics](../areas/graphics.md)
- **Affects:** [HdLayer_BindSheetTexture](../functions/HdLayer_BindSheetTexture.md), [HdLayer_BuildTextures](../functions/HdLayer_BuildTextures.md), [SceneUnit_BuildFromQueueEntry](../functions/SceneUnit_BuildFromQueueEntry.md), [sub_140260CF0](../functions/sub_140260CF0.md), [g_HdSheetEntryBySlot](../globals/g_HdSheetEntryBySlot.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

In Enhanced a pool's HD sheet comes from its sheet slot (the g2d entry) while its colours come from the pool record's palette.

## Behavior

- I: seen live 2026-11-13: a goblin record holding another unit's palette drew the goblin sheet in that unit's colours (the sheet slot held the goblin's entry 1070).
- V: g_HdSheetEntryBySlot (0x142E7FE6C, 30 dwords) holds the g2d entry of each HD sheet slot, -1 = not set; look pool p (0..9) uses slot 20 + p: SceneUnit_BuildFromQueueEntry (0x14026F047 / 0x14026F020) writes hd_entry_by_shape[sprite] there when the sprite is in range and its entry is not -1; sub_140260CF0 fills a slot that is -1 from the scene unit's sprite byte at its next draw.
- V: HdLayer_BindSheetTexture binds the HD texture ids of pool sheets (123 + 16 p + frame) to dword_142E7FEBC[p] (= slot 20 + p); HdLayer_BuildTextures loads an entry that differs from the slot's loaded one with PackFile_ReadEntry.
- V: PackFile_ReadEntry (0x1403D25D8) = PackEntry_Inflate(state, out, PackFile_EntryPtr(pack, n), size) with no test of n against the pack's entry count; the first access to the entry tests its flag byte +4 (0x1403D1EF0). An entry number past the pack faults there (seen live 2026-11-13).

## Open questions

None recorded.
