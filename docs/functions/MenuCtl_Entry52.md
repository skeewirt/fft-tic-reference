# MenuCtl_Entry52

- **Address:** `0x140346428`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char MenuCtl_Entry52(int *record)`
- **Callers:** the screen dispatcher ClassicMenu_RunScreenStack (table index 52)
- **Callees:** Party_RebuildFromBattleEntry, sub_1402B52E4, Input_TestAction

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Confirm step of the party loader (table index 52): while the number entry runs it waits for confirm or cancel; a confirm with the entered number below 512 rebuilds the party from that battle entry.

## Behavior

- V: while record dword 0 is 0 (or the number entry task in event slot 12 still runs) it reads input: cancel sets dword 0 to -1, confirm sets it to 1, both start the close.
- V: after the close it pops; on a confirm with the held number below 512 it calls sub_1402841D0(number), sub_1402B52E4 and sets the redraw mask; then it calls WorldMenu_RunTopOpenHook.
- V (read in PartyLoader_OpenPrompt and ClassicMenu_HubStep): it is the party loader's confirm: PartyLoader_OpenPrompt (sub_14034637C) opens the number entry 0..999 on word 0x140D498D4 and pushes kind 52; ClassicMenu_HubStep calls that function for mask 0x1000000, set from row 9 of the old main world menu.
- V: Party_RebuildFromBattleEntry (sub_1402841D0) empties every roster record and builds the units of battle entry `number`; sub_1402B52E4 (callee, read) then rebuilds variable-length per-unit lists through the pointer variable 0x14184A8E0: for each of the 54 save records it copies bytes from record +220 (up to 16, stopping after a 0xFE / 0xFF byte), an empty record giving one -2 byte, and it increments dword 0x143749F58.

## State touched

- Calls: [Party_RebuildFromBattleEntry](Party_RebuildFromBattleEntry.md), [Input_TestAction](Input_TestAction.md)

## Open questions

None recorded.
