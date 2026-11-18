# AbilityKind4_Charge

- **Kind:** table
- **Area:** [Ability data](../areas/ability-data.md)
- **Storage:** Executable
- **Address:** `0x140789280`
- **Rows:** 8 rows of 2 bytes
- **Keyed by:** ability id 0x196..0x19D (Charge)
- **Read by:** [Ability_GetAuxRecord](../functions/Ability_GetAuxRecord.md), [Action_BuildCurrentAction](../functions/Action_BuildCurrentAction.md), [sub_140281488](../functions/sub_140281488.md), [sub_14030DD8C](../functions/sub_14030DD8C.md), [sub_14030E368](../functions/sub_14030E368.md)
- **Row layout:** [AbilityKind4Row](../structs/AbilityKind4Row.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Charge time and power of each Charge ability. The real array starts at the first id of the range; the code addresses it through a virtual base before the array.

## Behavior

- V: six readers.

## Notes

Our names. Tags per member and behaviour line; read statically in the decompilation of the Enhanced executable.

## Open questions

None recorded.
