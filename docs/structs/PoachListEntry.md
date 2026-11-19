# PoachListEntry

- **Kind:** structure
- **Area:** [Items and shops](../areas/items.md)
- **Size:** 48 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One entry of the poacher list that PoachList_Build fills: a poach id the party holds.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="item_id"></a>`0x0` | item_id | `int32` | V | Item id (PoachItem +0x2C). |
| <a id="equipped_count"></a>`0x4` | equipped_count | `int32` | V | Number of that item currently equipped. |
| <a id="index"></a>`0x8` | index | `int32` | V | Index in the list. |
| <a id="total_held"></a>`0x10` | total_held | `int32` | V | Total of the item held. |
| <a id="poach_id"></a>`0x18` | poach_id | `int32` | V | Poach id, 1..96. |
| <a id="held_count"></a>`0x1C` | held_count | `int32` | V | Held count of the poach id (non-zero for every listed entry). |
| <a id="price"></a>`0x20` | price | `int32` | V | PoachItem +0x24 (column price). |
| <a id="sell_price"></a>`0x24` | sell_price | `int32` | V | PoachItem +0x28 (column sell_price); PoachSell_FillRow shows it as the row price. |
| <a id="new_flag"></a>`0x28` | new_flag | `int32` | V | New marker, from the per-poach-id flag at unk_1411A7B3F. |

## Behavior

- V: PoachList_Build fills the entries for poach ids 1..96 with a non-zero held count.

## Notes

Detail and evidence: the function sheet PoachList_Build.

## Open questions

None recorded.
