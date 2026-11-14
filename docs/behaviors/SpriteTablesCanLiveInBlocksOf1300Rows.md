# SpriteTablesCanLiveInBlocksOf1300Rows

- **Kind:** observed behaviour
- **Scope:** engine (sprite number tables)
- **Area:** [Graphics](../areas/graphics.md)
- **Affects:** [CharaRender_BuildAtlasTexture](../functions/CharaRender_BuildAtlasTexture.md), [CharaPalette_LoadClassic](../functions/CharaPalette_LoadClassic.md), [CharaPalette_ReloadForShape](../functions/CharaPalette_ReloadForShape.md), [sub_14026EB74](../functions/sub_14026EB74.md), [PartyUnit_BuildJobRecord](../functions/PartyUnit_BuildJobRecord.md), [Unit_GetSpriteSetId](../functions/Unit_GetSpriteSetId.md), [EventMessage_Scripted](../functions/EventMessage_Scripted.md), [sub_140300768](../functions/sub_140300768.md), [sub_140300D74](../functions/sub_140300D74.md), [sub_14032AB3C](../functions/sub_14032AB3C.md), [SpriteId_ToShape](../functions/SpriteId_ToShape.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The game reaches every table indexed by a look number only through a fixed set of instructions and bounds.

## Behavior

- V: the census of every code operand and data pointer into the ten tables finds 52 readers that address them (24 attribute, 7 HD, 2 per classic table, 1 per portrait copy and 2 for the shared one, 11 for the face table), no data pointer, and two operands that only look like readers (UnitFaceIndexReadsTheTableAfterTheHdTable and a byte table that starts at the last row of the copy at 0x140681A90).
- V: the bounds that compare a look number before a table read are 32-bit immediates of compares or of loads compared as 16-bit words (0xA9 three times, 0xAA once, 0xD3 six times, 0x9F eleven times); the four HD compares on the scene unit's sprite byte (+0xA against 0xAA) are byte immediates.
- V: out of range the stock readers fall back to a value a row can hold: -1 for the HD readers (they test the entry against -1), 0 for the six portrait readers (their code register is zeroed at entry), and for the face table the fixed list of SpriteId_ToShape (codes 176, 183, 188 to 201 and 205 name themselves, every other code -1).

## Open questions

None recorded.
