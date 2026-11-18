# Unit_GetSpriteSetId

- **Address:** `0x1402C06D4`
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Prototype:** `int Unit_GetSpriteSetId(int mode, unsigned id, int *outBits)`
- **Callers:** sub_1401F3F70, sub_1402C08C0, sub_1402C1310, sub_1402C1EA8, sub_14036F5D0, sub_140370414 (errand result scene)
- **Callees:** SpriteId_ToShape, SceneUnit_EntryById, sub_14032ACE0, sub_140214134, sub_1401E39BC, UITable_GetRowByKey

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Resolves a unit's sprite number for the event and scene code. In scenes of a few types it reads the generic-job selector table and converts its value to a sprite shape; otherwise it takes a generated or saved path.

## Behavior

- V: mode 0 returns whatever sub_140214134(id, outBits) gives; modes other than 0 and 1 return -1.
- V: mode 1 uses the selector path only when the scene id word at 0x141848BB0 is 21, 43, 44 or 51. Then the unit entry is looked up by SceneUnit_EntryById: entries are 564 bytes at 0x1408E6CB0, id 0..15, only valid in those scenes (else the call returns 0).
- V: selector index = (0x60, or 0x61 when bit 7 of entry byte +4 is clear) + 2 * (entry byte +2 - 74); entry byte +2 is the job id. If the index is below 0xD3, the 16-bit value at word_1406807C0[index] is read, else 0.
- V: the value goes through SpriteId_ToShape (a 160-entry u32 table at 0x1407146D0 for values up to 0x9F, a few fixed ids above) and is rejected (-1) when it exceeds 0xCD; the result is returned and `outBits` receives ((value >> 10) & 3) + 8.
- V: for generic jobs 74..91 the selector value, mapped through SpriteId_ToShape, gives the same shape number as the battle-sprite rule for all 36 job-sex pairs; for jobs 92 and 93 the two numberings differ (selector gives 132..135, the battle rule 130..133).
- V: in other scenes the id comes from sub_14032ACE0 and the save record (the table with key 0x112 is queried with the record's marker byte), is passed through SpriteId_ToShape when the global mode word allows, and is capped at 0xCD; it returns -1 when a float setting is below 2.0.
- I: the selector value is the second numbering of the same sprites (the event-character sprite number); the earlier note that it is a portrait index is not supported.
- V: on the save-record branch the code comes from sub_14032ACE0 -> sub_14032AB3C -> PortraitCode_FillCell and is a byte (or the record index when no code is set); the function writes it unmapped to dword_142E7FCAC[0] and dword_142FF9EDC before any face mapping.
- M (unicorn, codes 0..255): with the mode word & ~2 = 0 no code gives -1 at the cap 0x1402C0816: 146 codes map to faces up to 204 and the 110 unmapped codes return as themselves (50 of them 206..255); in modes 1 and 5 the codes 206..255 give -1.
- V (seen live 2026-11-14): a face number 9056 / 9057 returned for a unit whose look byte is 56 / 57 makes the roster and the Status screen draw the texture `wldface_9056_08` / `wldface_9057_08`: the face number is formatted into the texture name unchanged at four digits.

## State touched

- Calls: [SpriteId_ToShape](SpriteId_ToShape.md), [SceneUnit_EntryById](SceneUnit_EntryById.md), [sub_14032ACE0](sub_14032ACE0.md), [sub_140214134](sub_140214134.md), [UITable_GetRowByKey](UITable_GetRowByKey.md)
- Reads: [g_SceneIdWord](../globals/g_SceneIdWord.md), [g_GraphicsLevel](../globals/g_GraphicsLevel.md), [g_FaceDisplayMode](../globals/g_FaceDisplayMode.md)
- Writes: [g_DialogueFaceSlot0](../globals/g_DialogueFaceSlot0.md), [g_HdFaceSlotValues](../globals/g_HdFaceSlotValues.md)

## Referenced by

- Appears in flows: [PartyMenuFaceChain](../flows/PartyMenuFaceChain.md), [PartyMenuFaceChain](../flows/PartyMenuFaceChain.md)
- Called by: [EventScene_QueueHelpText](EventScene_QueueHelpText.md)
- Observed behaviours: [ClassicSpriteFilesByNumber](../behaviors/ClassicSpriteFilesByNumber.md), [FaceNumberCapsClipRawCodesToo](../behaviors/FaceNumberCapsClipRawCodesToo.md), [GenericUnitSpriteNumberFromJob](../behaviors/GenericUnitSpriteNumberFromJob.md), [LookSitesUseTheSaveRecordNotTheSlot](../behaviors/LookSitesUseTheSaveRecordNotTheSlot.md), [NamedCharactersKeepTheirOwnLookWhateverTheirJob](../behaviors/NamedCharactersKeepTheirOwnLookWhateverTheirJob.md), [PortraitCodeIsAByteOnTheSaveRecordPath](../behaviors/PortraitCodeIsAByteOnTheSaveRecordPath.md), [SpriteTablesCanLiveInBlocksOf1300Rows](../behaviors/SpriteTablesCanLiveInBlocksOf1300Rows.md), [SpriteTablesEndAtSprite169](../behaviors/SpriteTablesEndAtSprite169.md), [UnitFaceFromSpriteNumber](../behaviors/UnitFaceFromSpriteNumber.md)
- Reads tables: [PortraitCodes](../tables/PortraitCodes.md)
- Resolves registries: [SpriteNumberTables](../registries/SpriteNumberTables.md)

## Notes

Conflict between earlier readings: one pass called the selector value a shape id (via the table at 0x1407146D0), another called it the event-character sprite number; the code path supports both statements (the value is converted by SpriteId_ToShape). The selector is indexed by a shape-style number (96..133 for the 20 generic jobs), not by job id.

The selector words are one of six identical copies of one 211-word table (the words are portrait codes; five other readers use the other copies). The two face-number caps differ: on the scene path (0x1402C0816) the cap also clips the raw id when the mode word skips SpriteId_ToShape, on the generic path (0x1402C086C) it clips only SpriteId_ToShape's answer and an unmapped code is returned uncapped.

## Open questions

Which scenes use the 21/43/44/51 path in play, and how the non-scene branch picks its id.
