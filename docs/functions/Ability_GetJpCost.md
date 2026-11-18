# Ability_GetJpCost

- **Address:** `0x1402CC0AC`
- **Area:** [Ability data](../areas/ability-data.md)
- **Prototype:** `unsigned __int16 Ability_GetJpCost(unsigned int abilityId)`
- **Callers:** sub_1402780B0, sub_1402867BC, sub_14028A474, sub_1402B94E4, sub_1402B9AD0, sub_140367AA0, sub_140392D14
- **Callees:** sub_1403D325C, sub_1403D3AE8, sub_1403D2FD8

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the ability's JP cost: the u16 at Ability row +64 (JpCost1 | JpCost2 << 8); 0xFFFF when the table or row is missing.

## Behavior

- V: same cached table 39 as AbilityTable_GetRow; returns *(u16 *)(row + 64).
- V (data): decoded cost is 0..9999, 360 abilities cost > 0 (Cure 50, Curaga 450, Curaja 800).

## Referenced by

- Appears in flows: [AbilityLifecycle](../flows/AbilityLifecycle.md)
- Called by: [JobAbilityList_Build](JobAbilityList_Build.md), [Unit_SpendJp](Unit_SpendJp.md), [Unit_TryLearnAbility](Unit_TryLearnAbility.md), [sub_14028A474](sub_14028A474.md), [sub_140367AA0](sub_140367AA0.md)

## Notes

Also known as AbilityTable_GetJpCost (earlier sheet name). sub_1402B9AD0 subtracts the cost from the unit's per-job JP (unit + 202 + 2 * jobIndex, u16); sub_1402867BC / sub_14028A474 mark an ability learnable (|0x4000) when the unit's JP is not below the cost.

- Correction: arguments 2..4 are unused (the signature has no job argument); 7 callers.

## Open questions

Exact meaning of the 0x4000 / 0x2000 flag words (I: learned / learnable).
