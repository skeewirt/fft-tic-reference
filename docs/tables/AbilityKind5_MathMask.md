# AbilityKind5_MathMask

- **Kind:** table
- **Area:** [Ability data](../areas/ability-data.md)
- **Storage:** Executable
- **Address:** `0x140784688`
- **Rows:** 8 rows of 1 byte
- **Keyed by:** ability id 0x19E..0x1A5 (Arithmeticks)
- **Read by:** [Ability_GetAuxRecord](../functions/Ability_GetAuxRecord.md), [sub_14030E94C](../functions/sub_14030E94C.md)
- **Row layout:** [AbilityKind5Row](../structs/AbilityKind5Row.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Arithmeticks bit mask of each ability. The real array starts at the first id of the range; the code addresses it through a virtual base before the array.

## Behavior

- V: three readers.

## Notes

Our names. Tags per member and behaviour line; read statically in the decompilation of the Enhanced executable.

## Open questions

None recorded.
