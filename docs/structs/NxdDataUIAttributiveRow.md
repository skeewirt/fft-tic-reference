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
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="english_form_0"></a>`0x4` | english_form_0 | `string (int32 offset)` | M | Measured over every stock row: Short English word forms (articles and endings). Observed in the stock rows: 5 distinct values, 35 empty. |
| <a id="english_form_1"></a>`0x8` | english_form_1 | `string (int32 offset)` | M | Measured over every stock row: Short English word forms (articles and endings). Observed in the stock rows: 3 distinct values, 37 empty. |
| <a id="unknown0c"></a>`0xC` | unknown0c | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: empty in every row. |
| <a id="english_form_3"></a>`0x10` | english_form_3 | `string (int32 offset)` | M | Measured over every stock row: Short English word forms (articles and endings). Observed in the stock rows: 5 distinct values, 35 empty. |
| <a id="english_form_4"></a>`0x14` | english_form_4 | `string (int32 offset)` | M | Measured over every stock row: Short English word forms (articles and endings). Observed in the stock rows: 3 distinct values, 37 empty. |
| <a id="unknown18"></a>`0x18` | unknown18 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: empty in every row. |
| <a id="german_form_0"></a>`0x1C` | german_form_0 | `string (int32 offset)` | M | Measured over every stock row: Short German word forms (articles and endings). Observed in the stock rows: 11 distinct values, 26 empty. |
| <a id="german_form_1"></a>`0x20` | german_form_1 | `string (int32 offset)` | M | Measured over every stock row: Short German word forms (articles and endings). Observed in the stock rows: 10 distinct values, 26 empty. |
| <a id="german_form_2"></a>`0x24` | german_form_2 | `string (int32 offset)` | M | Measured over every stock row: Short German word forms (articles and endings). Observed in the stock rows: 11 distinct values, 26 empty. |
| <a id="german_form_3"></a>`0x28` | german_form_3 | `string (int32 offset)` | M | Measured over every stock row: Short German word forms (articles and endings). Observed in the stock rows: 8 distinct values, 27 empty. |
| <a id="german_form_4"></a>`0x2C` | german_form_4 | `string (int32 offset)` | M | Measured over every stock row: Short German word forms (articles and endings). Observed in the stock rows: 15 distinct values, 19 empty. |
| <a id="german_form_5"></a>`0x30` | german_form_5 | `string (int32 offset)` | M | Measured over every stock row: Short German word forms (articles and endings). Observed in the stock rows: 9 distinct values, 28 empty. |
| <a id="german_form_6"></a>`0x34` | german_form_6 | `string (int32 offset)` | M | Measured over every stock row: Short German word forms (articles and endings). Observed in the stock rows: 15 distinct values, 20 empty. |
| <a id="german_form_7"></a>`0x38` | german_form_7 | `string (int32 offset)` | M | Measured over every stock row: Short German word forms (articles and endings). Observed in the stock rows: 8 distinct values, 29 empty. |
| <a id="german_form_8"></a>`0x3C` | german_form_8 | `string (int32 offset)` | M | Measured over every stock row: Short German word forms (articles and endings). Observed in the stock rows: 11 distinct values, 24 empty. |
| <a id="german_form_9"></a>`0x40` | german_form_9 | `string (int32 offset)` | M | Measured over every stock row: Short German word forms (articles and endings). Observed in the stock rows: 9 distinct values, 28 empty. |
| <a id="german_form_10"></a>`0x44` | german_form_10 | `string (int32 offset)` | M | Measured over every stock row: Short German word forms (articles and endings). Observed in the stock rows: 11 distinct values, 25 empty. |
| <a id="german_form_11"></a>`0x48` | german_form_11 | `string (int32 offset)` | M | Measured over every stock row: Short German word forms (articles and endings). Observed in the stock rows: 9 distinct values, 28 empty. |
| <a id="german_form_12"></a>`0x4C` | german_form_12 | `string (int32 offset)` | M | Measured over every stock row: Short German word forms (articles and endings). Observed in the stock rows: 10 distinct values, 25 empty. |
| <a id="german_form_13"></a>`0x50` | german_form_13 | `string (int32 offset)` | M | Measured over every stock row: Short German word forms (articles and endings). Observed in the stock rows: 8 distinct values, 28 empty. |
| <a id="german_form_14"></a>`0x54` | german_form_14 | `string (int32 offset)` | M | Measured over every stock row: Short German word forms (articles and endings). Observed in the stock rows: 11 distinct values, 26 empty. |
| <a id="german_form_15"></a>`0x58` | german_form_15 | `string (int32 offset)` | M | Measured over every stock row: Short German word forms (articles and endings). Observed in the stock rows: 8 distinct values, 29 empty. |
| <a id="french_form_0"></a>`0x5C` | french_form_0 | `string (int32 offset)` | M | Measured over every stock row: Short French word forms (articles and endings). Observed in the stock rows: 5 distinct values, 34 empty. |
| <a id="french_form_1"></a>`0x60` | french_form_1 | `string (int32 offset)` | M | Measured over every stock row: Short French word forms (articles and endings). Observed in the stock rows: 10 distinct values, 30 empty. |
| <a id="french_form_2"></a>`0x64` | french_form_2 | `string (int32 offset)` | M | Measured over every stock row: Short French word forms (articles and endings). Observed in the stock rows: 9 distinct values, 30 empty. |
| <a id="french_form_3"></a>`0x68` | french_form_3 | `string (int32 offset)` | M | Measured over every stock row: Short French word forms (articles and endings). Observed in the stock rows: 9 distinct values, 30 empty. |
| <a id="french_form_4"></a>`0x6C` | french_form_4 | `string (int32 offset)` | M | Measured over every stock row: Short French word forms (articles and endings). Observed in the stock rows: 5 distinct values, 34 empty. |
| <a id="french_form_5"></a>`0x70` | french_form_5 | `string (int32 offset)` | M | Measured over every stock row: Short French word forms (articles and endings). Observed in the stock rows: 10 distinct values, 30 empty. |
| <a id="french_form_6"></a>`0x74` | french_form_6 | `string (int32 offset)` | M | Measured over every stock row: Short French word forms (articles and endings). Observed in the stock rows: 9 distinct values, 30 empty. |
| <a id="french_form_7"></a>`0x78` | french_form_7 | `string (int32 offset)` | M | Measured over every stock row: Short French word forms (articles and endings). Observed in the stock rows: 9 distinct values, 30 empty. |
| <a id="french_form_8"></a>`0x7C` | french_form_8 | `string (int32 offset)` | M | Measured over every stock row: Short French word forms (articles and endings). Observed in the stock rows: 5 distinct values, 34 empty. |
| <a id="french_form_9"></a>`0x80` | french_form_9 | `string (int32 offset)` | M | Measured over every stock row: Short French word forms (articles and endings). Observed in the stock rows: 10 distinct values, 30 empty. |
| <a id="french_form_10"></a>`0x84` | french_form_10 | `string (int32 offset)` | M | Measured over every stock row: Short French word forms (articles and endings). Observed in the stock rows: 9 distinct values, 30 empty. |
| <a id="french_form_11"></a>`0x88` | french_form_11 | `string (int32 offset)` | M | Measured over every stock row: Short French word forms (articles and endings). Observed in the stock rows: 9 distinct values, 30 empty. |
| <a id="french_form_12"></a>`0x8C` | french_form_12 | `string (int32 offset)` | M | Measured over every stock row: Short French word forms (articles and endings). Observed in the stock rows: 5 distinct values, 34 empty. |
| <a id="french_form_13"></a>`0x90` | french_form_13 | `string (int32 offset)` | M | Measured over every stock row: Short French word forms (articles and endings). Observed in the stock rows: 10 distinct values, 30 empty. |
| <a id="french_form_14"></a>`0x94` | french_form_14 | `string (int32 offset)` | M | Measured over every stock row: Short French word forms (articles and endings). Observed in the stock rows: 9 distinct values, 30 empty. |
| <a id="french_form_15"></a>`0x98` | french_form_15 | `string (int32 offset)` | M | Measured over every stock row: Short French word forms (articles and endings). Observed in the stock rows: 9 distinct values, 30 empty. |

## Referenced by

- Described by tables: [NxdDataUIAttributive](../tables/NxdDataUIAttributive.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 3 of 39 columns not decoded.
