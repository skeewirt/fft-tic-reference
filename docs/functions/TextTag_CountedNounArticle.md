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
- V: before that it adds an article string from a per-language table (sub_1400F3F10(language, row)) chosen by the tag record byte +24: row 3 * byte for a count of 1 (singular article), row 3 * byte + 1 for a count of 2 or more; a non-zero byte +27 skips the article. A count of 0 uses no article.

## State touched

- Calls: [UIText_ResolveCategoryRow](UIText_ResolveCategoryRow.md), [Str_Format](Str_Format.md)

## Referenced by

- Observed behaviours: [CountedNounTagRecord](../behaviors/CountedNounTagRecord.md), [ItemRowGrammarBytesAndGates](../behaviors/ItemRowGrammarBytesAndGates.md)

## Notes

Name is ours. The record bytes +24..+27 are filled by UIText_ResolveCategoryRow from C_Mes_Id_Sample bytes +0x10..+0x13 and the matching bytes of Ability (columns noun_class, noun_number_form, noun_class_2, noun_prefix_flag), Item and PoachItem. In the stock data every Ability row holds 0, 1, 0, 0 in those four columns (M).

## Open questions

? which builder serves which language (the builder is chosen by the caller TextTag_ExpandKeyIcon from the language and the tag).
