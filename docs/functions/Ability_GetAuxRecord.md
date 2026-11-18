# Ability_GetAuxRecord

- **Address:** `0x140275A78`
- **Area:** [Ability data](../areas/ability-data.md)
- **Prototype:** `int Ability_GetAuxRecord(int16_t abilityId, uint8_t **outAux, uint8_t **outExtra)`
- **Callers:** About a dozen battle, learn and UI functions (`sub_1400FA94C`, `sub_1400FBA58`, `sub_1401113B8`, `sub_140153CA0`, `sub_140206F90`, `sub_14022F868`, `sub_14028A474`, `sub_1402A102C`, `sub_1402A1DA0` and others)
- **Callees:** `sub_1402BB060` (per-ability extra record)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the executable's per-ability auxiliary record and an extra category-specific pointer for an ability id.

## Behavior

- V: the id is masked to 9 bits (0..511); *outAux points at the aux table base 0x140787F80 plus 8 bytes per id.
- V: record layout: u16 classic JP cost, u8 learn percent, u8 flags3, u32 flags4.
- V: ids below 0x170 return category 0 and *outExtra = the per-ability 20-byte record from a lazily initialised table (null for ids above 0x16F).
- V: ids from 0x170 return categories 1..8 with *outExtra pointing into one of six small byte tables: 0x170..0x17D is 1, ..0x189 is 2, ..0x195 is 3, ..0x19D is 4, ..0x1A5 is 5, ..0x1C5 is 6, ..0x1E5 is 7, the rest 8. Categories 3 and 4 use a 2-byte stride.
- V: the learn percent is the chance tested against Rng_Percent(100, v) when an ability is learned.
- I: the 8-byte aux header corresponds to the classic game's per-ability data; flags3 and flags4 bit meanings are not established (?).

## Referenced by

- Called by: [BattleCommand_BuildScreen](BattleCommand_BuildScreen.md), [sub_140153CA0](sub_140153CA0.md), [sub_140206F90](sub_140206F90.md), [sub_14022F868](sub_14022F868.md), [sub_140238444](sub_140238444.md), [sub_14028A474](sub_14028A474.md), [sub_1402A21B0](sub_1402A21B0.md)
- Reads tables: [AbilityAux](../tables/AbilityAux.md), [AbilityKind1_ItemByAbility](../tables/AbilityKind1_ItemByAbility.md), [AbilityKind2_ThrowCategory](../tables/AbilityKind2_ThrowCategory.md), [AbilityKind3_JumpReach](../tables/AbilityKind3_JumpReach.md), [AbilityKind4_Charge](../tables/AbilityKind4_Charge.md), [AbilityKind5_MathMask](../tables/AbilityKind5_MathMask.md), [AbilityKind6_PassiveIndex](../tables/AbilityKind6_PassiveIndex.md), [StatusProperties](../tables/StatusProperties.md)

## Notes

The function's eight id thresholds (0x140275A9F..0x140275B70) and its 9-bit mask (0x140275A7E) are immediates in its body. Its six kind tables are read through virtual bases: kind1 0x140785CA8, kind2 0x140789112, kind3 0x140788F4C, kind4 0x140788F54, kind5 0x1407844EA, kind6 0x140788DDA; three of those virtual bases lie inside the aux table and one inside the gap before kind3. Kind tables by role (V by readers, I by name): 1 Item-command item id, 2 Throw item type, 3 Jump horizontal/vertical, 4 Charge ct/power, 5 Arithmeticks masks, 6 running index of reaction/support/movement ids.

The nxd Ability JP columns are what the game reads for cost; this table keeps the classic values and the learn chance. About ten entries differ from the nxd cost.

## Open questions

Bit meanings of flags3 and flags4.
