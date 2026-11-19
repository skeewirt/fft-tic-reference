# GUIFontSlots_AcquireImage

- **Address:** `0x1403DB280`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned int GUIFontSlots_AcquireImage(GUIFontSlots *slots, const char *name, int a3)`
- **Callers:** GUIFontSlotGroup_SetImageByName (sub_1403F3DAC), sub_1403DB6B8 (id keyed variant), sub_1400F4E74
- **Callees:** sub_1403DBB00, sub_1403DB390, sub_1403DA4C0, sub_140037CA4, sub_140091124, GUISlotVec16_Insert (sub_1403EE77C)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Gets a kind-3 (image) slot for a name: reuses an existing one (refcount +1) or requests the resource and appends a new record.

## Behavior

- V: when slots+424 != 0 the name is first translated through sub_1403DBB00 (table 125, key 2000, column dword at slots+424); a failed translation keeps the original name.
- V: sub_1403DB390 finds an existing record: found = sub_1403DA4C0 refcount +1 and the id returned. Otherwise a 32-byte local {resource ptr from sub_140091124(qword_143CD9B88, name, hash, 0, ..), refcount 1, +12 u16 flag 0} is inserted into the vector at slots+104 (GUISlotVec16_Insert, 16 bytes copied) and (index + 1) | 0x3000000 is returned.
- V: the hash comes from sub_140037CA4(buf, name) (its first dword).

## State touched

- Calls: [GUISlotVec16_Insert](GUISlotVec16_Insert.md)

## Referenced by

- Called by: [GUIFontSlotGroup_SetImageByName](GUIFontSlotGroup_SetImageByName.md), [IconImage_AcquireById](IconImage_AcquireById.md)

## Notes

The name is ours (IDB: sub_1403DB280). sub_1403DB6B8 maps a numeric icon key to a slot: keys 50..71 and 1100..1265 go to sub_1403DB420 / sub_1403DB5B4, other keys resolve a name with sub_1403DB140 and call this.

## Open questions

? the kind-3 record layout beyond +0 / +8 / +12 (written by the loader).
