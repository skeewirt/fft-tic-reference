# UIGadgetFFTORadioButtonMenu_Event

- **Address:** `0x1402AD7F8`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void sub_1402AD7F8(UIGadgetFFTORadioButtonMenu *menu, GUINode *sender, GUIMessage *msg)`
- **Callers:** vtable `0x140716730` slot 2 (the gadget's event entry)
- **Callees:** None (walks its own entry array)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Maintains the radio menu's selected/hover index from the UI event stream. This is the writer of the command row's live selection.

## Behavior

- V: event `msg[0] == 0x0C` or `0x10`: clears `+280` (`0x1402AD881` for 0x0C, `0x1402AD8D1` for 0x10), finds `sender` in the entry-pointer array at `+24` (count at `+16`), and stores its index at `+280` (`0x1402AD8BA`). Event 0x10 also sets the pending-changed byte `+289 = 1` (`0x1402AD8B2`).
- V: event `0x0D`: clears `+280` (`0x1402AD8C7`) and returns.
- V: event `0x11` (hover): clears `+284` (`0x1402AD827`), finds the sender, and if it is the current GUI focus node (`sub_1403D7008(g_GUICore)`) stores the index at `+284` (`0x1402AD870`) and sets `+290 = 1` (`0x1402AD877`).
- V: no other event ids are handled.

## Notes

Menu index arithmetic: the gadget base is `UIAddonFFTOBattleCommand+840`, so `+280` is addon `+1120` (the selected command row) and `+284` is addon `+1124`. `sub_1402AD794` (vtable slot 4) copies `+289` into `+288` and clears `+289` each frame.

## Open questions

? the UI event id names (0x0C/0x0D/0x10/0x11 are raw ids); ? who fills the entry array.
