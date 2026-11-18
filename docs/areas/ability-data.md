# Ability data

Ability NXD row accessor, JP cost, aux header and the ability action records.

Functions: 6, Structures: 12, Registries: 2, Flows: 1, Observed behaviours: 7, Tables: 14.

## Functions (6)

| Name | Address | Purpose |
|---|---|---|
| [Ability_GetAuxRecord](../functions/Ability_GetAuxRecord.md) | `0x140275A78` | Returns the executable's per-ability auxiliary record and an extra category-specific pointer for an ability id. |
| [Ability_GetJpCost](../functions/Ability_GetJpCost.md) | `0x1402CC0AC` | Returns the ability's JP cost: the u16 at Ability row +64 (JpCost1 \| JpCost2 << 8); 0xFFFF when the table or row is missing. |
| [AbilityAction_BuildWorkingCopy](../functions/AbilityAction_BuildWorkingCopy.md) | `0x1402BAE24` | Creates the writable ability action table: copies the executable's built-in table of 368 records (20 bytes each) and then overwrites fields from the OverrideAbilityActionData nxd table (id 247). |
| [AbilityAction_GetRecord](../functions/AbilityAction_GetRecord.md) | `0x1402BB060` | Returns a pointer to the 20-byte action record of an ability, building the working table on first use. |
| [AbilityTable_GetRow](../functions/AbilityTable_GetRow.md) | `0x1400F8474` | Returns the Ability NXD row for an ability id, or null when the table or row is missing. |
| [sub_1402A21B0](../functions/sub_1402A21B0.md) | `0x1402A21B0` | Builds the help text of an ability row; for a movement ability it adds the '+N' number from the ability id. |

## Structures (12)

| Name | Size (bytes) | Summary |
|---|---|---|
| [AbilityActionRow](../structs/AbilityActionRow.md) | 20 | One action record of an ability. |
| [AbilityAnimRow](../structs/AbilityAnimRow.md) | 3 | Battle presentation of one ability. |
| [AbilityAuxRow](../structs/AbilityAuxRow.md) | 8 | One auxiliary ability record. |
| [AbilityEffectNumberRow](../structs/AbilityEffectNumberRow.md) | 2 | Effect word of one ability. |
| [AbilityKind1Row](../structs/AbilityKind1Row.md) | 1 | Item id of an Item-command ability. |
| [AbilityKind2Row](../structs/AbilityKind2Row.md) | 1 | Item type of a Throw ability. |
| [AbilityKind3Row](../structs/AbilityKind3Row.md) | 2 | Jump reach. |
| [AbilityKind4Row](../structs/AbilityKind4Row.md) | 2 | Charge values. |
| [AbilityKind5Row](../structs/AbilityKind5Row.md) | 1 | Arithmeticks mask. |
| [AbilityKind6Row](../structs/AbilityKind6Row.md) | 1 | Passive ability index. |
| [NxdDataAbilityRow](../structs/NxdDataAbilityRow.md) | 68 | One row of the nxd.ability table (English text table; the other languages share the layout). |
| [NxdDataOverrideAbilityActionDataRow](../structs/NxdDataOverrideAbilityActionDataRow.md) | 40 | One row of the nxd.override_ability_action_data table (data table). |

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

## Tables (14)

| Name | Storage | NXD table id | Rows | Summary |
|---|---|---|---|---|
| [Ability](../tables/Ability.md) | NXD file | 39 |  | The ability rows the game reads through AbilityTable_GetRow, loaded lazily and cached. |
| [AbilityActionRecords](../tables/AbilityActionRecords.md) | Executable |  | 368 records of 20 bytes (ids 0..0x16F) | The action record of each action ability. |
| [AbilityActionWorking](../tables/AbilityActionWorking.md) | Executable (filled at run time) |  | 368 records of 20 bytes | Working copy of AbilityActionRecords built at first use and read by every action builder. |
| [AbilityAnim](../tables/AbilityAnim.md) | Executable |  | 454 rows of 3 bytes | Battle presentation of each ability: charge type, execution motion and text selector. |
| [AbilityAux](../tables/AbilityAux.md) | Executable |  | 512 rows of 8 bytes | The per-ability auxiliary records: classic JP cost, learn percent and two flag fields. |
| [AbilityEffectNumbers](../tables/AbilityEffectNumbers.md) | Executable |  | 454 rows of 2 bytes | Battle effect number and flag of each ability. |
| [AbilityKind1_ItemByAbility](../tables/AbilityKind1_ItemByAbility.md) | Executable |  | 14 rows of 1 byte | Item-command table: ability 368 + i maps to one item id; the only table that pairs an Item-command ability with its item. |
| [AbilityKind2_ThrowCategory](../tables/AbilityKind2_ThrowCategory.md) | Executable |  | 12 rows of 1 byte | Throw table: ability 382 + i maps to one equip category; an item is throwable when its category matches a row of one of the unit throw abilities. |
| [AbilityKind3_JumpReach](../tables/AbilityKind3_JumpReach.md) | Executable |  | 12 rows of 2 bytes | Horizontal and vertical reach of each Jump ability. |
| [AbilityKind4_Charge](../tables/AbilityKind4_Charge.md) | Executable |  | 8 rows of 2 bytes | Charge time and power of each Charge ability. |
| [AbilityKind5_MathMask](../tables/AbilityKind5_MathMask.md) | Executable |  | 8 rows of 1 byte | Arithmeticks bit mask of each ability. |
| [AbilityKind6_PassiveIndex](../tables/AbilityKind6_PassiveIndex.md) | Executable |  | 90 rows of 1 byte | Running index of every passive ability. |
| [FormulaHandlers](../tables/FormulaHandlers.md) | Executable |  | 106 rows of 8 bytes | Dispatch table of the 106 ability formula handlers. |
| [NxdDataOverrideAbilityActionData](../tables/NxdDataOverrideAbilityActionData.md) | NXD file | 247 | 368 rows of 40 bytes | Ability data override rows: each field is -1 (keep the stock value) or a replacement for range, area, formula, status, CT or MP cost. |
