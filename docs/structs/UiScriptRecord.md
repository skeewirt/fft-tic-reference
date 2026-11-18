# UiScriptRecord

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One record of a UI script: an opcode byte, a length byte and the arguments.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="op"></a>`0x0` | op | `uint8` | V | opcode 0..28 (index into the 29-entry handler table); 0x21 ends the script |
| <a id="length"></a>`0x1` | length | `uint8` | V | total record length in bytes, this record included (opcode 22 has no length byte: it is one byte long) |
| <a id="args"></a>`0x2` | args | `bytes[length-2]` | ? | operands; their meaning depends on the opcode |

## Referenced by

- Described by tables: [ItemListScriptLanguage0](../tables/ItemListScriptLanguage0.md), [ItemListScriptLanguage1](../tables/ItemListScriptLanguage1.md), [ItemListScriptLanguage2](../tables/ItemListScriptLanguage2.md), [ItemListScriptLanguage3](../tables/ItemListScriptLanguage3.md), [JobLearnListScriptLang1](../tables/JobLearnListScriptLang1.md), [JobLearnListScriptLang2](../tables/JobLearnListScriptLang2.md), [JobLearnListScriptLang3](../tables/JobLearnListScriptLang3.md), [JobUnitRowsScriptLang0](../tables/JobUnitRowsScriptLang0.md), [JobUnitRowsScriptLang1](../tables/JobUnitRowsScriptLang1.md), [JobUnitRowsScriptLang2](../tables/JobUnitRowsScriptLang2.md), [JobUnitRowsScriptLang3](../tables/JobUnitRowsScriptLang3.md), [UnitPanelScriptBlock0](../tables/UnitPanelScriptBlock0.md), [UnitPanelScriptBlock1](../tables/UnitPanelScriptBlock1.md), [UnitPanelScriptBlock2](../tables/UnitPanelScriptBlock2.md), [UnitPanelScriptBlock3](../tables/UnitPanelScriptBlock3.md)

## Open questions

None recorded.
