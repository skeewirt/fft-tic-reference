# NxdDataContinuousSortieConfirmRow

- **Kind:** structure
- **Area:** [Battle](../areas/battle.md)
- **Size:** 108 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.continuous_sortie_confirm table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown04"></a>`0x4` | unknown04 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 1210, 3 distinct values. |
| <a id="unknown08"></a>`0x8` | unknown08 | `int32[] {int32 offset; uint32 count}` | ? | Not decoded. Observed in the stock rows: 8 distinct values. |
| <a id="unknown10"></a>`0x10` | unknown10 | `int32[] {int32 offset; uint32 count}` | ? | Not decoded. Observed in the stock rows: 8 distinct values. |
| <a id="unknown18"></a>`0x18` | unknown18 | `int32[] {int32 offset; uint32 count}` | ? | Not decoded. Observed in the stock rows: 6 distinct values. |
| <a id="unknown20"></a>`0x20` | unknown20 | `int32[] {int32 offset; uint32 count}` | ? | Not decoded. Observed in the stock rows: 8 distinct values. |
| <a id="unknown28"></a>`0x28` | unknown28 | `int32[] {int32 offset; uint32 count}` | ? | Not decoded. Observed in the stock rows: 2 distinct values. |
| <a id="unknown30"></a>`0x30` | unknown30 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 1220, 9 distinct values. |
| <a id="unknown34"></a>`0x34` | unknown34 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 39100, 26 distinct values. |
| <a id="unknown38"></a>`0x38` | unknown38 | `int32[] {int32 offset; uint32 count}` | ? | Not decoded. Observed in the stock rows: 26 distinct values. |
| <a id="unknown40"></a>`0x40` | unknown40 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 9, 10 distinct values. |
| <a id="unknown44"></a>`0x44` | unknown44 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 38, 7 distinct values. |
| <a id="unknown48"></a>`0x48` | unknown48 | `int32[] {int32 offset; uint32 count}` | ? | Not decoded. Observed in the stock rows: 7 distinct values. |
| <a id="unknown50"></a>`0x50` | unknown50 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 9, 10 distinct values. |
| <a id="unknown54"></a>`0x54` | unknown54 | `int32` | ? | Not decoded. Observed in the stock rows: -135 to 135, 4 distinct values. |
| <a id="unknown58"></a>`0x58` | unknown58 | `int32` | ? | Not decoded. Observed in the stock rows: 2 to 12, 2 distinct values. |
| <a id="unknown5c"></a>`0x5C` | unknown5c | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 3923, 10 distinct values. |
| <a id="unknown60"></a>`0x60` | unknown60 | `int32[] {int32 offset; uint32 count}` | ? | Not decoded. Observed in the stock rows: 2 distinct values. |
| <a id="unknown68"></a>`0x68` | unknown68 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 5, 6 distinct values. |
| <a id="unknown69"></a>`0x69` | unknown69 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown6a"></a>`0x6A` | unknown6a | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown6b"></a>`0x6B` | unknown6b | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |

## Referenced by

- Described by tables: [NxdDataContinuousSortieConfirm](../tables/NxdDataContinuousSortieConfirm.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 22 of 22 columns not decoded.
