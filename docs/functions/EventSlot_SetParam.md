# EventSlot_SetParam

- **Address:** `0x1402B1FB4`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void EventSlot_SetParam(int level, int b)`
- **Callers:** EventControl_PausedTick
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Stores an event parameter record: -996, 100 * level / 127 and b into xmmword_140D3A910, and level into dword_1418623B8, when qword_1418623A8 is set.

## Behavior

- V: when qword_1418623A8 is set it stores -996, 100 * level / 127 and b into xmmword_140D3A910 and level into dword_1418623B8.
- I: part of the event's sound and parameter slots; EventControl_PausedTick calls it with 0 on a skip unless the EventId skip_no_reset byte is set (the test is in the caller).

## Open questions

? what the three stored values drive.
