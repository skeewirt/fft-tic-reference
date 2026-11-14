# Unit_SetAbilityBit

- **Address:** `0x140276E5C`
- **Area:** [Unit data](../areas/unit-data.md)
- **Prototype:** `int16_t Unit_SetAbilityBit(UnitWorkRecord *unit, uint16_t abilityId)`
- **Callers:** Unit_BuildAbilityBits, sub_14030B4F0 (IDA code references)
- **Callees:** None

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Records one passive ability (a reaction, support or movement ability) in the battle unit's passive-ability bit map; a reaction-range id also becomes the unit's equipped reaction.

## Behavior

- V: index = abilityId - 422 (0x1A6); an id outside index 0..87 (ids 422..509) changes nothing.
- V: for an id below 454 (0x1C6) the word at unit +0x14 is set to the id (the equipped reaction); ids 454 and above leave +0x14 alone.
- V: then bit (0x80 >> (index & 7)) of byte unit +0x94 + (index >> 3) is set, so +0x94..+0x9E hold 88 bits, one per passive id, most significant bit first.
- I: the three id bands by the ability-type counts (32 reactions 422..453, 32 supports 454..485, 24 movement 486..509); the band split at 454 is the only one the code tests.
- V: the function only sets bits; Unit_BuildAbilityBits clears the map first.

## State touched

- Writes: [UnitWorkRecord.passive_bits](../structs/UnitWorkRecord.md#passive_bits), [UnitWorkRecord.equipped_reaction](../structs/UnitWorkRecord.md#equipped_reaction)

## Referenced by

- Appears in flows: [AbilityLifecycle](../flows/AbilityLifecycle.md)
- Called by: [Unit_BuildAbilityBits](Unit_BuildAbilityBits.md)
- Observed behaviours: [PassiveAbilitiesAreAPerUnitBitMap](../behaviors/PassiveAbilitiesAreAPerUnitBitMap.md)

## Notes

The name is ours (IDB: sub_140276E5C, renamed 2026-11-10); read 2026-11-10. 96 bytes, read whole. Struct fields: UnitWorkRecord +0x14, +0x94..+0x9E. Behaviour: PassiveAbilitiesAreAPerUnitBitMap.

## Open questions

? what sub_14030B4F0 does with the call (its reads of the bit map were not traced).
