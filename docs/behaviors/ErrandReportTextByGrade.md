# ErrandReportTextByGrade

- **Kind:** observed behaviour
- **Scope:** engine (errand report)
- **Area:** [Errands](../areas/errands.md)
- **Affects:** [sub_1401A4188](../functions/sub_1401A4188.md), [sub_14016FFC8](../functions/sub_14016FFC8.md), [sub_1401A1D78](../functions/sub_1401A1D78.md), [sub_14016E7F4](../functions/sub_14016E7F4.md), [ErrandReportEntry](../structs/ErrandReportEntry.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The errand report window shows one of four Profit texts, chosen by the grade of the result and by whether a second unit was sent.

## Behavior

- V: grade 0 (succeeded) shows Profit +0x0C (success_report); grade 2 (failed) +0x10 (failure_report); grade 1 (partial) +0x1C (partial_report_2) when the second unit slot (entry +200) is above 0 and the string is not empty, else +0x18 (partial_report); any other grade shows +0x0C.
- V: the report window's title is Profit +0x14 (report_title), shown by sub_14016FFC8; the detail panel shows +4 (title), +8 (description) and the client name through +0x20 (a key of UI table 0xC1).
- V: the board's list holds one 8-byte entry (errand id, +0x24 sort_order) per errand whose progress variable (864 + id) has bit 2, sorted by the second dword.

## Open questions

? the exact meaning of entry +200.
