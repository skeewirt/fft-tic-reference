# GUIFontSlots_IsLoaded

- **Address:** `0x1403DA3EC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `bool GUIFontSlots_IsLoaded(GUIFontSlots *slots, unsigned int slotId)`
- **Callers:** GUITextLayout_IconsReady (sub_1403DCE74), GUIFontSlotGroup_Poll, GUIWidget_AllResourcesLoaded, sub_1400F4F20
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

True when the slot exists, has a non-zero refcount and its loaded byte is set (the texture / image behind it finished loading).

## Behavior

- V: same id decode as GUIFontSlots_Release. For kind 0 / 1 / 3 the test is (u16 rec+8 != 0) and (byte rec+12 != 0); for kind 2 it is (u16 rec+24 != 0) and (byte rec+28 != 0).
- V: returns 1 when both hold, else 0. An out-of-range id or unknown kind returns 0 (the local result is initialised to 1 but only returned on the success path).
- V: pure read, no side effects.

## Referenced by

- Called by: [GUIFontSlotGroup_Poll](GUIFontSlotGroup_Poll.md), [GUITextLayout_IconsReady](GUITextLayout_IconsReady.md), [GUIWidget_AllResourcesLoaded](GUIWidget_AllResourcesLoaded.md)

## Notes

The name is ours (IDB: sub_1403DA3EC). Who sets the loaded byte (+12 / +28) was not traced.

## Open questions

? the writer of the loaded byte (probably the resource-load completion callback).
