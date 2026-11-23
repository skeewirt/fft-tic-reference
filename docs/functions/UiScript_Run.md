# UiScript_Run

- **Address:** `0x1403278EC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UiScript_Run(const unsigned char *script, int firstRow, int flag)`
- **Callers:** JobScreen_FillUnitRows, JobScreen_BuildLearnList, JobScreen_RefreshLearnList, sub_1402C4980, sub_1402D5854, sub_1402EED3C and others
- **Callees:** sub_140329E1C, the opcode handlers

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Runs one UI script: the byte-coded layout and behaviour program of a list or panel screen.

## Behavior

- V: stores the flag in a state dword, calls the state reset sub_140329E1C, clears the script cursor words and the pending-line flag, and takes the first row from the second argument unless the flag is non-zero.
- V: loops until the next opcode byte is 0x21: it calls the handler for that opcode from the 29-entry handler table (0x1406838F0, opcodes 0..28) with the record pointer, and the handler returns the pointer to the next record.
- V: record shape: opcode byte, total length byte, operands (opcode 22 is a single byte); conditional opcodes (the handler at 0x140327954) run the following records only while a row callback accepts the current row and skip them by their length otherwise.

## Referenced by

- Reads tables: [ItemListScriptLanguage0](../tables/ItemListScriptLanguage0.md), [ItemListScriptLanguage1](../tables/ItemListScriptLanguage1.md), [ItemListScriptLanguage2](../tables/ItemListScriptLanguage2.md), [ItemListScriptLanguage3](../tables/ItemListScriptLanguage3.md), [JobLearnListScriptLang1](../tables/JobLearnListScriptLang1.md), [JobLearnListScriptLang2](../tables/JobLearnListScriptLang2.md), [JobLearnListScriptLang3](../tables/JobLearnListScriptLang3.md), [JobUnitRowsScriptLang0](../tables/JobUnitRowsScriptLang0.md), [JobUnitRowsScriptLang1](../tables/JobUnitRowsScriptLang1.md), [JobUnitRowsScriptLang2](../tables/JobUnitRowsScriptLang2.md), [JobUnitRowsScriptLang3](../tables/JobUnitRowsScriptLang3.md)
- Resolves registries: [UiScriptOpcodes](../registries/UiScriptOpcodes.md)

## Notes

The handler table is addressed relative to the image base, and the conditional handler 0x140327954 is reached through that table, so neither address appears in this body. Read: the interpreter loop and two handlers (conditional and the one-byte opcode 22); the other opcodes are not decoded.

## Open questions

?: the operands and effect of each opcode.
