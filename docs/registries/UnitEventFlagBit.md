# UnitEventFlagBit

- **Kind:** registry
- **Area:** [Unit data](../areas/unit-data.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The bits of the unit flag word at battle unit +504, which the battle build stores from the entry override row: one bit per flag byte (OverrideEntryData +0x8E..+0x97 and +0x99), plus bit 11 set by the equipment build.

## Entries

| Id | Name | Value | Conf | Meaning |
|---|---|---|---|---|
| <a id="special"></a>0 | `special` | `0x1` | V | Column special (+0x8E): the unit shows the 'Special' presentation (yellow panel background, 'ShowSpecial'); sub_14036099C reports side category 3 for it; its tile marker is kind 4 instead of 2. |
| <a id="flag_1"></a>1 | `flag_1` | `0x2` | V | Column flag_1 (+0x8F): the unit's byte +401 is added to the list dword_1437A02D0 (sub_1401EE9B4) and sub_1401F5AFC treats the unit as valid. The reason is not known. |
| <a id="target_rescue"></a>2 | `target_rescue` | `0x4` | V | Column target_rescue (+0x90): the unit is an objective target while the active BattleObjective row has show_targets (BattleObjective_ShowsTarget): marker 'TargetRescue', panel state 'ShowRescue', and a stop of the objective camera tour. |
| <a id="target_attack"></a>3 | `target_attack` | `0x8` | V | Column target_attack (+0x91): marker 'TargetAttack' on the formation board, a stop of the objective camera tour (sub_1401EA2F0), and the turn panel's tag state 4. |
| <a id="target_boss"></a>4 | `target_boss` | `0x10` | V | Column target_boss (+0x92): marker 'TargetBoss', a stop of the objective camera tour, tag state 4. |
| <a id="guest_join_panel"></a>5 | `guest_join_panel` | `0x20` | V | Column guest_join_panel (+0x93): the preview-units event opcode runs the guest-join announcement (sub_14013F71C, states 'Guest01to02' / 'ShowGuest02StatusJoin') and clears the bit. |
| <a id="withdrawal_panel"></a>6 | `withdrawal_panel` | `0x40` | V | Column withdrawal_panel (+0x94): the preview-units opcode shows the withdrawal announcement (sub_140214404, sound 0xA5) and clears the bit. |
| <a id="betrayal_panel"></a>7 | `betrayal_panel` | `0x80` | V | Column betrayal_panel (+0x95): the preview-units opcode shows the betrayal announcement (sub_140214610, sound 0xA6, BattleVoice_AssignPatterns) and clears the bit. |
| <a id="flag_8"></a>8 | `flag_8` | `0x100` | ? | Column flag_8 (+0x96): no reader of the bit was found. |
| <a id="flag_9"></a>9 | `flag_9` | `0x200` | ? | Column flag_9 (+0x97): no reader of the bit was found. |
| <a id="acts_first"></a>10 | `acts_first` | `0x400` | V | Column acts_first (+0x99): Battle_TurnEngine phase 1 lets a unit with the bit act first once any unit has CT above 99; its CT is set to the highest CT and the bit is cleared. |
| <a id="equipment_flag"></a>11 | `equipment_flag` | `0x800` | V | Not from the row: Unit_ApplyEquipment sets or clears it from the equipment attribute record's byte 25; Battle_AwardUnitJp and sub_14030C5A0 read it. |

## Behavior

- V: OverrideEntry_FillUnitEntry builds bits 0..10 in order from the flag bytes (each non-zero byte sets its bit); Battle_PlaceEntryUnits stores the word at unit +504.

## Referenced by

- Observed behaviours: [UnitEventFlagWord](../behaviors/UnitEventFlagWord.md)

## Notes

Behaviour: UnitEventFlagWord. The bit names are ours.

## Open questions

? the role of bits 1, 8 and 9 (bit 11's first reader sheets are not read here).
