# NxdDataConfigCategoryRow

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)
- **Size:** 16 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.config_category table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="config_item_ids"></a>`0x4` | config_item_ids | `int32[] {int32 offset; uint32 count}` | I | Config item ids (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 11 distinct values. |
| <a id="name_ui_id"></a>`0xC` | name_ui_id | `int32` | I | UI text key (a row of the UI text table), from the column name. Observed in the stock rows: 0 to 3612, 10 distinct values. |

## Referenced by

- Described by tables: [NxdDataConfigCategory](../tables/NxdDataConfigCategory.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

None recorded.
