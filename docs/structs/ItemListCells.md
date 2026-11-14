# ItemListCells

- **Kind:** structure
- **Area:** [Battle](../areas/battle.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The static item-list cell store: 82 two-byte cells (kind tag in bits 15..11, id in bits 10..0) and the parallel per-cell arrays beside them. The cells are rebuilt in place for every list; no 32-bit per-cell field exists, so a cell carries 11 id bits at most.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="cell_word"></a>`0x0` | cell_word | `uint16[82]` | V | One cell per row: 0x3800 \| item id or 0x7000 \| ability id. The builders OR the tag into the word; the readers recover the id with word arithmetic or masks (0x7FF, 0x1FF, 0x3FF). |
| <a id="property"></a>`0xA4` | property | `uint16[82]` | ? | A per-cell word; its role is not established. |
| <a id="bare_ids"></a>`0x148` | bare_ids | `uint16[82]` | I | The untagged id per cell, filled from the byte list at +0x2E2 (I: the same id without the tag). |
| <a id="list_1ec"></a>`0x1EC` | list_1ec | `uint8[82]` | ? | A byte per cell; role not established. |
| <a id="list_23e"></a>`0x23E` | list_23e | `uint8[82]` | ? | A byte per cell; role not established. |
| <a id="list_290"></a>`0x290` | list_290 | `uint8[82]` | ? | A byte per cell; role not established. |
| <a id="id_bytes"></a>`0x2E2` | id_bytes | `uint8[82]` | I | A byte per cell, read as the source of the bare-id array at +0x148 (I: item ids). |
| <a id="list_334"></a>`0x334` | list_334 | `uint8[82]` | ? | A byte per cell; role not established. |

## Behavior

- V: cell i is at static object 0x1418716A0 + 2*i; the object pointer is 0x141871698, set once at startup by sub_1403166C0. 17 word readers in 10 functions and 9 word writers in 3 functions were read, all 16-bit; no 32-bit per-cell field exists.
- V: two near-identical builders (sub_14023678C and sub_1402EA58C) write 0x3800 | id or 0x7000 | id; a value of 8 goes to a separate static array (0x140D492D0), not to the cell array.
- V: the object is rebuilt per list build, never allocated or freed, and has no length header (the build count is a local; the visible window is held in two words, 0x1407831B0 and 0x1407831B2).
- V: published views: 0x1407831C0 = the object, 0x1407831C8 = object + 0xA4, 0x1407831D0 = object + 0x148, 0x1407831D8 = the separate static array. 0x14184A9B0 is an alias of the object pointer, written through by 11 task functions.
- I: the 11 id bits are the text-id index field, so the 0x800 ceiling of format TextId applies to a cell; the cell cannot carry a 16-bit item id.

## Referenced by

- Appears in flows: [ItemNameToScreen](../flows/ItemNameToScreen.md)

## Notes

V: object address 0x1418716A0; the highest field used is +0x385 and no label marks the end of the buffer.

## Open questions

? the roles of the property word and the five byte arrays; ? the object's exact size; ? which screen builds cells with the 0x7000 tag (ability cells).
