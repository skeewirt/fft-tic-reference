# GUIWidget_ReleaseSlotGroup

- **Address:** `0x1403FBB20`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUIWidget_ReleaseSlotGroup(GUIWidget *w, GUIFontSlotGroup *g)`
- **Callers:** sub_1402A8EC4, sub_1403DABF0
- **Callees:** GUIFactory_FreeSlotGroup

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Removes a slot group from the widget's group vector and returns it to the pool.

## Behavior

- V: scans w+224..+232 (8-byte pointers) for g; on a hit the tail is moved down with memmove, w+232 -= 8 and GUIFactory_FreeSlotGroup(qword_143CDA280, g) is called; no hit does nothing (the returned value is then stale).

## State touched

- Calls: [GUIFactory_FreeSlotGroup](GUIFactory_FreeSlotGroup.md)

## Notes

The name is ours (IDB: sub_1403FBB20). Mirror of GUIWidget_NewSlotGroup. Whole-widget teardown (sub_1403F9188) frees the same vector element by element without going through this.

## Open questions

? the two callers were not read (texture unload paths).
