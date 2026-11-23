# DrawCmd_PrintNumber

- **Address:** `0x14039C200`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `unsigned __int8 *__fastcall DrawCmd_PrintNumber(unsigned __int8 *cmd)`
- **Callers:** the draw-script interpreter through the handler table at 0x1406932E8 (index 14; a data reference at 0x140693358; the table address is reached by the interpreter, not from this body)
- **Callees:** sub_14032A204, sub_140395550, sub_1403953D8

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Draw-script command (entry 14 of the 16-entry handler table at 0x1406932E8): prints a number, right-aligned in a field, using a value function chosen by the command, and returns the next command.

## Behavior

- V: sets the text colour dword `dword_140906B28` by language: 6160587 when `g_LanguageInfo` is null or its dword at +8 equals 1; 5636343 when +8 equals 0; otherwise 2621648.
- V: calls the function at `qword_141D3B930[cmd[3]]` with `cmd[9]` and formats the result with `%d` into a local buffer (`sub_14032A204`).
- V: `cmd[4]` is the field width: it draws `cmd[4] - digits` blank cells first (`sub_140395550`, 8 pixels apart starting at x = `cmd[7]`, y = `cmd[8] + 4`), then each digit with `sub_1403953D8` at y = `cmd[8] + 1`, 8 pixels apart.
- V: each digit glyph is selected from the digit character code as `8 * char - 216`.
- V: returns `cmd + cmd[1]`, so byte 1 of a command is its length.
- I: the table at 0x1406932E8 is the handler table of a draw-script interpreter (rests on the handler's command-pointer-in, next-command-out shape; the interpreter itself was not read).

## Notes

V: whole body read. The name is ours.

## Open questions

?: the value function table at `qword_141D3B930`.
