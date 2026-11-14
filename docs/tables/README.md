# Tables

Where the game keeps its data tables, NXD files and the fixed tables inside the executable: what each holds, how it is keyed, how big its rows are, and which code reads it. Describes the tables; it does not reproduce their contents.

60 records. Format of a record: [kinds/table.json](../../kinds/table.json). Data: [data/tables.jsonl](../../data/tables.jsonl).

| Name | Storage | NXD table id | Rows | Summary |
|---|---|---|---|---|
| [Ability](Ability.md) | NXD file | 39 |  | The ability rows the game reads through AbilityTable_GetRow, loaded lazily and cached. |
| [AbilityActionRecords](AbilityActionRecords.md) | Executable |  | 368 records of 20 bytes (ids 0..0x16F) | The action record of each action ability, copied into a writable table on first use. |
| [AbilityAux](AbilityAux.md) | Executable |  | 8 bytes per id, ids 0..511 | The per-ability auxiliary records: classic JP cost, learn percent and two flag fields, with an extra category-specific record for each id. |
| [AbilityKind1_ItemByAbility](AbilityKind1_ItemByAbility.md) | Executable (constant) |  | 14 entries of 1 byte | The Item-command table: 14 bytes, ability 368 + i maps to item 240 + i (items 240..253). |
| [AbilityKind2_ThrowCategory](AbilityKind2_ThrowCategory.md) | Executable (constant) |  | 12 entries of 1 byte | The Throw table: 12 equip-category bytes, ability 382 + i maps to one category. |
| [BattleRangeMarks](BattleRangeMarks.md) | Executable (filled at run time) |  | 2560 entries of 1 byte | Range-mark array: 512 records of 5 bytes, index x + y * width + 256 * layer (layer 1 at +0x500). |
| [BattleTiles](BattleTiles.md) | Executable (filled at run time) |  | 512 records of 8 bytes | The battle map tile table: flags and movement cost per tile, filled by the map setup from the map's level record. |
| [BattleUnits](BattleUnits.md) | Executable (filled at run time) |  | 21 records of 512 bytes | The live battle unit table: hit points, magic points, tile, facing, charge time and action words. |
| [C_Mes_Id_Sample](C_Mes_Id_Sample.md) | NXD file | 172 |  | The battle message text table: CMesId_GetText reads one row by message id and the registry result is cached in g_CMesIdTable. |
| [CharaRectSizeTable](CharaRectSizeTable.md) | Executable (constant) |  |  | Width and height of a frame rectangle by its size code, in 8-pixel units (width at 2 * code, height at 2 * code + 4 words): read by CharaRender_DrawFrame. |
| [ChargeMotionPairs](ChargeMotionPairs.md) | Executable (constant) |  |  | 2 bytes per charge type of g_AbilityAnim: +0 the motion sub_140206C14 sets, +1 the motion BattleAnim_SetChargeMotion sets (each + 1; 0 = none) |
| [ClutFadeStep32](ClutFadeStep32.md) | Executable (constant) |  | 63 rows of 32 entries of 1 byte | Step table of the 32-step palette fade, same layout. |
| [ClutFadeStep8](ClutFadeStep8.md) | Executable (constant) |  | 63 rows of 8 entries of 1 byte | Step table of the 8-step palette fade: row = distance + 31, entry = how far the channel moves on that step; the entries of a row add up to the distance. |
| [CommandKind](CommandKind.md) | Executable (constant) |  | 256 entries of 1 byte | Command id to command kind: index 6 is 1 (Item), index 20 is 2 (Throw), and the battle range and action builders switch on the value. |
| [ErrandActive](ErrandActive.md) | Executable memory (saved with the game) |  | 8 rows of 9 entries of 1 byte | The eight active errand slot records, nine bytes each: flags, errand id, town and the three dispatched unit ids. |
| [ErrandDelay](ErrandDelay.md) | Executable memory (saved with the game) |  | 96 entries of 1 byte | The per-errand delay byte, one per errand id 0..95, saved with the game. |
| [FaceG2dEntryByFace](FaceG2dEntryByFace.md) | Executable (constant) |  | 206 entries of 4 bytes | g2d (pack) entry number per face number 0..205 for the HD layer (row 0 -1, rows 155..158 -1); four readers, each bounding the face with 0xCD. |
| [FastForwardMultipliers](FastForwardMultipliers.md) | Executable (constant) |  | 3 entries of 4 bytes | Game steps per displayed frame by fast-forward level: 1, 3, 5 (GlobalWork_GetSpeedMultiplier). |
| [FastForwardStates](FastForwardStates.md) | Executable (filled at run time) |  | 256 bytes | Whether fast-forward is allowed in each battle state; filled from the GameModeTypes NXD table. |
| [GameModeTypes](GameModeTypes.md) | NXD file | 88 |  | Per game-mode flags. |
| [GUIFontSlots](GUIFontSlots.md) | Executable (filled at run time) |  | 18 records of FontSlot | Per-UIFontType render slots (16 B each): byte +145 'loaded', signed byte at 16*(id+9) = renderer font slot. |
| [HdSheetEntryBySlot](HdSheetEntryBySlot.md) | Executable (filled at run time) |  | 30 entries of 4 bytes | HD sheet first-entry numbers per sheet slot; unit slots 20 to 28 follow pool index 0 to 8 and index 29 belongs to pool index 9; -1 means not set. |
| [HdSheetGroups](HdSheetGroups.md) | Executable (filled at run time) |  | 20 records of HdSheetGroup | The battle HD layer's 20 sheet groups (21144 bytes each): one sheet entry and up to 128 textures per group. |
| [HdSlotClut](HdSlotClut.md) | Executable (filled at run time) |  | 379 entries of 2 bytes | Palette id of each single-texture slot of the battle HD layer. |
| [HdSlotEntry](HdSlotEntry.md) | Executable (filled at run time) |  | 379 entries of 4 bytes | Sheet entry of each single-texture slot of the battle HD layer (-1 none): the cache key of HdLayer_BuildTextures with g_HdSlotClut. |
| [InventoryCounts](InventoryCounts.md) | Executable memory (saved with the game) |  | 261 entries of 1 byte | The party's inventory: one count per item id 0..260, saved with the game. |
| [Item](Item.md) | NXD file | 45 |  | The item rows (the Item-en table), read through ItemTable_GetRow and ItemTable_GetRowById and used by the text resolver for the category 'Item'. The item records the game keeps in the executable are a separate table. |
| [ItemAttributes](ItemAttributes.md) | Executable |  | 85 rows of 26 bytes | The equipment attribute records: stat bonuses, move and jump bonuses, status bytes and elements. |
| [ItemNewFlags](ItemNewFlags.md) | Executable memory (saved with the game) |  | 261 rows of 2 entries of 1 byte | Two flag bytes per item id 0..260, set at a new game; I: the shop 'new item' badges (byte 1 cleared when the item is first sold, byte 0 when it is first obtained). |
| [ItemRecords](ItemRecords.md) | Executable |  | 261 records of 12 bytes | The item records the executable keeps for equipment and chemist data: ids 0..255 in one block, ids 256..260 in a second block of five. |
| [ItemShopMask](ItemShopMask.md) | Executable (constant) |  | 512 entries of 1 byte | Which shops sell which item: two bytes per item id 0..0xFF, a mask word whose bit for shop s is 0x8000 >> s. |
| [Job](Job.md) | NXD file | 46 |  | The job rows (the Job-en table), read through JobTable_GetRow. |
| [JobAbilityPairList](JobAbilityPairList.md) | Executable (constant) |  |  | 146 entries of 8 bytes (word 0 = job, word 1 = skillset or ability id, words 2..3 unused by the producers); a list ends at the entry whose word 1 is 0xFFFF. sub_14000E114 initialises all 146 (0, 0xFFFF). |
| [JobCommand](JobCommand.md) | NXD file | 41 |  | The job command rows (the JobCommand-en table), read through JobCommandTable_GetRow. |
| [JobNeedLevelRows](JobNeedLevelRows.md) | Executable (constant) |  |  | 12 B/row; row r = requirement for job index r+1 (nibble-packed required job levels). |
| [JobTable](JobTable.md) | Executable |  | 174 rows of 49 bytes | The stock job table: skillset, growth, statuses, elements and two script bytes. |
| [LookPool](LookPool.md) | Executable (filled at run time) |  | 15 records of LookPoolRecord | The 15 look pool records (stride 0x32D6); byte +0 is the claim, byte +1 the sprite low byte. |
| [LookPoolFaceValue](LookPoolFaceValue.md) | Executable (filled at run time) |  | 10 entries of 4 bytes | Battle face value per look pool record 0..9: sub_14026E838 stores the scene unit's sprite byte; cleared to -1 by sub_140210AF0, saved and restored by sub_140304BEC; ten readers use it as a face number behind the 0xCD ... |
| [MonsterFaceIndexByJob](MonsterFaceIndexByJob.md) | Executable (constant) |  | 48 entries of 4 bytes | Face record index per monster job 94..141 (values 62 to 77, three jobs per family); Unit_GetFaceIndex reads it through the virtual base 0x140715378, 392 bytes inside the HD sheet entry table before it (2026-11-08). |
| [MoveBlockers](MoveBlockers.md) | Executable (filled at run time) |  | 112 entries of 1 byte | Up to 16 entries of 7 bytes, one per other unit on the map (record MoveBlockerRecord); an unused entry has id 0xFF. |
| [MoveTerrainCost](MoveTerrainCost.md) | Executable (filled at run time) |  | 64 entries of 1 byte | Movement cost per terrain type for the unit being built (0xFF = cannot enter), copied by Battle_MoveRangeSetup from one of the six sets of g_MoveTerrainCostSets and adjusted for weather and abilities. |
| [MoveTerrainCostSets](MoveTerrainCostSets.md) | Executable (constant) |  | 6 rows of 64 entries of 1 byte | Six constant cost sets by terrain type: walking, open (Fly / Teleport), float, water (two modes), one more water mode, lava walking. |
| [MoveTileFlags](MoveTileFlags.md) | Executable (filled at run time) |  | 512 entries of 1 byte | Per-tile flag byte of the move-range builder: 0x01 frontier, 0x02 one-axis slope, 0x04 occupied, 0x08 unit that can be stepped onto, 0x10 standable, 0x20 mountable ally, 0x40 steep, 0x80 blocked. |
| [PoachCount](PoachCount.md) | Executable memory (saved with the game) |  | 97 entries of 1 byte | Poach count per type, 97 bytes based at the badge block plus 522; the poach add routine clamps each byte to 99. |
| [PoachersDenStock](PoachersDenStock.md) | Executable memory (saved with the game) |  | 261 entries of 1 byte | Poachers' Den stock: one count per item id 0..260 (PoachersDen_AddStock adds to it, clamped 0..255); the shop list builder Shop_BuildItemList lists the ids with stock when the shop id is 100 or above. |
| [PoachItem](PoachItem.md) | NXD file | 236 |  | The poach rows (the PoachItem-en table), read through PoachTable_GetRowById. |
| [PoachNewFlags](PoachNewFlags.md) | Executable memory (saved with the game) |  | 97 entries of 2 bytes | Two new-flag bytes per poach type at the badge block plus 813; a new game fills them with 0x0101 and the badge routine clears the high byte. |
| [PoachOrder](PoachOrder.md) | Executable memory (saved with the game) |  | 97 entries of 1 byte | The player-visible order of collected poach types, 97 bytes at the badge block plus 619; maintained together with the sort list. |
| [PoachSort](PoachSort.md) | Executable memory (saved with the game) |  | 97 entries of 1 byte | The user reordering of the poach types, 97 bytes at the badge block plus 716. |
| [PortraitCodes](PortraitCodes.md) | Executable (constant) |  | 211 entries of 2 bytes | The portrait code words, one per portrait number. |
| [ReactionGates](ReactionGates.md) | Executable |  | 32 bytes | One byte per reaction id: the reaction executor refuses an id whose byte has 1 in its low two bits. |
| [RuntimeJobList](RuntimeJobList.md) | Executable (filled at run time) |  |  | uint16[48]: job id (low 13 bits) \| 0x2000 locked \| 0x4000 released by another member (mode 3) / current (mode 2); 0xFFFF ends it. |
| [SceneTaskSlots](SceneTaskSlots.md) | Executable (filled at run time) |  | 1512 entries of 1 byte | Nine scene-task data records of 0xA8 bytes, parsed from u16 token streams during the battle map setup and captured in a kind-1 snapshot. |
| [SceneUnitSlots](SceneUnitSlots.md) | Executable (filled at run time) |  | 16 records of SceneUnitSlot | The 16 scene-unit records (stride 0x548); the in-use dword is 8 bytes before each. |
| [StatusGroupMasks](StatusGroupMasks.md) | Executable (constant) |  | 10 rows of 5 entries of 1 byte | The ten party-wide status group masks, five bytes each: a group test ANDs these bytes against the unit status bytes at +0x61..+0x65. |
| [StatusIconFlags](StatusIconFlags.md) | Executable (constant) |  |  | The per-status flag words the status panel update reads: index status+1, no bound check. |
| [TextPools](TextPools.md) | Executable (filled at load) |  | 32 pointers | The thirty-two text pool pointers the generic text decoder indexes by a text id's kind bits. |
| [UnitEquipOverride](UnitEquipOverride.md) | Executable (filled at run time) |  |  | Five override equipment words per unit, ten bytes per unit index: when the pair is non-zero the equip pickers use it in place of the unit record's own hand words. |
| [UnitLookPoolIndex](UnitLookPoolIndex.md) | Executable (filled at run time) |  | 21 entries of 4 bytes | Look pool index of each battle unit by its unit index (+444): written by sub_14026EB74 when it builds the unit's scene unit, read back by it on the resume path (load mode 1) and by sub_1401D46B0; inside the battle sna... |
| [UnitSceneSlotIndex](UnitSceneSlotIndex.md) | Executable (filled at run time) |  | 21 entries of 4 bytes | Scene-unit slot of each battle unit by its unit index (+444), -1 none: written by sub_14026EB74 (a slot taken by another unit clears that unit's entry) and sub_14026A048, cleared by sub_140210AF0, read on the resume p... |
