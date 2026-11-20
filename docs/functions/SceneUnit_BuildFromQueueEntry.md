# SceneUnit_BuildFromQueueEntry

- **Address:** `0x14026EB74`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `SceneUnitSlot *SceneUnit_BuildFromQueueEntry(char a, char b, char c, int16_t d, uint16_t sprite, int16_t palette, int16_t slotRequest, void *unit, int flag, void *file)`
- **Callers:** CharaPalette_ReloadForShape
- **Callees:** LookPool_ClaimForSprite, sub_14027032C, sub_14026E838, sub_14026947C, SceneUnit_BuildPalette, SceneUnit_SetFlag12C, ItemSprite_LoadPalettes, NxdRegistry_Find, NxdTable_GetRowById, NxdEntry_GetRow

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the scene unit of one look queue entry: takes a scene-unit slot, claims the look pool record of the sprite, picks the palette row, loads the pool's palette and frames, sets the HD sheet slot and links the unit into the scene-object list; returns the scene unit or null.

## Behavior

- V: the arguments are the queue entry's fields (CharaPalette_ReloadForShape, pass 2) plus the classic file buffer.
- V: when the load mode dword at 0x142FF9E2C is 1 (the resume path) the scene-unit slot comes from g_UnitSceneSlotIndex[unit +444] and, after LookPool_ClaimForSprite, the pool index is replaced by g_UnitLookPoolIndex[unit +444]; a null unit or an index above 20 returns null.
- V: otherwise a slot request below 16 takes that slot (null when an in-use slot already carries that number or the slot is in use), else the first free one of the 16; the pool index from LookPool_ClaimForSprite(sprite) is stored into g_UnitLookPoolIndex[unit +444] and the slot into g_UnitSceneSlotIndex (another unit's entry naming the same slot becomes -1).
- V: writes the sprite's low byte to scene unit +0xA and the pool index to +9; a pool index of 0xFFFF frees the slot and returns null (the unit is not drawn).
- V: palette source: sprites 159..162 and 96..133 (the generic looks, tested as sprite - 0x60 <= 0x25) take unit byte +4 (the queue's palette word when there is no unit) with a limit of 5; every other sprite looks up its CharShape row (NXD 174, key = the sprite word): a non-zero colour override id at +12 gives sub_1401E3A10's answer with a limit of 16, else the queue palette with a limit of 5; scene unit +0xB = the value when below the limit, else 0.
- V: sprites 69 and 73 rewrite one byte of every battle unit (the loop walks 0x141853ECD, g_PreviewUnitTable + 493, in steps of 512): 1 -> 7 for 69, 7 -> 8 for 73.
- V: calls sub_14026E838 (palette, pool face value, frames) and sets the HD sheet slot word +0x14 = pool + 20 (17 from pool 9 up); with enhanced graphics and the HD mode dword set it copies hd_entry_by_shape[sprite] into g_HdSheetEntryBySlot[20 + pool] (pools 0..8) or dword_142E7FEE0 (pool 9) when it is not -1; pools 10..14 get no HD entry.
- V: stores the unit pointer at scene unit +0x148, links the scene unit at the head of qword_140D3A410 (except on the resume path when the slot was already in use) and loads the held item's palettes (ItemSprite_LoadPalettes).
- V: writes the scene unit's sprite byte +0xA from its sprite argument (bpl, 0x14026EDA0) and the pool index +9.
- V: in load mode 1 (resume) it calls LookPool_ClaimForSprite(sprite) but takes the pool index from g_UnitLookPoolIndex[unit +444] (0x14026ED8D), not from the claim; the scene slot comes from g_UnitSceneSlotIndex[unit +444] (0x14026ECB5; none -> no build), the in-use flag is tested (0x14026ECFB) and the record is not linked again when it was in use (the `!v87` test before `*v13 = qword_140D3A410`). In mode 0 it takes the scene slot named by its slot argument (refused when a slot with that id is in use) and links it.
- V: the queue entry layout: bytes +0 / +1 / +2 = x, y, layer, word +4 facing, +6 sprite, +8 palette, +0xA slot, qword +0x10 unit, dword +0x18 flag; the loader passes them in that order.

## State touched

- Calls: [LookPool_ClaimForSprite](LookPool_ClaimForSprite.md), [sub_14027032C](sub_14027032C.md), [sub_14026E838](sub_14026E838.md), [SceneUnit_BuildPalette](SceneUnit_BuildPalette.md), [SceneUnit_SetFlag12C](SceneUnit_SetFlag12C.md), [ItemSprite_LoadPalettes](ItemSprite_LoadPalettes.md), [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdEntry_GetRow](NxdEntry_GetRow.md)
- Reads: [g_UnitLookPoolIndex](../globals/g_UnitLookPoolIndex.md), [g_UnitSceneSlotIndex](../globals/g_UnitSceneSlotIndex.md), [g_SceneUnitSlots](../globals/g_SceneUnitSlots.md)
- Writes: [g_UnitLookPoolIndex](../globals/g_UnitLookPoolIndex.md), [g_UnitSceneSlotIndex](../globals/g_UnitSceneSlotIndex.md), [g_HdSheetEntryBySlot](../globals/g_HdSheetEntryBySlot.md)

## Referenced by

- Appears in flows: [BattleResumeRestoresTheLooks](../flows/BattleResumeRestoresTheLooks.md)
- Called by: [CharaPalette_ReloadForShape](CharaPalette_ReloadForShape.md)
- Observed behaviours: [BattlePaletteSourceByLookRange](../behaviors/BattlePaletteSourceByLookRange.md), [CharShapeRowsANewLookNeeds](../behaviors/CharShapeRowsANewLookNeeds.md), [HdSheetFromSlotColoursFromRecord](../behaviors/HdSheetFromSlotColoursFromRecord.md), [LookPoolOfFifteenIsWiredIntoFixedSlots](../behaviors/LookPoolOfFifteenIsWiredIntoFixedSlots.md), [LookSlotsAlreadyInTheGame](../behaviors/LookSlotsAlreadyInTheGame.md), [ResumeLoadsTheLookStateTwice](../behaviors/ResumeLoadsTheLookStateTwice.md), [SceneUnitShapeIsTheQueueWord](../behaviors/SceneUnitShapeIsTheQueueWord.md), [SixteenSceneUnitsComeOnlyFromTheLookQueue](../behaviors/SixteenSceneUnitsComeOnlyFromTheLookQueue.md), [SpriteTablesCanLiveInBlocksOf1300Rows](../behaviors/SpriteTablesCanLiveInBlocksOf1300Rows.md), [StatusVisualMasks](../behaviors/StatusVisualMasks.md)
- Reads tables: [NxdDataCharShape](../tables/NxdDataCharShape.md), [SpriteHdEntryByShape](../tables/SpriteHdEntryByShape.md), [SpriteLookAttributes](../tables/SpriteLookAttributes.md)

## Notes

Whole function read in the decompile (2026-11-08), written from scratch; it replaces the 2026-10-27 head-only sheet (whose purpose line called it a palette helper and the slot table a shape table). The HD entry bounds are at 0x14026F006 / 0x14026F02D and the attribute read is at 0x14026F452. The name stays the address.

## Open questions

? what sub_14027032C and sub_14026947C build; ? the meaning of the unit byte +493 rewrite for sprites 69 and 73.
