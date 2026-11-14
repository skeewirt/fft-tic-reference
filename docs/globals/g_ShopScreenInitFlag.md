# g_ShopScreenInitFlag

- **Kind:** global
- **Address:** `0x14184A641`
- **Area:** [Items and shops](../areas/items.md)
- **Type:** `uint8`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One-shot setup byte of the buy and sell screens: the first entry builds the rows, later entries keep the existing list and scroll position.

## Behavior

- V: sub_14036A9D8 and sub_14036C49C test it before building.

## Referenced by

- Read by: [sub_14036A9D8](../functions/sub_14036A9D8.md), [sub_14036C49C](../functions/sub_14036C49C.md)
- Written by: [sub_14036A9D8](../functions/sub_14036A9D8.md), [sub_14036C49C](../functions/sub_14036C49C.md)

## Open questions

None recorded.
