# GUIWidget_AllResourcesLoadedThunk

- **Address:** `0x1403FC0D8`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char GUIWidget_AllResourcesLoadedThunk(GUIWidget *w)`
- **Callers:** vtable entries (0x143D42214, 0x140721E38), sub_1400F4DDC
- **Callees:** sub_1403FCFEC, GUIWidget_AllResourcesLoaded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Vtable entry: when byte w+82 is set it first runs sub_1403FCFEC, then returns GUIWidget_AllResourcesLoaded(w).

## Behavior

- V: if (w+82) sub_1403FCFEC(w); return GUIWidget_AllResourcesLoaded(w).

## State touched

- Calls: [GUIWidget_AllResourcesLoaded](GUIWidget_AllResourcesLoaded.md)

## Notes

The name is ours (IDB: sub_1403FC0D8). 1568 hits per 4 s. sub_1403FCFEC is a long resource pass (not read); w+82 is I: 'resources pending'.

## Open questions

? What sub_1403FCFEC does.
