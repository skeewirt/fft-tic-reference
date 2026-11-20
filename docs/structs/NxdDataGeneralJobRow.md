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
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: 0 in every row. |
| <a id="unknown04"></a>`0x4` | unknown04 | `string (int32 offset)` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: empty in every row. |
| <a id="job_level_jp"></a>`0x8` | job_level_jp | `int32[] {int32 offset; uint32 count}` | V | JP needed to reach each job level: element [level] is read as u16 at row-data + 4*level. 9 entries per generic job ([0,100,200,400,700,1100,1600,2200,3000]). Observed in the stock rows: 2 distinct values. |
| <a id="required_jobs"></a>`0x10` | required_jobs | `int32[] {int32 offset; uint32 count}` | V | Tree requirements: generic job indices (0..19) the unit must have levelled. Observed in the stock rows: 17 distinct values. |
| <a id="required_levels"></a>`0x18` | required_levels | `int16[] {int32 offset; uint32 count}` | V | Job level needed in each required job (parallel to required_jobs). Observed in the stock rows: 8 distinct values. |
| <a id="required_label_slots"></a>`0x20` | required_label_slots | `int32[] {int32 offset; uint32 count}` | V | Label position index of each requirement on the tree panel (parallel list). Observed in the stock rows: 10 distinct values. |
| <a id="cursor_up"></a>`0x28` | cursor_up | `int32` | V | Read in the code: One of 16 cursor-neighbour slots of the Job Tree: the job panel (0..19) the pad cursor moves to from this job's panel when direction 'up' is pressed (candidate 1 of 2); 20 = none. Observed in the stock rows: 0 to 20, 20 distinct values. |
| <a id="cursor_up_right"></a>`0x2C` | cursor_up_right | `int32` | V | Read in the code: One of 16 cursor-neighbour slots of the Job Tree: the job panel (0..19) the pad cursor moves to from this job's panel when direction 'up-right' is pressed (candidate 1 of 2); 20 = none. Observed in the stock rows: 2 to 20, 10 distinct values. |
| <a id="cursor_right"></a>`0x30` | cursor_right | `int32` | V | Read in the code: One of 16 cursor-neighbour slots of the Job Tree: the job panel (0..19) the pad cursor moves to from this job's panel when direction 'right' is pressed (candidate 1 of 2); 20 = none. Observed in the stock rows: 0 to 20, 17 distinct values. |
| <a id="cursor_down_right"></a>`0x34` | cursor_down_right | `int32` | V | Read in the code: One of 16 cursor-neighbour slots of the Job Tree: the job panel (0..19) the pad cursor moves to from this job's panel when direction 'down-right' is pressed (candidate 1 of 2); 20 = none. Observed in the stock rows: 3 to 20, 11 distinct values. |
| <a id="cursor_down"></a>`0x38` | cursor_down | `int32` | V | Read in the code: One of 16 cursor-neighbour slots of the Job Tree: the job panel (0..19) the pad cursor moves to from this job's panel when direction 'down' is pressed (candidate 1 of 2); 20 = none. Observed in the stock rows: 0 to 20, 20 distinct values. |
| <a id="cursor_down_left"></a>`0x3C` | cursor_down_left | `int32` | V | Read in the code: One of 16 cursor-neighbour slots of the Job Tree: the job panel (0..19) the pad cursor moves to from this job's panel when direction 'down-left' is pressed (candidate 1 of 2); 20 = none. Observed in the stock rows: 0 to 20, 12 distinct values. |
| <a id="cursor_left"></a>`0x40` | cursor_left | `int32` | V | Read in the code: One of 16 cursor-neighbour slots of the Job Tree: the job panel (0..19) the pad cursor moves to from this job's panel when direction 'left' is pressed (candidate 1 of 2); 20 = none. Observed in the stock rows: 0 to 20, 15 distinct values. |
| <a id="cursor_up_left"></a>`0x44` | cursor_up_left | `int32` | V | Read in the code: One of 16 cursor-neighbour slots of the Job Tree: the job panel (0..19) the pad cursor moves to from this job's panel when direction 'up-left' is pressed (candidate 1 of 2); 20 = none. Observed in the stock rows: 0 to 20, 12 distinct values. |
| <a id="cursor_up_2"></a>`0x48` | cursor_up_2 | `int32` | V | Read in the code: One of 16 cursor-neighbour slots of the Job Tree: the job panel (0..19) the pad cursor moves to from this job's panel when direction 'up' is pressed (candidate 2 of 2); 20 = none. Observed in the stock rows: 8 to 20, 2 distinct values. |
| <a id="cursor_up_right_2"></a>`0x4C` | cursor_up_right_2 | `int32` | V | Read in the code: One of 16 cursor-neighbour slots of the Job Tree: the job panel (0..19) the pad cursor moves to from this job's panel when direction 'up-right' is pressed (candidate 2 of 2); 20 = none. Observed in the stock rows: 14 to 20, 2 distinct values. |
| <a id="cursor_right_2"></a>`0x50` | cursor_right_2 | `int32` | V | Read in the code: One of 16 cursor-neighbour slots of the Job Tree: the job panel (0..19) the pad cursor moves to from this job's panel when direction 'right' is pressed (candidate 2 of 2); 20 = none. Observed in the stock rows: 1 to 20, 3 distinct values. |
| <a id="cursor_down_right_2"></a>`0x54` | cursor_down_right_2 | `int32` | V | Read in the code: One of 16 cursor-neighbour slots of the Job Tree: the job panel (0..19) the pad cursor moves to from this job's panel when direction 'down-right' is pressed (candidate 2 of 2); 20 = none. Observed in the stock rows: 10 to 20, 2 distinct values. |
| <a id="cursor_down_2"></a>`0x58` | cursor_down_2 | `int32` | V | Read in the code: One of 16 cursor-neighbour slots of the Job Tree: the job panel (0..19) the pad cursor moves to from this job's panel when direction 'down' is pressed (candidate 2 of 2); 20 = none. Observed in the stock rows: 10 to 20, 2 distinct values. |
| <a id="cursor_down_left_2"></a>`0x5C` | cursor_down_left_2 | `int32` | V | Read in the code: One of 16 cursor-neighbour slots of the Job Tree: the job panel (0..19) the pad cursor moves to from this job's panel when direction 'down-left' is pressed (candidate 2 of 2); 20 = none. Observed in the stock rows: 20 in every row. |
| <a id="cursor_left_2"></a>`0x60` | cursor_left_2 | `int32` | V | Read in the code: One of 16 cursor-neighbour slots of the Job Tree: the job panel (0..19) the pad cursor moves to from this job's panel when direction 'left' is pressed (candidate 2 of 2); 20 = none. Observed in the stock rows: 12 to 20, 3 distinct values. |
| <a id="cursor_up_left_2"></a>`0x64` | cursor_up_left_2 | `int32` | V | Read in the code: One of 16 cursor-neighbour slots of the Job Tree: the job panel (0..19) the pad cursor moves to from this job's panel when direction 'up-left' is pressed (candidate 2 of 2); 20 = none. Observed in the stock rows: 20 in every row. |
| <a id="cursor_up_primary_only"></a>`0x68` | cursor_up_primary_only | `uint8` | V | Read in the code: When set, neighbour slot 'up' (candidate 1) is skipped if the pad direction arrived only through the second direction-byte group (g_InputModule +13652..13655); the first group never looks at the flag. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="cursor_up_right_primary_only"></a>`0x69` | cursor_up_right_primary_only | `uint8` | V | Read in the code: When set, neighbour slot 'up-right' (candidate 1) is skipped if the pad direction arrived only through the second direction-byte group (g_InputModule +13652..13655); the first group never looks at the flag. Observed in the stock rows: 0 in every row. |
| <a id="cursor_right_primary_only"></a>`0x6A` | cursor_right_primary_only | `uint8` | V | Read in the code: When set, neighbour slot 'right' (candidate 1) is skipped if the pad direction arrived only through the second direction-byte group (g_InputModule +13652..13655); the first group never looks at the flag. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="cursor_down_right_primary_only"></a>`0x6B` | cursor_down_right_primary_only | `uint8` | V | Read in the code: When set, neighbour slot 'down-right' (candidate 1) is skipped if the pad direction arrived only through the second direction-byte group (g_InputModule +13652..13655); the first group never looks at the flag. Observed in the stock rows: 0 in every row. |
| <a id="cursor_down_primary_only"></a>`0x6C` | cursor_down_primary_only | `uint8` | V | Read in the code: When set, neighbour slot 'down' (candidate 1) is skipped if the pad direction arrived only through the second direction-byte group (g_InputModule +13652..13655); the first group never looks at the flag. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="cursor_down_left_primary_only"></a>`0x6D` | cursor_down_left_primary_only | `uint8` | V | Read in the code: When set, neighbour slot 'down-left' (candidate 1) is skipped if the pad direction arrived only through the second direction-byte group (g_InputModule +13652..13655); the first group never looks at the flag. Observed in the stock rows: 0 in every row. |
| <a id="cursor_left_primary_only"></a>`0x6E` | cursor_left_primary_only | `uint8` | V | Read in the code: When set, neighbour slot 'left' (candidate 1) is skipped if the pad direction arrived only through the second direction-byte group (g_InputModule +13652..13655); the first group never looks at the flag. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="cursor_up_left_primary_only"></a>`0x6F` | cursor_up_left_primary_only | `uint8` | V | Read in the code: When set, neighbour slot 'up-left' (candidate 1) is skipped if the pad direction arrived only through the second direction-byte group (g_InputModule +13652..13655); the first group never looks at the flag. Observed in the stock rows: 0 in every row. |
| <a id="cursor_up_2_primary_only"></a>`0x70` | cursor_up_2_primary_only | `uint8` | V | Read in the code: When set, neighbour slot 'up' (candidate 2) is skipped if the pad direction arrived only through the second direction-byte group (g_InputModule +13652..13655); the first group never looks at the flag. Observed in the stock rows: 0 in every row. |
| <a id="cursor_up_right_2_primary_only"></a>`0x71` | cursor_up_right_2_primary_only | `uint8` | V | Read in the code: When set, neighbour slot 'up-right' (candidate 2) is skipped if the pad direction arrived only through the second direction-byte group (g_InputModule +13652..13655); the first group never looks at the flag. Observed in the stock rows: 0 in every row. |
| <a id="cursor_right_2_primary_only"></a>`0x72` | cursor_right_2_primary_only | `uint8` | V | Read in the code: When set, neighbour slot 'right' (candidate 2) is skipped if the pad direction arrived only through the second direction-byte group (g_InputModule +13652..13655); the first group never looks at the flag. Observed in the stock rows: 0 in every row. |
| <a id="cursor_down_right_2_primary_only"></a>`0x73` | cursor_down_right_2_primary_only | `uint8` | V | Read in the code: When set, neighbour slot 'down-right' (candidate 2) is skipped if the pad direction arrived only through the second direction-byte group (g_InputModule +13652..13655); the first group never looks at the flag. Observed in the stock rows: 0 in every row. |
| <a id="cursor_down_2_primary_only"></a>`0x74` | cursor_down_2_primary_only | `uint8` | V | Read in the code: When set, neighbour slot 'down' (candidate 2) is skipped if the pad direction arrived only through the second direction-byte group (g_InputModule +13652..13655); the first group never looks at the flag. Observed in the stock rows: 0 in every row. |
| <a id="cursor_down_left_2_primary_only"></a>`0x75` | cursor_down_left_2_primary_only | `uint8` | V | Read in the code: When set, neighbour slot 'down-left' (candidate 2) is skipped if the pad direction arrived only through the second direction-byte group (g_InputModule +13652..13655); the first group never looks at the flag. Observed in the stock rows: 0 in every row. |
| <a id="cursor_left_2_primary_only"></a>`0x76` | cursor_left_2_primary_only | `uint8` | V | Read in the code: When set, neighbour slot 'left' (candidate 2) is skipped if the pad direction arrived only through the second direction-byte group (g_InputModule +13652..13655); the first group never looks at the flag. Observed in the stock rows: 0 in every row. |
| <a id="cursor_up_left_2_primary_only"></a>`0x77` | cursor_up_left_2_primary_only | `uint8` | V | Read in the code: When set, neighbour slot 'up-left' (candidate 2) is skipped if the pad direction arrived only through the second direction-byte group (g_InputModule +13652..13655); the first group never looks at the flag. Observed in the stock rows: 0 in every row. |
| <a id="unknown78"></a>`0x78` | unknown78 | `uint8` | V | Read in the code: 0 clears, any other value sets, a saved flag of the job at the start of a new game; no code reads that flag: changing it has no effect. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown79"></a>`0x79` | unknown79 | `uint8` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: 0 in every row. |
| <a id="unknown7a"></a>`0x7A` | unknown7a | `uint8` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: 0 in every row. |
| <a id="unknown7b"></a>`0x7B` | unknown7b | `uint8` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: 0 in every row. |

## Referenced by

- Described by tables: [NxdDataGeneralJob](../tables/NxdDataGeneralJob.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

None recorded.
