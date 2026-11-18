# ItemListScriptLanguage1

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1408F5230`
- **Rows:** 1 script of 198 bytes
- **Keyed by:** script byte offset
- **Read by:** [sub_140333974](../functions/sub_140333974.md), [UiScript_Run](../functions/UiScript_Run.md)
- **Row layout:** [UiScriptRecord](../structs/UiScriptRecord.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The UI script that lays out and runs the item list screen's widgets, language 1 (198 bytes, then a block of rectangles). Verdict: designer-data.

## Behavior

- V: sub_140333974 (item list gadget handler): picks the language's script (0 -> here, 3 -> 0x1408F5570, 2 -> 0x1408F53D0, other -> 0x1408F5230) and runs it with the script interpreter loop until the 0x21 byte
- V: UiScript_Run (0x1403278EC) is the interpreter entry used by other screens
- V: records parse cleanly with the length byte (opcode 22 is one byte); the terminator 0x21 sits at byte 197; the bytes after it are rectangles

## Notes

Our names. Tags: V format and extent, ? operand meanings.

## Open questions

- ?: operand meaning of each opcode (cell, text, condition, select ops)
