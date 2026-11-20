# UnitWork_ApplyJobRow

- **Address:** `0x140276C64`
- **Area:** [Unit data](../areas/unit-data.md)
- **Prototype:** `uint8_t UnitWork_ApplyJobRow(uint8_t *work, void *growthTweaks)`
- **Callers:** UnitWork_BuildFromSave, sub_140275EF4, UnitWork_InitFromSpawnRecord
- **Callees:** sub_14002630C (block copy), sub_1401EA910

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Copies a unit's JobTable row into its work record: skillset, innate abilities, equipment flags, growth pairs, Move/Jump, status groups, elemental groups and the three trailing bytes. Run after the save fields are copied in.

## Behavior

- V: the row is JobTable + 49 * work[3] (job id); job 161 uses row 164 when the low nibble at work+238 (level of job index 21) is 8 or more.
- V: row byte 0 (skillset id) goes to +18; bytes 1..8 (four u16 innate ability ids) to +10; bytes 9..13 (equipment bit field) to +82; bytes 14..23 (growth C/M pairs) to +138.
- V: after the growth copy, sub_1401EA910 may add small amounts to the HP and SP pairs (+138, +139, +142, +143, each capped at 254) from the optional tweak tables in the second argument, indexed by a byte of a global record (I: a difficulty or new-game-plus setting).
- V: byte 24 (Move) goes to +66; byte 25 bits 0..6 (Jump) to +67 and bit 7 sets or clears bit 0x40 of +81, the unit that blocks its allies in move ranges (see the behaviour UnitThatBlocksItsAlliesInMoveRanges).
- V: bytes 27..31, 32..36 and 37..41 (three status bit fields) go to +87, +92 and +97; when bit 2 of work+5 and either of bits 0 and 3 of work+6 are set, the +92 group is OR-ed with two bit fields from a global record (I).
- V: bytes 42..45 (four element bit fields) go to +118..+121, and +122 is cleared.
- V: bytes 46, 47 and 48 are copied to +399, +400 and +398. For marker byte 130, Unit_ResolvePreviewShape returns work+399 as the sprite shape and work+400 as the palette byte, so row byte 46 is the shape id and 47 the palette for such units. Byte 48 lands in +398, which damage formulas for dragon-type units read (I: species or family).
- V: separately, work+402 gets the skillset id of the row indexed by marker byte work[0] when that byte is below 0x4A (special characters), or is 162 or 163; otherwise 0.
- V: the three trailing bytes are zero in the stock generic rows and in rows 160 and 161 read from the running game.

## State touched

- Calls: [sub_1401EA910](sub_1401EA910.md)

## Referenced by

- Called by: [UnitWork_BuildFromSave](UnitWork_BuildFromSave.md), [UnitWork_InitFromSpawnRecord](UnitWork_InitFromSpawnRecord.md), [sub_140275EF4](sub_140275EF4.md)
- Observed behaviours: [EntryGrowthBonusesByPlayMode](../behaviors/EntryGrowthBonusesByPlayMode.md), [SkillsetIdsPastTheByte](../behaviors/SkillsetIdsPastTheByte.md), [SpriteNumberStoreWidths](../behaviors/SpriteNumberStoreWidths.md), [UnitThatBlocksItsAlliesInMoveRanges](../behaviors/UnitThatBlocksItsAlliesInMoveRanges.md)

## Notes

Same copy pattern appears in two reload paths (sub_140278688, sub_1402788EC). Job 94 is the stock example of a non-zero byte 46. Status and element groups are zero in all stock generic rows, so their order is untested there.

## Open questions

Whether byte 48 is a species id.
