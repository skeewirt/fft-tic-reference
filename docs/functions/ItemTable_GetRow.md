# ItemTable_GetRow

- **Address:** `0x1400F8674`
- **Area:** [Data access](../areas/data.md)
- **Prototype:** `char *ItemTable_GetRow(unsigned int itemId)`
- **Callers:** sub_140109134, sub_14029F950, sub_1402A0A08, sub_1402C80D8, sub_14030E774 (plus inlined copies sub_1402B889C / 892C / 89F8)
- **Callees:** sub_1403D325C, sub_1403D3AE8, sub_1403D2FD8

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the Item-en row (table 45, cache qword_143CDA2E8).

## Behavior

- V: id 45 = Item (text resolver sub_1400F3BB0 maps the category string 'Item' to 0x2D).

## Referenced by

- Called by: [EquipDetail_SetHelpText](EquipDetail_SetHelpText.md), [sub_1402C80D8](sub_1402C80D8.md)
- Reads tables: [Item](../tables/Item.md)

## Open questions

None recorded.
