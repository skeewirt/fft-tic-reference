# AbilityKind1_ItemByAbility

- **Kind:** table
- **Area:** [Ability data](../areas/ability-data.md)
- **Storage:** Executable
- **Address:** `0x140785E18`
- **Rows:** 14 rows of 1 byte
- **Keyed by:** ability id 0x170..0x17D (Item command)
- **Read by:** [Ability_GetAuxRecord](../functions/Ability_GetAuxRecord.md), [Unit_ListItemCommandItems](../functions/Unit_ListItemCommandItems.md)
- **Held in:** [g_AbilityKind1_ItemByAbility](../globals/g_AbilityKind1_ItemByAbility.md)
- **Row layout:** [AbilityKind1Row](../structs/AbilityKind1Row.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Item-command table: ability 368 + i maps to one item id; the only table that pairs an Item-command ability with its item. The real array starts at the first id of the range; the code addresses it through a virtual base before the array.

## Behavior

- V: the range thresholds 0x170, 0x17E, 0x18A, 0x196, 0x19E, 0x1A6, 0x1C6 and 0x1E6 are immediates in Ability_GetAuxRecord.

## Notes

Our names. Tags per member and behaviour line; read statically in the decompilation of the Enhanced executable.

## Open questions

None recorded.
