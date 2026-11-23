# WorldMenu_RunTopCloseHook

- **Address:** `0x1402D0488`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 WorldMenu_RunTopCloseHook(void)`
- **Callers:** sub_1402D50E4, MenuCtl_Entry43, MenuCtl_Entry28
- **Callees:** indirect: table 0x140681030

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Calls the second-table hook of the world-menu control on top of the control stack (V: callers run it right after decrementing the stack depth; I: it is the counterpart of the open hook).

## Behavior

- V: as `WorldMenu_RunTopOpenHook` but the table is the one at 0x140681030.
- I: its entries are the counterpart hooks (entries 6 and 7 set `dword_140D498D0` to -1); callers invoke it after popping a level (rests on call order in sub_1402D50E4 and MenuCtl_Entry43).

## Notes

Whole body read.

## Open questions

Exact role of the hook tables.
