# ItemNameToScreen

- **Kind:** flow
- **Area:** [Data access](../areas/data.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

How an item id becomes a name on screen, by two independent routes: the 0x3800 text id (a pool id decoded by sub_140226208, carried in a 2-byte list cell or a 32-bit message argument) and the Item-en row lookup (ItemTable_GetName, a full 32-bit key). The route decides the id width and whether the string is a pool entry or a table row.

## Steps

| Step | Where | Conf | What happens |
|---|---|---|---|
| <a id="1"></a>1 |  | V | A builder adds the tag to an item id: 0x3800 for the name pool, 0x6800 for the help pool. There are 12 name-tag sites in 11 functions (mostly 16-bit ids, one 8-bit) and 7 help sites in 6 functions. |
| <a id="2"></a>2 | [ItemListCells](../structs/ItemListCells.md) | V | The tagged word is stored in a list cell (2 bytes, tag in bits 15..11) or as a 32-bit argument in the current-message block 0x140783210 or the shared help slot 0x1418736B4. |
| <a id="3"></a>3 | [TextId](../formats/TextId.md) | V | A consumer splits the word: kind = bits 15..11, index = bits 10..0. The item branches test kind 7 and recover the id with an 11-bit mask. |
| <a id="4"></a>4 | [sub_140226208](../functions/sub_140226208.md) | V | The pool decoder looks the kind up in qword_140D40990 and walks the index-th record of that pool. Kinds 14 and 22 are redirected; there is no bounds check. |
| <a id="5"></a>5 | [sub_140243390](../functions/sub_140243390.md) | V | The text command's callback receives the id at 32 bits (the posting thunk sign-extends it), calls the decoder and attaches the string to the node. A second callback uses the duplicate decoder EventText_FindMessage. |
| <a id="6"></a>6 | [ItemTable_GetName](../functions/ItemTable_GetName.md) | V | The other route: the Item-en row (nxd table 45) by the full 32-bit item id. ItemCell_BindIconAndName and the name branch of sub_140153CA0 call it directly and never form a text id. |
| <a id="7"></a>7 | [ItemCell_BindIconAndName](../functions/ItemCell_BindIconAndName.md) | V | The cell sets icon path and name only when the Item-en row exists and the id is not negative; with no row it leaves the cell unset. |
| <a id="8"></a>8 | [ItemIcon_FormatSmallPath](../functions/ItemIcon_FormatSmallPath.md) | V | The list picture is built from the same id, unmasked, and bound with the name; the picture path has its own format record (ItemIconPath). |

## Behavior

- V: the carriers differ in width. The list cell is 2 bytes; the current-message block, the text command and the help slot carry 32 bits with no 16-bit store; the battle message queue's item branch keeps only the low 8 bits of its value when bit 15 is set.
- V: the tag arithmetic is the limit: 0x3800 + N changes kind for N >= 0x800, and 0x6800 + N becomes the ability kind 0x7000. The Item-en accessor takes the full 32-bit id; only its callers mask.
- V: the name and the help have different sources. The name may come from Item-en (panels) or pool 7 (text ids); the help may be pool 13 (a 0x6800 token) or the Item-en description field (the equipment detail panel).

## Notes

V: the decode points are the generic decoder, the battle-name masks, the cell id mask and the tag builders.

## Open questions

? which screens use the pool route and which the Item-en route for a stock item; ? whether a pool-backed name ever disagrees with the Item-en name in stock play.
