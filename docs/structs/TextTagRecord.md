# TextTagRecord

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The record UIText_ResolveCategoryRow gives the counted-noun text tag builders: three strings and four grammar bytes.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="singular"></a>`0x0` | singular | `string` | V | Used for a count of 1: the category row's singular string, or its plain text when that is empty. |
| <a id="plural"></a>`0x8` | plural | `string` | V | Used for a count of 2 or more. |
| <a id="plain"></a>`0x10` | plain | `string` | V | Used for a count of 0 (the plain form). |
| <a id="grammar_0"></a>`0x18` | grammar_0 | `uint8` | V | Byte +24 (C_Mes_Id_Sample +0x10, Ability +22, Item +0x18 noun_class, PoachItem +0x1C): TextTag_CountedNounArticle picks the UIAttributive (table 0xE5) article at 3 x this byte (one more for a count of 2 or more); TextTag_CountedNounIndexed uses 4 x (this byte + 2 x byte +26) as the form index. |
| <a id="grammar_1"></a>`0x19` | grammar_1 | `uint8` | V | Byte +25 (C_Mes_Id_Sample +0x11, Item +0x19 noun_number_form, PoachItem +0x1D): read only by TextTag_CountedNounIndexed (0 / 1 / 2 pick the plural form rule). |
| <a id="grammar_2"></a>`0x1A` | grammar_2 | `uint8` | V | Byte +26 (C_Mes_Id_Sample +0x12, Item +0x1A noun_class_2, PoachItem +0x1E): a gender-like class read by TextTag_CountedNounForms and TextTag_CountedNounIndexed. |
| <a id="grammar_3"></a>`0x1B` | grammar_3 | `uint8` | V | Byte +27 (C_Mes_Id_Sample +0x13, Item +0x1B noun_prefix_flag, PoachItem +0x1F): when non-zero the noun is written bare, with no article (TextTag_CountedNounArticle). |

## Behavior

- V: the four builders pick the string by the count and replace '[n]' with the count.

## Referenced by

- Observed behaviours: [ItemRowGrammarBytesAndGates](../behaviors/ItemRowGrammarBytesAndGates.md)

## Notes

Name is ours. The meaning of each grammar byte per language is open.

## Open questions

? which builder serves which language, and so the grammatical meaning of each byte.
