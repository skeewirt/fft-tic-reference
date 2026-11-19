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
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown04"></a>`0x4` | unknown04 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: empty in every row. |
| <a id="job_level_jp"></a>`0x8` | job_level_jp | `int32[] {int32 offset; uint32 count}` | V | JP needed to reach each job level: element [level] is read as u16 at row-data + 4*level. 9 entries per generic job ([0,100,200,400,700,1100,1600,2200,3000]). Observed in the stock rows: 2 distinct values. |
| <a id="required_jobs"></a>`0x10` | required_jobs | `int32[] {int32 offset; uint32 count}` | V | Tree requirements: generic job indices (0..19) the unit must have levelled. Observed in the stock rows: 17 distinct values. |
| <a id="required_levels"></a>`0x18` | required_levels | `int16[] {int32 offset; uint32 count}` | V | Job level needed in each required job (parallel to required_jobs). Observed in the stock rows: 8 distinct values. |
| <a id="required_label_slots"></a>`0x20` | required_label_slots | `int32[] {int32 offset; uint32 count}` | V | Label position index of each requirement on the tree panel (parallel list). Observed in the stock rows: 10 distinct values. |
| <a id="unknown28"></a>`0x28` | unknown28 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 20, 20 distinct values. |
| <a id="unknown2c"></a>`0x2C` | unknown2c | `int32` | ? | Not decoded. Observed in the stock rows: 2 to 20, 10 distinct values. |
| <a id="unknown30"></a>`0x30` | unknown30 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 20, 17 distinct values. |
| <a id="unknown34"></a>`0x34` | unknown34 | `int32` | ? | Not decoded. Observed in the stock rows: 3 to 20, 11 distinct values. |
| <a id="unknown38"></a>`0x38` | unknown38 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 20, 20 distinct values. |
| <a id="unknown3c"></a>`0x3C` | unknown3c | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 20, 12 distinct values. |
| <a id="unknown40"></a>`0x40` | unknown40 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 20, 15 distinct values. |
| <a id="unknown44"></a>`0x44` | unknown44 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 20, 12 distinct values. |
| <a id="unknown48"></a>`0x48` | unknown48 | `int32` | ? | Not decoded. Observed in the stock rows: 8 to 20, 2 distinct values. |
| <a id="unknown4c"></a>`0x4C` | unknown4c | `int32` | ? | Not decoded. Observed in the stock rows: 14 to 20, 2 distinct values. |
| <a id="unknown50"></a>`0x50` | unknown50 | `int32` | ? | Not decoded. Observed in the stock rows: 1 to 20, 3 distinct values. |
| <a id="unknown54"></a>`0x54` | unknown54 | `int32` | ? | Not decoded. Observed in the stock rows: 10 to 20, 2 distinct values. |
| <a id="unknown58"></a>`0x58` | unknown58 | `int32` | ? | Not decoded. Observed in the stock rows: 10 to 20, 2 distinct values. |
| <a id="unknown5c"></a>`0x5C` | unknown5c | `int32` | ? | Not decoded. Observed in the stock rows: 20 in every row. |
| <a id="unknown60"></a>`0x60` | unknown60 | `int32` | ? | Not decoded. Observed in the stock rows: 12 to 20, 3 distinct values. |
| <a id="unknown64"></a>`0x64` | unknown64 | `int32` | ? | Not decoded. Observed in the stock rows: 20 in every row. |
| <a id="unknown68"></a>`0x68` | unknown68 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown69"></a>`0x69` | unknown69 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown6a"></a>`0x6A` | unknown6a | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown6b"></a>`0x6B` | unknown6b | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown6c"></a>`0x6C` | unknown6c | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown6d"></a>`0x6D` | unknown6d | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown6e"></a>`0x6E` | unknown6e | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown6f"></a>`0x6F` | unknown6f | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown70"></a>`0x70` | unknown70 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown71"></a>`0x71` | unknown71 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown72"></a>`0x72` | unknown72 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown73"></a>`0x73` | unknown73 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown74"></a>`0x74` | unknown74 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown75"></a>`0x75` | unknown75 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown76"></a>`0x76` | unknown76 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown77"></a>`0x77` | unknown77 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown78"></a>`0x78` | unknown78 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown79"></a>`0x79` | unknown79 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown7a"></a>`0x7A` | unknown7a | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown7b"></a>`0x7B` | unknown7b | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |

## Referenced by

- Described by tables: [NxdDataGeneralJob](../tables/NxdDataGeneralJob.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 38 of 42 columns not decoded.
