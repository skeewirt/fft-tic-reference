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
| <a id="grammar_0"></a>`0x18` | grammar_0 | `uint8` | V | Byte +24 (C_Mes_Id_Sample +0x10, Ability +22, Item and PoachItem bytes): article row index times 3 in TextTag_CountedNounArticle. |
| <a id="grammar_1"></a>`0x19` | grammar_1 | `uint8` | V | Byte +25 (C_Mes_Id_Sample +0x11): read by TextTag_CountedNounIndexed. |
| <a id="grammar_2"></a>`0x1A` | grammar_2 | `uint8` | V | Byte +26 (C_Mes_Id_Sample +0x12): read by TextTag_CountedNounForms and TextTag_CountedNounIndexed. |
| <a id="grammar_3"></a>`0x1B` | grammar_3 | `uint8` | V | Byte +27 (C_Mes_Id_Sample +0x13): the no-article flag. |

## Behavior

- V: the four builders pick the string by the count and replace '[n]' with the count.

## Notes

Name is ours. The meaning of each grammar byte per language is open.

## Open questions

? which builder serves which language, and so the grammatical meaning of each byte.
