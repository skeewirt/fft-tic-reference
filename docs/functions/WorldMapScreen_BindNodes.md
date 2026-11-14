# WorldMapScreen_BindNodes

- **Address:** `0x140159304`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int WorldMapScreen_BindNodes(WorldMapAddon *a)`
- **Callers:** sub_14015E880, sub_14015EA90
- **Callees:** GUINode_FindDescendant, GUINode_FindDescendant2, GUINode_FindPartByName, GUINode_FindGadgetPart, UITable_GetRowByKey, UIName_Key, Str_Format

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Binds the world-map screen's nodes: the widget's root, MapAll with its Route and Bases groups, the 48 base/point nodes, and each base's TextBoardMapName title.

## Behavior

- V: the root comes from sub_1403F9DA0(a+24); 'MapAll' is found under it and its part (size x 0.5 and x 0.25 are stored at +2440..+2452); 'Route' and 'Bases' are descendants of MapAll.
- V: for i in 0..47 the UITable 0x34 row i names the base ('Base%s' when its byte +48 is set, else 'Point%s'); the node is bound at a+520+24*i, tagged (+544 = 31, +548 = i) and, when it is a base, set up with sub_140158E30; the 'Title' part of its 'TextBoardMapName' gadget gets the row's name text.

## State touched

- Calls: [GUINode_FindDescendant](GUINode_FindDescendant.md), [GUINode_FindDescendant2](GUINode_FindDescendant2.md), [GUINode_FindPartByName](GUINode_FindPartByName.md), [GUINode_FindGadgetPart](GUINode_FindGadgetPart.md), [UITable_GetRowByKey](UITable_GetRowByKey.md), [UIName_Key](UIName_Key.md), [Str_Format](Str_Format.md)
- Reads: [GUINode.kind](../structs/GUINode.md#kind), [g_UINameTable](../globals/g_UINameTable.md)

## Notes

The name is ours; only the first half of the function (to the 'Days' group) was read. It uses the same TextBoardxx / 'Title' gadget lookup as the Job Tree's MainTab_BindNodes.

## Open questions

The rest (Days, and whatever follows); what UITable 0x34 is.
