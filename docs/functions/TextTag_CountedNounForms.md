# TextTag_CountedNounForms

- **Address:** `0x1400F4200`
- **Area:** [Data access](../areas/data.md)
- **Prototype:** `void TextTag_CountedNounForms(void *text, ..., int count)`
- **Callers:** sub_1400F2648
- **Callees:** UIText_ResolveCategoryRow, strstr, sub_1400F40D8, sub_1400769EC, sub_1400F3E2C, Str_Format

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Counted-noun text tag builder that adds a form string chosen by two record bytes.

## Behavior

- V: same count rule as TextTag_CountedNounArticle (0 plain, 1 singular, 2 or more plural, '[n]' replaced by the count).
- V: the added form string comes from sub_1400F40D8 (a UI table row by key), chosen by tag record bytes +26 and +27.

## State touched

- Calls: [UIText_ResolveCategoryRow](UIText_ResolveCategoryRow.md), [Str_Format](Str_Format.md)

## Notes

Name is ours.

## Open questions

? which language it serves.
