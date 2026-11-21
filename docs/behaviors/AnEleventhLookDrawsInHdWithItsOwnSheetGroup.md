# AnEleventhLookDrawsInHdWithItsOwnSheetGroup

- **Kind:** observed behaviour
- **Scope:** engine (battle unit looks, Enhanced HD)
- **Area:** [Graphics](../areas/graphics.md)
- **Affects:** [sub_140260CF0](../functions/sub_140260CF0.md), [SceneUnit_BuildFromQueueEntry](../functions/SceneUnit_BuildFromQueueEntry.md), [HdSheetGroup_ClaimClutEntry](../functions/HdSheetGroup_ClaimClutEntry.md), [g_HdSheetEntryBySlot](../globals/g_HdSheetEntryBySlot.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Look pool 10 draws correctly in HD as soon as it has a sheet group of its own: the scrambled image of looks past the 10th is only the shared sheet word, and nothing else in the HD path stands in the way.

## Behavior

- V (code): sheet word 30 draws through HD sheet group 14 and claims its palette entry through HdSheetGroup_ClaimClutEntry (id 0x2823 + entry), like the unit words; its case writes a fixed sheet entry (0x9E) into g_HdSheetEntryBySlot slot 30 on every draw (0x140261918, immediate at +6); group 14 serves sprite 158 only.
- V (tested 2026-11-21, random battle at Mandalia Plain, 11 enemy looks, no sprite 158 present): with that immediate changed in memory to pool 10's entry (tbl_SpriteHdEntryByShape[144] = 1088) and pool 10's scene unit sheet word (+0x14) changed from 17 to 30, the Dryad of pool 10 drew correctly in HD at once, and after it walked in the enemy phase; the other units were unchanged and Ramza in pool 11 still drew from pool 9's sheet (the control); the word, the entry and the face slot stayed put over an enemy phase, and no fault was recorded.
- I: so a build gives each look past the 10th a sheet group of its own (new groups in our memory, as in HdLayerUnitSheetsAreTenFixedGroups); borrowing group 14 was a test aid only, since sprite 158 needs it when present.

## Open questions

None recorded.
