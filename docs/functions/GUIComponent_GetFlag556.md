# GUIComponent_GetFlag556

- **Address:** `0x14040A52C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char GUIComponent_GetFlag556(GUIComponent *c)`
- **Callers:** 16 vtables (0x140721F48, 0x140721FC0, ..., entries of the UIAddon component classes)
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Trivial virtual accessor: returns byte c+556.

## Behavior

- V: return *(byte *)(c + 556).

## Notes

The name is ours (IDB: sub_14040A52C). 28 hits per 4 s. I: a per-component flag exposed to the widget (e.g. 'modal' or 'blocks input'); only the offset is known.

## Open questions

? Meaning of byte +556.
