# GuideSlot

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One slot of a guide bar or window entry (GuideSlot_DrawButtons): up to four buttons given as actions or icon numbers.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="actions"></a>`0x68` | actions | `int32[]` | V | Action ids (UIKeyAssign rows) of the buttons (+104..). |
| <a id="icons"></a>`0x78` | icons | `int32[]` | V | Fixed icon numbers of the buttons (+120..). |
| <a id="icon_variants"></a>`0x88` | icon_variants | `uint8[]` | V | Variant byte per icon (+136..), the third argument of GuideIcon_ToGlyph. |
| <a id="key_glyph_mode"></a>`0x8C` | key_glyph_mode | `int32[]` | V | When 1 or 2 in keyboard mode a second key glyph is drawn (+140..). |
| <a id="keyboard_flag"></a>`0x9C` | keyboard_flag | `uint8[]` | V | When set and the input mode is keyboard, the icon is a key texture (+156..). |
| <a id="button_count"></a>`0xA4` | button_count | `int32` | V | Number of buttons drawn (+164). |

## Behavior

- V: GuideBar_LayoutRow shows or hides the second to fourth button states by button_count.

## Notes

Name is ours.

## Open questions

? the array strides.
