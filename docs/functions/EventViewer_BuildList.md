# EventViewer_BuildList

- **Address:** `0x1402D1FD8`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t EventViewer_BuildList(void)`
- **Callers:** EventViewer_EntryPage, the tavern page code
- **Callees:** EventVar_Read, EventViewer_IsHidden, sub_140379F3C, sub_140379DF0

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the list of replayable story events: for each of 78 positions, one event variable decides whether the entry is listed.

## Behavior

- V: walks positions 0..77; positions 14, 16, 28, 33, 47, 61..66, 75, 76 and 77 read event variable 427 + n (n counts the special ones), every other position reads 444 + k (k counts the plain ones: 64 of them, variables 444..507).
- V: an entry is listed when its variable is nonzero and EventViewer_IsHidden is false; the list item is a 16-bit text reference: 0xE800 + k for a plain entry, 0xE840 + n for a special one (bank 29 message index 0..63 and 64..77).
- V: stores the item in the shared list array (0x140D498F0, 128 words) and a zero in the parallel array (0x140D497D0), with a range check at a byte offset of 0x100; then sets up the list widget (sub_140379F3C(10, n), sub_140379DF0) and pushes the page kind 29.
- V: each store comes before its range check (the byte offset is compared with 0x100 after the write); the loop lists at most 78 entries, so the check never fires in this builder.
- V: after the loop the count goes to the page record (dword at 0x140D8D8F0 + 0x5C x depth, the depth at 0x140D8DBA0) and to the widget, which shows at most 8 rows at once (the count capped at 8 for the visible window).

## State touched

- Calls: [EventVar_Read](EventVar_Read.md), [EventViewer_IsHidden](EventViewer_IsHidden.md)

## Referenced by

- Called by: [EventViewer_EntryPage](EventViewer_EntryPage.md)
- Observed behaviours: [StoryEventListBuildsASharedBoardArrayFromBitVariablesAndHoldsTextReferences](../behaviors/StoryEventListBuildsASharedBoardArrayFromBitVariablesAndHoldsTextReferences.md)

## Notes

The special positions are a chain of compares with constants; the table of event numbers has 78 words in the order plain 0..63 then special 64..77. The references 0xE800 and 0xE840 are results of the 16-bit subtraction of 0x19BC (6588) and 0x196B (6507) from the variable number, not constants in the code.

## Open questions

Which tavern row opens it.
