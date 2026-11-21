# Unit data

Unit save, work and party records, stat and growth computation, egg hatching and scripted battle entries.

Functions: 76, Structures: 4, Globals: 6, Registries: 3, Observed behaviours: 7, Tables: 1.

## Functions (76)

| Name | Address | Purpose |
|---|---|---|
| [Battle_BuildEntryUnits](../functions/Battle_BuildEntryUnits.md) | `0x14030428C` | Builds the battle units of the current battle from its 16 entries: fetches the entry block, lets the battle's OverrideEntryData rows overwrite the entries, then places the units. |
| [Battle_GetEntryBlock](../functions/Battle_GetEntryBlock.md) | `0x14028416C` | The 16 spawn entries (40 bytes each, 640 bytes) of the current battle inside the loaded entry data. |
| [Battle_PlaceEntryUnits](../functions/Battle_PlaceEntryUnits.md) | `0x14027128C` | Builds battle unit i (g_PreviewUnitTable + 512 x i) from entry i for the 16 entries of a battle, decides who is placed and queues each placed unit's look. |
| [CharaColorSkin_Resolve](../functions/CharaColorSkin_Resolve.md) | `0x1401E39BC` | Resolves a CharCLUT chara_color_skin value to the skin to use. |
| [CharaName_GetDisplayName](../functions/CharaName_GetDisplayName.md) | `0x1401E8B7C` | Returns the display name of a name key: the CharaName table's name, or the unit's own stored name string when the row says so. |
| [CharClut_GetColorSkin](../functions/CharClut_GetColorSkin.md) | `0x1401E3A10` | Reads the chara_color_skin column (+0x10) of the CharCLUT row (key, 0) and resolves it. |
| [GameState_ResetParty](../functions/GameState_ResetParty.md) | `0x140284500` | Resets the party-wide item state for a new game or a partial reset: the roster markers, the inventory counts, the Poachers' Den stock, the item badge block and the poach arrays, then the starting inventory and gil. |
| [Item_CanUnitEquip](../functions/Item_CanUnitEquip.md) | `0x1402886D0` | Answers whether a unit's job may equip an item, combining the job's equip-category bits with a small set of item ids the game special-cases. |
| [Item_CanUnitEquipPreview](../functions/Item_CanUnitEquipPreview.md) | `0x140396F1C` | The preview-record twin of the equip check: it decides whether the job shown in an equip preview could equip the candidate item. |
| [JobScreen_RefreshAfterChange](../functions/JobScreen_RefreshAfterChange.md) | `0x1402BD05C` | Refreshes the job/equip screen after a change: it copies the selected party record into the 0x1407B27xx record, the 0x141876E90 panel block and the 0x141876C80 tail record, then rebuilds the job list. |
| [OverrideEntry_FillUnitEntry](../functions/OverrideEntry_FillUnitEntry.md) | `0x1401EA638` | Copies one OverrideEntryData row into a 40-byte unit entry of a scripted battle: the fields whose row value is not the 'keep' marker overwrite the entry, and the flag bytes build a bit set. |
| [OverrideEntry_LoadBattleEntries](../functions/OverrideEntry_LoadBattleEntries.md) | `0x1401EA574` | Fetches the 16 pre-placed unit entries of one scripted battle from OverrideEntryData (nxd table 96) and converts each row into a 40-byte unit entry. |
| [Party_EggUpkeep](../functions/Party_EggUpkeep.md) | `0x140289900` | Per-step upkeep of monster eggs over the 54 save slots: counts down existing eggs and hatches them, and may also create a new egg from a monster that carries an Egg key. |
| [Party_GetSlotState](../functions/Party_GetSlotState.md) | `0x140289298` | Returns the availability state of one party slot: usable, absent, blocked or a special job, as a small signed code. |
| [Party_GetSlotStateSpecial](../functions/Party_GetSlotStateSpecial.md) | `0x140289320` | Wrapper around the party slot check that replaces the usable result with the special-job code for jobs 161 and 164. |
| [Party_ReturnHandItems](../functions/Party_ReturnHandItems.md) | `0x140288A24` | Returns a party unit's equipment to the inventory and clears its slots, with special handling for the two-handed and dual-wield cases. |
| [PartyUnit_FaceIndexForJob](../functions/PartyUnit_FaceIndexForJob.md) | `0x1402897B4` | Maps a job id to the face (portrait) record index of a generic unit. |
| [PartyUnit_FillFromWork](../functions/PartyUnit_FillFromWork.md) | `0x140284A08` | Builds the 640-byte party record B from a work record C and the save record A. B is the record the status and job screens read, including the job unlock mask they test. |
| [PartyUnit_FillFromWorkRecord](../functions/PartyUnit_FillFromWorkRecord.md) | `0x140360048` | Builds a party record B from a work record C alone (the per-job arrays come from C). |
| [PartyUnit_GetFaceRecord](../functions/PartyUnit_GetFaceRecord.md) | `0x140289548` | Selects the face / portrait record of a party unit and writes it to the output: 12 bytes copied from `g_PartyFaceRecords` plus a rebuilt face-variant word. |
| [PartyUnit_ReloadEquipment](../functions/PartyUnit_ReloadEquipment.md) | `0x1402BD924` | Rebuilds the selected unit's work record from its save row and refreshes the three screen records: the 0x1407B27xx party record, the 0x141876E90 panel block and the per-unit stat block. |
| [PartyUnit_WriteBackToSave](../functions/PartyUnit_WriteBackToSave.md) | `0x140285744` | Writes one party unit's record back into its 600-byte save row. |
| [Recruit_GenerateUnit](../functions/Recruit_GenerateUnit.md) | `0x140275310` | Fills a fresh save record with a newly generated unit: identity marker, starting job, birth sign, Brave and Faith, stat accumulators, equipment and sprite palette. |
| [sub_1400DC4C8](../functions/sub_1400DC4C8.md) | `0x1400DC4C8` | One of the battle targeting predicates: it decides whether a unit (or its target list) qualifies, and in this variant it accepts only a Mime and then walks the unit's stored target list through the caller's callback. |
| [sub_1400DDC70](../functions/sub_1400DDC70.md) | `0x1400DDC70` | The complement of the Mime predicate: it accepts a battle unit that is not a Mime and carries a particular marker, then walks the target list looking for an entry that is flagged. |
| [sub_1400FA7AC](../functions/sub_1400FA7AC.md) | `0x1400FA7AC` | Adds an equipped item's attribute record and added-effect statuses to a unit's status state. |
| [sub_1401EA910](../functions/sub_1401EA910.md) | `0x1401EA910` | Adds an OverrideEntryData row's HP and Speed growth bonuses to a unit work record, by the play mode (the configuration byte +196). |
| [sub_140275EF4](../functions/sub_140275EF4.md) | `0x140275EF4` | Builds a unit's working stats from its job row and its equipment words, one of the two paths that turn equipped items into stats. |
| [sub_1402760E8](../functions/sub_1402760E8.md) | `0x1402760E8` | The end of a unit build: loads the unit's equipment, applies the equipment attributes and the move and jump bonuses, then sets the name key. |
| [sub_140285A6C](../functions/sub_140285A6C.md) | `0x140285A6C` | Writes every party unit's record back to its save row. |
| [sub_140287118](../functions/sub_140287118.md) | `0x140287118` | The stat calculator behind `sub_140287354`: it masks the five unit and candidate words and computes the attack/defence differences into the block. |
| [sub_14028728C](../functions/sub_14028728C.md) | `0x14028728C` | Computes the equip block's stat deltas from the unit's live words and the candidate array, comparing each pair masked to ten bits. |
| [sub_140287354](../functions/sub_140287354.md) | `0x140287354` | Clears the equip block and recomputes it from the record, the unit words and the candidate words through `sub_140287118`. |
| [sub_140287398](../functions/sub_140287398.md) | `0x140287398` | Sums the stat contributions of five equipment words into the 0x141876E90 block (or a caller block) using only their masked ids. |
| [sub_140288590](../functions/sub_140288590.md) | `0x140288590` | Equips one item into a party slot: it validates the id, returns the old item to the inventory and writes the masked id into the slot; for a one-handed weapon it may swap the two hand words. |
| [sub_140288788](../functions/sub_140288788.md) | `0x140288788` | Validates whether a unit can equip an id in a slot and whether the other hand's weapon conflicts with it; returns 1 for a legal pick, 0 for a legal-but-not-needed pick, and a negative value for a refusal. |
| [sub_1402888E8](../functions/sub_1402888E8.md) | `0x1402888E8` | Sets a party unit's job, returns the old equipment to the inventory and, when asked, equips the best available set for the new job. |
| [sub_14028916C](../functions/sub_14028916C.md) | `0x14028916C` | Writes one word into a party unit's ability slots (primary skillset, secondary skillset, reaction, support, movement) and re-derives the unit's state, used by the Status screen's ability lists and the combat sets when... |
| [sub_1402D5B6C](../functions/sub_1402D5B6C.md) | `0x1402D5B6C` | The Outfitter cancel/restore: for every party unit and every one of its five equipment words, it puts the override word back when the live word is flagged or when an override exists, then clears the override. |
| [sub_1402D6464](../functions/sub_1402D6464.md) | `0x1402D6464` | Clears one party equipment slot and either refunds a pending purchase or preserves the original word in the per-unit override array. |
| [sub_1402D64CC](../functions/sub_1402D64CC.md) | `0x1402D64CC` | Puts the override word back into a cleared slot, or clears the slot's override when the slot is not restored. |
| [sub_1402D65D4](../functions/sub_1402D65D4.md) | `0x1402D65D4` | The Outfitter commit strip: it removes the session bits from every party equipment word, returns each stored original to the inventory, and clears the override array. |
| [sub_1402D7280](../functions/sub_1402D7280.md) | `0x1402D7280` | Applies one shop/Outfitter pick to a party unit slot: it refuses a "cannot equip" candidate, removes the old slot, records the new price, and writes the chosen item id with the session-pending bit 15. |
| [sub_1402D7584](../functions/sub_1402D7584.md) | `0x1402D7584` | Copies the selected unit's equipment words to a caller buffer and substitutes the override word for any word that is session-pending (or, with the third argument, empty). |
| [sub_140316C90](../functions/sub_140316C90.md) | `0x140316C90` | A thin weapon-record lookup for a unit: it filters the empty and out-of-range ids and returns the weapon sub-record. |
| [sub_1403331F8](../functions/sub_1403331F8.md) | `0x1403331F8` | Changes one equipment slot of the unit shown in the status panel, including the two-hand and shield-slot cases, and refreshes the panel afterwards. |
| [sub_140333338](../functions/sub_140333338.md) | `0x140333338` | Equips one ability list word into an ability slot of the selected party unit (the Status screen's ability lists and the combat sets): it checks the word's list flags, strips them, and hands the plain id to sub_14028916C. |
| [sub_14034DE90](../functions/sub_14034DE90.md) | `0x14034DE90` | Equipment refresh for the scene and battle unit records: it rewrites the per-slot item-id word at unit +0x1C2 from the party records. |
| [sub_140396984](../functions/sub_140396984.md) | `0x140396984` | Fills the attribute part of an equip preview: which stats an item would add and which of them the unit already has. |
| [sub_140396D08](../functions/sub_140396D08.md) | `0x140396D08` | Validates an equip preview against the unit's current equipment: it compares the candidate item with the item already in the slot and with the job's equip rules. |
| [Unit_ApplyEquipment](../functions/Unit_ApplyEquipment.md) | `0x1402779EC` | Adds the armor and attribute contributions of a unit's equipped items to the unit's stats. |
| [Unit_ApplyLevelGrowth](../functions/Unit_ApplyLevelGrowth.md) | `0x140278B24` | Raises a save record's level by a number of levels, growing the five 24-bit stat accumulators at each step from the job row's growth C values. |
| [Unit_ApplySpawnRecord](../functions/Unit_ApplySpawnRecord.md) | `0x14027612C` | Applies a 40-byte spawn entry to a unit work record before the job and stat build: copies the side and presence byte, picks the save-record path for party and guest units, and sets level, birthday, Brave and Faith wit... |
| [Unit_BuildAbilityBits](../functions/Unit_BuildAbilityBits.md) | `0x140276DF4` | Rebuilds a battle unit's passive-ability bit map from its innate ability words and its equipped reaction, support and movement ability. |
| [Unit_BuildFromRecord](../functions/Unit_BuildFromRecord.md) | `0x140275CA4` | Builds a unit work record from a spawn record: applies the record, sets up job state, abilities and growth, computes the stats and the starting equipment. |
| [Unit_BuildRsmAbilityList](../functions/Unit_BuildRsmAbilityList.md) | `0x140278358` | Answers a reaction / support / movement request of a spawn record: a fixed id is returned as is, a 'random' request (>= 0x1FE) picks one of the learned RSM abilities of the unit. |
| [Unit_ComputeStats](../functions/Unit_ComputeStats.md) | `0x140276EBC` | Turns a work record's five 24-bit stat accumulators and the job row's growth pairs into the unit's displayed HP, MP, Speed, PA and MA. Called whenever a work record is built or refreshed. |
| [Unit_GetFaceIndex](../functions/Unit_GetFaceIndex.md) | `0x1402896B8` | Maps a unit job and its variant byte to the face index the portrait and unit panel draw. |
| [Unit_InitAbilitiesFromJob](../functions/Unit_InitAbilitiesFromJob.md) | `0x1402771C8` | Sets a unit work record's skillset and innate ability words from its job row (head read: the skillset choice and the innate copy). |
| [Unit_InitJobJp](../functions/Unit_InitJobJp.md) | `0x1402770BC` | A new unit's starting JP in one job: the GeneralJob curve's value at the job's level plus a random part. |
| [Unit_LoadEquipmentAndEvade](../functions/Unit_LoadEquipmentAndEvade.md) | `0x1402778D4` | Fills the unit work record's weapon and evade bytes (+68..+78) from the job row and the equipped items. |
| [Unit_QueueJobAbilitiesToLearn](../functions/Unit_QueueJobAbilitiesToLearn.md) | `0x1402781A8` | Marks the abilities of one job as learned in a work record when they appear in a given list (unit setup). |
| [Unit_ReloadFromJobRowEx](../functions/Unit_ReloadFromJobRowEx.md) | `0x1402788EC` | The same re-read of the job row as Unit_BuildInnateStatuses (0x140278688, the plain variant), reading the status bytes from a second copy at +495 (head read). |
| [Unit_RollStartingStats](../functions/Unit_RollStartingStats.md) | `0x1402757B0` | Rolls the five 24-bit stat accumulators (HP, MP, Speed, PA, MA) of a new unit from a base value and a random span taken from the start row; the job is not an input. |
| [Unit_SetAbilityBit](../functions/Unit_SetAbilityBit.md) | `0x140276E5C` | Records one passive ability (a reaction, support or movement ability) in the battle unit's passive-ability bit map; a reaction-range id also becomes the unit's equipped reaction. |
| [Unit_TryLearnAbility](../functions/Unit_TryLearnAbility.md) | `0x1402780B0` | Attempts to mark one ability of a job as learned in a work record, optionally charging JP and rolling the ability's learn chance. |
| [UnitWork_ApplyJobRow](../functions/UnitWork_ApplyJobRow.md) | `0x140276C64` | Copies a unit's JobTable row into its work record: skillset, innate abilities, equipment flags, growth pairs, Move/Jump, status groups, elemental groups and the three trailing bytes. |
| [UnitWork_ApplyStartingEquipment](../functions/UnitWork_ApplyStartingEquipment.md) | `0x140277564` | Seeds a unit work record with its starting equipment while the unit is built from a setup record: the five slot bytes of the setup record are resolved to item ids and the hand slots and the two-handed state are derive... |
| [UnitWork_BuildForSlot](../functions/UnitWork_BuildForSlot.md) | `0x140284F6C` | Builds a unit work record for a party slot from the save record, then applies the job row and the equipment so the caller can read derived stats without touching the live unit. |
| [UnitWork_BuildFromGuestOrPartyRecord](../functions/UnitWork_BuildFromGuestOrPartyRecord.md) | `0x1402766C8` | Finds the save record a spawn entry names and builds the work record from it. |
| [UnitWork_BuildFromSave](../functions/UnitWork_BuildFromSave.md) | `0x140275B84` | Builds the 512-byte unit work record C from a save unit record A. It first refreshes the unit's unlock mask inside the save record, then copies and completes the work record. |
| [UnitWork_CopySaveFields](../functions/UnitWork_CopySaveFields.md) | `0x140276758` | Copies the fields of a save unit record A into the work record C. It defines the A -> C offset mapping. |
| [UnitWork_InitFromSpawnRecord](../functions/UnitWork_InitFromSpawnRecord.md) | `0x14027699C` | Builds a new unit's job state in its work record from a spawn record: job levels, unlock mask, job row and secondary skillset. |
| [UnitWork_PickStartingItem](../functions/UnitWork_PickStartingItem.md) | `0x140277F10` | Chooses one item id for a starting-equipment slot: it scans a category of the item table, keeps the ids the unit may use at its level, and returns one of them at random, or 0xFE when the category offers nothing. |
| [UnitWork_SetNameKey](../functions/UnitWork_SetNameKey.md) | `0x140277CF0` | Sets a unit's name key (work dword +508) and name string (work +332). |
| [UnitWork_StoreToSaveSlot](../functions/UnitWork_StoreToSaveSlot.md) | `0x140274EB8` | Writes a work record back into a save record: the unit's slot (a new slot for a recruit), job, flags, equipment and the per-job arrays. |

## Structures (4)

| Name | Size (bytes) | Summary |
|---|---|---|
| [BattleSpawnEntry](../structs/BattleSpawnEntry.md) | 40 | One 40-byte entry of a scripted battle's entry block: the description of one unit to build. |
| [PartyUnitRecord](../structs/PartyUnitRecord.md) | 640 | A unit as the party, status and job screens read it (55 records at g_PartyUnitRecords, reached through g_PartyUnits). |
| [UnitSaveRecord](../structs/UnitSaveRecord.md) | 600 | A unit as the save keeps it (54 records at g_UnitSaveData; copied whole into the save slot at +1304 + 600 n). |
| [UnitWorkRecord](../structs/UnitWorkRecord.md) | 512 | The working copy of a unit: the 21 battle units (g_BattleUnits) and temporary copies for previews and the job screens. |

## Globals (6)

| Name | Address | Type | Summary |
|---|---|---|---|
| [g_BattleEntrySource](../globals/g_BattleEntrySource.md) | `0x141856930` | `unit data` | 16 bytes: dword +0 the battle key (set from scene variable 50 by BattleLoad_StepFresh, read by Battle_GetEntryBlock and Battle_BuildEntryUnits as the OverrideEntryData key), qword +8 the base of the loaded entry data ... |
| [g_CurrentSpawnEntry](../globals/g_CurrentSpawnEntry.md) | `0x1411A3868` | `unit data` | Pointer to the spawn entry being built: set by Battle_PlaceEntryUnits and sub_1402841D0 before each Unit_BuildFromRecord; Unit_ApplySpawnRecord copies its bytes +33..+39 into unit +407..+413, and Battle_PlaceEntryUnit... |
| [g_SelectedCharaSkin](../globals/g_SelectedCharaSkin.md) | `0x1411A7550` | `uint16` | The selected character skin: its high byte is the skin CharaColorSkin_Resolve returns. |
| [g_UnitEquipOverride](../globals/g_UnitEquipOverride.md) | `0x14184A680` | `uint16[]` | Five override equipment words per unit, ten bytes per unit index: when the pair is non-zero the equip pickers use it in place of the unit record's own hand words. |
| [g_UnitSaveData](../globals/g_UnitSaveData.md) | `0x1411A7D10` | `data` | 54 x 600 bytes; builder sub_140275C70 -> sub_140275B84 -> sub_140276758 |
| [qword_141801100](../globals/qword_141801100.md) | `0x141801100` | `PartyUnitB *` | Pointer to a 640-byte scratch party record (unk_143749CA0). |

## Registries (3)

| Name | Summary |
|---|---|
| [NewUnitStartRows](../registries/NewUnitStartRows.md) | The four start rows that Unit_RollStartingStats reads: base and random span of the five stat accumulators in whole raw units, and the seven starting equipment words; a new unit's row is its kind (gender), never its job. |
| [UnitEventFlagBit](../registries/UnitEventFlagBit.md) | The bits of the unit flag word at battle unit +504, which the battle build stores from the entry override row: one bit per flag byte (OverrideEntryData +0x8E..+0x97 and +0x99), plus bit 11 set by the equipment build. |
| [UnitIdentityIds](../registries/UnitIdentityIds.md) | A unit is identified by its marker (save record +0, the character template), not by its job (+2): the job changes, the marker stays. |

## Observed behaviours (7)

| Name | Scope | Summary |
|---|---|---|
| [EntryAbilityListsOfPreplacedUnits](../behaviors/EntryAbilityListsOfPreplacedUnits.md) | engine (battle unit build) | A pre-placed unit's OverrideEntryData row can name abilities its skillsets start with learned and abilities that the learning pass leaves out, and can turn off the JP cost of the learning. |
| [EntryGrowthBonusesByPlayMode](../behaviors/EntryGrowthBonusesByPlayMode.md) | engine (battle unit build) | A pre-placed unit's OverrideEntryData row can hold four arrays indexed by the play mode that add to the unit's HP and Speed growth pairs, and one word that adds to its final Speed. |
| [PassiveAbilitiesAreAPerUnitBitMap](../behaviors/PassiveAbilitiesAreAPerUnitBitMap.md) | engine (battle unit record) | A battle unit's reactions, supports and movement abilities are kept as an 88-bit map (ids 422..509) in bytes +0x94..+0x9E of its record, rebuilt from the innate ability words and the three equipped words; the game's t... |
| [PerJobSlotStateLayouts](../behaviors/PerJobSlotStateLayouts.md) | engine (party, battle and save unit records) | Per-job state (learned flags, level nibbles, JP, total JP) sits in several unit layouts at different offsets, indexed by the job slot that Job_IdToIndex returns. |
| [PreplacedUnitsStartWithOneByteItems](../behaviors/PreplacedUnitsStartWithOneByteItems.md) | engine (scripted battle entries) | A pre-placed unit of a scripted battle takes its starting equipment from one-byte item ids, so no item above id 255 can be a starting item. |
| [UnitEventFlagWord](../behaviors/UnitEventFlagWord.md) | engine (battle unit table) | A battle unit's dword +504 holds one bit per OverrideEntryData flag byte (bits 0..10) and bit 11 from the equipment build. |
| [WarriorsGuildCandidatesAreMadeEachVisit](../behaviors/WarriorsGuildCandidatesAreMadeEachVisit.md) | engine (Warriors' Guild recruit list) | The Warriors' Guild's recruit list is 15 candidate records of 564 bytes at 0x1408E6CB0 (the first 564 bytes of a save record's layout), made by Guild_MakeCandidates each time the guild is opened and never saved; hirin... |

## Tables (1)

| Name | Storage | NXD table id | Rows | Summary |
|---|---|---|---|---|
| [UnitEquipOverride](../tables/UnitEquipOverride.md) | Executable (filled at run time) |  |  | Five override equipment words per unit, ten bytes per unit index: when the pair is non-zero the equip pickers use it in place of the unit record's own hand words. |
