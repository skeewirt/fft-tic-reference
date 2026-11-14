# GUIFontSlots_GetTextureRect

- **Address:** `0x1403E9590`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUIFontSlots_GetTextureRect(Rect *out, unsigned int slotId)`
- **Callers:** GUITextNode_Draw, ComponentEffects_Collect
- **Callees:** GUIFontSlots_GetSlot, UIPartRef_GetTextureSize

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Writes the full-texture rectangle {0, 0, width, height} of a slot's texture into out; leaves out unchanged when the slot does not exist.

## Behavior

- V: slot = GUIFontSlots_GetSlot(g_GUIFontSlots, slotId); non-null: UIPartRef_GetTextureSize(slot, &size) then out = {dword 0 = 0, dword 4 = 0, qword 8 = size (width, height)}.
- V: returns the slot pointer / out. Hex-Rays loses the out pointer (it shows as a register); the disassembly stores through the hidden return-value pointer.

## State touched

- Calls: [GUIFontSlots_GetSlot](GUIFontSlots_GetSlot.md), [UIPartRef_GetTextureSize](UIPartRef_GetTextureSize.md)
- Reads: [g_GUIFontSlots](../globals/g_GUIFontSlots.md)

## Referenced by

- Called by: [ComponentEffects_Collect](ComponentEffects_Collect.md)

## Notes

The name is ours (IDB: sub_1403E9590). The prototype is partly I because of the lost out pointer.

## Open questions

? whether out is the first argument (rcx) as assumed; verify in the disassembly before relying on the name.
