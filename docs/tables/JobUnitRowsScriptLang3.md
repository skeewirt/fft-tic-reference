# JobUnitRowsScriptLang3

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable
- **Address:** `0x140810A00`
- **Rows:** 1 script of 217 bytes
- **Keyed by:** script byte offset
- **Read by:** [JobScreen_FillUnitRows](../functions/JobScreen_FillUnitRows.md), [UiScript_Run](../functions/UiScript_Run.md)
- **Row layout:** [UiScriptRecord](../structs/UiScriptRecord.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

UI script (layout of the job screen's unit rows) for text language 3. Same record language as UiScriptRecord. Verdict: designer-data.

## Behavior

- V: JobScreen_FillUnitRows picks the script of the current text language (0 -> 0x140810760, 1 -> 0x140810840, 2 -> 0x140810920, 3 -> 0x140810A00) and runs it

## Notes

Our names. Tags: V layout, ? operands.

## Open questions

None recorded.
