# EventVarEditor_DrawPage

- **Address:** `0x14036DC28`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int64_t EventVarEditor_DrawPage(int *record)`
- **Callers:** EventVarEditor_Open, EventVarEditor_ListInput, EventVarEditor_ValueInput
- **Callees:** EventVar_Read, WinRec_SetRect, WinRec_PutText, WinRec_CopyToVram

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Draws one page of the event variable editor: ten variable numbers with their current values.

## Behavior

- V: the page starts at record dword 2 and holds 10 rows (fewer at the end of the 1024 variables).
- V: each row reads EventVar_Read(n) and prints text id 47140 with the number and value, or 47141 when the value is above 9999.
- V: the window width depends on the language (172 or 104).

## State touched

- Calls: [EventVar_Read](EventVar_Read.md), [WinRec_SetRect](WinRec_SetRect.md), [WinRec_PutText](WinRec_PutText.md), [WinRec_CopyToVram](WinRec_CopyToVram.md)

## Referenced by

- Called by: [EventVarEditor_ListInput](EventVarEditor_ListInput.md), [EventVarEditor_Open](EventVarEditor_Open.md), [EventVarEditor_ValueInput](EventVarEditor_ValueInput.md)

## Open questions

None recorded.
