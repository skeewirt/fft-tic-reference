# g_PoachCount

- **Kind:** global
- **Address:** `0x1411A7A1A`
- **Area:** [Items and shops](../areas/items.md)
- **Type:** `uint8[97]`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Poach count per type, 97 bytes based at the badge block plus 522; the poach add routine clamps each byte to 99.

## Behavior

- V: sub_1400D6FB0 reads and writes it; sub_140346524 reads it for types 1 to 96.

## Referenced by

- Described by tables: [PoachCount](../tables/PoachCount.md)
- Read by: [sub_1400D6FB0](../functions/sub_1400D6FB0.md), [sub_140346524](../functions/sub_140346524.md)
- Written by: [GameState_ResetParty](../functions/GameState_ResetParty.md), [sub_1400D6FB0](../functions/sub_1400D6FB0.md)

## Open questions

None recorded.
