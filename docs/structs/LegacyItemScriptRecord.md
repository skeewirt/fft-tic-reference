# LegacyItemScriptRecord

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)
- **Size:** 1 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

First byte of one record of an item page layout script; the handler of the opcode returns the start of the next record.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="opcode"></a>`0x0` | opcode | `uint8` | V | handler id 0..24 (table 0x1406932A0; slot 8 empty); 25 ends the script; the record length rule is not read here |

## Referenced by

- Described by tables: [LegacyItemListLayoutLang0](../tables/LegacyItemListLayoutLang0.md), [LegacyItemListLayoutLang1](../tables/LegacyItemListLayoutLang1.md), [LegacyItemListLayoutLang2](../tables/LegacyItemListLayoutLang2.md), [LegacyItemListLayoutLang3](../tables/LegacyItemListLayoutLang3.md), [LegacyItemUseLayoutLang0](../tables/LegacyItemUseLayoutLang0.md), [LegacyItemUseLayoutLang1](../tables/LegacyItemUseLayoutLang1.md), [LegacyItemUseLayoutLang2](../tables/LegacyItemUseLayoutLang2.md), [LegacyItemUseLayoutLang3](../tables/LegacyItemUseLayoutLang3.md)

## Open questions

None recorded.
