# AbilityKind6_PassiveIndex

- **Kind:** table
- **Area:** [Ability data](../areas/ability-data.md)
- **Storage:** Executable
- **Address:** `0x140788F80`
- **Rows:** 90 rows of 1 byte
- **Keyed by:** ability id 0x1A6..0x1FF (reaction 0x1A6..0x1C5, support 0x1C6..0x1E5, movement 0x1E6 and up)
- **Read by:** [Ability_GetAuxRecord](../functions/Ability_GetAuxRecord.md), [Battle_StatusApply](../functions/Battle_StatusApply.md)
- **Row layout:** [AbilityKind6Row](../structs/AbilityKind6Row.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Running index of every passive ability. The real array starts at the first id of the range; the code addresses it through a virtual base before the array.

## Behavior

- V: one reader.

## Notes

Our names. Tags per member and behaviour line; read statically in the decompilation of the Enhanced executable.

## Open questions

None recorded.
