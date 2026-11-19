# FaceWidget_SetFace

- **Address:** `0x14028FF34`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `void FaceWidget_SetFace(void *widget, int face, int colour)`
- **Callers:** sub_1402C1EA8 (party list), sub_1401173D4, sub_140172B70, sub_140177004, sub_140291490
- **Callees:** FaceNumber_Remap, FaceTexture_FormatName, GUIWidget_EnsureSlotGroup, UIName_Key, UIName_Assign, UIName_ReleaseKey, GUINode_StopState

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Points a face widget at the texture of a face number and colour, and restarts its blink.

## Behavior

- V: does nothing unless sub_1400F5828(0, 0, widget + 32, 2) succeeds.
- V: the face number goes through FaceNumber_Remap, then FaceTexture_FormatName(buffer, face, colour) makes the name.
- V: when the name differs from the one the widget's node holds (+232 of the node at widget + 32): GUIWidget_EnsureSlotGroup(widget + 16, name, 0) when that pointer is set, then the name key is assigned to both nodes (widget + 32 and widget + 40), and when byte +48 is set the state 'Blink' of the node at +24 is stopped.

## State touched

- Calls: [FaceNumber_Remap](FaceNumber_Remap.md), [FaceTexture_FormatName](FaceTexture_FormatName.md), [GUIWidget_EnsureSlotGroup](GUIWidget_EnsureSlotGroup.md), [UIName_Key](UIName_Key.md), [UIName_Assign](UIName_Assign.md), [UIName_ReleaseKey](UIName_ReleaseKey.md), [GUINode_StopState](GUINode_StopState.md)

## Referenced by

- Appears in flows: [PartyMenuFaceChain](../flows/PartyMenuFaceChain.md)
- Called by: [GlossaryCharacterPage_Fill](GlossaryCharacterPage_Fill.md), [GlossaryDetail_Fill](GlossaryDetail_Fill.md)

## Notes

No bound on the face number here: any int reaches the texture name. The name is ours (IDB: sub_14028FF34).

## Open questions

? whether GUIWidget_EnsureSlotGroup can serve a name the UI packs do not hold.
