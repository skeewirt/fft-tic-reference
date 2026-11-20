# NxdDataProfitRow

- **Kind:** structure
- **Area:** [Errands](../areas/errands.md)
- **Size:** 40 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.profit table (English text table; the other languages share the layout). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: 0 in every row. |
| <a id="title"></a>`0x4` | title | `string (int32 offset)` | M | Measured over every stock row: The plain word for what the column holds. Observed in the stock rows: 96 distinct values, 0 empty. |
| <a id="description"></a>`0x8` | description | `string (int32 offset)` | V | Read in the code: The errand's offer text, shown with the title in the errand board's detail view. Observed in the stock rows: 96 distinct values, 0 empty. |
| <a id="success_report"></a>`0xC` | success_report | `string (int32 offset)` | V | Read in the code: The report text for the best result (grade 0, succeeded) of the errand. Observed in the stock rows: 96 distinct values, 0 empty. |
| <a id="failure_report"></a>`0x10` | failure_report | `string (int32 offset)` | V | Read in the code: The report text for grade 2 (failed): it adds that the errand can be tried again later. Observed in the stock rows: 96 distinct values, 0 empty. |
| <a id="report_title"></a>`0x14` | report_title | `string (int32 offset)` | V | Read in the code: The short title of the report window ('Life as a Diver'). Observed in the stock rows: 96 distinct values, 0 empty. |
| <a id="partial_report"></a>`0x18` | partial_report | `string (int32 offset)` | V | Read in the code: The report text for grade 1 (partial result) when a single unit was sent. Observed in the stock rows: 96 distinct values, 0 empty. |
| <a id="partial_report_2"></a>`0x1C` | partial_report_2 | `string (int32 offset)` | V | Read in the code: The grade 1 report text used instead of +0x18 when the errand entry's second unit slot (a3 + 200) is filled and this string is non-empty. Observed in the stock rows: 96 distinct values, 0 empty. |
| <a id="profit_client_name"></a>`0x20` | profit_client_name | `int32` | M | Measured over every stock row: Every value is a key of nxd.ProfitClientName-en. Observed in the stock rows: 1 to 85, 84 distinct values. |
| <a id="sort_order"></a>`0x24` | sort_order | `int32` | V | Read in the code: Ascending sort key of the errand list: the board builds one 8-byte entry (errand id, this value) per unlocked errand and sorts the entries by the second dword. Observed in the stock rows: 1 to 96, 96 distinct values. |

## Referenced by

- Described by tables: [NxdDataProfit](../tables/NxdDataProfit.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

None recorded.
