# PoachSell_FillRow

- **Address:** `0x1401B2140`
- **Area:** [Items and shops](../areas/items.md)
- **Prototype:** `void PoachSell_FillRow(...)`
- **Callers:** the poacher sell screen
- **Callees:** sub_1402A4230, ShopItemList_SetPrice

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills one row of the poacher sell list.

## Behavior

- V: runs sub_1402A4230, ShopItemList_SetPrice(entry +36), plays 'ShowPoacherSell' and sets the new marker from entry +40.

## State touched

- Calls: [ShopItemList_SetPrice](ShopItemList_SetPrice.md)

## Open questions

None recorded.
