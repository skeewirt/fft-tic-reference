# EventScript_LoadFile

- **Address:** `0x1402F3BC4`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `bool EventScript_LoadFile(uint32_t sectorIndex, uint8_t *buffer)`
- **Callers:** GameData_ReadSectors
- **Callees:** `sub_1402F420C` (number formatting), `sub_14002620C` and `sub_140026288` (string copy and append), the file helpers `sub_1403D2004`, `sub_1403D21F0`, `sub_1403D2358` and `sub_1403D21C8`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Loads one event script file from the game's script folder into a caller buffer.

## Behavior

- V: builds the file name `<root>/script/enhanced/event<NNN>.e`, or `script/classic/event<NNN>.e` when `dword_1407D453C` is 0, where NNN is the sector index divided by 5, or by 3 when the language-info field at +8 is 0, printed with `%03u`.
- V: the root is the game data path in `byte_142C81598`.
- V: opens the file; on failure it returns 1 without touching the buffer.
- V: on success it writes the file size plus 4 into the first four bytes of the buffer, then reads the whole file to `buffer + 4`, and closes the file; it returns 0.
- I: the divisor 5 versus 3 reflects the enhanced and classic layouts, in which one event spans 5 or 3 original disc sectors.

## State touched

- Calls: [sub_14002620C](sub_14002620C.md)
- Reads: [g_LanguageInfo](../globals/g_LanguageInfo.md)

## Referenced by

- Called by: [EventDataLoad_Poll](EventDataLoad_Poll.md), [GameData_ReadSectors](GameData_ReadSectors.md)

## Notes

This is how event scripts reach memory.

## Open questions

Where the loaded buffer is parsed into the event interpreter.
