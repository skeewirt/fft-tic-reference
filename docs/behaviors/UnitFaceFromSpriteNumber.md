# UnitFaceFromSpriteNumber

- **Kind:** observed behaviour
- **Scope:** engine (small unit portraits)
- **Area:** [Graphics](../areas/graphics.md)
- **Affects:** [Unit_GetSpriteSetId](../functions/Unit_GetSpriteSetId.md), [SpriteId_ToShape](../functions/SpriteId_ToShape.md), [PartyUnit_BuildJobRecord](../functions/PartyUnit_BuildJobRecord.md), [JobRecord_FillIconAndGenericFlag](../functions/JobRecord_FillIconAndGenericFlag.md), [sub_14032AB3C](../functions/sub_14032AB3C.md), [sub_140300D74](../functions/sub_140300D74.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The small unit face is chosen from the sprite number through three portrait-code tables, then a face number, and the face number is capped at 0xCD; the status card's large job picture follows a different path through the job type.

## Behavior

- V (read in the database): the face cap is a compare with 0xCD at 0x1402C0816 (Unit_GetSpriteSetId) and 0x1401F3A03 (sub_1401F3858); the two other cap sites (0x214272 in sub_140214134, 0x21519D in TurnPanel_SetUnitPanel, 0x215786 in TurnPanel_SetTag) compare against a register.
- I: the chain is sprite number, portrait code (the word tables of SpriteTablesEndAtSprite169; the table used depends on the screen: 0x683A70 menus, 0x680070 battle, 0x6807C0 the party list), face number (code up to 0x9F through the dword table at 0x7146D0; 0xB0 to 0xC7 special cases; else -1 and the callers keep the code, capped), a few remaps in FaceNumber_Remap, then the texture name wldface_<number>_<colour> with colour = ((code >> 10) & 3) + 8 (the format string is a row of the UI texture path table).
- I (reported from play): a sprite whose portrait code is 0 shows face 1 (the main character's); portrait numbers 170 to 204 are taken.
- I: portrait codes of 0x53 and above mean story characters: the battle reader sub_140300D74 then reads a byte at +0x2F of a global character record (the load at 0x140301451), so a code of 212 there crashed in battle.
- V: SpriteId_ToShape is the function that turns a code up to 0x9F into the face number through g_SpriteIdToShape and answers fixed values for the codes 176, 183, 188 to 201, 205; its current name describes the scene sprite use, the face-number use above is the same function reached from the portrait readers (I).

## Open questions

? whether the name SpriteId_ToShape should become a face-number name; both uses read the same table and need a sheet note.
