# NxdDataIconGroupRow

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)
- **Size:** 12 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.icon_group table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: engine-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: 0 in every row. |
| <a id="first_icon"></a>`0x4` | first_icon | `int32` | V | Read in the code: The first Icon id of the group: an icon belongs to the last group (in table order from row 1) whose first_icon is <= the icon id; 0 ends the list. Observed in the stock rows: 0 to 14000, 61 distinct values. |
| <a id="unknown08"></a>`0x8` | unknown08 | `uint8` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="select_4k"></a>`0x9` | select_4k | `uint8` | V | Read in the code: When set, the icon paths of the group's id range go through UITexturePath_Select4k, which rewrites '_2k_' in the path to '_4k_'. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown0a"></a>`0xA` | unknown0a | `uint8` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: 0 in every row. |
| <a id="unknown0b"></a>`0xB` | unknown0b | `uint8` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: 0 in every row. |

## Referenced by

- Described by tables: [NxdDataIconGroup](../tables/NxdDataIconGroup.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

None recorded.
