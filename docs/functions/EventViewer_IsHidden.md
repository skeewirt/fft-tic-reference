# EventViewer_IsHidden

- **Address:** `0x1402D1F90`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `bool EventViewer_IsHidden(int variable)`
- **Callers:** EventViewer_BuildList
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Says whether an unlock variable of the story event list is hidden: such entries are never listed.

## Behavior

- V: true for variables 427, 428, 429, 431, 432, 434, 435, 436, 437, 438 and 439; false for all others (so of the 14 special entries only 430, 433 and 440 can be listed).

## Referenced by

- Called by: [EventViewer_BuildList](EventViewer_BuildList.md)
- Observed behaviours: [StoryEventListBuildsASharedBoardArrayFromBitVariablesAndHoldsTextReferences](../behaviors/StoryEventListBuildsASharedBoardArrayFromBitVariablesAndHoldsTextReferences.md)

## Open questions

Why these entries exist but are never listed.
