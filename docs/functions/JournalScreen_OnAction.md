# JournalScreen_OnAction

- **Address:** `0x1401694E4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void JournalScreen_OnAction(void *screen, int action)`
- **Callers:** not recorded
- **Callees:** JournalReplay_StartEvent, JournalReplay_StartMovie, JournalList_RestoreCursor, UIGuide_Set, UIGuide_Show, sub_140169678, sub_1401163C4, sub_1400DF354

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Handles the actions of the Events screen.

## Behavior

- V: action 1: when the entry's new mark (entry +9 of the 12-byte list entries) is set it clears it and, for every word of the save block's list at +6666 (128 entries) equal to the entry key, clears the byte at +6922 + i and sets the byte at +7050 + i to 1.
- V: action 2 calls JournalReplay_StartEvent; action 3 calls JournalReplay_StartMovie.
- V: action 65537 (0x10001): when panel +112 is non-zero it calls sub_1401163C4(save block, 4, 1, 0) and sends a JournalNotification carrying panel +112; then JournalList_RestoreCursor and the guide 13002. Action 65538 calls sub_140169678 (both tested as the action number minus 3 minus 65534, so 0x10001 does not appear as a constant).

## State touched

- Calls: [JournalReplay_StartEvent](JournalReplay_StartEvent.md), [JournalReplay_StartMovie](JournalReplay_StartMovie.md), [JournalList_RestoreCursor](JournalList_RestoreCursor.md), [UIGuide_Set](UIGuide_Set.md), [UIGuide_Show](UIGuide_Show.md)

## Referenced by

- Appears in flows: [ChronicleEventReplay](../flows/ChronicleEventReplay.md)

## Open questions

None recorded.
