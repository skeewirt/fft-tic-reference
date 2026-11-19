# ActionResult

- **Kind:** structure
- **Area:** [Battle](../areas/battle.md)
- **Size:** 48 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The result of one action on one target, filled by the formula handler and read by the result applier, the preview and the messages. One lives at +0x1BE of each battle unit record (g_BattleActionBlock points at the target's); a second, the caster's own result, is a separate static block (g_BattleCasterResult). Battle_ResultReset sets it up before the handler runs: hit flag 1, hit percent 100, nearly everything else 0.

## Fields

| Offset | Field | Type | Conf | Meaning | Written by | Observed behaviours |
|---|---|---|---|---|---|---|
| <a id="hit"></a>`0x0` | hit | `uint8` | V | 1 = the effect lands, 0 = nothing happens. Battle_ResultReset stores 1; every miss path stores 0 (Formula_EvadeByteRoll, Formula_ChanceRoll, Formula_ZeroResult, Formula_StealGate). | [Formula_ChanceRoll](../functions/Formula_ChanceRoll.md), [Formula_ZeroResult](../functions/Formula_ZeroResult.md) |  |
| <a id="critical"></a>`0x1` | critical | `uint8` | V | Set to 1 by Formula_CritRoll. | [Formula_CritRoll](../functions/Formula_CritRoll.md) |  |
| <a id="miss_reason"></a>`0x2` | miss_reason | `uint8` | V | The reason when hit is 0: 1..4 an evade by evade byte k (Formula_EvadeRoll), 5 nullified (Formula_ZeroResult), 6 failed the chance roll (Formula_ChanceRoll, Formula_BardDancerGate), 7 no effect, 8 the caster-side katana result (Formula_DrawOutGate on the caster's block), 9, 11 and 13 reaction results. The meaning of each reason for the messages is I. | [Formula_ChanceRoll](../functions/Formula_ChanceRoll.md), [Formula_ZeroResult](../functions/Formula_ZeroResult.md) |  |
| <a id="item_id"></a>`0x4` | item_id | `uint16` | V | The picked equipment id of a steal or break (Action_PickTargetEquipment); on the caster's block the caster's word +0x1A8 (Formula_DrawOutGate). |  |  |
| <a id="hp_damage"></a>`0x6` | hp_damage | `int16` | V | HP damage (Formula_DamageAB; about 70 sites). Held at 0x7FFF by Formula_DamageAB and clamped to 999 by sub_14030A11C. | [Formula_DamageAB](../functions/Formula_DamageAB.md) | [PoisonAndRegenActAtTheEndOfTheUnitsTurn](../behaviors/PoisonAndRegenActAtTheEndOfTheUnitsTurn.md) |
| <a id="hp_heal"></a>`0x8` | hp_heal | `int16` | V | HP heal (Formula_HealSwap, Formula_DrainHP, Formula_FinalizeAbsorb). | [Formula_DrainHP](../functions/Formula_DrainHP.md), [Formula_HealSwap](../functions/Formula_HealSwap.md) | [PoisonAndRegenActAtTheEndOfTheUnitsTurn](../behaviors/PoisonAndRegenActAtTheEndOfTheUnitsTurn.md) |
| <a id="mp_damage"></a>`0xA` | mp_damage | `int16` | V | MP damage (Formula_DrainMP and the MP formulas). | [Formula_DrainMP](../functions/Formula_DrainMP.md) |  |
| <a id="mp_heal"></a>`0xC` | mp_heal | `int16` | V | MP heal (Formula_DrainMP on the caster's block, the MP restore formulas). | [Formula_DrainMP](../functions/Formula_DrainMP.md) |  |
| <a id="gil"></a>`0xE` | gil | `int16` | V | Gil change: the caster's block +gil, the target's block -gil (Formula_StealGilApply). |  |  |
| <a id="reaction_id"></a>`0x10` | reaction_id | `uint16` | V | The reaction ability id to run after the result (440, 448..452 in the stock formulas 42 and 99 and in sub_14030AFEC). |  |  |
| <a id="flags"></a>`0x12` | flags | `uint16` | V | Flag word: 0x0002 recruit, 0x0004 equipment broken, 0x0008 draw-out kept, 0x0010 equipment stolen, 0x0040 status result, 0x0080, 0x0100 level drain, 0x0200 inflict roll passed (Formula_StatusChance19), 0x0400 absorbed (Formula_ElementAffinity), 0x0800 weak (doubled), 0x1000 draw-out katana broken, 0x2000 action failed banner, 0x4000 knockback present (Formula_KnockbackCalc). Stored by Formula_ElementAffinity, Formula_FinalizeAbsorb, Formula_StatusChance19, Formula_KnockbackCalc, Formula_56_StatusOnlyApplication and formulas 20, 37, 38, 46, 87, 88, 89. |  |  |
| <a id="speed_delta"></a>`0x14` | speed_delta | `uint8` | V | A stat change: bit 7 = increase, the low 7 bits the amount. Written by formulas 57, 28 (ability 88), 29 (ability 95) and Formula_SapStatPick (143, 197). Which of +0x14 / +0x16 / +0x17 the game applies as which stat is I (the stock abilities that write each are known). |  |  |
| <a id="ct_delta"></a>`0x15` | ct_delta | `uint8` | V | CT change: 0xFF = +127, 127 = -127 (formulas 18, 21, 93, 28 ability 92, 29 ability 99, 42 ability 117). |  |  |
| <a id="pa_delta"></a>`0x16` | pa_delta | `uint8` | V | PA change (formulas 54, 85, 59; 28 ability 89; 29 ability 96; Formula_SapStatPick 144 / 198): Battle_ApplyActionResult applies it to the PA base +0x38 through Unit_ChangeBattleStat (cap 99, min 1). |  |  |
| <a id="ma_delta"></a>`0x17` | ma_delta | `uint8` | V | MA change (formulas 86, 59; 28 ability 90; 29 ability 97; Formula_SapStatPick 145 / 199): applied to the MA base +0x39 through Unit_ChangeBattleStat (cap 99, min 1). |  |  |
| <a id="brave_delta"></a>`0x18` | brave_delta | `uint8` | V | Brave change (formulas 58, 59, 97, 98 and 42 abilities 118 / 119). |  |  |
| <a id="faith_delta"></a>`0x19` | faith_delta | `uint8` | V | Faith change (formula 42 abilities 120 / 121). |  |  |
| <a id="action_class"></a>`0x1A` | action_class | `uint8` | V | Stored by Battle_ResolveAction from dword_140787F84[2 * ability id] & 3, with 0x80 added when bit 0x1000000 of that dword is set, before the handler runs. Its meaning is ?. |  |  |
| <a id="equipment_slot_mask"></a>`0x1B` | equipment_slot_mask | `uint8` | V | The picked equipment slot of a steal or break: 0x80 head, 0x40 body, 0x20 accessory, 0x10 right weapon, 0x08 right shield, 0x04 left weapon, 0x02 left shield (Action_PickTargetEquipment; Formula_StealGate clears it). |  |  |
| <a id="status_add"></a>`0x1D` | status_add | `uint8[5]` | V | The statuses to add: status s is bit 0x80 >> (s & 7) of byte s >> 3 (Formula_56_StatusOnlyApplication; sub_1403067D0 adds a bit in byte +0x1E). |  |  |
| <a id="status_remove"></a>`0x22` | status_remove | `uint8[5]` | V | The statuses to remove (the name Status_FilterPendingSets gives the set at +34..38; bit 0x10 of the inflict flag copies the record into it). Formula_ElementAffinity sets bit 0x80 of byte +0x24 (I: status 16, Oil, so a doubled hit takes Oil away). |  |  |
| <a id="kind_bits"></a>`0x27` | kind_bits | `uint8` | V | Result-kind bits: 0x80 HP damage, 0x40 HP heal, 0x20 MP damage, 0x10 MP heal, 0x08 status change pending, 0x01 another change (stat, gil, CT, EXP). Every routing block sets the matching bit with the amount. | [Formula_DamageAB](../functions/Formula_DamageAB.md), [Formula_HealSwap](../functions/Formula_HealSwap.md) | [PoisonAndRegenActAtTheEndOfTheUnitsTurn](../behaviors/PoisonAndRegenActAtTheEndOfTheUnitsTurn.md) |
| <a id="reaction_copy"></a>`0x28` | reaction_copy | `uint16` | I | A copy of the reaction ability id (formula 99 writes 450 here and at +0x10); read by the message and reaction code. |  |  |
| <a id="exp_delta"></a>`0x2A` | exp_delta | `uint8` | V | EXP change: the amount ORed with 0x80 on the target's block (Formula_40_StealEXP). |  |  |
| <a id="hit_percent"></a>`0x2C` | hit_percent | `int16` | V | The hit percent the preview shows and sub_14030A11C tests for 0 (it then clears the hit flag). Battle_ResultReset stores 100; Formula_EvadeRoll, Formula_BardDancerGate, Formula_ChanceRoll and Formula_56_StatusOnlyApplication scale it. | [Formula_ChanceRoll](../functions/Formula_ChanceRoll.md), [Formula_EvadeRoll](../functions/Formula_EvadeRoll.md), [Formula_ZeroResult](../functions/Formula_ZeroResult.md) |  |

## Behavior

- V: Battle_ResultReset (0x14030A410) clears the word at +1, the qword at +4 (+4..+0x0B), the dword at +0x0C, the qword at +0x12 (+0x12..+0x19), the word at +0x1A (+0x1A, +0x1B), the byte at +0x1C and the kind byte +0x27, stores 0x00640000 over the dword at +0x2A (hit percent 100) and 1 at +0, then calls sub_14030A43C, which clears the two status sets (+0x1D..+0x26) and a five-byte array at 0x14186B028. Not cleared: +0x03, the reaction id +0x10 and the copy +0x28 (so everything else is 0 after the reset except these three bytes).
- V: Battle_ResolveAction resets both the target's block (g_BattleActionBlock) and the caster's static block (g_BattleCasterResult) before it runs the handler, so a handler may write the caster's own result without clearing it first.
- V: the block is 0x30 bytes: the next field of the battle unit record after it is at +0x1EE (read as flag bits by sub_14030A11C).
- V: after the handler (and sub_1403067D0 for ids below 7) sub_14030A11C(1) clamps the four amounts to 999, scales HP and MP damage by the difficulty row, runs the post hook of 12 formulas and clears the hit flag when the hit percent is 0; Battle_ResolveAction then ORs 1 into the kind byte (+0x27) when the flag word (+0x12) is non-zero (0x140309F84..0x140309F8B).
- V (Battle_ApplyActionResult): Unit_ChangeBattleStat applies +0x14 to Speed (+0x3A, cap 50), +0x15 to CT (+0x41), +0x16 to PA (+0x38), +0x17 to MA (+0x39), +0x18 to Brave (+0x2B), +0x19 to Faith (+0x2D).

## Referenced by

- Global instances: [g_BattleActionBlock](../globals/g_BattleActionBlock.md), [g_BattleCasterResult](../globals/g_BattleCasterResult.md)
- Observed behaviours: [FormulaHandlerContract](../behaviors/FormulaHandlerContract.md), [FormulaIdsWithNoHandlerBody](../behaviors/FormulaIdsWithNoHandlerBody.md)
- Written by: [Battle_ResolveAction](../functions/Battle_ResolveAction.md)

## Notes

Read 2026-11-12. Offsets are relative to the start of the block, which is unit +0x1BE. The status sets and the array at 0x14186B028 are cleared by the reset through sub_14030A43C; the reaction id (+0x10) is not cleared by it.

## Open questions

? the meaning of +0x1A (action_class) and of the bytes +0x03, +0x1C, +0x28, +0x29 and +0x2B; what the five-byte array at 0x14186B028 holds (I: a staging copy of the pending status set).
