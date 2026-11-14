# PassiveAbilitiesAreAPerUnitBitMap

- **Kind:** observed behaviour
- **Scope:** engine (battle unit record)
- **Area:** [Unit data](../areas/unit-data.md)
- **Affects:** [Unit_SetAbilityBit](../functions/Unit_SetAbilityBit.md), [Unit_BuildAbilityBits](../functions/Unit_BuildAbilityBits.md), [UnitWorkRecord.passive_bits](../structs/UnitWorkRecord.md#passive_bits), [UnitWorkRecord.innate_words](../structs/UnitWorkRecord.md#innate_words), [UnitWorkRecord.equipped_reaction](../structs/UnitWorkRecord.md#equipped_reaction), [UnitWorkRecord.equipped_support](../structs/UnitWorkRecord.md#equipped_support), [UnitWorkRecord.equipped_movement](../structs/UnitWorkRecord.md#equipped_movement)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A battle unit's reactions, supports and movement abilities are kept as an 88-bit map (ids 422..509) in bytes +0x94..+0x9E of its record, rebuilt from the innate ability words and the three equipped words; the game's tests of a passive are bit tests on that map.

## Behavior

- V: Unit_SetAbilityBit(unit, id) ignores an id outside 422..509; otherwise it sets bit 0x80 >> (index & 7) of byte +0x94 + (index >> 3) with index = id - 422, and an id below 454 also becomes the unit's equipped reaction word (+0x14).
- V: Unit_BuildAbilityBits clears the 11 bytes, then sets the bit of each of the four innate words (+0x0A..+0x10) and of the equipped reaction (+0x14), support (+0x16) and movement (+0x18): seven calls, in that order.
- V: callers of the rebuild are the unit build and reload paths (UnitWork_BuildFromSave, Unit_BuildFromRecord, Unit_ReloadFromJobRow, Unit_ReloadFromJobRowEx, sub_140275EF4); sub_14030B4F0 calls Unit_SetAbilityBit directly.
- V: the last three bytes of the map (+0x9C, +0x9D, +0x9E: the movement ids 486..509) are the bytes the move range builder reads as movement flags (see the UnitWorkRecord members move_flags_c, move_flags_d, move_flags).
- V: byte +0x99 bit 0x80 is the map's bit for id 462 and is the bit that halves an action's MP cost (sub_1402828E4, sub_14030B1A0); +0x99 bit 0x40 (id 463) is the JP Boost test of the JP award (BattleActionJpFormulaAndSpillover).
- I: that 462 is the Halve MP support and 463 JP Boost: by their effects only; the names were not read from the text table.
- V: the after-damage chain tests +0x94 bits 0x80, 0x40, 0x20, 0x02 and +0x95 bits 0x40, 0x20, 0x10, 0x08 and +0x96 bits 0x40, 0x10; see AfterDamageReactionChain.
- ?: whether other code tests bits of the map that was not found (the study read only the places named here); the compares of ids 422..509 over the whole executable were not counted.

## Notes

Offsets are those of the 512-byte battle unit record (table at 0x141853CE0).

## Open questions

? whether unused passive rows (443, 481, 484, 485) have a reader anywhere (not searched exhaustively).
