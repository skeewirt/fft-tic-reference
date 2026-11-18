# NxdDataGeneralJobRow

- **Kind:** structure
- **Area:** [Job data](../areas/job-data.md)
- **Size:** 124 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.general_job table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | DLC gate bit set (0 in every row). Observed in the stock rows: 0 in every row. |
| <a id="comment"></a>`0x4` | comment | `string (int32 offset)` | I | Designer comment (null in every row). Observed in the stock rows: empty in every row. |
| <a id="required_job_exp"></a>`0x8` | required_job_exp | `int32[] {int32 offset; uint32 count}` | V | JP needed to reach each job level: element [level] is read as u16 at row-data + 4*level. 9 entries per generic job ([0,100,200,400,700,1100,1600,2200,3000]). Observed in the stock rows: 2 distinct values. |
| <a id="required_job_ids"></a>`0x10` | required_job_ids | `int32[] {int32 offset; uint32 count}` | V | Tree requirements: generic job indices (0..19) the unit must have levelled. Observed in the stock rows: 17 distinct values. |
| <a id="required_job_levels"></a>`0x18` | required_job_levels | `int16[] {int32 offset; uint32 count}` | V | Job level needed in each required job (parallel to RequiredJobIds). Observed in the stock rows: 8 distinct values. |
| <a id="required_job_positions"></a>`0x20` | required_job_positions | `int32[] {int32 offset; uint32 count}` | V | Label position index of each requirement on the tree panel (parallel list). Observed in the stock rows: 10 distinct values. |
| <a id="unk_28"></a>`0x28` | unk_28 | `int32` | I | One of 16 slots at +0x28..+0x64: a generic job index 0..19, or 20 = empty. I: tree arrow/line slots; belongs to the tree work. Observed in the stock rows: 0 to 20, 20 distinct values. |
| <a id="unk_2c"></a>`0x2C` | unk_2c | `int32` | I | One of 16 slots at +0x28..+0x64: a generic job index 0..19, or 20 = empty. I: tree arrow/line slots; belongs to the tree work. Observed in the stock rows: 2 to 20, 10 distinct values. |
| <a id="unk_30"></a>`0x30` | unk_30 | `int32` | I | One of 16 slots at +0x28..+0x64: a generic job index 0..19, or 20 = empty. I: tree arrow/line slots; belongs to the tree work. Observed in the stock rows: 0 to 20, 17 distinct values. |
| <a id="unk_34"></a>`0x34` | unk_34 | `int32` | I | One of 16 slots at +0x28..+0x64: a generic job index 0..19, or 20 = empty. I: tree arrow/line slots; belongs to the tree work. Observed in the stock rows: 3 to 20, 11 distinct values. |
| <a id="unk_38"></a>`0x38` | unk_38 | `int32` | I | One of 16 slots at +0x28..+0x64: a generic job index 0..19, or 20 = empty. I: tree arrow/line slots; belongs to the tree work. Observed in the stock rows: 0 to 20, 20 distinct values. |
| <a id="unk_3c"></a>`0x3C` | unk_3c | `int32` | I | One of 16 slots at +0x28..+0x64: a generic job index 0..19, or 20 = empty. I: tree arrow/line slots; belongs to the tree work. Observed in the stock rows: 0 to 20, 12 distinct values. |
| <a id="unk_40"></a>`0x40` | unk_40 | `int32` | I | One of 16 slots at +0x28..+0x64: a generic job index 0..19, or 20 = empty. I: tree arrow/line slots; belongs to the tree work. Observed in the stock rows: 0 to 20, 15 distinct values. |
| <a id="unk_44"></a>`0x44` | unk_44 | `int32` | I | One of 16 slots at +0x28..+0x64: a generic job index 0..19, or 20 = empty. I: tree arrow/line slots; belongs to the tree work. Observed in the stock rows: 0 to 20, 12 distinct values. |
| <a id="unk_48"></a>`0x48` | unk_48 | `int32` | I | One of 16 slots at +0x28..+0x64: a generic job index 0..19, or 20 = empty. I: tree arrow/line slots; belongs to the tree work. Observed in the stock rows: 8 to 20, 2 distinct values. |
| <a id="unk_4c"></a>`0x4C` | unk_4c | `int32` | I | One of 16 slots at +0x28..+0x64: a generic job index 0..19, or 20 = empty. I: tree arrow/line slots; belongs to the tree work. Observed in the stock rows: 14 to 20, 2 distinct values. |
| <a id="unk_50"></a>`0x50` | unk_50 | `int32` | I | One of 16 slots at +0x28..+0x64: a generic job index 0..19, or 20 = empty. I: tree arrow/line slots; belongs to the tree work. Observed in the stock rows: 1 to 20, 3 distinct values. |
| <a id="unk_54"></a>`0x54` | unk_54 | `int32` | I | One of 16 slots at +0x28..+0x64: a generic job index 0..19, or 20 = empty. I: tree arrow/line slots; belongs to the tree work. Observed in the stock rows: 10 to 20, 2 distinct values. |
| <a id="unk_58"></a>`0x58` | unk_58 | `int32` | I | One of 16 slots at +0x28..+0x64: a generic job index 0..19, or 20 = empty. I: tree arrow/line slots; belongs to the tree work. Observed in the stock rows: 10 to 20, 2 distinct values. |
| <a id="unk_5c"></a>`0x5C` | unk_5c | `int32` | I | One of 16 slots at +0x28..+0x64: a generic job index 0..19, or 20 = empty. I: tree arrow/line slots; belongs to the tree work. Observed in the stock rows: 20 in every row. |
| <a id="unk_60"></a>`0x60` | unk_60 | `int32` | I | One of 16 slots at +0x28..+0x64: a generic job index 0..19, or 20 = empty. I: tree arrow/line slots; belongs to the tree work. Observed in the stock rows: 12 to 20, 3 distinct values. |
| <a id="unk_64"></a>`0x64` | unk_64 | `int32` | I | One of 16 slots at +0x28..+0x64: a generic job index 0..19, or 20 = empty. I: tree arrow/line slots; belongs to the tree work. Observed in the stock rows: 20 in every row. |
| <a id="unk_68"></a>`0x68` | unk_68 | `uint8` | ? | Flag byte. J1 listed sub_1401321FC as reader; the decompile reads only +16/+20/+24/+28 (the lists), so no reader is confirmed. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unk_69"></a>`0x69` | unk_69 | `uint8` | ? | Flag byte (0/1). Not read by any function studied. Observed in the stock rows: 0 in every row. |
| <a id="unk_6a"></a>`0x6A` | unk_6a | `uint8` | ? | Flag byte (0/1). Not read by any function studied. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unk_6b"></a>`0x6B` | unk_6b | `uint8` | ? | Flag byte (0/1). Not read by any function studied. Observed in the stock rows: 0 in every row. |
| <a id="unk_6c"></a>`0x6C` | unk_6c | `uint8` | ? | Flag byte (0/1). Not read by any function studied. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unk_6d"></a>`0x6D` | unk_6d | `uint8` | ? | Flag byte (0/1). Not read by any function studied. Observed in the stock rows: 0 in every row. |
| <a id="unk_6e"></a>`0x6E` | unk_6e | `uint8` | ? | Flag byte (0/1). Not read by any function studied. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unk_6f"></a>`0x6F` | unk_6f | `uint8` | ? | Flag byte (0/1). Not read by any function studied. Observed in the stock rows: 0 in every row. |
| <a id="unk_70"></a>`0x70` | unk_70 | `uint8` | ? | Flag byte (0/1). Not read by any function studied. Observed in the stock rows: 0 in every row. |
| <a id="unk_71"></a>`0x71` | unk_71 | `uint8` | ? | Flag byte (0/1). Not read by any function studied. Observed in the stock rows: 0 in every row. |
| <a id="unk_72"></a>`0x72` | unk_72 | `uint8` | ? | Flag byte (0/1). Not read by any function studied. Observed in the stock rows: 0 in every row. |
| <a id="unk_73"></a>`0x73` | unk_73 | `uint8` | ? | Flag byte (0/1). Not read by any function studied. Observed in the stock rows: 0 in every row. |
| <a id="unk_74"></a>`0x74` | unk_74 | `uint8` | ? | Flag byte (0/1). Not read by any function studied. Observed in the stock rows: 0 in every row. |
| <a id="unk_75"></a>`0x75` | unk_75 | `uint8` | ? | Flag byte (0/1). Not read by any function studied. Observed in the stock rows: 0 in every row. |
| <a id="unk_76"></a>`0x76` | unk_76 | `uint8` | ? | Flag byte (0/1). Not read by any function studied. Observed in the stock rows: 0 in every row. |
| <a id="unk_77"></a>`0x77` | unk_77 | `uint8` | ? | Flag byte (0/1). Not read by any function studied. Observed in the stock rows: 0 in every row. |
| <a id="unk_78"></a>`0x78` | unk_78 | `uint8` | V | Start-of-game flag source: the new-game reset writes byte_1411A7490[jobIndex] = (Unknown78 == 0). 0 only in rows 0 (Squire) and 1 (Chemist). Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unk_79"></a>`0x79` | unk_79 | `uint8` | ? | Flag byte (0/1). Not read by any function studied. Observed in the stock rows: 0 in every row. |
| <a id="unk_7a"></a>`0x7A` | unk_7a | `uint8` | ? | Flag byte (0/1). Not read by any function studied. Observed in the stock rows: 0 in every row. |
| <a id="unk_7b"></a>`0x7B` | unk_7b | `uint8` | ? | Flag byte (0/1). Not read by any function studied. Observed in the stock rows: 0 in every row. |

## Referenced by

- Described by tables: [NxdDataGeneralJob](../tables/NxdDataGeneralJob.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

19 of 42 columns not decoded.
