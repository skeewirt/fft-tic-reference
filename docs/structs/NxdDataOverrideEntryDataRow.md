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
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown04"></a>`0x4` | unknown04 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: empty in every row. |
| <a id="sprite_shape"></a>`0x8` | sprite_shape | `uint32` | V | Read in the code: When not 0 it becomes the first byte of the unit's entry, its sprite shape. Observed in the stock rows: 0 to 48, 5 distinct values. |
| <a id="chara_name"></a>`0xC` | chara_name | `uint32` | V | Read in the code: When not 0 it becomes the unit's name key; every non-zero value in the rows is a key of nxd.CharaName. Observed in the stock rows: 0 to 764, 41 distinct values. |
| <a id="job"></a>`0x10` | job | `uint32` | V | Read in the code: When not 0 it becomes the unit's job (one byte). Observed in the stock rows: 0 to 173, 8 distinct values. |
| <a id="leveled_job"></a>`0x14` | leveled_job | `uint32` | V | Read in the code: The generic job (0..19) whose level is set; 20 = keep. Observed in the stock rows: 0 to 20, 10 distinct values. |
| <a id="skillset"></a>`0x18` | skillset | `int32` | V | Read in the code: When 0 or more it becomes the unit's command. Observed in the stock rows: -1 in every row. |
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
| <a id="unknown4c"></a>`0x4C` | unknown4c | `int32[] {int32 offset; uint32 count}` | ? | Not decoded. Observed in the stock rows: 22 distinct values. |
| <a id="unknown54"></a>`0x54` | unknown54 | `int32[] {int32 offset; uint32 count}` | ? | Not decoded. Observed in the stock rows: 6 distinct values. |
| <a id="unknown5c"></a>`0x5C` | unknown5c | `int16[] {int32 offset; uint32 count}` | ? | Not decoded. Observed in the stock rows: 6 distinct values. |
| <a id="unknown64"></a>`0x64` | unknown64 | `int16[] {int32 offset; uint32 count}` | ? | Not decoded. Observed in the stock rows: 32 distinct values. |
| <a id="unknown6c"></a>`0x6C` | unknown6c | `int16[] {int32 offset; uint32 count}` | ? | Not decoded. Observed in the stock rows: 1 distinct values. |
| <a id="unknown74"></a>`0x74` | unknown74 | `int16[] {int32 offset; uint32 count}` | ? | Not decoded. Observed in the stock rows: 19 distinct values. |
| <a id="level"></a>`0x7C` | level | `int16` | V | Read in the code: Level of a pre-placed unit (> 0 overrides): 1..99 as given, 100..253 = highest party level + value - 100, 254 = random just below the highest party level. Observed in the stock rows: -1 to 254, 4 distinct values. |
| <a id="job_level"></a>`0x7E` | job_level | `int16` | V | Read in the code: The level given to that job. Observed in the stock rows: -1 to 8, 6 distinct values. |
| <a id="unknown80"></a>`0x80` | unknown80 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 255, 2 distinct values. |
| <a id="unknown81"></a>`0x81` | unknown81 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 255, 2 distinct values. |
| <a id="brave"></a>`0x82` | brave | `int16` | V | Read in the code: Brave of a pre-placed unit (>= 0 overrides; above 100 = random 45..74). Observed in the stock rows: -1 in every row. |
| <a id="faith"></a>`0x84` | faith | `int16` | V | Read in the code: Faith of a pre-placed unit (>= 0 overrides; above 100 = random 45..74). Observed in the stock rows: -1 in every row. |
| <a id="unknown86"></a>`0x86` | unknown86 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown87"></a>`0x87` | unknown87 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="tile_x"></a>`0x88` | tile_x | `int16` | V | Read in the code: When 0 or more it becomes the unit's tile x. Observed in the stock rows: -1 to 7, 7 distinct values. |
| <a id="tile_y"></a>`0x8A` | tile_y | `int16` | V | Read in the code: When 0 or more it becomes the unit's tile y. Observed in the stock rows: -1 to 6, 5 distinct values. |
| <a id="upper_level"></a>`0x8C` | upper_level | `uint8` | V | Read in the code: 0 or 1 sets the unit's upper height layer bit. Observed in the stock rows: 0 to 255, 3 distinct values. |
| <a id="remove_unit"></a>`0x8D` | remove_unit | `uint8` | V | Read in the code: Non-zero empties the unit's entry. Observed in the stock rows: 0 in every row. |
| <a id="flag_0"></a>`0x8E` | flag_0 | `uint8` | V | Read in the code: Non-zero sets bit 0 of the entry's flag word. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="flag_1"></a>`0x8F` | flag_1 | `uint8` | V | Read in the code: Non-zero sets bit 1 of the entry's flag word. Observed in the stock rows: 0 in every row. |
| <a id="flag_2"></a>`0x90` | flag_2 | `uint8` | V | Read in the code: Non-zero sets bit 2 of the entry's flag word. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="flag_3"></a>`0x91` | flag_3 | `uint8` | V | Read in the code: Non-zero sets bit 3 of the entry's flag word. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="flag_4"></a>`0x92` | flag_4 | `uint8` | V | Read in the code: Non-zero sets bit 4 of the entry's flag word. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="flag_5"></a>`0x93` | flag_5 | `uint8` | V | Read in the code: Non-zero sets bit 5 of the entry's flag word. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="flag_6"></a>`0x94` | flag_6 | `uint8` | V | Read in the code: Non-zero sets bit 6 of the entry's flag word. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="flag_7"></a>`0x95` | flag_7 | `uint8` | V | Read in the code: Non-zero sets bit 7 of the entry's flag word. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="flag_8"></a>`0x96` | flag_8 | `uint8` | V | Read in the code: Non-zero sets bit 8 of the entry's flag word. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="flag_9"></a>`0x97` | flag_9 | `uint8` | V | Read in the code: Non-zero sets bit 9 of the entry's flag word. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="from_guest_record"></a>`0x98` | from_guest_record | `uint8` | V | Read in the code: Non-zero builds the unit from the guest save record (slots 50..53) whose marker equals the entry's marker, instead of from the entry. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="flag_10"></a>`0x99` | flag_10 | `uint8` | V | Read in the code: Non-zero sets bit 10 of the entry's flag word. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown9a"></a>`0x9A` | unknown9a | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown9b"></a>`0x9B` | unknown9b | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown9c"></a>`0x9C` | unknown9c | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 244, 94 distinct values. |

## Referenced by

- Described by tables: [NxdDataOverrideEntryData](../tables/NxdDataOverrideEntryData.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 15 of 52 columns not decoded.
