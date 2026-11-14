# EventCmd_Run

- **Address:** `0x1402F146C`
- **Area:** [Event commands](../areas/event-commands.md)
- **Prototype:** `bool EventCmd_Run(void)`
- **Callers:** `sub_1401E1618`, `sub_140372F9C`
- **Callees:** EventVar_Read (3), EventCmd_ServiceRequests, `sub_1402F18CC` and the 54 command handlers

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Runs the 4-byte scripted command loop: it services pending requests, fetches the next 32-bit command into the command register, calls the handler for its command class, and repeats until a command stops or yields.

## Behavior

- V: each pass reads event variables 0x5C, 0x5D and 0x5E and passes them to EventCmd_ServiceRequests, then calls `sub_1402F18CC`.
- V: the command lives in a 128-bit command register at `xmmword_141862440` (with companion words at `xmmword_141862450`, `xmmword_141862460` and `qword_141862470`); byte 8 of the register is the command class and the flags word is at +12.
- V: when flag bit 2 of the command register is set, the whole register block is saved into one of five 56-byte context slots at `unk_1411A7560` (slot number `word_140D8DBA4`, only if below 5), a bit for it is set in the bitset at `dword_1411A7030`, and the slot number is advanced.
- V: the handler is picked from a 54-entry table at 0x140681DE0 (image base + 0x681DE0) indexed by the command class, and is called with the flags word and `qword_143CD9E28` as arguments.
- V: command class 22 with operand 1, 2, 3 or 4 is skipped when `qword_143CD9E28` has a non-zero field at +48 and a field of 1 at +80.
- V: the loop ends when flag bits 0x28 are set; it clears 0x08 and returns true when bit 0x20 is clear.
- V: when flag bit 4 is set it fetches the next command: it clears bit 2 and sets bit 4 of the flags (0x10), takes the script index from the high word of the register and the position from the low word of `xmmword_141862450`, finds the script's start as `dword_140D4CC70[index] >> 2`, loads the 32-bit command at that start plus the position into the register's dword at +8 (class in byte 8, three operand bytes in bytes 9 to 11), and advances the position by one.
- V: so the command stream is an array of 32-bit commands with a table of script start offsets at its head; each command is 4 bytes, unlike the variable-length byte-opcode event scripts.
- I: this is a separate small script language with 54 command classes, probably the world-map or scene script; it is not the byte-opcode battle-event interpreter.

## State touched

- Calls: [EventVar_Read](EventVar_Read.md), [EventCmd_ServiceRequests](EventCmd_ServiceRequests.md)

## Referenced by

- Called by: [sub_1401E1618](sub_1401E1618.md), [sub_140372F9C](sub_140372F9C.md)

## Notes

The command classes are 0-53; entries 54 and above in the table are not code. The byte-opcode event interpreter is a different routine and is still unresolved.

## Open questions

What each command class does, and which routine interprets the byte-opcode event scripts.
