# NxdDataOverrideEntryDataRow

- **Kind:** structure
- **Area:** [Battle](../areas/battle.md)
- **Size:** 160 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.override_entry_data table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: 0 in every row. |
| <a id="unknown04"></a>`0x4` | unknown04 | `string (int32 offset)` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: empty in every row. |
| <a id="sprite_shape"></a>`0x8` | sprite_shape | `uint32` | V | Read in the code: A non-zero value becomes the first byte of the unit's spawn entry, which Unit_ApplySpawnRecord keeps as the unit's byte +0, the sprite shape selector (1..0x7F is a shape id itself; 0x80 / 0x81 generic male / female whose shape follows the job; other values special looks). Observed in the stock rows: 0 to 48, 5 distinct values. |
| <a id="chara_name"></a>`0xC` | chara_name | `uint32` | V | Read in the code: When not 0 it becomes the unit's name key; every non-zero value in the rows is a key of nxd.CharaName. Observed in the stock rows: 0 to 764, 41 distinct values. |
| <a id="job"></a>`0x10` | job | `uint32` | V | Read in the code: When not 0 it becomes the unit's job (one byte). Observed in the stock rows: 0 to 173, 8 distinct values. |
| <a id="leveled_job"></a>`0x14` | leveled_job | `uint32` | V | Read in the code: The generic job (0..19) whose level is set; 20 = keep. Observed in the stock rows: 0 to 20, 10 distinct values. |
| <a id="skillset"></a>`0x18` | skillset | `int32` | V | Read in the code: A row value of 1..254 becomes the unit's primary skillset (command set) through spawn entry +0x1D; a negative value (the stock -1) leaves the entry unchanged, and 0 or 255 and above are stored but ignored by the consumer, so the job's own skillset stays. Observed in the stock rows: -1 in every row. |
| <a id="secondary_skillset"></a>`0x1C` | secondary_skillset | `int32` | V | Read in the code: When 0 or more it becomes the unit's second command. Observed in the stock rows: -1 to 18, 10 distinct values. |
| <a id="reaction"></a>`0x20` | reaction | `int32` | V | Read in the code: When 0 or more it becomes the unit's reaction ability. Observed in the stock rows: -1 to 451, 8 distinct values. |
| <a id="support"></a>`0x24` | support | `int32` | V | Read in the code: When 0 or more it becomes the unit's support ability. Observed in the stock rows: -1 to 479, 7 distinct values. |
| <a id="movement"></a>`0x28` | movement | `int32` | V | Read in the code: When 0 or more it becomes the unit's movement ability. Observed in the stock rows: -1 to 509, 6 distinct values. |
| <a id="head"></a>`0x2C` | head | `int32` | V | Read in the code: Starting head item of a pre-placed unit without a save record (-1 = keep the entry's value; 0xFE in the entry = pick a default). Observed in the stock rows: -1 to 255, 4 distinct values. |
| <a id="body"></a>`0x30` | body | `int32` | V | Read in the code: Starting body item of a pre-placed unit without a save record (-1 = keep). Observed in the stock rows: -1 to 186, 3 distinct values. |
| <a id="accessory"></a>`0x34` | accessory | `int32` | V | Read in the code: Starting accessory of a pre-placed unit without a save record (-1 = keep). Observed in the stock rows: -1 in every row. |
| <a id="right_hand"></a>`0x38` | right_hand | `int32` | V | Read in the code: Starting item of the first hand (weapon or shield) of a pre-placed unit without a save record (-1 = keep). Observed in the stock rows: -1 to 62, 4 distinct values. |
| <a id="left_hand"></a>`0x3C` | left_hand | `int32` | V | Read in the code: Starting item of the second hand (weapon or shield) of a pre-placed unit without a save record (-1 = keep). Observed in the stock rows: -1 in every row. |
| <a id="facing"></a>`0x40` | facing | `int32` | V | Read in the code: When not 255 it becomes the unit's facing. Observed in the stock rows: 0 to 255, 3 distinct values. |
| <a id="chara_control"></a>`0x44` | chara_control | `int32` | V | Read in the code: When not 0, a key of nxd.CharaControlId. Observed in the stock rows: 0 to 2, 2 distinct values. |
| <a id="presence"></a>`0x48` | presence | `int32` | V | Read in the code: Its top two bits choose whether the unit is on the field at battle start: 0x80 placed; 0x40 placed or not on a 50 % roll; 0xC0 built and its look loaded but kept off the field; 0x00 kept off unless the same unit is already present (one battle mode). 255 = keep the entry's bits. Observed in the stock rows: 0 to 255, 2 distinct values. |
| <a id="granted_abilities"></a>`0x4C` | granted_abilities | `int32[] {int32 offset; uint32 count}` | V | Read in the code: Ability ids (one i32 each, low 16 bits used) of the unit's skillsets that the unit starts with learned; free of charge when the byte +0x9A is set. Observed in the stock rows: 22 distinct values. |
| <a id="withheld_abilities"></a>`0x54` | withheld_abilities | `int32[] {int32 offset; uint32 count}` | V | Read in the code: Ability ids (i32 elements) of the unit's skillsets that the second learning pass leaves out: every other ability of the job's skillsets is bought with the unit's JP when affordable. Observed in the stock rows: 6 distinct values. |
| <a id="hp_growth_constant_bonus"></a>`0x5C` | hp_growth_constant_bonus | `int16[] {int32 offset; uint32 count}` | V | Read in the code: I16 array indexed by the play mode (configuration byte +196 = DifficultyLevel row id): the element is added to the unit's HP growth constant (work +138) after the job row is copied, only if the sum stays at 254 or below. Observed in the stock rows: 6 distinct values. |
| <a id="hp_multiplier_bonus"></a>`0x64` | hp_multiplier_bonus | `int16[] {int32 offset; uint32 count}` | V | Read in the code: I16 array indexed by the play mode: the element is added to the unit's HP growth multiplier (work +139), capped so the sum stays at 254 or below. Observed in the stock rows: 32 distinct values. |
| <a id="speed_growth_constant_bonus"></a>`0x6C` | speed_growth_constant_bonus | `int16[] {int32 offset; uint32 count}` | V | Read in the code: I16 array indexed by the play mode: the element is added to the unit's Speed growth constant (work +142). Observed in the stock rows: 1 distinct values. |
| <a id="speed_multiplier_bonus"></a>`0x74` | speed_multiplier_bonus | `int16[] {int32 offset; uint32 count}` | V | Read in the code: I16 array indexed by the play mode: the element is added to the unit's Speed growth multiplier (work +143). Observed in the stock rows: 19 distinct values. |
| <a id="level"></a>`0x7C` | level | `int16` | V | Read in the code: Level of a pre-placed unit (> 0 overrides): 1..99 as given, 100..253 = highest party level + value - 100, 254 = random just below the highest party level. Observed in the stock rows: -1 to 254, 4 distinct values. |
| <a id="job_level"></a>`0x7E` | job_level | `int16` | V | Read in the code: The level given to that job. Observed in the stock rows: -1 to 8, 6 distinct values. |
| <a id="speed_bonus"></a>`0x80` | speed_bonus | `int16` | V | Read in the code: Layout boundary: +0x80..+0x81 is ONE i16; when non-zero it is added to the unit's final Speed (work +58) after the Speed formula (which is clamped to 50 first). |
| <a id="brave"></a>`0x82` | brave | `int16` | V | Read in the code: Brave of a pre-placed unit (>= 0 overrides; above 100 = random 45..74). Observed in the stock rows: -1 in every row. |
| <a id="faith"></a>`0x84` | faith | `int16` | V | Read in the code: Faith of a pre-placed unit (>= 0 overrides; above 100 = random 45..74). Observed in the stock rows: -1 in every row. |
| <a id="unknown86"></a>`0x86` | unknown86 | `uint8` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: 0 in every row. |
| <a id="unknown87"></a>`0x87` | unknown87 | `uint8` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: 0 in every row. |
| <a id="tile_x"></a>`0x88` | tile_x | `int16` | V | Read in the code: When 0 or more it becomes the unit's tile x. Observed in the stock rows: -1 to 7, 7 distinct values. |
| <a id="tile_y"></a>`0x8A` | tile_y | `int16` | V | Read in the code: When 0 or more it becomes the unit's tile y. Observed in the stock rows: -1 to 6, 5 distinct values. |
| <a id="upper_level"></a>`0x8C` | upper_level | `uint8` | V | Read in the code: 0 or 1 sets the unit's upper height layer bit. Observed in the stock rows: 0 to 255, 3 distinct values. |
| <a id="remove_unit"></a>`0x8D` | remove_unit | `uint8` | V | Read in the code: Non-zero empties the unit's entry. Observed in the stock rows: 0 in every row. |
| <a id="special"></a>`0x8E` | special | `uint8` | V | Read in the code: Bit 0 of unit +504 gives the unit the 'Special' presentation: yellow panel background and the 'ShowSpecial' tag in the unit panel, marker kind 4 instead of 2 on the tiles, unit category 3 in the side classifier. I: this is how a guest ally (computer-controlled, team 0) is marked; the panel's 'ShowGuest' state is chosen by a different byte (unit info +186 = 2). Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="flag_1"></a>`0x8F` | flag_1 | `uint8` | V | Read in the code: Non-zero sets bit 1 of the entry's flag word. Observed in the stock rows: 0 in every row. |
| <a id="target_rescue"></a>`0x90` | target_rescue | `uint8` | V | Read in the code: Bit 2 marks the unit as an objective target, shown only while the active BattleObjective row has show_targets non-zero (BattleObjective_ShowsTarget), with the 'TargetRescue' marker and the 'ShowRescue' panel state. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="target_attack"></a>`0x91` | target_attack | `uint8` | V | Read in the code: Bit 3: the unit gets the 'TargetAttack' marker on the formation board and a stop in the objective camera tour. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="target_boss"></a>`0x92` | target_boss | `uint8` | V | Read in the code: Bit 4: the unit gets the 'TargetBoss' marker on the formation board and a stop in the objective camera tour. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="guest_join_panel"></a>`0x93` | guest_join_panel | `uint8` | V | Read in the code: Bit 5: when the preview-units event opcode (0xC1) runs the unit is put in the guest-join announcement (panel states 'Guest01to02', 'ShowGuest02StatusJoin'); the bit is cleared once its panel was shown. A set byte also makes EventScript_Run arm skip-once for the event (g_EventSkipOnce = 1: the event may be skipped only once; it becomes 2 after the first skip). Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="withdrawal_panel"></a>`0x94` | withdrawal_panel | `uint8` | V | Read in the code: Bit 6: the preview-units event opcode shows the unit's panel with the 'ShowWithdrawal' state (sound 0xA5, event 0x411) once and clears the bit; also makes EventScript_Run arm skip-once for the event (g_EventSkipOnce 0x142FF9EBC = 1: the event may be skipped only once). Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="betrayal_panel"></a>`0x95` | betrayal_panel | `uint8` | V | Read in the code: Bit 7: the preview-units event opcode shows the unit's panel with the 'ShowGafgarionBetrayal' state (sound 0xA6, event 0x410, battle voices assigned) once and clears the bit; also makes EventScript_Run arm skip-once for the event (g_EventSkipOnce 0x142FF9EBC = 1: the event may be skipped only once). Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="flag_8"></a>`0x96` | flag_8 | `uint8` | V | Read in the code: Non-zero sets bit 8 of the entry's flag word. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="flag_9"></a>`0x97` | flag_9 | `uint8` | V | Read in the code: Non-zero sets bit 9 of the entry's flag word. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="from_guest_record"></a>`0x98` | from_guest_record | `uint8` | V | Read in the code: Non-zero builds the unit from the guest save record (slots 50..53) whose marker equals the entry's marker, instead of from the entry. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="acts_first"></a>`0x99` | acts_first | `uint8` | V | Read in the code: Bit 10 (0x400): as soon as any unit has CT above 99, the turn engine lets a unit with this bit act first (its own CT does not have to be above 99); its CT is then set to the highest CT found and the bit is cleared. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="free_abilities"></a>`0x9A` | free_abilities | `uint8` | V | Read in the code: Non-zero: the listed abilities (spawn reaction / support / movement words plus the +0x4C array) are learned without charging the unit's JP. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown9b"></a>`0x9B` | unknown9b | `uint8` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: 0 in every row. |
| <a id="unknown9c"></a>`0x9C` | unknown9c | `uint8` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: 0 to 244, 94 distinct values. |

## Referenced by

- Described by tables: [NxdDataOverrideEntryData](../tables/NxdDataOverrideEntryData.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

None recorded.
