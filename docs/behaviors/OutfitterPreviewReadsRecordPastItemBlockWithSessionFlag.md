# OutfitterPreviewReadsRecordPastItemBlockWithSessionFlag

- **Kind:** observed behaviour
- **Scope:** engine (Outfitter preview)
- **Area:** [Items and shops](../areas/items.md)
- **Affects:** [PartyHandWord](../structs/PartyHandWord.md), [sub_1402D6FB8](../functions/sub_1402D6FB8.md), [sub_1402D6464](../functions/sub_1402D6464.md), [sub_1402D65D4](../functions/sub_1402D65D4.md), [sub_1402D7280](../functions/sub_1402D7280.md), [Item_GetRecord](../functions/Item_GetRecord.md), [sub_1400FA7AC](../functions/sub_1400FA7AC.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The Outfitter preview builder, the equip-clear price step and the equip commit each reduce a party hand word to an item id with an AND that must strip the session flag (bit 15); an AND whose mask keeps bit 15 turns the id into 0x8000 + id, and Item_GetRecord, which does no range check, then reads a 12-byte record 32,768 rows past the item block.

## Behavior

- V: in the stock code bit 15 of a party hand word means 'picked or bought in this Outfitter session' (sub_1402D7280 stores id | 0x8000 and adds the price to the running total); the preview builder takes the id as word AND 0x3FF (mask loaded at 0x1402D7027), the equip-clear step as word AND 0x3FF (0x1402D64AA), the commit as word AND 0x3FF (0x1402D6609); the mask strips the flag and every id bit above bit 9.
- V: the preview builder (sub_1402D6FB8) extracts bit 15 by a shift (0x1402D704C), prices a flagged slot with the record's +8 price, and posts the five id and price pairs through sub_140295558; the equip-clear step (sub_1402D6464) subtracts the price of a flagged slot from the running total and stores an unflagged word in the override array; the commit (sub_1402D65D4) strips the flags of every party word, returns each stored original to the inventory and clears the override array.
- V (disassembly): Item_GetRecord has no bound check: an id below 0x100 indexes one 12-byte table, any other id indexes the second table by 12 times the id, so an id of 0x8000 + n reads the record 393,216 bytes after the record for n.
- V (seen live): with the flag left in the id, the Fitting preview of a picked item showed a blank After row and the stat compare of the wrong record; for two ids (16,383 and 20,000) it raised one access violation inside sub_1400FA7AC and the game stopped answering; a stock item previewed without a fault.
- I: the fault needs the unrelated record to carry an attribute byte of 0x55 or more: sub_1400FA7AC then sets its attribute-record pointer to null and loads through it. Whether a given pick faults depends on what memory follows the item block, not on the item.
- I: the same wrong id in the equip-clear step subtracts the price of the record past the block from the total, and in the commit makes the new word differ from the stored one at the 'not changed' compare, so a pending slot always takes the new-item-flag branch; the code path was read, not seen.
- V (tested limit): with the strip mask 0x7FFF (the exact id mask), a flagged word and a plain word give the same id for every id from 0 to 32,767, and the preview, buy-and-equip, cancel and the Status equip behaved with the item's own name, icon, stats and price at ids 300, 16,383, 20,000 and 32,000.

## Notes

The census of the other equip-session masks (0x1402D59CB, 0x1402D60F3, 0x1402D72F3, 0x1402D7314, 0x1402D7392, 0x14028B67F): I, each reads a word without the flag or an id that is never flagged. Three more were wrongly in that list until 2026-11-24: 0x1402D5F3D, 0x1402D6A50 and 0x1402D6B1E mask a marked candidate or a pending hand word (behaviour OptimalFittingBuysTheCandidatesMarkedWithBit15). The equip-change function sub_1402D7280 refuses a word with bit 14 set (test at 0x1402D72A0) and its callers pass a plain id; the cancel (sub_1402D5B6C) and commit decide 'session word or plain id' by comparing the word with 0x4000, which a plain id of 16,384 or more also passes.

## Open questions

? what the Optimal Fitting button does with a picked id of 16,384 or more (not run).
