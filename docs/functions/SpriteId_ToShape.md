# SpriteId_ToShape

- **Address:** `0x140274028`
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Prototype:** `uint32_t SpriteId_ToShape(void *unused, int spriteId)`
- **Callers:** Unit_GetSpriteSetId, EventMessage_Scripted, EventMessage_Task and several scene and event functions
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Maps a scene sprite id (the value Unit_GetSpriteSetId hands to event and scene code) to a sprite shape number.

## Behavior

- V: ids 0..159 are looked up in a 160-entry dword table.
- V: ids 176, 183, 188..201 and 205 map to themselves.
- V: every other id returns 0xFFFFFFFF (no shape).
- V: table entries for ids 25..64 are the shapes 96..135 (generic job sprites, id 25 is shape 96).
- I: for job ids 74..91 this agrees with the battle shape formula of Unit_ResolvePreviewShape; for Dancer and Mime the scene numbering is offset by two (shapes 132..135 against 130..133).

## Referenced by

- Appears in flows: [PartyMenuFaceChain](../flows/PartyMenuFaceChain.md)
- Called by: [Unit_GetSpriteSetId](Unit_GetSpriteSetId.md), [sub_1402F8684](sub_1402F8684.md), [sub_140300768](sub_140300768.md), [sub_140338A28](sub_140338A28.md), [sub_1403980AC](sub_1403980AC.md)
- Observed behaviours: [FaceLookupInlineCopiesDisagreeAboveCode159](../behaviors/FaceLookupInlineCopiesDisagreeAboveCode159.md), [SpriteTablesCanLiveInBlocksOf1300Rows](../behaviors/SpriteTablesCanLiveInBlocksOf1300Rows.md), [SpriteTablesEndAtSprite169](../behaviors/SpriteTablesEndAtSprite169.md), [UnitFaceFromSpriteNumber](../behaviors/UnitFaceFromSpriteNumber.md)

## Notes

The value is the face number of a portrait code. Ten functions carry an inline copy of this lookup (each with its own compare of the code with 0x9F); five of them answer codes above 0x9F differently (code 205 gives no face in sub_140214134 and the two turn panel functions; Battle_UnitStatusFillAlt and sub_1402DF374 use an older list for 184 to 205), found by running every copy under unicorn.

## Open questions

Which art shapes 134 and 135 show for Mime was not checked.
