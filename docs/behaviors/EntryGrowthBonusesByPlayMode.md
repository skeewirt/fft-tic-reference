# EntryGrowthBonusesByPlayMode

- **Kind:** observed behaviour
- **Scope:** engine (battle unit build)
- **Area:** [Unit data](../areas/unit-data.md)
- **Affects:** [sub_1401EA910](../functions/sub_1401EA910.md), [UnitWork_InitFromSpawnRecord](../functions/UnitWork_InitFromSpawnRecord.md), [UnitWork_ApplyJobRow](../functions/UnitWork_ApplyJobRow.md), [Unit_ComputeStats](../functions/Unit_ComputeStats.md), [sub_1402760E8](../functions/sub_1402760E8.md), [Unit_ApplyEquipment](../functions/Unit_ApplyEquipment.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A pre-placed unit's OverrideEntryData row can hold four arrays indexed by the play mode that add to the unit's HP and Speed growth pairs, and one word that adds to its final Speed.

## Behavior

- V: sub_1401EA910 adds element [play mode] of the four i16 arrays at row +0x5C, +0x64, +0x6C and +0x74 to unit work bytes +138, +139, +142 and +143, each only while the sum stays at 254 or below; an array shorter than the play mode's index adds nothing.
- V: Unit_ComputeStats treats work +138 + 2 i as the (growth constant, multiplier) pair of stat i in the order HP, MP, Speed, PA, MA: so the four arrays are the HP growth constant, HP multiplier, Speed growth constant and Speed multiplier (columns hp_growth_constant_bonus, hp_multiplier_bonus, speed_growth_constant_bonus, speed_multiplier_bonus), not HP and MP.
- V: the growth constant divides the accumulator growth per level (accumulator += accumulator / (constant - 1 + level)) for a generated unit; the multiplier scales the accumulator into the stat ((accumulator x multiplier / 100) >> 14).
- V: Speed is capped at 50 before the row's word at +0x80 (column speed_bonus, one i16) is added to it, so the bonus can exceed the cap; the sum is stored at work +58.

## Open questions

None recorded.
