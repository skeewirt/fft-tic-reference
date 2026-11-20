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
- V: record byte +26 is the initial form index (replaced by 3 for a count of 2 or more); a non-zero byte +27, or a string containing the marker [t], skips the extra word that is otherwise put before the string (not for a count of 0); the form strings come from sub_1400F40D8(language, index) (UI table 0xE5, 14 per-language form strings per row).
- V: after the string is written the markers [t], [p], [pa], [a] and [n] are replaced (the count for [n]; [t], [pa] and [a] by form strings of the same table, [p] by an empty string when the string has no [p]).

## State touched

- Calls: [UIText_ResolveCategoryRow](UIText_ResolveCategoryRow.md), [Str_Format](Str_Format.md)

## Referenced by

- Observed behaviours: [CountedNounTagRecord](../behaviors/CountedNounTagRecord.md)

## Notes

Name is ours. The UI table id 0xE5 is read inside the callee sub_1400F40D8, not in this body.

## Open questions

? which language it serves.
