# Ability data

Ability NXD row accessor, JP cost, aux header and the ability action records.

Functions: 6, Registries: 2, Flows: 1, Observed behaviours: 7, Tables: 3.

## Functions (6)

| Name | Address | Purpose |
|---|---|---|
| [Ability_GetAuxRecord](../functions/Ability_GetAuxRecord.md) | `0x140275A78` | Returns the executable's per-ability auxiliary record and an extra category-specific pointer for an ability id. |
| [Ability_GetJpCost](../functions/Ability_GetJpCost.md) | `0x1402CC0AC` | Returns the ability's JP cost: the u16 at Ability row +64 (JpCost1 \| JpCost2 << 8); 0xFFFF when the table or row is missing. |
| [AbilityAction_BuildWorkingCopy](../functions/AbilityAction_BuildWorkingCopy.md) | `0x1402BAE24` | Creates the writable ability action table: copies the executable's built-in table of 368 records (20 bytes each) and then overwrites fields from the OverrideAbilityActionData nxd table (id 247). |
| [AbilityAction_GetRecord](../functions/AbilityAction_GetRecord.md) | `0x1402BB060` | Returns a pointer to the 20-byte action record of an ability, building the working table on first use. |
| [AbilityTable_GetRow](../functions/AbilityTable_GetRow.md) | `0x1400F8474` | Returns the Ability NXD row for an ability id, or null when the table or row is missing. |
| [sub_1402A21B0](../functions/sub_1402A21B0.md) | `0x1402A21B0` | Builds the help text of an ability row; for a movement ability it adds the '+N' number from the ability id. |

## Registries (2)

| Name | Summary |
|---|---|
| [AbilityAuxFlagBits](../registries/AbilityAuxFlagBits.md) | The meaning of the bits of exe.ability.aux flags3 (byte +3) and flags4 (u32 at +4) as named here: flags3 holds the ability type in bits 0..4 and three flags in bits 5..7, flags4 the AI behaviour flags, one bit each. |
| [AbilityTypes](../registries/AbilityTypes.md) | The ability type nibble in the low five bits of exe.ability.aux flags3, with names. |

## Flows (1)

| Name | Summary |
|---|---|
| [AbilityLifecycle](../flows/AbilityLifecycle.md) | The order in which the game reads an ability, from the skillset row that offers it to the presentation and the save: where it comes from for a unit, the menus and lists, choosing and targeting, the action request and ... |

## Observed behaviours (7)

| Name | Scope | Summary |
|---|---|---|
| [AbilityListWordsCarryFlags](../behaviors/AbilityListWordsCarryFlags.md) | engine | An ability list word holds the ability id in bits 0..9 and flags above it (0x800 equipped or innate, 0x1000 learned, 0x4000 greyed); every consumer strips them with & 0x3FF before the id is stored or looked up. |
| [AbilityTextKeysPast2047](../behaviors/AbilityTextKeysPast2047.md) | engine | The game names an ability by the 16-bit key pool << 11 \| id (11 bits). |
| [BattleItemsAreUsedThroughItemAbilities](../behaviors/BattleItemsAreUsedThroughItemAbilities.md) | engine | A battle item is used through an Item ability: the Chemist's Items command lists skillset 6's abilities 368..381 as items through the kind1 table, and the action's ability word is item + 0x80. |
| [FormulaHandlersBranchOnTheAbilityId](../behaviors/FormulaHandlersBranchOnTheAbilityId.md) | engine | Battle_ResolveAction reads one formula id per action (a byte), clamps it and calls one registry handler; many handlers then branch on the id of the ability being resolved (the formula block's +8 word). |
| [FormulaIdsPastTheByte](../behaviors/FormulaIdsPastTheByte.md) | engine | Every hop of a formula id is one byte and the registry has 106 rows; the clamp `(u8)(id - 1) > 0x69 -> 1` sends any other value to formula 1. |
| [SkillsetIdsPastTheByte](../behaviors/SkillsetIdsPastTheByte.md) | engine | A skillset id is one byte everywhere the game keeps it (job row +0, unit +0x12 / +0x13 / +0x192, save A+7, the action's command byte +0x1A1, the battle menu arrays, the command table). |
| [StockFormulaHandlersAreBlockSequences](../behaviors/StockFormulaHandlersAreBlockSequences.md) | engine | The 106 stock formula handlers are plain functions with no arguments over the frame Battle_ResolveAction sets up; 47 of them are sequences of the game's own building blocks. |

## Tables (3)

| Name | Storage | NXD table id | Rows | Summary |
|---|---|---|---|---|
| [Ability](../tables/Ability.md) | NXD file | 39 |  | The ability rows the game reads through AbilityTable_GetRow, loaded lazily and cached. |
| [AbilityActionRecords](../tables/AbilityActionRecords.md) | Executable |  | 368 records of 20 bytes (ids 0..0x16F) | The action record of each action ability, copied into a writable table on first use. |
| [AbilityAux](../tables/AbilityAux.md) | Executable |  | 8 bytes per id, ids 0..511 | The per-ability auxiliary records: classic JP cost, learn percent and two flag fields, with an extra category-specific record for each id. |
