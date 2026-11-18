# AbilityAux

- **Kind:** table
- **Area:** [Ability data](../areas/ability-data.md)
- **Storage:** Executable
- **Address:** `0x140787F80`
- **Rows:** 512 rows of 8 bytes
- **Keyed by:** ability id (masked to 9 bits)
- **Read by:** [Ability_GetAuxRecord](../functions/Ability_GetAuxRecord.md), [Action_BuildCurrentAction](../functions/Action_BuildCurrentAction.md), [Battle_ResolveAction](../functions/Battle_ResolveAction.md), [Battle_StatusApply](../functions/Battle_StatusApply.md), [JobAbilityList_Build](../functions/JobAbilityList_Build.md), [Unit_TryLearnAbility](../functions/Unit_TryLearnAbility.md), [sub_140281488](../functions/sub_140281488.md), [sub_14028A474](../functions/sub_14028A474.md), [sub_14030CD08](../functions/sub_14030CD08.md)
- **Row layout:** [AbilityAuxRow](../structs/AbilityAuxRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The per-ability auxiliary records: classic JP cost, learn percent and two flag fields.

## Behavior

- V: ability ids are 9 bits everywhere (skillset slots, this index, the NXD Ability keys).
- V: Ability_GetAuxRecord returns the record and a category-specific extra pointer; ids below 0x170 are category 0 with the action record as the extra pointer, ids from 0x170 use the six small kind tables.
- V: 15 functions read this table (cross-references in the database); the first ten are linked.

## Notes

Our names. Tags per member and behaviour line; read statically in the decompilation of the Enhanced executable.

## Open questions

- ?: meaning of every bit of flags3 and flags4
