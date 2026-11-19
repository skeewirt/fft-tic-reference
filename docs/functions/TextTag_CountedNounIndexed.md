# TextTag_CountedNounIndexed

- **Address:** `0x1400F4558`
- **Area:** [Data access](../areas/data.md)
- **Prototype:** `void TextTag_CountedNounIndexed(void *text, ..., int count)`
- **Callers:** sub_1400F2648
- **Callees:** UIText_ResolveCategoryRow, sub_1400F4430, sub_1400769EC, sub_1400F3E2C, Str_Format

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Counted-noun text tag builder that indexes a per-language form table with three record bytes.

## Behavior

- V: same count rule as TextTag_CountedNounArticle.
- V: the form string comes from sub_1400F4430 at index 4 * (record +24 + 2 * record +26) plus a variant, with record +25 and +27 also read.

## State touched

- Calls: [UIText_ResolveCategoryRow](UIText_ResolveCategoryRow.md), [Str_Format](Str_Format.md)

## Notes

Name is ours.

## Open questions

? which language it serves.
