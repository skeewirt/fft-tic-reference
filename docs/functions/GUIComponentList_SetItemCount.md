# GUIComponentList_SetItemCount

- **Address:** `0x14040CA1C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 GUIComponentList_SetItemCount(GUIComponentList *list, int count)`
- **Callers:** sub_1400F56D8, sub_14028D7BC, sub_14028D870, sub_1403F2BD4
- **Callees:** sub_14040C604

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sets the number of list items; when it changed, invalidates the bound slots and marks both the scroll bars and the layout dirty.

## Behavior

- V: when list+648 != count: list+672 = -1; list+648 = count; sub_14040C604(list) (not read); word list+684 = 0x0101, i.e. +684 (scroll bars dirty) = 1 and +685 (layout dirty) = 1. Equal count does nothing.

## Notes

The name is ours (IDB: sub_14040CA1C). list+672 = -1 is the 'nothing bound / no cursor item' marker (I; not read elsewhere here).

## Open questions

? what sub_14040C604 does (a re-layout or slot reset). ? role of +672.
