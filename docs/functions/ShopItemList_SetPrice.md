# ShopItemList_SetPrice

- **Address:** `0x1402A5A80`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void ShopItemList_SetPrice(void *unused, GUINode *row, int price, char greyed)`
- **Callers:** ShopItemList_DrawRow (sub_1402A57AC), sub_1401B2140, sub_1401B23A0
- **Callees:** GUINode_FindPartByName, GUITextNode_SetTextById, sub_1400FE9D0

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Prints a price into the row's 'TextPrice' part with UI text 1717 (1753 when greyed).

## Behavior

- V: one integer argument (the price) and GUITextNode_SetTextById(part, greyed ? 1753 : 1717, args).

## State touched

- Calls: [GUINode_FindPartByName](GUINode_FindPartByName.md), [GUITextNode_SetTextById](GUITextNode_SetTextById.md)

## Referenced by

- Called by: [ShopItemList_DrawRow](ShopItemList_DrawRow.md)

## Open questions

None recorded.
