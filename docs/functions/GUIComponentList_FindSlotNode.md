# GUIComponentList_FindSlotNode

- **Address:** `0x14040C1DC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `GUINode *GUIComponentList_FindSlotNode(GUIComponentList *list, int slot)`
- **Callers:** GUIComponentList_GetSlotComponent, GUIComponentList_LayoutSlots and sub_140153CA0, sub_14028D44C, sub_14040C37C
- **Callees:** sub_1403D8E5C, GUINode_FindPartByName, sub_1403D8D1C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Finds the layer node of slot number `slot`: the part named 'ListItem' for slot 0 and 'ListItem#n' for slot n.

## Behavior

- V: key = sub_1403D8E5C(list, tmp, "ListItem", slot): when slot != 0 the name is Str_Format("%s#%d", "ListItem", slot), else plain 'ListItem'; then UIName_Key; node = GUINode_FindPartByName(list+272, key); the key's interned id is released.

## State touched

- Calls: [GUINode_FindPartByName](GUINode_FindPartByName.md)
- Reads: [g_UINameTable](../globals/g_UINameTable.md)

## Referenced by

- Called by: [GUIComponentList_GetSlotComponent](GUIComponentList_GetSlotComponent.md), [GUIComponentList_LayoutSlots](GUIComponentList_LayoutSlots.md)

## Notes

The name is ours (IDB: sub_14040C1DC). The UIB of a list authors one node per slot: ListItem, ListItem#1, ListItem#2 ...

## Open questions

None recorded.
