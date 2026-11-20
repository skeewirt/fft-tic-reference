# TextTag_CountedNounPlain

- **Address:** `0x1400F4718`
- **Area:** [Data access](../areas/data.md)
- **Prototype:** `void TextTag_CountedNounPlain(void *text, ..., int count)`
- **Callers:** sub_1400F2648
- **Callees:** UIText_ResolveCategoryRow, sub_1400769EC, sub_1400F3E2C, Str_Format

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Counted-noun text tag builder with no article or form string.

## Behavior

- V: resolves the tag row and picks the string by the count (count 0 = record pointer +16, 1 = +0, 2 or more = +8), then replaces '[n]' with the count.
- V: reads none of the four record bytes.

## State touched

- Calls: [UIText_ResolveCategoryRow](UIText_ResolveCategoryRow.md), [Str_Format](Str_Format.md)

## Referenced by

- Observed behaviours: [CountedNounTagRecord](../behaviors/CountedNounTagRecord.md)

## Notes

Name is ours.

## Open questions

None recorded.
