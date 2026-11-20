# LookQueue_Add

- **Address:** `0x1403041A4`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `void LookQueue_Add(char a, char b, char c, int16_t d, int16_t sprite, int16_t palette, int16_t slotRequest, void *unit, int flag)`
- **Callers:** Battle_BuildRosterTeam, Battle_AddJoinedUnit, Battle_PlaceEntryUnits, sub_1402730C4, ScenePreview_ShowEntry
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Appends one entry to the 16-entry look load queue that CharaPalette_ReloadForShape later turns into scene units.

## Behavior

- V: writes the nine arguments into the entry at the current count (entry n is at 0x141856720 + 8 + 32 * n; the count is the dword at 0x141856720).
- V: the sprite argument is stored as a 16-bit word at entry +6; a signed value of 170 (0xAA) or more is replaced by 1 right after (the compare at 0x140304207).
- V: the count is increased only while it is below 16, so the 17th call overwrites entry 16 and the count stays 16.
- M (unicorn, pristine exe, empty queue; the values are arguments fed in, not constants of the code): the stored word for the sprite argument 0, 1, 169 is itself; 170, 200, 254, 255, 256 and 0x7FFF become 1; 0x8000 and 0xFFFF stay (the compare is signed).
- M (unicorn, Unit_ResolvePreviewShape for every marker x job): 10,320 of the 65,536 pairs give a shape of 170 or more (Unit_ResolvePreviewShape's markers above 0x82 with jobs from 130, its markers 0x80 / 0x81 with jobs below 43; no generic job 74..93), so the clamp is reachable by stock data.

## Referenced by

- Appears in flows: [ScriptedBattleUnitsFromEntries](../flows/ScriptedBattleUnitsFromEntries.md)
- Called by: [Battle_AddJoinedUnit](Battle_AddJoinedUnit.md), [Battle_PlaceEntryUnits](Battle_PlaceEntryUnits.md), [ScenePreview_ShowEntry](ScenePreview_ShowEntry.md)
- Observed behaviours: [BattlePaletteSourceByLookRange](../behaviors/BattlePaletteSourceByLookRange.md), [LookSlotsAlreadyInTheGame](../behaviors/LookSlotsAlreadyInTheGame.md), [SceneUnitShapeIsTheQueueWord](../behaviors/SceneUnitShapeIsTheQueueWord.md)

## Notes

Structure: LookQueueEntry. The name is ours (IDB: sub_1403041A4). The clamp at 0x140304207 is a ceiling: the queue feeds the battle's byte-wide stores.

The function is a leaf: at the point after the clamp's store (0x140304222) the sprite argument is at rsp+0x28 and the unit pointer at rsp+0x40, r10 = &g_LookQueueCount and rcx the entry index.

## Open questions

? whether any caller can queue more than 16 entries.
