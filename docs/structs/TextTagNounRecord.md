# TextTagNounRecord

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 28 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The 28-byte result record of UIText_ResolveCategoryRow for a <category=key> text tag: three string pointers and four bytes. The counted-noun tag builders read it.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="singular"></a>`0x0` | singular | `pointer` | V | String used for a count of 1. For category 'Ability': the name. |
| <a id="plural"></a>`0x8` | plural | `pointer` | V | String used for a count of 2 or more. For category 'Ability': the Ability row's plural string (+0x10). |
| <a id="zero_form"></a>`0x10` | zero_form | `pointer` | V | String used for a count of 0. For category 'Ability': the name again. |
| <a id="noun_class"></a>`0x18` | noun_class | `uint8` | V | For 'Ability': copied from the Ability row byte +0x16. Article builder: selects the article row group (3 per value); indexed builder: part of the block number. |
| <a id="noun_number_form"></a>`0x19` | noun_number_form | `uint8` | V | For 'Ability': Ability row byte +0x17. Indexed builder: 0, 1 or 2 chooses the form variant. |
| <a id="noun_class_2"></a>`0x1A` | noun_class_2 | `uint8` | V | For 'Ability': Ability row byte +0x18. Forms builder: the initial form index; indexed builder: part of the block number. |
| <a id="noun_prefix_flag"></a>`0x1B` | noun_prefix_flag | `uint8` | V | For 'Ability': Ability row byte +0x19. A non-zero value skips the article or extra word in the article and forms builders and adds form 0 first in the indexed builder. |

## Behavior

- V: the four bytes are copied unchanged from the row; what they mean is decided per language by the builder (see behavior CountedNounTagRecord).

## Referenced by

- Observed behaviours: [CountedNounTagRecord](../behaviors/CountedNounTagRecord.md)

## Notes

Detail and evidence: sheets UIText_ResolveCategoryRow, TextTag_CountedNounPlain, TextTag_CountedNounArticle, TextTag_CountedNounForms, TextTag_CountedNounIndexed.

## Open questions

? the roles of the four bytes for the other categories (Item, PoachItem, C_MES_ID_SAMPLE).
