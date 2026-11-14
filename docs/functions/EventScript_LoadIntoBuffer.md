# EventScript_LoadIntoBuffer

- **Address:** `0x1402340A4`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t EventScript_LoadIntoBuffer(uint32_t eventNumber)`
- **Callers:** `sub_14023F37C`
- **Callees:** SceneTask_WaitFrame, GameData_ReadSectors, `sub_1401DC8BC`, `sub_14021EA00`, `sub_14021EA68`, `sub_14021EAD4`, `sub_1401DAE20`, `sub_14002630C`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Loads an event script into the shared 10,240-byte event buffer and substitutes a variant for a few special events.

## Behavior

- V: loops, waiting a frame each time (SceneTask_WaitFrame), until GameData_ReadSectors(17, eventNumber * 5 or * 3, 10240, buffer) succeeds; the buffer is `unk_140D3CD50` and the script itself starts at `unk_140D3CD54`, after the 4-byte size prefix.
- V: when `xmmword_1437A62B0` is non-zero and the event number is one of 0x19B, 0x19D, 0x19F, 0x1A1, 0x1A3, 0x1A5, 0x1A7 or 0x1A9 (411 to 425, odd), it picks a slot 0 to 7 and replaces the tail of the loaded script with that slot's stored variant, then rewrites the size prefix.
- V: when no variant was applied and the enhanced flag `dword_1407D453C` is 1, it calls `sub_1401DAE20(qword_143CD9DB8, eventNumber)`.
- V: finally, unless the size prefix already holds the marker 0xF2F2F2F2, it stores a pointer to the end of the script (buffer plus the size prefix) in `qword_140D40990[0]` and overwrites the size prefix with 0xF2F2F2F2.
- I: the eight variant events are the scripts that carry per-run changes, such as player-chosen content.

## State touched

- Calls: [SceneTask_WaitFrame](SceneTask_WaitFrame.md), [GameData_ReadSectors](GameData_ReadSectors.md)
- Reads: [g_LanguageInfo](../globals/g_LanguageInfo.md)

## Referenced by

- Called by: [EventScript_LoadCurrent](EventScript_LoadCurrent.md)

## Notes

After this call the interpreter and the scan helpers read the script through the pointer `qword_140D40A90`.

## Open questions

What the stored variants are and who writes them.
