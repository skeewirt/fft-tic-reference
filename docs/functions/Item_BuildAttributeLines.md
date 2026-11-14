# Item_BuildAttributeLines

- **Address:** `0x14029F710`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void Item_BuildAttributeLines(void *lines, uint16_t item_id)`
- **Callers:** sub_1402A0E58
- **Callees:** Item_GetRecord, sub_14029F4B4

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Appends the equipment attribute lines of an item to the detail panel: the five stat bonuses, the move and jump bonuses and the element list.

## Behavior

- V: the item record is fetched by id and its attribute index byte +7 is read.
- V: an index of 0x55 or above skips the attribute block and leaves the lines unchanged.
- V: each valid index selects a 0x1A-byte row in the table at 0x14080FEA0.
- V: the row bytes +3, +4, +2, +0 and +1 are emitted with the text ids 0x39D, 0x39E, 0x39F, 0x3A0 and 0x3A1 when they are non-zero.
- V: sub_14029F4B4 formats one line per call into the caller buffer; the function does not write text itself.
- V: the five calls are unconditional in order except for the zero test, so the panel always gets the same line order.
- I: the five values are the HP, MP, speed, attack and magic bonuses in the order the item attribute record stores them.
- ?: what the row bytes past +4 hold; the element and status fields are not emitted here.

## State touched

- Calls: [Item_GetRecord](Item_GetRecord.md)
- Reads: [g_ItemAttributeTable](../globals/g_ItemAttributeTable.md)

## Notes

Whole function read (184 bytes). The attribute table layout is the one the W1a item study lists.

## Open questions

None recorded.
