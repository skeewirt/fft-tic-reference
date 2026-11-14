# EquipDetail_Refresh

- **Address:** `0x14029F950`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void EquipDetail_Refresh(void *panel, const void *selection)`
- **Callers:** sub_1400ED254, sub_14019A110, sub_1401AEEF0, sub_14022F868 (two sites), sub_1402A54E8, sub_1402E600C (two sites)
- **Callees:** ItemIcon_FormatLargePath, ItemCell_BindIconAndName, sub_1400F5828

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Refreshes the item detail panel for one selected item: it builds the item's large picture path, then binds the picture and the
item name to the panel's parts.

## Behavior

- V: takes the panel object and a selection record whose first dword is the item id.
- V: returns early when a pointer field of the panel is null, or when a helper called with the panel's own record area rejects the
  selection.
- V: copies a 16-byte block out of the selection record into the panel at +0x2A0.
- V: formats the large item picture path for the selected id into a 260-byte stack buffer.
- V: calls the shared item-cell binder with the same id, that path and show-empty cleared, so the large picture and the name go to
  the panel's icon and text parts.
- V: eight direct call sites.
- I: all eight are UI controllers: item, shop and unit screens, because each one binds the large picture or refreshes a panel.
- I: the panel is the equipment/item detail panel, because its callers are item, shop and unit screens and it binds the large
  picture rather than the small list one.
- ?: what the early-out helper validates about the selection record.

## State touched

- Calls: [ItemIcon_FormatLargePath](ItemIcon_FormatLargePath.md), [ItemCell_BindIconAndName](ItemCell_BindIconAndName.md)

## Referenced by

- Called by: [BattleCommand_BuildScreen](BattleCommand_BuildScreen.md), [sub_1401AEEF0](sub_1401AEEF0.md)

## Notes

- V: the head and the large-path site were read; the rest of the body (1746 bytes) was not.

## Open questions

- ?: the exact field at panel +0x2A0 that receives the copied block.
