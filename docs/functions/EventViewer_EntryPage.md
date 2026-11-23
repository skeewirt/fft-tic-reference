# EventViewer_EntryPage

- **Address:** `0x1402D2578`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void EventViewer_EntryPage(int *page)`
- **Callers:** the page dispatcher ClassicMenu_RunScreenStack (kind 30)
- **Callees:** EventVar_Read, Input_TestAction, EventVar_Write, EventChain_Find, WorldMenu_SetFade, sub_1401D80A8, sub_14033FDAC, PagedText_Step, EventViewer_BuildList, PagedText_Init

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The page of one replayable story event (page kind 30): shows the entry's text and, on the confirm, replays the event; on cancel it rebuilds the list.

## Behavior

- V: dispatches on the page state at +0xC: state 1 counts frames at +0x10, state 2 (after 20 frames) sets a text reference of 0x8800 plus the entry index (+0) and opens it with PagedText_Init, state 3 returns to the list when the window is done.
- V: on the confirm input (Input_TestAction with 0x10 / 0x1E) it writes event variable 508 = 1, then event variable 39 = the word of tbl_EventViewerList at the entry index (a zero-extended 16-bit read, twice), stores (EventChain_Find(event) != -1) in g_EventViewerChained, sets a flag bit and starts the scene change (WorldMenu_SetFade(7, 0)).
- V: row 67 of the table holds 0xFFFF: the confirm then writes 65535 to variable 39 and the chain lookup misses (seen in an emulation of the page's code on the pristine image).
- V: on cancel it clears the page's highlight bits and calls EventViewer_BuildList to show the list again.
- I: the reference 0x8800 + index is a message of text bank 17 by the same reference format (5-bit bank, 11-bit index) as the list's bank 29.

## State touched

- Calls: [EventVar_Read](EventVar_Read.md), [Input_TestAction](Input_TestAction.md), [EventVar_Write](EventVar_Write.md), [EventChain_Find](EventChain_Find.md), [WorldMenu_SetFade](WorldMenu_SetFade.md), [sub_1401D80A8](sub_1401D80A8.md), [sub_14033FDAC](sub_14033FDAC.md), [PagedText_Step](PagedText_Step.md), [EventViewer_BuildList](EventViewer_BuildList.md), [PagedText_Init](PagedText_Init.md)

## Referenced by

- Observed behaviours: [StoryEventListBuildsASharedBoardArrayFromBitVariablesAndHoldsTextReferences](../behaviors/StoryEventListBuildsASharedBoardArrayFromBitVariablesAndHoldsTextReferences.md)
- Reads tables: [EventViewerList](../tables/EventViewerList.md)

## Notes

The entry index comes from EventViewer_OpenEntry (the message index of the list item). 0x8800 is built by an `add` of the index; 65535 is the table word of row 67, not a constant in the code.

## Open questions

Which scene the start with variable 39 = 65535 would load (no retail script sets variable 430, so the row is never listed in the retail game).
