# MenuCtl_Entry28

- **Address:** `0x140375538`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char MenuCtl_Entry28(int *record)`
- **Callers:** the screen dispatcher ClassicMenu_RunScreenStack (table index 28; opened by ClassicMenu_HubStep (mask 0x100) and sub_140374B50)
- **Callees:** EventViewer_BuildList, sub_140375AD0, sub_140377118, sub_1403741C4, sub_140371984, PackedBlock767_Load, HelpMessage_Open, MenuCtl_Entry28_ResetRows

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Step of the row menu that opens the other list screens (table index 28): each row opens one list builder.

## Behavior

- V: it first copies the three globals at 0x141856700, 04 and 08 into 0x140D4941C, 0x140D40A98 and 0x140D492C8.
- V: the states are record dword 6: 1 the intro (a confirm or cancel starts the close and music 283), 2 and 3 the close animation and pop, 0 the menu; the menu has dword 12 rows with the cursor in dword 7 and a row kind per row in dwords 13 and up.
- V: confirm acts on the row kind: 1 loads packed block 4 and calls EventViewer_BuildList (kind 29), 2 calls sub_140375AD0 (the second tavern list, kind 31), 3 loads block 10 and calls sub_140377118 (kind 37), 4 loads block 2 and calls sub_1403741C4 (kind 24), 5 loads block 3 and calls sub_140371984 (kind 26), 6 prints text id 47178 and goes to the intro state.
- V: the help action opens HelpMessage_Open(4096 + byte at 0x140684E84 + row kind); cancel does what row kind 6 does.

## State touched

- Calls: [EventViewer_BuildList](EventViewer_BuildList.md), [sub_140375AD0](sub_140375AD0.md), [PackedBlock767_Load](PackedBlock767_Load.md), [HelpMessage_Open](HelpMessage_Open.md), [MenuCtl_Entry28_ResetRows](MenuCtl_Entry28_ResetRows.md)

## Notes

I: it is the top menu of the records and archive screens, because the lists it opens are the story event list and the tavern lists.

## Open questions

None recorded.
