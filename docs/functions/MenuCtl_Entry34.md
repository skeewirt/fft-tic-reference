# MenuCtl_Entry34

- **Address:** `0x140376B58`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int64_t MenuCtl_Entry34(void)`
- **Callers:** the screen dispatcher ClassicMenu_RunScreenStack (table index 34)
- **Callees:** sub_14037A694, sub_140376678

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Step of the page of an entry of list 33 (table index 34): runs a text widget and returns to the list.

## Behavior

- V: when its window is not busy it runs the widget step sub_14037A694 on the block at 0x140D49580; when that returns 0 it plays cue 2, pops, clears mask 0x10 of the windows below and sets mask 0x100 on the list window.
- V: when this record's own dword 1 is 170 or 171 it does the same one level further down; then it calls sub_140376678(0) to rebuild the list.

## Open questions

None recorded.
