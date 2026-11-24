# ClassicMenu_OpenNumberEntry

- **Address:** `0x140379F8C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int *ClassicMenu_OpenNumberEntry(int64_t unused, uint32_t minMax, int textId, int16_t *pos)`
- **Callers:** PartyLoader_OpenPrompt, EventVarEditor_ListInput
- **Callees:** EventText_FindMessage, sub_1402D8E64, EventTask_Start

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Opens the classic number entry window: a range packed in one dword, an optional caption text, and a value word the window edits (word 0x140D498D4).

## Behavior

- V: min = low word, max = high word of the second argument; the digit count is 1 when both are below 10, else 2 below 100, 3 below 1000, 4 otherwise.
- V: with a text id it measures the message (EventText_FindMessage, sub_1402D8E64) and widens the window by its width; the width per digit is 5 or 3 by language.
- V: fills the window record at 0x140D499F0 (position from pos[0] and pos[2] + 8, the range words at 0x140D498D8 / DA, the value pointer 0x140D498D4) and starts sub_140361410 in event task slot 12 with that record.
- V: returns the window record.

## State touched

- Calls: [EventText_FindMessage](EventText_FindMessage.md), [EventTask_Start](EventTask_Start.md)

## Referenced by

- Called by: [EventVarEditor_ListInput](EventVarEditor_ListInput.md), [PartyLoader_OpenPrompt](PartyLoader_OpenPrompt.md)

## Open questions

None recorded.
