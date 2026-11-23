# EventViewer_OpenEntry

- **Address:** `0x1402D2468`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void *EventViewer_OpenEntry(int entryIndex)`
- **Callers:** EventViewer_ListInput
- **Callees:** sub_1400FF714

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Opens the page of one story event list entry: stores the entry index and sets the entry's text.

## Behavior

- V: pushes page kind 30 with the entry index as its argument and sets the page text id to the index + 59392 (0xE800, bank 29).

## Referenced by

- Called by: [EventViewer_ListInput](EventViewer_ListInput.md), [ScreenReopen_Step](ScreenReopen_Step.md)
- Observed behaviours: [StoryEventListBuildsASharedBoardArrayFromBitVariablesAndHoldsTextReferences](../behaviors/StoryEventListBuildsASharedBoardArrayFromBitVariablesAndHoldsTextReferences.md)

## Open questions

None recorded.
