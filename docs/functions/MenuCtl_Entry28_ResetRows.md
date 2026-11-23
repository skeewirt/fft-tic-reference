# MenuCtl_Entry28_ResetRows

- **Address:** `0x14037544C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int64_t MenuCtl_Entry28_ResetRows(int *record)`
- **Callers:** MenuCtl_Entry28 (six call sites)
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sets the windows of the row menu (kind 28) to their idle styles before it opens a list.

## Behavior

- V: sets the style words of the windows named by record dwords 0, 1, 2, 8, 9 and 10 (10, 6, 2, 5, 5, 5), the first window's pointer rows to 1 and 0.
- V: when record dword 6 is 2 it sets the style of the window named by dword 3 to 2; otherwise, when the row kind of the current row (dword 13 + dword 7) is not 2, it sets mask 0x10 in the first dword of the window record 0x140D4B9B0 + 56 x dword 3 and mask 0x800 of the state dword.

## Referenced by

- Called by: [MenuCtl_Entry28](MenuCtl_Entry28.md)

## Notes

The window record 0x140D4B9B0 + 56 x dword 3 is reached through a register (base + stride x index).

## Open questions

None recorded.
