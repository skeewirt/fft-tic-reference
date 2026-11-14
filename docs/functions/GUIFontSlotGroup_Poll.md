# GUIFontSlotGroup_Poll

- **Address:** `0x1403F3EA4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char GUIFontSlotGroup_Poll(GUIFontSlotGroup *g)`
- **Callers:** GUIWidget_AllResourcesLoaded, sub_1401C0534, sub_1402A8EC4, sub_1403E9344
- **Callees:** GUIFontSlots_IsLoaded, sub_1403F40AC, sub_1403F3FAC

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Per-frame poll of one texture / font group: once its slots are loaded it runs the finishing steps and returns whether the group is complete.

## Behavior

- V: slot id g+84 (type byte 3 with g+89 set looks in the type-3 vector of g_GUIFontSlots, +112 / +120 stride 16, loaded when byte +12 and +13 are set; otherwise sub_1403DA3EC) loaded -> sub_1403F40AC(g) (copies the group's entries from the slot, grows the vector at g+24, not read further).
- V: slot id g+80 loaded and g+88 = 0 -> sub_1403F3FAC(g): reads the texture size (sub_1403DCA04), pushes {0, size} to the entry vector at g+24, g+88 = 1, posts event xmmword_140723480.
- V: when g+90 (all dependants done) is set returns g+88. Otherwise the dword list g+56..+64 is walked: every id must be loaded; if all are, g+90 = 1; the return value is g+88 (0 when a dependant is missing).

## State touched

- Calls: [GUIFontSlots_IsLoaded](GUIFontSlots_IsLoaded.md)
- Reads: [g_GUIFontSlots](../globals/g_GUIFontSlots.md)

## Referenced by

- Called by: [GUIWidget_AllResourcesLoaded](GUIWidget_AllResourcesLoaded.md)

## Notes

The name is ours (IDB: sub_1403F3EA4). 37761 hits per 4 s because it is polled for every group every frame. It also fills the per-group size entry that UIImage_ResolvePart / UIImage_DrawTiled read (texture size), but only once.

## Open questions

Exact record layouts (g+24 entries, +56 list).
