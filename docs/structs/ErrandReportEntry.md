# ErrandReportEntry

- **Kind:** structure
- **Area:** [Errands](../areas/errands.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The errand entry the errand report and detail windows read: three 104-byte unit blocks, then the errand id. Only the fields the report readers use are named.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unit_blocks"></a>`0x0` | unit_blocks | `uint8[312]` | V | Three 104-byte unit blocks, copied into the report window by sub_1401A4188 (stride 104). |
| <a id="second_unit_slot"></a>`0xC8` | second_unit_slot | `int32` | V | The second unit block's value at its offset 96 (entry +200): when above 0 the grade 1 (partial) report uses the Profit partial_report_2 text instead of partial_report. |
| <a id="errand_id"></a>`0x138` | errand_id | `int32` | V | The errand's key in the Profit table (UI table 0xB6): sub_1401A4188 and sub_1401A1D78 look the row up with it. |

## Behavior

- V: the report windows take every text of the errand from the Profit row of errand_id and choose the report string by the grade.

## Referenced by

- Observed behaviours: [ErrandReportTextByGrade](../behaviors/ErrandReportTextByGrade.md)

## Notes

Partial. Sheets: sub_1401A4188, sub_1401A1D78. The total size of the entry is I: 344 bytes from the notes of the reading (the code read here shows 0x138 + 4).

## Open questions

? what the bytes inside a unit block hold beyond +96, and the bytes after +316.
