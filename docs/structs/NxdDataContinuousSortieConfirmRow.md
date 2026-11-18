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
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="unk_04"></a>`0x4` | unk_04 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 1210, 3 distinct values. |
| <a id="unk_08"></a>`0x8` | unk_08 | `int32[] {int32 offset; uint32 count}` | ? | Not decoded. Observed in the stock rows: 8 distinct values. |
| <a id="unk_10"></a>`0x10` | unk_10 | `int32[] {int32 offset; uint32 count}` | ? | Not decoded. Observed in the stock rows: 8 distinct values. |
| <a id="unk_18"></a>`0x18` | unk_18 | `int32[] {int32 offset; uint32 count}` | ? | Not decoded. Observed in the stock rows: 6 distinct values. |
| <a id="unk_20"></a>`0x20` | unk_20 | `int32[] {int32 offset; uint32 count}` | ? | Not decoded. Observed in the stock rows: 8 distinct values. |
| <a id="unk_28"></a>`0x28` | unk_28 | `int32[] {int32 offset; uint32 count}` | ? | Not decoded. Observed in the stock rows: 2 distinct values. |
| <a id="unk_30"></a>`0x30` | unk_30 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 1220, 9 distinct values. |
| <a id="unk_34"></a>`0x34` | unk_34 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 39100, 26 distinct values. |
| <a id="unk_38"></a>`0x38` | unk_38 | `int32[] {int32 offset; uint32 count}` | ? | Not decoded. Observed in the stock rows: 26 distinct values. |
| <a id="unk_40"></a>`0x40` | unk_40 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 9, 10 distinct values. |
| <a id="unk_44"></a>`0x44` | unk_44 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 38, 7 distinct values. |
| <a id="unk_48"></a>`0x48` | unk_48 | `int32[] {int32 offset; uint32 count}` | ? | Not decoded. Observed in the stock rows: 7 distinct values. |
| <a id="unk_50"></a>`0x50` | unk_50 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 9, 10 distinct values. |
| <a id="unk_54"></a>`0x54` | unk_54 | `int32` | ? | Not decoded. Observed in the stock rows: -135 to 135, 4 distinct values. |
| <a id="unk_58"></a>`0x58` | unk_58 | `int32` | ? | Not decoded. Observed in the stock rows: 2 to 12, 2 distinct values. |
| <a id="unk_5c"></a>`0x5C` | unk_5c | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 3923, 10 distinct values. |
| <a id="unk_60"></a>`0x60` | unk_60 | `int32[] {int32 offset; uint32 count}` | ? | Not decoded. Observed in the stock rows: 2 distinct values. |
| <a id="unk_68"></a>`0x68` | unk_68 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 5, 6 distinct values. |
| <a id="unk_69"></a>`0x69` | unk_69 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unk_6a"></a>`0x6A` | unk_6a | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unk_6b"></a>`0x6B` | unk_6b | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |

## Referenced by

- Described by tables: [NxdDataContinuousSortieConfirm](../tables/NxdDataContinuousSortieConfirm.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

21 of 22 columns not decoded.
