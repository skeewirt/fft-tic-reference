# UiSpriteCell

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)
- **Size:** 12 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the MessageWindowTagCellsLanguage2 table and the tables that share its shape.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="tex_u"></a>`0x0` | tex_u | `int16` | V | texture u inside the page (negative = keep the primitive's texture coordinates) |
| <a id="tex_v"></a>`0x2` | tex_v | `int16` | V | texture v inside the page |
| <a id="width"></a>`0x4` | width | `int16` | V | cell width in pixels |
| <a id="height"></a>`0x6` | height | `int16` | V | cell height in pixels |
| <a id="x"></a>`0x8` | x | `int16` | V | screen x offset added to the panel origin |
| <a id="y"></a>`0xA` | y | `int16` | V | screen y offset added to the panel origin |

## Referenced by

- Described by tables: [BannerWordCells](../tables/BannerWordCells.md), [EquipPanelCellsLanguage0A](../tables/EquipPanelCellsLanguage0A.md), [EquipPanelCellsLanguage0B](../tables/EquipPanelCellsLanguage0B.md), [EquipPanelCellsLanguage0V0](../tables/EquipPanelCellsLanguage0V0.md), [EquipPanelCellsLanguage0V1](../tables/EquipPanelCellsLanguage0V1.md), [EquipPanelCellsLanguage0V2](../tables/EquipPanelCellsLanguage0V2.md), [EquipPanelCellsLanguage0V3](../tables/EquipPanelCellsLanguage0V3.md), [EquipPanelCellsLanguage2A](../tables/EquipPanelCellsLanguage2A.md), [EquipPanelCellsLanguage2B](../tables/EquipPanelCellsLanguage2B.md), [EquipPanelCellsLanguage2V0](../tables/EquipPanelCellsLanguage2V0.md), [EquipPanelCellsLanguage2V1](../tables/EquipPanelCellsLanguage2V1.md), [EquipPanelCellsLanguage2V2](../tables/EquipPanelCellsLanguage2V2.md), [EquipPanelCellsLanguage2V3](../tables/EquipPanelCellsLanguage2V3.md), [EquipPanelCellsLanguage3A](../tables/EquipPanelCellsLanguage3A.md), [EquipPanelCellsLanguage3B](../tables/EquipPanelCellsLanguage3B.md), [EquipPanelCellsLanguage3V0](../tables/EquipPanelCellsLanguage3V0.md), [EquipPanelCellsLanguage3V1](../tables/EquipPanelCellsLanguage3V1.md), [EquipPanelCellsLanguage3V2](../tables/EquipPanelCellsLanguage3V2.md), [EquipPanelCellsLanguage3V3](../tables/EquipPanelCellsLanguage3V3.md), [GridArrowCells](../tables/GridArrowCells.md), [LegacyTask10CellsSlot0](../tables/LegacyTask10CellsSlot0.md), [LegacyTask10CellsSlot1](../tables/LegacyTask10CellsSlot1.md), [LegacyTask10CellsSlot10](../tables/LegacyTask10CellsSlot10.md), [LegacyTask10CellsSlot11](../tables/LegacyTask10CellsSlot11.md), [LegacyTask10CellsSlot12](../tables/LegacyTask10CellsSlot12.md), [LegacyTask10CellsSlot13](../tables/LegacyTask10CellsSlot13.md), [LegacyTask10CellsSlot14](../tables/LegacyTask10CellsSlot14.md), [LegacyTask10CellsSlot15](../tables/LegacyTask10CellsSlot15.md), [LegacyTask10CellsSlot2](../tables/LegacyTask10CellsSlot2.md), [LegacyTask10CellsSlot3](../tables/LegacyTask10CellsSlot3.md), [LegacyTask10CellsSlot4](../tables/LegacyTask10CellsSlot4.md), [LegacyTask10CellsSlot5](../tables/LegacyTask10CellsSlot5.md), [LegacyTask10CellsSlot6](../tables/LegacyTask10CellsSlot6.md), [LegacyTask10CellsSlot7](../tables/LegacyTask10CellsSlot7.md), [LegacyTask10CellsSlot8](../tables/LegacyTask10CellsSlot8.md), [LegacyTask10CellsSlot9](../tables/LegacyTask10CellsSlot9.md), [MessageWindowTagCellsDefault](../tables/MessageWindowTagCellsDefault.md), [MessageWindowTagCellsLanguage0](../tables/MessageWindowTagCellsLanguage0.md), [MessageWindowTagCellsLanguage2](../tables/MessageWindowTagCellsLanguage2.md), [MessageWindowTagCellsLanguage3](../tables/MessageWindowTagCellsLanguage3.md), [StatsPanelCellsDefault](../tables/StatsPanelCellsDefault.md), [StatsPanelCellsLanguage0](../tables/StatsPanelCellsLanguage0.md), [StatsPanelCellsLanguage2](../tables/StatsPanelCellsLanguage2.md), [StatsPanelCellsLanguage3](../tables/StatsPanelCellsLanguage3.md), [UnitPanelCellsLanguage0](../tables/UnitPanelCellsLanguage0.md), [UnitPanelCellsLanguage1](../tables/UnitPanelCellsLanguage1.md), [UnitPanelCellsLanguage2](../tables/UnitPanelCellsLanguage2.md), [UnitPanelCellsLanguage3](../tables/UnitPanelCellsLanguage3.md)

## Open questions

None recorded.
