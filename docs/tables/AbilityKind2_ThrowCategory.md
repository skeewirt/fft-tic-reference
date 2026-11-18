# AbilityKind2_ThrowCategory

- **Kind:** table
- **Area:** [Ability data](../areas/ability-data.md)
- **Storage:** Executable
- **Address:** `0x140789290`
- **Rows:** 12 rows of 1 byte
- **Keyed by:** ability id 0x17E..0x189 (Throw)
- **Read by:** [Ability_GetAuxRecord](../functions/Ability_GetAuxRecord.md), [Ai_SurveyTargets](../functions/Ai_SurveyTargets.md)
- **Held in:** [g_AbilityKind2_ThrowCategory](../globals/g_AbilityKind2_ThrowCategory.md)
- **Row layout:** [AbilityKind2Row](../structs/AbilityKind2Row.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Throw table: ability 382 + i maps to one equip category; an item is throwable when its category matches a row of one of the unit throw abilities. The real array starts at the first id of the range; the code addresses it through a virtual base before the array.

## Behavior

- V: one AI scoring routine walks the bytes from +1.

## Notes

Our names. Tags per member and behaviour line; read statically in the decompilation of the Enhanced executable.

## Open questions

None recorded.
