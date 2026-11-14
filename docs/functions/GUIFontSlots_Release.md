# GUIFontSlots_Release

- **Address:** `0x1403DA30C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUIFontSlots_Release(GUIFontSlots *slots, unsigned int slotId)`
- **Callers:** GUIFontSlotGroup_ReleaseAll (3 sites), GUITextNode_Layout (end of layout, per icon reference), sub_1403DCF00, sub_1403F3BFC, sub_1403F40AC, sub_1403F43C8, sub_1403FCFEC, sub_1400F4EC4
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Drops one reference from a slot of the GUI slot registry (g_GUIFontSlots): decrements the record's u16 refcount, never below 0, and never frees anything.

## Behavior

- V: index = (slotId & 0xFFFFFF) - 1, kind = slotId & 0xFF000000. kind 0 reads the vector at slots+16 / +24 (16-byte records, refcount at rec+8), kind 0x1000000 the vector at +48 / +56 (refcount rec+8), kind 0x2000000 the vector at +80 / +88 (32-byte records, refcount rec+24), kind 0x3000000 the vector at +112 / +120 (refcount rec+8).
- V: the index is bounds-checked against the vector size; an out-of-range id or an unknown kind returns without effect. If the refcount is non-zero it is decremented by 1 (a u16 store); at 0 nothing happens (saturating).
- V: no destructor, texture release or list removal runs here; the resource stays in the record with refcount 0. The slot is reused later by the insert helpers (they take the first record whose first qword is 0, see GUISlotVec16_Insert), so a refcount-0 record is only 'free' for lookups (they skip refcount 0 records).

## Referenced by

- Called by: [GUIFontSlotGroup_ReleaseAll](GUIFontSlotGroup_ReleaseAll.md)

## Notes

Slot id layout (V, from the decode in GUIFontSlots_Release / _GetResource): id = (index + 1) | (kind << 24); kind 0 = plain slot vector (16-byte records at slots+16, refcount u16 at rec+8, loaded byte rec+12), kind 1 = vector at slots+48 (16-byte records, refcount rec+8), kind 2 = texture-part vector at slots+80 (32-byte records, refcount rec+24, loaded byte rec+28), kind 3 = image vector at slots+112 (16-byte records, refcount rec+8). The resource pointer is the first qword of the record. The name is ours (IDB: sub_1403DA30C). The sibling that increments is sub_1403DA4C0 (same decode, +1, returns the old count).

## Open questions

? who finally frees the resource of a refcount-0 record (not traced; sub_1403D8D1C does the same for UIName records and frees there).
