# Unit_BuildAbilityBits

- **Address:** `0x140276DF4`
- **Area:** [Unit data](../areas/unit-data.md)
- **Prototype:** `int16_t Unit_BuildAbilityBits(UnitWorkRecord *unit)`
- **Callers:** UnitWork_BuildFromSave, Unit_BuildFromRecord, Unit_ReloadFromJobRow, Unit_ReloadFromJobRowEx, sub_140275EF4 (IDA code references)
- **Callees:** Unit_SetAbilityBit

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Rebuilds a battle unit's passive-ability bit map from its innate ability words and its equipped reaction, support and movement ability.

## Behavior

- V: clears unit +0x94 (8 bytes), +0x9C (one word) and +0x9E (one byte): the whole 11-byte map.
- V: calls Unit_SetAbilityBit for the four innate words at +0x0A, +0x0C, +0x0E, +0x10, then for the equipped reaction (+0x14), support (+0x16) and movement (+0x18) words, seven calls in that order.
- V: Unit_SetAbilityBit stores a reaction-range id (below 454) in +0x14, and the equipped reaction word is read only after the four innate calls, so an innate reaction-range id has already replaced the equipped reaction word when that word is read.

## State touched

- Calls: [Unit_SetAbilityBit](Unit_SetAbilityBit.md)
- Reads: [UnitWorkRecord.innate_words](../structs/UnitWorkRecord.md#innate_words), [UnitWorkRecord.equipped_reaction](../structs/UnitWorkRecord.md#equipped_reaction), [UnitWorkRecord.equipped_support](../structs/UnitWorkRecord.md#equipped_support), [UnitWorkRecord.equipped_movement](../structs/UnitWorkRecord.md#equipped_movement)
- Writes: [UnitWorkRecord.passive_bits](../structs/UnitWorkRecord.md#passive_bits)

## Referenced by

- Observed behaviours: [PassiveAbilitiesAreAPerUnitBitMap](../behaviors/PassiveAbilitiesAreAPerUnitBitMap.md)

## Notes

The name is ours (IDB: sub_140276DF4, renamed 2026-11-10); read 2026-11-10. 104 bytes, read whole. The five callers are the unit build and reload paths.

## Open questions

None recorded.
