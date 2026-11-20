# ItemRowGrammarBytesAndGates

- **Kind:** observed behaviour
- **Scope:** engine (item rows)
- **Area:** [Items and shops](../areas/items.md)
- **Affects:** [UIText_ResolveCategoryRow](../functions/UIText_ResolveCategoryRow.md), [TextTag_CountedNounArticle](../functions/TextTag_CountedNounArticle.md), [sub_1402B89F8](../functions/sub_1402B89F8.md), [Item_IsOwned](../functions/Item_IsOwned.md), [ShopEntry_Fill](../functions/ShopEntry_Fill.md), [ShopItemList_DrawRow](../functions/ShopItemList_DrawRow.md), [TextTagRecord](../structs/TextTagRecord.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Item row bytes +0x18..+0x1B are the four grammar bytes of the counted-noun record; +0x2C gates the 'item owned' story condition and the flagged state of the sell list row.

## Behavior

- V: UIText_ResolveCategoryRow copies Item row bytes +0x18..+0x1B (PoachItem +0x1C..+0x1F, Ability +0x16..+0x19, UI table 0xAC +0x10..+0x13) to tag record +24..+27.
- V: TextTag_CountedNounArticle picks the article row of UIAttributive (table 0xE5, article kind argument) at 3 x byte +24 (one more for a count of 2 or more); a non-zero byte +27 writes the bare noun with no article.
- V: sub_1402B89F8 returns Item row byte +0x1A; three callers push it as a numeric format argument after the item id.
- V: Item_IsOwned returns 0 for an item whose row byte +0x2C is 0; the stock rows are all 0.
- V: ShopEntry_Fill (sell mode) sets entry byte +32 from byte +0x2C; ShopItemList_DrawRow turns it into the flagged row state.
- I: byte +0x2C marks a story item that the party keeps; the sell-list state (greyed or unsellable) is not seen.

## Open questions

? what the flagged row state shows in play.
