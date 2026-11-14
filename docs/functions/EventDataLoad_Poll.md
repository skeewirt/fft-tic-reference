# EventDataLoad_Poll

- **Address:** `0x140274324`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `bool EventDataLoad_Poll(void)`
- **Callers:** MultiStr_Includes at 0x1402737A4 (MultiStr_Includes returns this routine's result as a nonzero test; opcode 0x8A reaches it through SceneCallback_Dispatch mode 1). Also sub_140210AF0 (at 0x140212D50), sub_140318090 (at 0x140318190 and 0x1403182CD), and one data reference at 0x143D39400.
- **Callees:** `sub_1402742CC` (language table pair for a track index), GameData_ReadSectors (at 0x1402F40C4; sends kind 17 to EventScript_LoadFile and other kinds through `sub_1402F3D58` or `sub_1403D2358`)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

A state machine that starts a table-selected game data read for the current track index and reports busy until the read and a timed delay have finished; it is the busy test that opcode 0x8A waits on, through MultiStr_Includes.

## Behavior

- V: returns false at once when word_141D330BC (the current track index) is negative.
- V: the state is the byte byte_140D40927. States 0 to 3 are handled below; any other value leaves the result false.
- V: state 0: sets word_143D1A1B0 (a delay counter) to 60 when byte_140D405AA is non-zero, otherwise to 0. Calls `sub_1402742CC` with the track index, which returns two dwords from the per-language table (dword_1406739C0 and dword_1406739C4 when the language flag at g_LanguageInfo + 8 is non-zero, otherwise dword_1406749C0 and dword_1406749C4) into a first value and a second value. If the second value is 0, it sets word_141D330BC to 1 and reads again. When the second value is then non-zero it calls GameData_ReadSectors(first value, 0, second value, &unk_1418A2E00). It then sets the state to 1 and returns busy.
- V: state 1: returns busy while the high dword of qword_141856AB0 is non-zero. When it is zero, it sets the state to 2 and returns busy.
- V: state 2: when word_143D1A1B0 is 0, and byte_140D405AA is non-zero, it writes 3 to the dword at unk_1437A5C48 + 96 times byte_140D405AA. It then sets qword_1411A3828 to v + the dword at v + 24, where v is qword_143740220 indexed by the track index, and sets the state to 3. In either case the result is busy.
- V: state 3: returns busy while the dword at unk_1437A5C48 + 96 times byte_140D405AA is non-zero. It does not change the state.
- V: after the state work, when the function has not returned early, it decrements word_143D1A1B0 by 1 if that value is positive.
- V: the function does not wait by itself. Each call is one poll; the caller repeats it once per frame.
- I: state 3 ends when some other code sets that dword to 0. Nothing in this routine sets the high dword of qword_141856AB0 to non-zero; GameData_ReadSectors sets it to 0 at its end.

## State touched

- Calls: [GameData_ReadSectors](GameData_ReadSectors.md), [EventScript_LoadFile](EventScript_LoadFile.md)

## Referenced by

- Called by event opcodes: [0x8A](../opcodes/README.md)

## Notes

MultiStr_Includes (0x1402737A0) is the callback the 0x8A loop sets; it is not this address. It returns the result of this routine as a 0 or 1 value.

## Open questions

What clears byte_140D40927 and sets word_141D330BC back, and who sets the high dword of qword_141856AB0 while a read runs. What the dword tables dword_1406739C0, dword_1406739C4 and their language twins hold. What the records at unk_1437A5C48 (stride 96 bytes) represent. What sub_140210AF0 and sub_140318090 do with the result.
