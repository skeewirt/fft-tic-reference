# LegacyUiScriptRecord

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)
- **Size:** 2 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Header of one record of a legacy menu layout script; the record is {opcode, length, arguments} and the next record starts length bytes later.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="opcode"></a>`0x0` | opcode | `uint8` | V | handler id: 0 window frame, 1 if, 2 if-else, 4 / 5 draw cell, 9 / 10 texture page and palette word, 12 blend word, 13 number or gauge, 14 layer word, 15 priority word, 17 tile grid, 18 animated window frame; 3, 6, 7, 8, 11 have no handler; 22 ends the script |
| <a id="length"></a>`0x1` | length | `uint8` | V | record length in bytes (this record + length is the next record); the arguments are the bytes 2 .. length - 1 |

## Referenced by

- Described by tables: [LegacyJobChoiceLayoutLang0](../tables/LegacyJobChoiceLayoutLang0.md), [LegacyJobChoiceLayoutLang1](../tables/LegacyJobChoiceLayoutLang1.md), [LegacyJobChoiceLayoutLang2](../tables/LegacyJobChoiceLayoutLang2.md), [LegacyJobChoiceLayoutLang3](../tables/LegacyJobChoiceLayoutLang3.md), [LegacyJobDetailLayoutLang0](../tables/LegacyJobDetailLayoutLang0.md), [LegacyJobDetailLayoutLang1](../tables/LegacyJobDetailLayoutLang1.md), [LegacyJobDetailLayoutLang2](../tables/LegacyJobDetailLayoutLang2.md), [LegacyJobDetailLayoutLang3](../tables/LegacyJobDetailLayoutLang3.md), [LegacyTask12LayoutLang0](../tables/LegacyTask12LayoutLang0.md), [LegacyTask12LayoutLang1](../tables/LegacyTask12LayoutLang1.md), [LegacyTask12LayoutLang2](../tables/LegacyTask12LayoutLang2.md), [LegacyTask12LayoutLang3](../tables/LegacyTask12LayoutLang3.md), [LegacyTask13LayoutMode13](../tables/LegacyTask13LayoutMode13.md), [LegacyTask13LayoutOther](../tables/LegacyTask13LayoutOther.md)

## Open questions

None recorded.
