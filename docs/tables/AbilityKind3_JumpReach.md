# AbilityKind3_JumpReach

- **Kind:** table
- **Area:** [Ability data](../areas/ability-data.md)
- **Storage:** Executable
- **Address:** `0x140789260`
- **Rows:** 12 rows of 2 bytes
- **Keyed by:** ability id 0x18A..0x195 (Jump)
- **Read by:** [Ability_GetAuxRecord](../functions/Ability_GetAuxRecord.md), [Action_BuildCurrentAction](../functions/Action_BuildCurrentAction.md), [sub_14027F270](../functions/sub_14027F270.md)
- **Row layout:** [AbilityKind3Row](../structs/AbilityKind3Row.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Horizontal and vertical reach of each Jump ability. The real array starts at the first id of the range; the code addresses it through a virtual base before the array.

## Behavior

- V: sub_14027F270 uses it to light the reachable tiles of Jump abilities.

## Notes

Our names. Tags per member and behaviour line; read statically in the decompilation of the Enhanced executable.

## Open questions

None recorded.
