# Unit_ReactionVoiceAllowed

- **Address:** `0x1402178C0`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `bool Unit_ReactionVoiceAllowed(uint8_t *unit, ..., int slot)`
- **Callers:** sub_1401FAEE8, sub_14020CC50, sub_14031BA38, sub_14031C674, sub_14031D010
- **Callees:** AbilityTable_GetRow, NxdRegistry_Find, NxdTable_GetRowById, NxdEntry_GetRow, sub_14026A508

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Answers a yes / no question about a unit's reaction voice line by the rule row of its current ability.

## Behavior

- V: gets the Ability row of the unit's current ability (unit word +322), reads row +0x38 (column ability_reaction_voice_type) as a key of AbilityReactionVoiceType (nxd 330, cache qword_143CDA2C8), copies that row's 11 dwords (+4..+0x2C) and switches on the dword picked by the third argument.
- V: rule value 0 -> true; 1 -> false; 2 -> sub_14026A508(unit); 3 -> not sub_14026A508(unit); 4 -> a once-per-unit gate in byte_141873180 indexed by the unit (+8) or by the other unit (+8 of the second argument); other values -> true.
- V: returns false when a row is missing.
- M: the Ability column holds 0 on 486 rows, 2 on 21 rows and 3 on 5 rows; the rule table has rows 0..3.

## State touched

- Calls: [AbilityTable_GetRow](AbilityTable_GetRow.md), [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdEntry_GetRow](NxdEntry_GetRow.md), [sub_14026A508](sub_14026A508.md)

## Open questions

? what sub_14026A508 tests and which reaction each of the 11 slots is.
