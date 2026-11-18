# NxdDataCharaNameRow

- **Kind:** structure
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Size:** 24 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.chara_name table (English text table; the other languages share the layout). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="comment"></a>`0x4` | comment | `string (int32 offset)` | I | Designer comment slot. Observed in the stock rows: empty in every row. |
| <a id="name"></a>`0x8` | name | `string (int32 offset)` | I | Name text. Observed in the stock rows: 829 distinct values, 180 empty. |
| <a id="unk_0c"></a>`0xC` | unk_0c | `union {int32 kind; int32 id}` | ? | Not decoded. Observed in the stock rows: 74 distinct values. |
| <a id="is_generic"></a>`0x14` | is_generic | `uint8` | I | Is generic (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 0 to 1, 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataCharaName](../tables/NxdDataCharaName.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

1 of 5 columns not decoded.
