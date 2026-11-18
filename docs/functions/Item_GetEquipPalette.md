# Item_GetEquipPalette

- **Address:** `0x1402B8E60`
- **Area:** [Items and shops](../areas/items.md)
- **Prototype:** `const unsigned short *Item_GetEquipPalette(unsigned short itemId)`
- **Callers:** ItemSprite_LoadPalettes, sub_14026BC60
- **Callees:** Item_FindCategoryIndex

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the palette-selector row of an item, chosen by the item's equipment category, or null when the item has no palette.

## Behavior

- V: gets a category index for the id from Item_FindCategoryIndex.
- V: a category index of -1 returns null.
- V: a per-category selector dword (14 entries at 0x14067FB78) picks the table: values 0 and 1 use the table at
  0x140785CF0, values 5 and 6 use the table at 0x140672B54, any other value returns null.
- V: the first table is indexed by the raw id and covers ids 0x00..0x8F, which is where 0x8F comes from in the earlier
  reading; the bound is not an immediate in this body.
- V: the row is the table base plus twice the raw item id, so a row is two bytes.
- V: for the second table the ids 0x100 and 0x101 land at 0x140672D54, which is 0x200 bytes past the base (twice 0x100).
- V: reuses cx after Item_FindCategoryIndex, because that callee leaves rcx untouched.
- V: only two direct call sites exist: ItemSprite_LoadPalettes and a second sprite routine.
- V: byte 0 of the row holds two four-bit palette indices; ItemSprite_LoadPalettes loads the high nibble into palette slot 5
  and the low nibble into slot 6. Byte 1 has no reader found.
- V: Item_FindCategoryIndex accepts ids 1 to 253 and 256 to 260; 0, 254, 255 and 261 and above return -1, so those ids
  have no palette selector.
- I: the palette colours themselves live in a separate 512-byte table of 16 palettes at 0x140D35750 (that address is not
  referenced by this body; the sprite loader reads it), since the row only selects.

## State touched

- Calls: [Item_FindCategoryIndex](Item_FindCategoryIndex.md)

## Referenced by

- Called by: [ItemSprite_LoadPalettes](ItemSprite_LoadPalettes.md)
- Reads tables: [ItemCategoryTypes](../tables/ItemCategoryTypes.md), [ItemEquipPalettes](../tables/ItemEquipPalettes.md), [ItemEquipPalettesHigh](../tables/ItemEquipPalettesHigh.md)

## Notes

- V: whole body read.

## Open questions

- ?: the extent and index base of the second table (0x140672B54).
- ?: the reader of byte 1 (sub_14026BC60 not studied).
