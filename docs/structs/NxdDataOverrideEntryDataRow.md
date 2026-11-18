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
| <a id="unk_00"></a>`0x0` | unk_00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unk_04"></a>`0x4` | unk_04 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: empty in every row. |
| <a id="spriteset"></a>`0x8` | spriteset | `uint32` | I | If non-zero, replaces the unit's sprite set (marker); Disable=1 sets it to 0. Observed in the stock rows: 0 to 48, 5 distinct values. |
| <a id="unk_0c"></a>`0xC` | unk_0c | `uint32` | ? | Not decoded. Observed in the stock rows: 0 to 764, 41 distinct values. |
| <a id="main_job"></a>`0x10` | main_job | `uint32` | I | Job key forced on the unit; 0 = keep. Values 2, 154, 169..173 (story / variant jobs). Observed in the stock rows: 0 to 173, 8 distinct values. |
| <a id="job_unlock"></a>`0x14` | job_unlock | `uint32` | I | Generic job index (0..19) the unit is given as an unlocked job; 20 = none (503 of 516 rows). Observed in the stock rows: 0 to 20, 10 distinct values. |
| <a id="entry_unknown1_d"></a>`0x18` | entry_unknown1_d | `int32` | I | Entry unknown1 d (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: -1 in every row. |
| <a id="secondary_skillset"></a>`0x1C` | secondary_skillset | `int32` | I | JobCommand key for the secondary command; -1 = keep. Values 5..18 are generic commands (6 = Items, 9 = Martial Arts...). Observed in the stock rows: -1 to 18, 10 distinct values. |
| <a id="reaction"></a>`0x20` | reaction | `int32` | I | Ability key of the reaction ability (427..451 = Dragonheart, Counter, Shirahadori...); -1 keep. Observed in the stock rows: -1 to 451, 8 distinct values. |
| <a id="support"></a>`0x24` | support | `int32` | I | Support ability key (465..479). Observed in the stock rows: -1 to 479, 7 distinct values. |
| <a id="movement"></a>`0x28` | movement | `int32` | I | Movement ability key (486..509). Observed in the stock rows: -1 to 509, 6 distinct values. |
| <a id="head"></a>`0x2C` | head | `int32` | I | Head (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: -1 to 255, 4 distinct values. |
| <a id="body"></a>`0x30` | body | `int32` | I | Body (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: -1 to 186, 3 distinct values. |
| <a id="accessory"></a>`0x34` | accessory | `int32` | I | Accessory (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: -1 in every row. |
| <a id="right_hand"></a>`0x38` | right_hand | `int32` | I | Right hand (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: -1 to 62, 4 distinct values. |
| <a id="left_hand"></a>`0x3C` | left_hand | `int32` | I | Left hand (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: -1 in every row. |
| <a id="initial_direction"></a>`0x40` | initial_direction | `int32` | I | Initial direction (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 0 to 255, 3 distinct values. |
| <a id="unit_id_characontrolid_id"></a>`0x44` | unit_id_characontrolid_id | `int32` | I | Unit id characontrolid id (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 0 to 2, 2 distinct values. |
| <a id="present"></a>`0x48` | present | `int32` | I | Present (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 0 to 255, 2 distinct values. |
| <a id="unk_4c"></a>`0x4C` | unk_4c | `int32[] {int32 offset; uint32 count}` | ? | Not decoded. Observed in the stock rows: 22 distinct values. |
| <a id="unk_54"></a>`0x54` | unk_54 | `int32[] {int32 offset; uint32 count}` | ? | Not decoded. Observed in the stock rows: 6 distinct values. |
| <a id="unk_5c"></a>`0x5C` | unk_5c | `int16[] {int32 offset; uint32 count}` | ? | Not decoded. Observed in the stock rows: 6 distinct values. |
| <a id="unk_64"></a>`0x64` | unk_64 | `int16[] {int32 offset; uint32 count}` | ? | Not decoded. Observed in the stock rows: 32 distinct values. |
| <a id="unk_6c"></a>`0x6C` | unk_6c | `int16[] {int32 offset; uint32 count}` | ? | Not decoded. Observed in the stock rows: 1 distinct values. |
| <a id="unk_74"></a>`0x74` | unk_74 | `int16[] {int32 offset; uint32 count}` | ? | Not decoded. Observed in the stock rows: 19 distinct values. |
| <a id="level"></a>`0x7C` | level | `int16` | I | Unit level. Observed in the stock rows: -1 to 254, 4 distinct values. |
| <a id="job_level"></a>`0x7E` | job_level | `int16` | I | Job level of the forced job (1..8); -1 keep. Observed in the stock rows: -1 to 8, 6 distinct values. |
| <a id="unk_80"></a>`0x80` | unk_80 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 255, 2 distinct values. |
| <a id="unk_81"></a>`0x81` | unk_81 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 255, 2 distinct values. |
| <a id="bravery"></a>`0x82` | bravery | `int16` | I | Bravery (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: -1 in every row. |
| <a id="faith"></a>`0x84` | faith | `int16` | I | Faith (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: -1 in every row. |
| <a id="unk_86"></a>`0x86` | unk_86 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unk_87"></a>`0x87` | unk_87 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="position_x"></a>`0x88` | position_x | `int16` | I | Position x (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: -1 to 7, 7 distinct values. |
| <a id="position_y"></a>`0x8A` | position_y | `int16` | I | Position y (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: -1 to 6, 5 distinct values. |
| <a id="higher_elevation"></a>`0x8C` | higher_elevation | `uint8` | I | Higher elevation (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 0 to 255, 3 distinct values. |
| <a id="disable"></a>`0x8D` | disable | `uint8` | I | Disable (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 0 in every row. |
| <a id="unk_8e"></a>`0x8E` | unk_8e | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unk_8f"></a>`0x8F` | unk_8f | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unk_90"></a>`0x90` | unk_90 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unk_91"></a>`0x91` | unk_91 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unk_92"></a>`0x92` | unk_92 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unk_93"></a>`0x93` | unk_93 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unk_94"></a>`0x94` | unk_94 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unk_95"></a>`0x95` | unk_95 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unk_96"></a>`0x96` | unk_96 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unk_97"></a>`0x97` | unk_97 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="load_formation"></a>`0x98` | load_formation | `uint8` | I | Load formation (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unk_99"></a>`0x99` | unk_99 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unk_9a"></a>`0x9A` | unk_9a | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unk_9b"></a>`0x9B` | unk_9b | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unk_9c"></a>`0x9C` | unk_9c | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 244, 94 distinct values. |

## Referenced by

- Described by tables: [NxdDataOverrideEntryData](../tables/NxdDataOverrideEntryData.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

27 of 52 columns not decoded.
