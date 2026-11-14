# ItemAction_SetAmount

- **Address:** `0x140306BD0`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void ItemAction_SetAmount(void)`
- **Callers:** none direct; reached as slot 73 of the ability-formula handler table (`0x140682BC8 + 73*8`) through the dispatcher in Battle_ResolveAction
- **Callees:** `sub_1402B8E04` (Item_GetChemistRecord)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The formula handler for the MP-restoring consumables: it rebuilds the used item's id, reads that item's chemist row and
writes the item's amount into the battle result block.

## Behavior

- V: it takes no arguments; it reads the battle context the same way the other item formulas do.
- V: it rebuilds the item id from the byte at `0x1407B077E`, which Battle_ResolveAction fills with the item id's low byte
  plus `0x10`, by adding `0xF0`.
- V: only the low byte of the id survives that round trip: an item whose low byte is `0xF0` or above rebuilds as one of
  240..255 instead of itself, while every other id is rebuilt exactly, including ids above 255.
- V: it calls Item_GetChemistRecord with the rebuilt id and reads the row's second byte, the amount field.
- V: it multiplies that byte by ten (four times the byte plus the byte, then doubled).
- V: it stores the product as a 16-bit amount in the result block at +0xC.
- V: it writes `0x10` into the result block byte at +0x27.
- I: this is the MP formula rather than the HP one, because the only stock items with formula 73 are Ether and High
  Ether, and the HP formula writes its amount at +6 instead.
- I: the ten-times scaling means the chemist amount byte is stored in tens in the item table (Ether's 2 becomes 20).
- ?: what result bit `0x27 & 0x10` tells the later result stages.

## State touched

- Calls: [sub_1402B8E04](sub_1402B8E04.md)
- Reads: [g_ActionItemIdByte](../globals/g_ActionItemIdByte.md)

## Notes

- V: the whole function was read; the formula table slot was confirmed against the dispatcher's index expression.

## Open questions

None recorded.
