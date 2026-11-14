# dword_143D1AC68

- **Kind:** global
- **Address:** `0x143D1AC68`
- **Area:** [Items and shops](../areas/items.md)
- **Type:** `int32`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Running price accumulator of an Outfitter equip visit: a positive charge for equipment bought or applied during the visit, added to gil and zeroed by the commit handler.

## Behavior

- V: sub_1402D7280 adds the new item's price when it sets bit 15 (0x1402D732C-0x1402D7345); sub_1402D6464 subtracts the price of a bit-15 word it clears (0x1402D64AA-0x1402D64BB); sub_1402D5CC4 and sub_1402D6914 add or subtract per candidate.
- V: the commit handler sub_1402D6E14 flushes it to gil with sub_140284684(-sum) (0x1402D6E54), zeroes the accumulator (0x1402D6E5B) and then strips the flags.
- V: sub_1402D67C8 zeroes it when the equip change screen closes (0x1402D67C8 end).

## Referenced by

- Observed behaviours: [EquipSessionFlagLifecycle](../behaviors/EquipSessionFlagLifecycle.md)
- Written by: [sub_1402D58EC](../functions/sub_1402D58EC.md), [sub_1402D5CC4](../functions/sub_1402D5CC4.md), [sub_1402D6464](../functions/sub_1402D6464.md), [sub_1402D6914](../functions/sub_1402D6914.md), [sub_1402D7280](../functions/sub_1402D7280.md)

## Open questions

? whether a negative accumulator is possible; the commit path negates whatever it holds.
