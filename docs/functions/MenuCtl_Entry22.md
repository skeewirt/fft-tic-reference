# MenuCtl_Entry22

- **Address:** `0x140373784`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char MenuCtl_Entry22(int *record)`
- **Callers:** the screen dispatcher ClassicMenu_RunScreenStack (table index 22)
- **Callees:** sub_1403793DC, sub_14009B2E8, sub_14036D66C, sub_14037370C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Two-row question with a fade (table index 22): the first answer ends with a fade to a new scene, the other leaves.

## Behavior

- V: record dword 5 (a fade level written to a colour byte) rises by 8 a frame to 96 on its own and, after a confirm, by 8 to 255; on a cancel or on leaving, dword 4 is set from dword 5 and counts down by 8 to 0, after which the screen pops.
- V: up and down toggle dword 7; the help action opens sub_14036D66C with a text id from the byte table at 0x1406848F0 (index row + 36) plus 4096.
- V: confirm with row 0 sets the close mask 0x4, queues audio, sets mask 0x10 and clears 0x8 of a UI object's flag dword and calls sub_14009B2E8 with the string 'default'.
- V: when the fade reaches 255 with the message window idle it pops two levels, restores three globals from 0x141856700 to 08 and calls sub_1403793DC(27, ...).

## State touched

- Calls: [sub_1403793DC](sub_1403793DC.md)

## Open questions

? which question it asks; the string passed to sub_14009B2E8 is the only literal.
