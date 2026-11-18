# EventChain_Find

- **Address:** `0x14033D840`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int EventChain_Find(int event)`
- **Callers:** EventViewer_EntryPage, sub_1402D28C8, ScenarioSetup_ApplyRecord
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Looks an event number up in a 9-entry table of chained events and records the entry's two bytes.

## Behavior

- V: walks 9 entries of 4 bytes at 0x1406848F0 and compares the event with each entry's first word read as a signed 16-bit value.
- V: on a match it stores byte +3 of the entry in the dword at 0x143807790 and byte +2 in the dword at 0x143807794 and returns byte +2.
- V: on a miss it stores 1 in the dword at 0x143807790 and returns -1.

## Referenced by

- Called by: [EventViewer_EntryPage](EventViewer_EntryPage.md), [ScenarioSetup_ApplyRecord](ScenarioSetup_ApplyRecord.md)

## Notes

An event number above 32,767 never matches (the table word is sign-extended, the argument is not). The two globals are addressed rip-relatively; their addresses are computed from the displacements.

## Open questions

What the two recorded bytes mean.
