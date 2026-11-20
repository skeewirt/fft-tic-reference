# CountedNounTagRecord

- **Kind:** observed behaviour
- **Scope:** engine (UI text tags)
- **Area:** [Data access](../areas/data.md)
- **Affects:** [UIText_ResolveCategoryRow](../functions/UIText_ResolveCategoryRow.md), [TextTag_CountedNounPlain](../functions/TextTag_CountedNounPlain.md), [TextTag_CountedNounArticle](../functions/TextTag_CountedNounArticle.md), [TextTag_CountedNounForms](../functions/TextTag_CountedNounForms.md), [TextTag_CountedNounIndexed](../functions/TextTag_CountedNounIndexed.md), [TextTagNounRecord](../structs/TextTagNounRecord.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

How the four counted-noun tag builders use the four grammar bytes of a text tag record. The bytes are language specific data of the Ability table; in the stock data every Ability row holds the same four values (0, 1, 0, 0).

## Behavior

- V: UIText_ResolveCategoryRow fills the record for category 'Ability' (UI table 0x27): singular = name (row +8), plural = row +0x10 string, zero form = name; bytes +24..+27 = row bytes +0x16..+0x19 (columns noun_class, noun_number_form, noun_class_2, noun_prefix_flag).
- V: Plain: count 0 -> zero form, 1 -> singular, 2 or more -> plural; reads no byte. '[n]' is replaced by the count in all four builders.
- V: Article: byte +24 selects row group 3 * byte (singular) or 3 * byte + 1 (plural) of the per-language article table; byte +27 non-zero skips the article.
- V: Forms: byte +26 is the initial form index (3 for a count of 2 or more) into the per-language form table (UI table 0xE5, 14 form strings per row); byte +27 non-zero, or a string containing [t], skips the extra word; the markers [t], [p], [pa], [a] and [n] are substituted afterwards.
- V: Indexed: block = 4 * (byte +24 + 2 * byte +26) of the per-language index table; byte +27 non-zero adds form 0 of the block first; otherwise byte +25 = 0 adds form 3 (singular string), 1 adds form 1 (count 1) or 2 (larger), 2 adds form 2 (plural string).
- M: all 512 Ability rows of the stock data hold 0, 1, 0, 0 in the four columns.

## Open questions

? which language uses which of the four builders and what the Ability byte values mean per language.
