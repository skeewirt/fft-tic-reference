# TextTag_ExpandKeyIcon

- **Address:** `0x1400F2648`
- **Area:** [Data access](../areas/data.md)
- **Prototype:** `void TextTag_ExpandKeyIcon(void *text, const char *tag, const char *argument, ...)`
- **Callers:** UI_FrameUpdate
- **Callees:** UITable_GetRow, UITable_GetRowByKey, sub_1400F39EC, sub_1400F3998, sub_1400F3F94, sub_1400F4200, sub_1400F4558, sub_1400F4718, UIText_ResolveCategoryRow, JobTable_GetNameText

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Expands the in-text tags of the UI text engine; the 'keyicon' tag inserts the button glyph of a named input action. The same function dispatches the counted-noun tags.

## Behavior

- V: for the tag 'keyicon' it loops UIKeyAssign rows 1..255 and compares the tag argument with the row's name string (+0x18); on a match it writes the glyph of that action with InputGlyph_AppendPadButton (action 57 asks for the alternate glyph).
- V: other tags call UIText_ResolveCategoryRow and the four counted-noun builders (sub_1400F3F94, sub_1400F4200, sub_1400F4558, sub_1400F4718), job-name text (JobTable_GetNameText) and others not read here.

## State touched

- Calls: [UITable_GetRow](UITable_GetRow.md), [UITable_GetRowByKey](UITable_GetRowByKey.md), [UIText_ResolveCategoryRow](UIText_ResolveCategoryRow.md), [JobTable_GetNameText](JobTable_GetNameText.md)

## Referenced by

- Observed behaviours: [KeyIconTag](../behaviors/KeyIconTag.md)

## Notes

Name is ours; only the keyicon branch was read closely.

## Open questions

? the other tags this function handles.
