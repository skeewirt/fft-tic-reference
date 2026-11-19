# NxdDataEntryNoRow

- **Kind:** structure
- **Area:** [Battle](../areas/battle.md)
- **Size:** 28 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.entry_no table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown04"></a>`0x4` | unknown04 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: empty in every row. |
| <a id="sortie_confirm"></a>`0x8` | sortie_confirm | `int32` | M | Measured over every stock row: Every value is a key of nxd.SortieConfirm. Observed in the stock rows: 0 to 341, 196 distinct values. |
| <a id="unknown0c"></a>`0xC` | unknown0c | `int32[] {int32 offset; uint32 count}` | ? | Not decoded. Observed in the stock rows: 41 distinct values. |
| <a id="unknown14"></a>`0x14` | unknown14 | `int32[] {int32 offset; uint32 count}` | ? | Not decoded. Observed in the stock rows: 3 distinct values. |

## Referenced by

- Described by tables: [NxdDataEntryNo](../tables/NxdDataEntryNo.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 4 of 5 columns not decoded.
