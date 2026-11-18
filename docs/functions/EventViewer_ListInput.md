# EventViewer_ListInput

- **Address:** `0x1402D22A8`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `char EventViewer_ListInput(int *state)`
- **Callers:** the page dispatcher sub_140246078 (table at 0x140681400, kind 29)
- **Callees:** EventViewer_OpenEntry, sub_1401D80A8

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Input handler of the story event list (page kind 29): confirms an entry, cancels, or scrolls.

## Behavior

- V: on the confirm it takes the list item at the cursor (a signed 16-bit cursor), masks it with 0x7FF and opens the entry's page (EventViewer_OpenEntry); on cancel it clears the state and returns to the tavern top.

## State touched

- Calls: [EventViewer_OpenEntry](EventViewer_OpenEntry.md), [sub_1401D80A8](sub_1401D80A8.md)

## Referenced by

- Observed behaviours: [StoryEventListBuildsASharedBoardArrayFromBitVariablesAndHoldsTextReferences](../behaviors/StoryEventListBuildsASharedBoardArrayFromBitVariablesAndHoldsTextReferences.md)

## Open questions

None recorded.
