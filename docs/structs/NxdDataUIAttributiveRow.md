# NxdDataUIAttributiveRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 156 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.ui_attributive table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: text.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="string1_0"></a>`0x4` | string1_0 | `string (int32 offset)` | I | String1_0 text. Observed in the stock rows: 5 distinct values, 35 empty. |
| <a id="string1_1"></a>`0x8` | string1_1 | `string (int32 offset)` | I | String1_1 text. Observed in the stock rows: 3 distinct values, 37 empty. |
| <a id="string1_2"></a>`0xC` | string1_2 | `string (int32 offset)` | I | String1_2 text. Observed in the stock rows: empty in every row. |
| <a id="string1_3"></a>`0x10` | string1_3 | `string (int32 offset)` | I | String1_3 text. Observed in the stock rows: 5 distinct values, 35 empty. |
| <a id="string1_4"></a>`0x14` | string1_4 | `string (int32 offset)` | I | String1_4 text. Observed in the stock rows: 3 distinct values, 37 empty. |
| <a id="string1_5"></a>`0x18` | string1_5 | `string (int32 offset)` | I | String1_5 text. Observed in the stock rows: empty in every row. |
| <a id="string2_0"></a>`0x1C` | string2_0 | `string (int32 offset)` | I | String2_0 text. Observed in the stock rows: 11 distinct values, 26 empty. |
| <a id="string2_1"></a>`0x20` | string2_1 | `string (int32 offset)` | I | String2_1 text. Observed in the stock rows: 10 distinct values, 26 empty. |
| <a id="string2_2"></a>`0x24` | string2_2 | `string (int32 offset)` | I | String2_2 text. Observed in the stock rows: 11 distinct values, 26 empty. |
| <a id="string2_3"></a>`0x28` | string2_3 | `string (int32 offset)` | I | String2_3 text. Observed in the stock rows: 8 distinct values, 27 empty. |
| <a id="string2_4"></a>`0x2C` | string2_4 | `string (int32 offset)` | I | String2_4 text. Observed in the stock rows: 15 distinct values, 19 empty. |
| <a id="string2_5"></a>`0x30` | string2_5 | `string (int32 offset)` | I | String2_5 text. Observed in the stock rows: 9 distinct values, 28 empty. |
| <a id="string2_6"></a>`0x34` | string2_6 | `string (int32 offset)` | I | String2_6 text. Observed in the stock rows: 15 distinct values, 20 empty. |
| <a id="string2_7"></a>`0x38` | string2_7 | `string (int32 offset)` | I | String2_7 text. Observed in the stock rows: 8 distinct values, 29 empty. |
| <a id="string2_8"></a>`0x3C` | string2_8 | `string (int32 offset)` | I | String2_8 text. Observed in the stock rows: 11 distinct values, 24 empty. |
| <a id="string2_9"></a>`0x40` | string2_9 | `string (int32 offset)` | I | String2_9 text. Observed in the stock rows: 9 distinct values, 28 empty. |
| <a id="string2_10"></a>`0x44` | string2_10 | `string (int32 offset)` | I | String2_10 text. Observed in the stock rows: 11 distinct values, 25 empty. |
| <a id="string2_11"></a>`0x48` | string2_11 | `string (int32 offset)` | I | String2_11 text. Observed in the stock rows: 9 distinct values, 28 empty. |
| <a id="string2_12"></a>`0x4C` | string2_12 | `string (int32 offset)` | I | String2_12 text. Observed in the stock rows: 10 distinct values, 25 empty. |
| <a id="string2_13"></a>`0x50` | string2_13 | `string (int32 offset)` | I | String2_13 text. Observed in the stock rows: 8 distinct values, 28 empty. |
| <a id="string2_14"></a>`0x54` | string2_14 | `string (int32 offset)` | I | String2_14 text. Observed in the stock rows: 11 distinct values, 26 empty. |
| <a id="string2_15"></a>`0x58` | string2_15 | `string (int32 offset)` | I | String2_15 text. Observed in the stock rows: 8 distinct values, 29 empty. |
| <a id="string3_0"></a>`0x5C` | string3_0 | `string (int32 offset)` | I | String3_0 text. Observed in the stock rows: 5 distinct values, 34 empty. |
| <a id="string3_1"></a>`0x60` | string3_1 | `string (int32 offset)` | I | String3_1 text. Observed in the stock rows: 10 distinct values, 30 empty. |
| <a id="string3_2"></a>`0x64` | string3_2 | `string (int32 offset)` | I | String3_2 text. Observed in the stock rows: 9 distinct values, 30 empty. |
| <a id="string3_3"></a>`0x68` | string3_3 | `string (int32 offset)` | I | String3_3 text. Observed in the stock rows: 9 distinct values, 30 empty. |
| <a id="string3_4"></a>`0x6C` | string3_4 | `string (int32 offset)` | I | String3_4 text. Observed in the stock rows: 5 distinct values, 34 empty. |
| <a id="string3_5"></a>`0x70` | string3_5 | `string (int32 offset)` | I | String3_5 text. Observed in the stock rows: 10 distinct values, 30 empty. |
| <a id="string3_6"></a>`0x74` | string3_6 | `string (int32 offset)` | I | String3_6 text. Observed in the stock rows: 9 distinct values, 30 empty. |
| <a id="string3_7"></a>`0x78` | string3_7 | `string (int32 offset)` | I | String3_7 text. Observed in the stock rows: 9 distinct values, 30 empty. |
| <a id="string3_8"></a>`0x7C` | string3_8 | `string (int32 offset)` | I | String3_8 text. Observed in the stock rows: 5 distinct values, 34 empty. |
| <a id="string3_9"></a>`0x80` | string3_9 | `string (int32 offset)` | I | String3_9 text. Observed in the stock rows: 10 distinct values, 30 empty. |
| <a id="string3_10"></a>`0x84` | string3_10 | `string (int32 offset)` | I | String3_10 text. Observed in the stock rows: 9 distinct values, 30 empty. |
| <a id="string3_11"></a>`0x88` | string3_11 | `string (int32 offset)` | I | String3_11 text. Observed in the stock rows: 9 distinct values, 30 empty. |
| <a id="string3_12"></a>`0x8C` | string3_12 | `string (int32 offset)` | I | String3_12 text. Observed in the stock rows: 5 distinct values, 34 empty. |
| <a id="string3_13"></a>`0x90` | string3_13 | `string (int32 offset)` | I | String3_13 text. Observed in the stock rows: 10 distinct values, 30 empty. |
| <a id="string3_14"></a>`0x94` | string3_14 | `string (int32 offset)` | I | String3_14 text. Observed in the stock rows: 9 distinct values, 30 empty. |
| <a id="string3_15"></a>`0x98` | string3_15 | `string (int32 offset)` | I | String3_15 text. Observed in the stock rows: 9 distinct values, 30 empty. |

## Referenced by

- Described by tables: [NxdDataUIAttributive](../tables/NxdDataUIAttributive.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

None recorded.
