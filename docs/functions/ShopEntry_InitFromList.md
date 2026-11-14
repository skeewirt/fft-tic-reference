# ShopEntry_InitFromList

- **Address:** `0x14028B65C`
- **Area:** [Items and shops](../areas/items.md)
- **Prototype:** `void ShopEntry_InitFromList(ShopEntry *entry, int index)`
- **Callers:** ShopEntry_Fill (sub_14036B2D0), sub_140334A48, sub_140336664, sub_140338060
- **Callees:** Item_CountEquippedByParty, Item_CountTotal

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Starts a shop entry from list word `index` of word_141811470: the id (masked 0x3FF), the index and the equipped and owned counts.

## Behavior

- V: entry +8 = index; entry +0 = word_141811470[index] & 0x3FF; entry +12 = Item_CountEquippedByParty(word); entry +16 = Item_CountTotal(word).
- V: only the id field is masked (sign-extended load at 0x14028B67B, 0x3FF mask at 0x14028B67F); the two count calls at 0x14028B686 and 0x14028B692 receive the whole word, and their callees mask it themselves.

## State touched

- Calls: [Item_CountEquippedByParty](Item_CountEquippedByParty.md), [Item_CountTotal](Item_CountTotal.md)
- Reads: [MenuListWord.item_id](../structs/MenuListWord.md#item_id)
- Writes: [ShopEntry.item_id](../structs/ShopEntry.md#item_id), [ShopEntry.equipped](../structs/ShopEntry.md#equipped), [ShopEntry.owned](../structs/ShopEntry.md#owned)

## Referenced by

- Called by: [ShopEntry_Fill](ShopEntry_Fill.md), [sub_140334A48](sub_140334A48.md), [sub_140336664](sub_140336664.md), [sub_140338060](sub_140338060.md)

## Open questions

None recorded.
