# g_PoachOrder

- **Kind:** global
- **Address:** `0x1411A7A7B`
- **Area:** [Items and shops](../areas/items.md)
- **Type:** `uint8[97]`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The player-visible order of collected poach types, 97 bytes at the badge block plus 619; maintained together with the sort list.

## Behavior

- V: sub_1400D6FB0 moves a type in and out of it; sub_1401ABE14 reads it while assembling the den rows.

## Referenced by

- Described by tables: [PoachOrder](../tables/PoachOrder.md)
- Read by: [sub_1400D6FB0](../functions/sub_1400D6FB0.md), [sub_1401ABE14](../functions/sub_1401ABE14.md)
- Written by: [GameState_ResetParty](../functions/GameState_ResetParty.md), [sub_1400D6FB0](../functions/sub_1400D6FB0.md)

## Open questions

None recorded.
