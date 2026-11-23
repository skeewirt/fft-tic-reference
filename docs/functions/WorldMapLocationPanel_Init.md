# WorldMapLocationPanel_Init

- **Address:** `0x14015F730`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void WorldMapLocationPanel_Init(void *panel)`
- **Callers:** not recorded
- **Callees:** UIListGadget_Bind, GUINode_FindDescendant, GUINode_FindPartByName, UITable_GetRowByKey, Icon_FormatPath, Str_Format, sub_140158D98

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Binds the location panel's nodes (worldmap_base_info.uib) once: the list, the tab buttons, the field and town info, and one node per item category.

## Behavior

- V: finds 'BaseInfo' (kept at +344), its 'List' (+352, bound to the list gadget at +720 with 'ListButton' rows), the 'TabButton' guides and texts (+360..+376) and 'FieldInfo' (+712) with its picture and texts.
- V: in the town info node: texts 'Text01'..'Text03' (ids 1575, 1573, 1574), 'Text05' and 'Text00' (+1800, +1808).
- V: then for categories 0..34 (the bound 35 is compared at 0x14016023E): UIItemCategory row c (table 38), node 'IconEquipCategory%02d' of the row's +20 (unknown14) under the town info node into the array at +64 + 8c (35 qwords; the field after it is the BaseInfo pointer at +344), and the node's part 'Icon' gets the picture of Icon row 14 (`equip_cat/textureparts/ec_%03d_uitx`) of c (sub_140158D98). A row whose +20 names no node leaves the slot null.
- V: the loop counter is edi, the slot pointer rsi (the panel rbx + 0x40), stepped at 0x140160238.

## State touched

- Calls: [UIListGadget_Bind](UIListGadget_Bind.md), [GUINode_FindDescendant](GUINode_FindDescendant.md), [GUINode_FindPartByName](GUINode_FindPartByName.md), [UITable_GetRowByKey](UITable_GetRowByKey.md), [Icon_FormatPath](Icon_FormatPath.md), [Str_Format](Str_Format.md)

## Notes

The array it fills is what WorldMapLocationPanel_Fill plays 'On' / 'Off' on.

## Open questions

None recorded.
