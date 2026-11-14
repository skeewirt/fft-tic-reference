# g_PoachNewFlags

- **Kind:** global
- **Address:** `0x1411A7B3D`
- **Area:** [Items and shops](../areas/items.md)
- **Type:** `uint16[97]`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Two new-flag bytes per poach type at the badge block plus 813; a new game fills them with 0x0101 and the badge routine clears the high byte.

## Behavior

- V: sub_140346524 clears the high byte of the pair when the type has stock.

## Referenced by

- Described by tables: [PoachNewFlags](../tables/PoachNewFlags.md)
- Read by: [sub_140346524](../functions/sub_140346524.md)
- Written by: [GameState_ResetParty](../functions/GameState_ResetParty.md), [sub_140346524](../functions/sub_140346524.md)

## Open questions

None recorded.
