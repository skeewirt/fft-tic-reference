# UIText_ResolveCategoryRow

- **Address:** `0x1400F3BB0`
- **Area:** [Data access](../areas/data.md)
- **Prototype:** `char __fastcall UIText_ResolveCategoryRow(__int64 out, const char *category, unsigned int key)`
- **Callers:** sub_1400F2648, sub_1400F3F94, sub_1400F4200, sub_1400F4558, sub_1400F4718 (V: 5 code xrefs)
- **Callees:** sub_140079090 (string compare), UITable_GetRowByKey

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Resolves the category name and key of a <category=key> text tag to a table row and fills a 28-byte result record with three string pointers and four flag bytes.

## Behavior

- V: category is compared with sub_140079090(a2, name, len incl NUL) (string compare, 0 = equal) in this order: 'Item' (len 5) -> UITable_GetRowByKey(0x2D, key); 'PoachItem' (10) -> table 0xEC; 'C_MES_ID_SAMPLE' (16) -> table 0xAC; 'Ability' (8) -> table 0x27; 'CharaSlot' (10) -> no table, array qword_143CDA350; 'JobCommand' (11) -> table 0x29. Anything else, or a missing row, returns 0 (the local v6 = 0).
- V: result record out: +0, +8, +16 are three string pointers, +24, +25, +26, +27 are four bytes copied from the row (see per-category lines). Returns 1 on success.
- V: Item (0x2D): base = row+4; out[+24..+27] = row bytes 24..27; out+0 = base + base[1] (dword), out+8 = base + base[2], out+16 = base + base[0] unless the byte there is 0, in which case it falls back to out+0's offset (base[1]). PoachItem (0xEC) is the same with base = row+8 and the four bytes from row bytes 28..31.
- V: C_MES_ID_SAMPLE (0xAC): p = row+4; out+0 = row+4+row[+8] unless that string is empty (first byte 0), then out+0 = p + *(int*)p; out+8 = row+4+row[+12]; out+16 = p + *(int*)p; bytes +24..+27 = row bytes 16..19.
- V: Ability (0x27): out+0 = out+16 = row + row[2] + 8 (dword index 2); out+8 = row + row[4] + 8; bytes out+24 = row byte 22 (Ability column noun_class), +25 = 23 (noun_number_form), +26 = 24 (noun_class_2), +27 = 25 (noun_prefix_flag); the pointer at out+8 is the Ability plural column (+0x10), out+0 and out+16 the name (+8).
- V: CharaSlot: row = qword_143CDA350 + 4*(9*key + 12) (36-byte stride, key*9 dwords); all three pointers = that address; out+24 = row byte 32, out+26 = row byte 33, out+25 = 1, out+27 = 0. JobCommand (0x29): pointers = row + row[2] + 8; dword at out+24 is set to 256 (so +25 = 1, others 0).
- V (Ability): the three string pointers are (singular name, plural name, name used for a count of 0); the four bytes are the noun grammar bytes of the counted-noun builders. I (other categories): the same roles.

## State touched

- Calls: [UITable_GetRowByKey](UITable_GetRowByKey.md)

## Referenced by

- Called by: [TextTag_CountedNounArticle](TextTag_CountedNounArticle.md), [TextTag_CountedNounForms](TextTag_CountedNounForms.md), [TextTag_CountedNounIndexed](TextTag_CountedNounIndexed.md), [TextTag_CountedNounPlain](TextTag_CountedNounPlain.md), [TextTag_ExpandKeyIcon](TextTag_ExpandKeyIcon.md)
- Observed behaviours: [CountedNounTagRecord](../behaviors/CountedNounTagRecord.md), [ItemRowGrammarBytesAndGates](../behaviors/ItemRowGrammarBytesAndGates.md)
- Reads tables: [Ability](../tables/Ability.md), [C_Mes_Id_Sample](../tables/C_Mes_Id_Sample.md), [Item](../tables/Item.md), [JobCommand](../tables/JobCommand.md), [PoachItem](../tables/PoachItem.md)

## Notes

The IDA comment already names the categories; this sheet adds the row layouts. Tables 0x2D / 0xEC / 0xAC / 0x27 / 0x29 are keyed UI tables (V from the calls).

## Open questions

? what the four bytes mean for each category other than Ability (for Ability they are the language specific noun grammar bytes read by the four counted-noun builders, see behavior CountedNounTagRecord). ? layout of the CharaSlot array (36-byte stride, base qword_143CDA350).
