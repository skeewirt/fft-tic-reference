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
- V: block = 4 * (record +24 + 2 * record +26) of sub_1400F4430(language, index): a non-zero record byte +27 adds form 0 of the block before the string (singular or plural by the count); otherwise record byte +25 chooses the form: 0 adds form 3 and uses the singular string, 1 adds form 1 for a count of 1 and form 2 for a larger count, 2 adds form 2 and uses the plural string. A count of 0 adds nothing.

## State touched

- Calls: [UIText_ResolveCategoryRow](UIText_ResolveCategoryRow.md), [Str_Format](Str_Format.md)

## Referenced by

- Observed behaviours: [CountedNounTagRecord](../behaviors/CountedNounTagRecord.md)

## Notes

Name is ours.

## Open questions

? which language it serves.
