# GuideSlot_DrawButtons

- **Address:** `0x14028BE4C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GuideSlot_DrawButtons(void *slot, ...)`
- **Callers:** GuideBar_LayoutRow, sub_1400F74F4, sub_14016A5EC, UIAddonFFTOConfig_Update and others
- **Callees:** sub_1400F69BC, UIName_Key, UIName_Assign, UIName_ReleaseKey, sub_1400F5490, sub_1403DC8D0, sub_1400F681C, sub_1400F555C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Draws the buttons of one guide-bar slot: action buttons, fixed icons or keyboard key textures.

## Behavior

- V: slot fields +104.. hold action ids (UIKeyAssign rows) drawn with sub_1400F69BC: the pad glyph and, when the field at +140.. is 1 or 2 in keyboard mode, a second key glyph.
- V: fields +120.. hold icon numbers drawn with GuideIcon_ToGlyph(icon, byte +136..), or, when the byte at +156.. is set and the input mode is keyboard, with sub_1403DC8D0, which builds the key texture path 'ui/platform/win/textureparts/key_%03d_uitx'.
- V: slot +164 is the number of buttons drawn; GuideBar_LayoutRow shows or hides the second to fourth button states by it.

## State touched

- Calls: [sub_1400F69BC](sub_1400F69BC.md), [UIName_Key](UIName_Key.md), [UIName_Assign](UIName_Assign.md), [UIName_ReleaseKey](UIName_ReleaseKey.md), [sub_1403DC8D0](sub_1403DC8D0.md)

## Notes

Name is ours.

## Open questions

None recorded.
