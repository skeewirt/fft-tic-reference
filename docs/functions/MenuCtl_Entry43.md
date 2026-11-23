# MenuCtl_Entry43

- **Address:** `0x140318BBC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char MenuCtl_Entry43(int *record)`
- **Callers:** the screen dispatcher ClassicMenu_RunScreenStack (table index 43; opened by ClassicMenu_HubStep (mask 0x100000) and sub_140318860)
- **Callees:** sub_140319218, sub_1403196DC, HelpMessage_Open, PackedBlock767_Load, sub_1402D5068, Input_TestAction

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Step of a row menu with a short intro and a close animation (table index 43): its rows open kinds 44, 45 and 33 or print a notice.

## Behavior

- V: record dword 6 is the state: 1 is the intro (a confirm or cancel starts the close, sets mask 0x4 of the state dword and starts music 283 or an audio command), 2 and 3 run the close animation and then pop, re-open the screen below and set the redraw masks; 0 is the menu.
- V: the menu has record dword 12 rows with the cursor in dword 7 (16 pixels a row, wrapping); each row has a row kind in dwords 13 and up. Confirm acts on the row kind: 0 calls sub_140319218 (pushes kind 44), 1 calls sub_1403196DC (pushes kind 45), 2 builds a list of 43 entries and pushes kind 33, 3 prints text id 47326 and goes to the intro state.
- V: the help action (0x20) opens HelpMessage_Open(4235 + row kind), 4265 for row kind 4; cancel prints text id 47326 (state 1), like row kind 3.
- V: confirm saves the row in 0x140D49688 and the row kind in dword 1 of 0x1437A62B0.

## State touched

- Calls: [HelpMessage_Open](HelpMessage_Open.md), [PackedBlock767_Load](PackedBlock767_Load.md), [Input_TestAction](Input_TestAction.md)

## Open questions

? which game screen it is: the mask that opens it is set by the screens that close.
