# GUIFontSlotGroup_OnTextureLoaded

- **Address:** `0x1403F3FAC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 GUIFontSlotGroup_OnTextureLoaded(GUIFontSlotGroup *g)`
- **Callers:** GUIFontSlotGroup_Poll (when g+80 != 0, g+88 == 0 and sub_1403DA3EC says the slot is loaded)
- **Callees:** sub_1403DA594, GUIFontSlots_GetSlot, UIPartRef_GetTextureSize, sub_14006635C, sub_1403F43C8, GUIOwners_PostEvent

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Called by GUIFontSlotGroup_Poll once the group's texture slot (g+80) is loaded: stores the whole-texture rectangle as the first entry of the group's part vector, marks the group loaded and posts event 41 to its owners.

## Behavior

- V: record = sub_1403DA594(g_GUIFontSlots, g+80) (the slot record of the id at g+80, null when the slot's count is 0). Everything below happens only when the dword at record+80 (read with an atomic add of 0) is exactly 1; otherwise g+88 = 1 and g+90 = 1 and nothing else (the group is marked loaded / finished without data).
- V (refcount 1): size = UIPartRef_GetTextureSize(GUIFontSlots_GetSlot(g_GUIFontSlots, g+80)); a 16-byte entry {0, 0, width, height} (qword 0, then the two size dwords) is written over the first element of the part vector (g+24 begin, g+32 end, g+40 cap) when it is non-empty, else it is pushed back (grown with sub_14006635C when full).
- V: g+88 = 1; when the dependant dword list (g+56 / g+64) is not empty sub_1403F43C8(g) runs; then event {41, 0, 0, 0} with ev+16 = *g (the group's name string pointer) is posted: GUIOwners_PostEvent(g+96, 0, ev).
- I: the dword at record+80 is the texture object's reference count, so 'exactly 1' reads as 'only the slot table itself still holds it', i.e. the load finished; the else branch is the failed / shared case. Not tested live.

## State touched

- Calls: [GUIFontSlots_GetSlot](GUIFontSlots_GetSlot.md), [UIPartRef_GetTextureSize](UIPartRef_GetTextureSize.md), [GUIOwners_PostEvent](GUIOwners_PostEvent.md)
- Reads: [g_GUIFontSlots](../globals/g_GUIFontSlots.md)

## Notes

The name is ours (IDB: sub_1403F3FAC);  the only caller found is the poll. Group layout read here (V): +0 name key {char *, id}, +16 allocator, +24..+40 part rectangle vector (16-byte entries), +48 allocator, +56..+72 dependant slot-id vector (dwords), +80 texture slot id, +84 part-table slot id, +88 loaded flag, +89 part table is a type-3 slot, +90 finished flag, +96 four owner widget ids. Entry 0 being the whole texture is I (it is overwritten only when the part table was filled first).

## Open questions

? what sub_1403F43C8 does (dependant groups kick-off). ? the exact meaning of record+80 == 1. ? the order of the two loaders in practice (part table first, then texture, is what the poll code implies).
