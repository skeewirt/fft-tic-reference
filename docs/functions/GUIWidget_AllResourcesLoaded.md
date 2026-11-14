# GUIWidget_AllResourcesLoaded

- **Address:** `0x1403FB514`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char GUIWidget_AllResourcesLoaded(GUIWidget *w)`
- **Callers:** sub_1401980FC, sub_1401D1148, sub_1402AC9C4, sub_1403FC0D8
- **Callees:** GUIFontSlots_IsLoaded (sub_1403DA3EC), sub_1403F3C3C, GUIFontSlotGroup_Poll, GUIOwners_PostEvent

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Polls the widget's three resource vectors (texture refs, font / atlas groups, standalone refs) and returns 1 only when everything has finished loading.

## Behavior

- V: vector w+192..+200 (elements with a font-slot id at +16 and a loaded byte +20): an element whose id (type byte 1 or untyped) is loaded in g_GUIFontSlots gets sub_1403F3C3C (sets +20 = 1 and posts event xmmword_1407234A0 when the slot's refcount at +80 is 1); returns 0 as soon as one element is still not loaded.
- V: vector w+224..+232 (elements = groups): sub_1403F3EA4 per element, 0 when any is not ready. Vector w+256..+264: same pattern with event xmmword_1407234B0 (posted through GUIOwners_PostEvent). Returns 1 when all three vectors pass.

## State touched

- Calls: [GUIFontSlots_IsLoaded](GUIFontSlots_IsLoaded.md), [GUIFontSlotGroup_Poll](GUIFontSlotGroup_Poll.md), [GUIOwners_PostEvent](GUIOwners_PostEvent.md)
- Reads: [g_GUIFontSlots](../globals/g_GUIFontSlots.md)

## Referenced by

- Called by: [GUIWidget_AllResourcesLoadedThunk](GUIWidget_AllResourcesLoadedThunk.md)

## Notes

The name is ours (IDB: sub_1403FB514). Loading gate only; no pixel effect once everything is resident (2296 hits per 4 s = polled every frame).

## Open questions

What the three vectors are in file terms.
