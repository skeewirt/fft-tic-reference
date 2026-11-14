# ItemShopMask

- **Kind:** table
- **Area:** [Items and shops](../areas/items.md)
- **Storage:** Executable (constant)
- **Rows:** 512 entries of 1 byte
- **Held in:** [g_ItemShopMask](../globals/g_ItemShopMask.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Which shops sell which item: two bytes per item id 0..0xFF, a mask word whose bit for shop s is 0x8000 >> s. A constant table in read-only data; no code writes it and it is never saved.

## Open questions

None recorded.
