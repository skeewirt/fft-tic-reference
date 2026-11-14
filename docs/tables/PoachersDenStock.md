# PoachersDenStock

- **Kind:** table
- **Area:** [Items and shops](../areas/items.md)
- **Storage:** Executable memory (saved with the game)
- **Rows:** 261 entries of 1 byte
- **Held in:** [g_PoachersDenStock](../globals/g_PoachersDenStock.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Poachers' Den stock: one count per item id 0..260 (PoachersDen_AddStock adds to it, clamped 0..255); the shop list builder Shop_BuildItemList lists the ids with stock when the shop id is 100 or above. Saved with the game.

## Open questions

None recorded.
