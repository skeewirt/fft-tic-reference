# NxdDataDeepDungeonRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 12 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.deep_dungeon table (English text table; the other languages share the layout). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="name"></a>`0x4` | name | `string (int32 offset)` | I | Name text. Observed in the stock rows: 10 distinct values, 0 empty. |
| <a id="description"></a>`0x8` | description | `string (int32 offset)` | I | Description text. Observed in the stock rows: 10 distinct values, 0 empty. |

## Referenced by

- Described by tables: [NxdDataDeepDungeon](../tables/NxdDataDeepDungeon.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

None recorded.
