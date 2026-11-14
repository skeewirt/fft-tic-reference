# GUILayer_SetCurrent

- **Address:** `0x1403E9218`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char GUILayer_SetCurrent(UIRenderer *r, int index)`
- **Callers:** GUILayer_Select, GUICore_DrawWidget, ComponentLayer_DrawMaskComponent and a vtable entry
- **Callees:** GUILayer_Flush

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Flushes the batch and makes layer record `index` current; out-of-range indices select the next free slot (capped at 510). Returns 1 when the current layer changed.

## Behavior

- V: GUILayer_Flush(r) first. When index < 0 or index >= count (dword r+606584): index = min(count, 510). Equal to the current (dword r+606588) -> return 0.
- V: otherwise r+606588 = index; (*(qword_143CDA098 + 37936) + 208) = &r[+303480 + 592 * index] (the UI renderer's current layer record pointer); dword r+606604 = -1; return 1.

## State touched

- Calls: [GUILayer_Flush](GUILayer_Flush.md)
- Reads: [Renderer.ui_manager](../structs/Renderer.md#ui_manager), [g_Renderer](../globals/g_Renderer.md)

## Referenced by

- Called by: [GUICore_DrawWidget](GUICore_DrawWidget.md), [GUILayer_Select](GUILayer_Select.md)
- Observed behaviours: [JobTreeLayerList](../behaviors/JobTreeLayerList.md)

## Notes

The name is ours (IDB: sub_1403E9218). 2091 hits per 4 s. Layer records are 592 bytes (148 dwords) from r+303480, count r+606584, current r+606588; r+606604 = -1 invalidates a cached value.

## Open questions

? What r+606604 caches.
