# TextTag_CountedNounArticle

- **Address:** `0x1400F3F94`
- **Area:** [Data access](../areas/data.md)
- **Prototype:** `void TextTag_CountedNounArticle(void *text, ..., int count)`
- **Callers:** sub_1400F2648
- **Callees:** UIText_ResolveCategoryRow, sub_1400F3F10, sub_1400769EC, Str_Format, sub_1400F3E2C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Counted-noun text tag builder that first adds an article or form string from a per-language table.

## Behavior

- V: resolves the tag row with UIText_ResolveCategoryRow and picks the record string by the count: 0 plain (+16), 1 singular (+0), 2 or more plural (+8); then replaces '[n]' with the count.
- V: before that it adds an article string from a per-language table (sub_1400F3F10) chosen by the tag record bytes +24 (article row index times 3) and +27 (no article).

## State touched

- Calls: [UIText_ResolveCategoryRow](UIText_ResolveCategoryRow.md), [Str_Format](Str_Format.md)

## Notes

Name is ours. The record bytes +24..+27 are filled by UIText_ResolveCategoryRow from C_Mes_Id_Sample bytes +0x10..+0x13 and the matching bytes of Ability, Item and PoachItem.

## Open questions

? which builder serves which language.
