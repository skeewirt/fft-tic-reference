# GUIFontSlots_GetResource

- **Address:** `0x1403DA594`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void *GUIFontSlots_GetResource(GUIFontSlots *slots, unsigned int slotId)`
- **Callers:** GUITextNode_PlaceIcon, GUITextNode_Draw, GUIWidget_AllResourcesLoaded, sub_1403F3C3C, sub_1403F3FAC, sub_1403F40AC, sub_1403F43C8, sub_1403FC440, sub_1400F4F20
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the resource pointer (first qword of the record) of a live slot, or 0 when the id is bad or the refcount is 0.

## Behavior

- V: same id decode as GUIFontSlots_Release. kind 0: returns *(qword *)rec when u16 rec+8 != 0, else 0. kinds 1 and 3: same with the 16-byte records; kind 2: 32-byte records, refcount at rec+24.
- V: bad index or unknown kind returns 0; a refcount of 0 returns 0 (so a released slot reads as empty even though the record is kept).
- V: pure read; the caller in GUITextNode_PlaceIcon uses the result to test the record's own refcount (+80 of the pointed-to object) for exactly 1 before replacing the icon texture handle.

## Notes

The name is ours (IDB: sub_1403DA594). Different from GUIFontSlots_GetSlot (0x1403DB240), which is the lookup that GUITextNode_Draw uses by key; not compared here.

## Open questions

? the exact relation to GUIFontSlots_GetSlot.
