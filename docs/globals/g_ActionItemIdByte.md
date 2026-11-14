# g_ActionItemIdByte

- **Kind:** global
- **Address:** `0x1407B077E`
- **Area:** [Battle](../areas/battle.md)
- **Type:** `uint8`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The item-id byte the battle action resolver leaves for the item formulas: the item id's low byte plus 0x10, so the formulas rebuild the id by adding 0xF0.

## Behavior

- V: ItemAction_SetAmount, sub_140308C30, sub_140308C98 and sub_1401F9CC4 rebuild the id from it; only the low byte survives.

## Referenced by

- Read by: [ItemAction_SetAmount](../functions/ItemAction_SetAmount.md), [sub_140308C30](../functions/sub_140308C30.md), [sub_140308C98](../functions/sub_140308C98.md)

## Open questions

None recorded.
