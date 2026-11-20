# UnitWorkRecord

- **Kind:** structure
- **Area:** [Unit data](../areas/unit-data.md)
- **Size:** 512 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The working copy of a unit: the 21 battle units (g_BattleUnits) and temporary copies for previews and the job screens. Same per-job arrays as the save record at other offsets.

## Fields

| Offset | Field | Type | Conf | Meaning | Read by | Observed behaviours | Written by |
|---|---|---|---|---|---|---|---|
| <a id="marker"></a>`0x0` | marker | `uint8` | V | Copied from the save record +0. |  |  |  |
| <a id="slot_id"></a>`0x2` | slot_id | `uint8` | V | The unit's slot id (save record +1). |  |  |  |
| <a id="job"></a>`0x3` | job | `uint8` | V | Job id. | [Unit_GetFaceIndex](../functions/Unit_GetFaceIndex.md) |  |  |
| <a id="innate_words"></a>`0xA` | innate_words | `uint16[4]` | V | Four innate ability words (+0x0A, +0x0C, +0x0E, +0x10); Unit_BuildAbilityBits passes each to Unit_SetAbilityBit. | [Unit_BuildAbilityBits](../functions/Unit_BuildAbilityBits.md) | [PassiveAbilitiesAreAPerUnitBitMap](../behaviors/PassiveAbilitiesAreAPerUnitBitMap.md) |  |
| <a id="equipped_reaction"></a>`0x14` | equipped_reaction | `uint16` | V | The equipped reaction ability id; Unit_SetAbilityBit also writes it for any reaction-range id (below 454). | [Unit_BuildAbilityBits](../functions/Unit_BuildAbilityBits.md) | [PassiveAbilitiesAreAPerUnitBitMap](../behaviors/PassiveAbilitiesAreAPerUnitBitMap.md) | [Unit_SetAbilityBit](../functions/Unit_SetAbilityBit.md) |
| <a id="equipped_support"></a>`0x16` | equipped_support | `uint16` | V | The equipped support ability id (Unit_BuildAbilityBits sets its bit). | [Unit_BuildAbilityBits](../functions/Unit_BuildAbilityBits.md) | [PassiveAbilitiesAreAPerUnitBitMap](../behaviors/PassiveAbilitiesAreAPerUnitBitMap.md) |  |
| <a id="equipped_movement"></a>`0x18` | equipped_movement | `uint16` | V | The equipped movement ability id (Unit_BuildAbilityBits sets its bit). | [Unit_BuildAbilityBits](../functions/Unit_BuildAbilityBits.md) | [PassiveAbilitiesAreAPerUnitBitMap](../behaviors/PassiveAbilitiesAreAPerUnitBitMap.md) |  |
| <a id="head"></a>`0x1A` | head | `uint16` | V | Equipped item, 0xFF = none (UnitWork_ApplyStartingEquipment: setup byte 18, default picked with slot bit 0x20; I: head). |  |  |  |
| <a id="body"></a>`0x1C` | body | `uint16` | V | Equipped item, 0xFF = none (setup byte 19, slot bit 0x10; I: body). |  |  |  |
| <a id="accessory"></a>`0x1E` | accessory | `uint16` | V | Equipped item, 0xFF = none (setup byte 20, slot bit 0x08); Unit_LoadEquipmentAndEvade reads its accessory sub-record. |  |  |  |
| <a id="right_weapon"></a>`0x20` | right_weapon | `uint16` | V | Weapon of the first hand, 0xFF = none: UnitWork_ApplyStartingEquipment puts the first hand item here when it is not a shield; BattleRange_MarkWeaponReach takes the Attack weapon from here first; Unit_LoadEquipmentAndEvade copies its power / evade to +0x44 / +0x46. I: the right hand (Status lists it first). | [BattleRange_MarkWeaponReach](../functions/BattleRange_MarkWeaponReach.md) |  |  |
| <a id="right_shield"></a>`0x22` | right_shield | `uint16` | V | Shield of the first hand, 0xFF = none (the first hand item when its slot bits have 0x40). |  |  |  |
| <a id="left_weapon"></a>`0x24` | left_weapon | `uint16` | V | Weapon of the second hand, 0xFF = none; the Attack weapon when +0x20 is empty; cleared when the first weapon's flags have bit 0x01 or +0x9A bit 0x02. | [BattleRange_MarkWeaponReach](../functions/BattleRange_MarkWeaponReach.md) |  |  |
| <a id="left_shield"></a>`0x26` | left_shield | `uint16` | V | Shield of the second hand, 0xFF = none. |  |  |  |
| <a id="pa_base"></a>`0x38` | pa_base | `uint8` | V | PA before equipment: Unit_ComputeStats writes it in mode 0; Unit_ChangeBattleStat moves it within 1..99 for the PA change of an action (result block +0x16) and keeps the total +0x3E. |  |  | [Unit_ChangeBattleStat](../functions/Unit_ChangeBattleStat.md) |
| <a id="ma_base"></a>`0x39` | ma_base | `uint8` | V | MA before equipment (result block +0x17 changes it, 1..99). |  |  |  |
| <a id="speed_base"></a>`0x3A` | speed_base | `uint8` | V | Speed before equipment (result block +0x14 changes it, 1..50). |  |  |  |
| <a id="stat_bonus"></a>`0x3B` | stat_bonus | `uint8[3]` | V | PA, MA, Speed from the attribute records of the equipped items (Unit_ApplyEquipment zeroes and sums them). |  |  |  |
| <a id="pa_total"></a>`0x3E` | pa_total | `uint8` | V | PA = min(+0x38 + +0x3B, 99) (the last loop of Unit_ApplyEquipment; Unit_ChangeBattleStat keeps it). |  |  | [Unit_ChangeBattleStat](../functions/Unit_ChangeBattleStat.md) |
| <a id="ma_total"></a>`0x3F` | ma_total | `uint8` | V | MA = min(+0x39 + +0x3C, 99). |  |  |  |
| <a id="speed_total"></a>`0x40` | speed_total | `uint8` | V | Speed = min(+0x3A + +0x3D, 50): the CT gain Battle_TurnEngine phase 0 adds to +0x41 each tick (halved by Slow, x1.5 by Haste). |  |  |  |
| <a id="ct"></a>`0x41` | ct | `uint8` | V | CT: phase 0 adds the gain and clamps to 254; a unit acts at 100 or more (result block +0x15 changes it). |  |  |  |
| <a id="move"></a>`0x42` | move | `uint8` | V | Move: Battle_MoveRangeSetup caps it at 124; the move range's start budget is move + 1. | [Battle_MoveRangeSetup](../functions/Battle_MoveRangeSetup.md) |  |  |
| <a id="jump"></a>`0x43` | jump | `uint8` | V | Jump: Battle_MoveRangeSetup caps it at 7; a step may differ by 2 * jump half-steps and a jump passes over jump / 2 tiles. | [Battle_MoveRangeSetup](../functions/Battle_MoveRangeSetup.md) |  |  |
| <a id="weapon_power"></a>`0x44` | weapon_power | `uint8[2]` | V | Weapon power of +0x20 / +0x24 (ItemWeaponRecord +4), written by Unit_LoadEquipmentAndEvade. |  |  |  |
| <a id="weapon_evade"></a>`0x46` | weapon_evade | `uint8[2]` | V | Weapon evade of +0x20 / +0x24 (ItemWeaponRecord +5). |  |  |  |
| <a id="phys_evade"></a>`0x48` | phys_evade | `uint8[3]` | V | Accessory, first shield, second shield sub-record byte 0 (I: physical evade). |  |  |  |
| <a id="class_evade"></a>`0x4B` | class_evade | `uint8` | V | JobTable byte 26 of the unit's job (Unit_LoadEquipmentAndEvade). |  |  |  |
| <a id="magic_evade"></a>`0x4C` | magic_evade | `uint8[3]` | V | Accessory, first shield, second shield sub-record byte 1 (I: magic evade). |  |  |  |
| <a id="tile_x"></a>`0x4F` | tile_x | `uint8` | V | Map tile x (the range builders seed from it). | [BattleRange_MarkStrikeOrLunge](../functions/BattleRange_MarkStrikeOrLunge.md), [BattleRange_MarkWeaponReach](../functions/BattleRange_MarkWeaponReach.md) |  |  |
| <a id="tile_y"></a>`0x50` | tile_y | `uint8` | V | Map tile y. | [BattleRange_MarkStrikeOrLunge](../functions/BattleRange_MarkStrikeOrLunge.md), [BattleRange_MarkWeaponReach](../functions/BattleRange_MarkWeaponReach.md) |  |  |
| <a id="layer_facing"></a>`0x51` | layer_facing | `uint8` | V | Bit 7 = map layer of the unit's tile (Unit_GetReachHeight indexes the tile table with it); low bits facing (playbook, live). | [Unit_GetReachHeight](../functions/Unit_GetReachHeight.md) |  |  |
| <a id="status_16_23"></a>`0x63` | status_16_23 | `uint8` | V | Status bits 16..23, status s = bit 0x80 >> (s & 7): 0x40 (Float) raises the reach height; 0x02 (Toad) makes Attack use item 0. | [Battle_MoveRangeSetup](../functions/Battle_MoveRangeSetup.md), [BattleRange_MarkWeaponReach](../functions/BattleRange_MarkWeaponReach.md), [Unit_GetReachHeight](../functions/Unit_GetReachHeight.md) |  |  |
| <a id="spawn_byte_4"></a>`0x4` | spawn_byte_4 | `uint8` | V | Copied from spawn entry +23 (Unit_ApplySpawnRecord); its meaning is not decoded. |  |  |  |
| <a id="side_presence"></a>`0x5` | side_presence | `uint8` | V | Copied from spawn entry +24 (also to +0x1EE): bits 0x30 = side, bits 0xC0 = presence at battle start (Battle_PlaceEntryUnits: 0x00 off the field unless a preview unit shares the marker, 0x40 one random bit decides, 0x80 placed, 0xC0 built and look queued but not on the field and not counted). |  |  |  |
| <a id="spawn_byte_28"></a>`0x28` | spawn_byte_28 | `uint8` | V | From spawn entry +28 (above 99 = random 0..99). |  |  |  |
| <a id="level"></a>`0x29` | level | `uint8` | V | Level, from spawn entry +3 by Unit_ApplySpawnRecord (clamped 1..99). |  |  |  |
| <a id="brave_base"></a>`0x2A` | brave_base | `uint8` | V | Written from spawn entry +6 together with +0x2B (that +0x2A is a base copy is I). |  |  |  |
| <a id="brave"></a>`0x2B` | brave | `uint8` | V | Brave (spawn entry +6; above 100 replaced by 45 + random 0..29). |  |  |  |
| <a id="faith_base"></a>`0x2C` | faith_base | `uint8` | V | Written from spawn entry +7 together with +0x2D (that +0x2C is a base copy is I). |  |  |  |
| <a id="faith"></a>`0x2D` | faith | `uint8` | V | Faith (spawn entry +7, same rule as Brave). |  |  |  |
| <a id="name_string"></a>`0x14C` | name_string | `uint8[64]` | V | The unit's own name string (UnitWork_SetNameKey: save record +0xDC). |  |  |  |
| <a id="spawn_tail"></a>`0x197` | spawn_tail | `uint8[7]` | V | Copied from spawn entry +33..+39 (Unit_ApplySpawnRecord). |  |  |  |
| <a id="spawn_flags"></a>`0x1F8` | spawn_flags | `uint32` | V | The spawn flag set: OverrideEntryData flag bytes as bits 0..10, stored by Battle_PlaceEntryUnits. One bit per flag byte (OverrideEntryData +0x8E..+0x97 and +0x99 as bits 0..10, bit 11 from the equipment build): see the registry UnitEventFlagBit and the behaviour UnitEventFlagWord. |  |  |  |
| <a id="growth_pairs"></a>`0x8A` | growth_pairs | `uint8[10]` | V | Five (growth constant, multiplier) byte pairs for the stats HP, MP, Speed, PA, MA in that order (Unit_ComputeStats reads work +138 + 2 i); sub_1401EA910 adds the OverrideEntryData play-mode arrays to the HP pair (+138 / +139) and the Speed pair (+142 / +143). |  |  |  |
| <a id="name_key"></a>`0x1FC` | name_key | `uint32` | V | Name key (CharaName table), set by UnitWork_SetNameKey; read by CharaName_GetDisplayName callers. |  |  |  |
| <a id="ko_counter"></a>`0x7` | ko_counter | `uint8` | V | The KO counter: Unit_SetStatusCountdown sets it to 3 when KO is applied (0xFF when +5 bit 2 or +6 bits 0x09 are set: the unit never crystallises); BTurn_OnTurnStartStatus counts it down at the turn start; at 0 the unit becomes a crystal or a chest. |  |  | [Unit_InitBattleStatusState](../functions/Unit_InitBattleStatusState.md) |
| <a id="innate_status_a"></a>`0x57` | innate_status_a | `uint8[5]` | V | Status set (40 bits, status s = bit 0x80 >> (s & 7) of byte s >> 3): the statuses the unit always has = job row status_a \| equipment status_a (UnitWork_ApplyJobRow, Unit_ReloadFromJobRow, Unit_ApplyEquipment). Timed statuses (24..39) in it never expire. | [EventUnitStatus_SaveAndHide](../functions/EventUnitStatus_SaveAndHide.md), [Unit_InitBattleStatusState](../functions/Unit_InitBattleStatusState.md), [Unit_SetChargeStateBits](../functions/Unit_SetChargeStateBits.md) |  |  |
| <a id="innate_status_b"></a>`0x5C` | innate_status_b | `uint8[5]` | V | Status set: the statuses the unit is immune to = job row status_b \| equipment status_b. Status_FilterPendingSets drops them from a pending add; Unit_ReinitStatusCountdowns removes the always-on ones from it. |  |  |  |
| <a id="status_effective"></a>`0x61` | status_effective | `uint8[5]` | V | The effective status set the behaviour code tests: always innate_status_a \| applied_status (Battle_StatusApply, Battle_StatusRefresh, Unit_ReinitStatusCountdowns, Unit_ReloadFromJobRow all end with that OR). Byte 2 is status_16_23 below. A job row's status_c is copied here only until the next recompute. | [Ai_StatusLastsTurns](../functions/Ai_StatusLastsTurns.md), [Battle_StatusResolve](../functions/Battle_StatusResolve.md), [EventUnitStatus_SaveAndHide](../functions/EventUnitStatus_SaveAndHide.md), [Unit_InitBattleStatusState](../functions/Unit_InitBattleStatusState.md), [Unit_SetChargeStateBits](../functions/Unit_SetChargeStateBits.md) | [StatusesAreFortyBitSetsInEightRegions](../behaviors/StatusesAreFortyBitSetsInEightRegions.md), [StatusBitWritersAndTheRemovalPath](../behaviors/StatusBitWritersAndTheRemovalPath.md) | [Unit_SetChargeStateBits](../functions/Unit_SetChargeStateBits.md) |
| <a id="status_countdown"></a>`0x66` | status_countdown | `uint8[16]` | V | Remaining duration (CT ticks) of the statuses 24..39, byte = id - 24: started from the property table (+3) by Unit_SetStatusCountdown, decremented once per engine pass for battle-applied, non-innate statuses (Battle_TurnEngine phase 4); Doom (byte 15) counts at the unit's turn start. | [Ai_StatusLastsTurns](../functions/Ai_StatusLastsTurns.md), [EventUnitStatus_SaveAndHide](../functions/EventUnitStatus_SaveAndHide.md) |  | [Unit_InitBattleStatusState](../functions/Unit_InitBattleStatusState.md) |
| <a id="charge_counter"></a>`0x18D` | charge_counter | `uint8` | V | The remaining charge time of a Readying or Jumping unit (0xFF = none); Battle_StatusResolve sets 0xFF when none of Readying, Jumping, Performing is set. | [Ai_StatusLastsTurns](../functions/Ai_StatusLastsTurns.md) |  | [Battle_StatusResolve](../functions/Battle_StatusResolve.md), [Unit_SetChargeStateBits](../functions/Unit_SetChargeStateBits.md) |
| <a id="pending_status_add"></a>`0x1DB` | pending_status_add | `uint8[5]` | V | The statuses the action or event in progress wants to give (result block +29): written by the formulas, the turn-start rules, the tile effects and event opcode 0x92; consumed by Battle_StatusResolve and cleared by Battle_ResultResetStatusSets. | [StatusList_BuildFromResultBlock](../functions/StatusList_BuildFromResultBlock.md) | [StatusesAreFortyBitSetsInEightRegions](../behaviors/StatusesAreFortyBitSetsInEightRegions.md) | [Battle_ResultResetStatusSets](../functions/Battle_ResultResetStatusSets.md) |
| <a id="pending_status_remove"></a>`0x1E0` | pending_status_remove | `uint8[5]` | V | The statuses the action or event in progress wants to take away (result block +34); Status_FilterPendingSets limits it to applied statuses that are not innate. | [StatusList_BuildFromResultBlock](../functions/StatusList_BuildFromResultBlock.md) | [StatusesAreFortyBitSetsInEightRegions](../behaviors/StatusesAreFortyBitSetsInEightRegions.md) | [Battle_ResultResetStatusSets](../functions/Battle_ResultResetStatusSets.md), [EventUnitStatus_SaveAndHide](../functions/EventUnitStatus_SaveAndHide.md) |
| <a id="applied_status"></a>`0x1EF` | applied_status | `uint8[5]` | V | The statuses applied in battle: the only set Battle_StatusApply sets and Battle_StatusRefresh clears (the engine decrements the countdown of its timed members). | [EventUnitStatus_SaveAndHide](../functions/EventUnitStatus_SaveAndHide.md) | [StatusesAreFortyBitSetsInEightRegions](../behaviors/StatusesAreFortyBitSetsInEightRegions.md), [StatusBitWritersAndTheRemovalPath](../behaviors/StatusBitWritersAndTheRemovalPath.md) | [Unit_InitBattleStatusState](../functions/Unit_InitBattleStatusState.md), [Unit_SetChargeStateBits](../functions/Unit_SetChargeStateBits.md) |
| <a id="passive_bits"></a>`0x94` | passive_bits | `uint8[11]` | V | Passive-ability bit map, 88 bits for the ids 422..509 (bit 0x80 >> (index & 7) of byte +0x94 + (index >> 3), index = id - 422); the last three bytes (+0x9C..+0x9E) are the ones also listed below as move_flags_c, move_flags_d and move_flags. | [sub_14030BE18](../functions/sub_14030BE18.md) | [PassiveAbilitiesAreAPerUnitBitMap](../behaviors/PassiveAbilitiesAreAPerUnitBitMap.md), [AfterDamageReactionChain](../behaviors/AfterDamageReactionChain.md), [AbilityAboveStockBoundaryHasNoMpCheckOrCost](../behaviors/AbilityAboveStockBoundaryHasNoMpCheckOrCost.md) | [Unit_BuildAbilityBits](../functions/Unit_BuildAbilityBits.md), [Unit_SetAbilityBit](../functions/Unit_SetAbilityBit.md) |
| <a id="passive_bits_halve_mp"></a>`0x99` | passive_bits_halve_mp | `uint8` | V | Byte 5 of the passive map: bit 0x80 (id 462) halves the MP cost of an action (sub_1402828E4, sub_14030B1A0); bit 0x40 (id 463) is the JP Boost test of the JP award. | [sub_1402828E4](../functions/sub_1402828E4.md), [sub_14030B1A0](../functions/sub_14030B1A0.md) |  |  |
| <a id="move_flags_c"></a>`0x9C` | move_flags_c | `uint8` | V | Bit 0x02: Battle_MoveRangeSetup sets the jump to 31 (no height limit). | [Battle_MoveRangeSetup](../functions/Battle_MoveRangeSetup.md) |  |  |
| <a id="move_flags_d"></a>`0x9D` | move_flags_d | `uint8` | V | Battle_MoveRangeSetup: bits 0x0C select Teleport (cleared for Toad / Chicken); 0x10 keeps the unit out of water; 0x02 makes the weather-dependent terrains cost 1; 0x01 makes every enterable terrain cost 1. | [Battle_MoveRangeSetup](../functions/Battle_MoveRangeSetup.md) |  |  |
| <a id="move_flags"></a>`0x9E` | move_flags | `uint8` | V | Bit 0x08 raises the reach height like Float; bits 0x80 / 0x40 add the tile's water depth / depth - 2 (Unit_GetReachHeight). Battle_MoveRangeSetup picks the movement mode from it: 0x04 Fly, 0x08 float, 0x20, 0x80, 0x40, 0x10 the lava and water modes (record MoveRangeScratch). I: movement-ability flags. | [Battle_MoveRangeSetup](../functions/Battle_MoveRangeSetup.md), [Unit_GetReachHeight](../functions/Unit_GetReachHeight.md) |  |  |
| <a id="unlock_mask"></a>`0x9F` | unlock_mask | `uint8[3]` | V | Unlock bits (Unit_AwardJobJp rebuilds them after an award). |  |  |  |
| <a id="learned"></a>`0xA2` | learned | `uint8[66]` | V | Learned-ability bits. |  |  |  |
| <a id="job_levels"></a>`0xE4` | job_levels | `uint8[12]` | V | Job level nibbles. |  |  |  |
| <a id="jp"></a>`0xF0` | jp | `uint16[23]` | V | Current JP (Unit_AwardJobJp adds to it). |  |  |  |
| <a id="total_jp"></a>`0x11E` | total_jp | `uint16[23]` | V | Total JP. |  |  |  |
| <a id="confirm_result"></a>`0x194` | confirm_result | `int32` | V | The result of the target-confirm shape routine (sub_140206F90): -1 drops the confirm, 0 or 1 opens the target confirmation (battle state 25), 2 starts the charge motion, 3 and above do nothing. |  |  | [sub_140206F90](../functions/sub_140206F90.md) |
| <a id="action_request"></a>`0x1A0` | action_request | `uint8[20]` | V | The unit's pending 20-byte action block (+1 command byte, +2 ability id u16). Only four direct stores write it (BattleAction_BuildUnitRequest 0x1402832AD, sub_1402831D8 0x140283235, Formula_37_RendEquipment 0x140307EB9 and its restore 0x140307EED); every other copy (the request queue, BattleAction_BuildReaction, BattleAction_ReleaseCharged, Battle_ExecuteSecondaryAction, BTurn_PreviewAction, the AI current action) is a call of Mem_CopyChecked with size 0x14. BTurn_PreviewAction saves and restores it around a preview. | [BTurn_PreviewAction](../functions/BTurn_PreviewAction.md) |  | [BTurn_PreviewAction](../functions/BTurn_PreviewAction.md), [Mem_CopyChecked](../functions/Mem_CopyChecked.md) |
| <a id="action_command"></a>`0x1A1` | action_command | `uint8` | V | The command (skillset) byte of the request (index into g_CommandKind; 18 = jump); TurnList_InsertEntry writes bit 0x20 of a turn entry when it is 18. A byte holds sets up to 253. The name token of the command is 0xB000 plus this byte (BattleMsg_UnitTurnScene 0x14023750F). | [sub_140217630](../functions/sub_140217630.md), [sub_1402828E4](../functions/sub_1402828E4.md) | [BattleCommandMenuCarriesSetsAsBytes](../behaviors/BattleCommandMenuCarriesSetsAsBytes.md) |  |
| <a id="action_ability"></a>`0x1A2` | action_ability | `uint16` | V | The ability word of the request; the turn order and the action message read it; BTurn_PreviewAction restores the block. | [sub_1402828E4](../functions/sub_1402828E4.md) |  |  |
| <a id="mount"></a>`0x1B4` | mount | `uint8` | V | Bit 7: Unit_GetReachHeight adds 2 and reads the flags of the record at slot (low 5 bits). I: riding, the low bits the mount. Battle_MoveRangeSetup also reads bit 6 with the low 5 bits (a unit paired with the acting unit is not an obstacle). | [Battle_MoveRangeSetup](../functions/Battle_MoveRangeSetup.md), [Unit_GetReachHeight](../functions/Unit_GetReachHeight.md) |  |  |
| <a id="side"></a>`0x1EE` | side | `uint8` | V | Battle_MoveRangeSetup compares bits 0x30 of every other unit's byte +0x05 with this byte of the acting unit: different = the other side (an obstacle). I: the side the unit currently fights for. | [Battle_MoveRangeSetup](../functions/Battle_MoveRangeSetup.md) |  |  |

## Behavior

- V: UnitWork_CopySaveFields fills the arrays from a save record; UnitWork_StoreToSaveSlot writes them back.
- V (2026-11-10): the Toad restriction on abilities tests status byte +0x63 mask 0x02 (sub_1402828E4, sub_14030B1A0): a Toad unit may use only ability 0, 367 and 29 (a command kind of 10 never).
- V: the passive-ability map is rebuilt by Unit_BuildAbilityBits; see PassiveAbilitiesAreAPerUnitBitMap.

## Referenced by

- Observed behaviours: [UnitEventFlagWord](../behaviors/UnitEventFlagWord.md)
- Read by: [Unit_HasStatusGroup](../functions/Unit_HasStatusGroup.md)
- Written by: [BattleAction_ApplyRequest](../functions/BattleAction_ApplyRequest.md), [Unit_BuildInnateStatuses](../functions/Unit_BuildInnateStatuses.md), [Unit_ReinitStatusCountdowns](../functions/Unit_ReinitStatusCountdowns.md)

## Notes

Detail and evidence: the function sheets linked from this page.

## Open questions

None recorded.
