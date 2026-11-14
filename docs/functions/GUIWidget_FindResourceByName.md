# GUIWidget_FindResourceByName

- **Address:** `0x1403FBB80`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `NameKey **GUIWidget_FindResourceByName(GUIWidget *w, NameKey *key)`
- **Callers:** ComponentEffects_Collect, GUINineGridNode_Draw, UIImageNode_Draw, GUITextNode_Draw's siblings sub_1403EBFA0 / sub_1403EC794, sub_1403DABF0, sub_1403DB420, sub_1403DB5B4, sub_1403F495C and a vtable entry (12 total)
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Linear search of the widget's resource-name vector (w+224..+232, pointers to name records) for the entry equal to a name key; returns the entry or null.

## Behavior

- V: entry = *it; a pair matches by interned id when entry+8 (dword) and key+8 are both non-zero (ids equal), otherwise by byte-wise C string compare of *entry with *key (both char*). First match is returned; end of vector returns 0.

## Referenced by

- Called by: [ComponentEffects_Collect](ComponentEffects_Collect.md), [GUINode_DrawKind5](GUINode_DrawKind5.md), [GUINode_DrawKind7](GUINode_DrawKind7.md), [GUIWidget_EnsureSlotGroup](GUIWidget_EnsureSlotGroup.md), [sub_1403DABF0](sub_1403DABF0.md)

## Notes

The name is ours (IDB: sub_1403FBB80). 4567 hits per 4 s. The name-key compare (id first, string fallback) is the same one used by GUINode_FindPartByName.

## Open questions

? What the vector at w+224 holds exactly (I: resource / texture names of the widget).
