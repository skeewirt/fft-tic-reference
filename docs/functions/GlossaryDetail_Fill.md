# GlossaryDetail_Fill

- **Address:** `0x140172B70`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GlossaryDetail_Fill(void *panel, const void *entry)`
- **Callers:** not recorded
- **Callees:** FaceWidget_SetFace, SpriteRecord_Fill, GuiImage_SetIconById, GUINode_PlayState

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills the glossary detail page (part read).

## Behavior

- V: node 'Clear' (+3552) plays 'Enable' / 'Disable' by clear_mark (+0x4F); face 'Image00' (+3528) from LoreDictionary_GetFace ('Unknown' when 0); the unit figure (+3520, part 'Unit' +4304) by SpriteRecord_Fill(sprite_shape +0x20, palette +0x50); icon_2 (+0x28); full_name (+0x34); family_name_first (+0x40, reached as dword index 16 of the row).
- V: the figure call is SpriteRecord_Fill(rec, 0, shape, palette, 0, .., 4, flag).
- V: the face, affiliation, alias and icon values come through the getter functions of the entry's current row (LoreDictionary_GetFace, _GetAffiliationName, _GetAliasName, _GetIcon).

## State touched

- Calls: [FaceWidget_SetFace](FaceWidget_SetFace.md), [SpriteRecord_Fill](SpriteRecord_Fill.md), [GuiImage_SetIconById](GuiImage_SetIconById.md), [GUINode_PlayState](GUINode_PlayState.md)

## Referenced by

- Observed behaviours: [ClearMarkAppearsOnFourScreens](../behaviors/ClearMarkAppearsOnFourScreens.md)

## Open questions

None recorded.
