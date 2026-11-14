# ShopItemList_DrawRow

- **Address:** `0x1402A57AC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void ShopItemList_DrawRow(ShopItemList *list, GUINode *row, ShopEntry *entry, int index)`
- **Callers:** sub_140199440, sub_140199680, sub_140199BC8, sub_140199FD8, sub_14019A5B8
- **Callees:** ShopItemList_FillRow, ShopItemList_SetPrice, SceneVar_Read, GUINode_FindState, GUINode_PlayState, GUINode_StopState

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Draws one shop list row: fills it (ShopItemList_FillRow), colours the owned count and the price, prints the price and shows the 'new' and 'selected' marks.

## Behavior

- V: in sell mode (list +2080 == 1) a set entry +32 greys the row; outside it an owned count (entry +16) of 99 or more turns the count red.
- V: outside sell mode the price turns red when the party's gil (SceneVar_Read(44)) is below entry +24.
- V: the price is printed by ShopItemList_SetPrice(row, entry +24, greyed).
- V: entry +33 is passed to sub_1402A4804 (I: the 'new' mark); entry +35 selects the 'ShowIconSelect' / 'HideIconSelect' states.

## State touched

- Calls: [ShopItemList_FillRow](ShopItemList_FillRow.md), [ShopItemList_SetPrice](ShopItemList_SetPrice.md), [SceneVar_Read](SceneVar_Read.md), [GUINode_FindState](GUINode_FindState.md), [GUINode_PlayState](GUINode_PlayState.md), [GUINode_StopState](GUINode_StopState.md)
- Reads: [ShopEntry.price](../structs/ShopEntry.md#price), [ShopEntry.owned](../structs/ShopEntry.md#owned)

## Open questions

None recorded.
