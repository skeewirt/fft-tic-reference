# PoachersDen_AddStock

- **Address:** `0x140287564`
- **Area:** [Items and shops](../areas/items.md)
- **Prototype:** `int PoachersDen_AddStock(unsigned short id, int delta)`
- **Callers:** Shop_BuildItemList
- **Callees:** none found

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Adds a signed delta to the Poachers' Den stock count of one item id and returns the resulting count, clamped to the byte
range the store uses; the shop list builder calls it with a zero delta, so in the shop path it is a stock query.

## Behavior

- V: the id argument is masked with 0x3FF before use, so only the low ten bits reach the store.
- V: an id at or above 261 (0x105) is rejected and the function returns 0 without touching the store.
- V: the count is one byte per id in the array at 0x1411A7700; the address is loaded by the rip-relative lea at
  0x14028757F, in the continuation the early return falls through to, which lies past the end of the unwind range the
  cross-check scans.
- V: the function reads that byte, adds the delta and keeps the result in a 32-bit register.
- V: a negative result is replaced by 0, and a result above 255 is clamped to 255.
- V: the clamped byte is written back and returned in the low 32 bits of the return value.
- V: the function reads and writes only the den stock array; it has no other state and calls nothing.
- V: its only direct caller is Shop_BuildItemList, which passes a delta of zero, so the shop path only reads the count.
- I: the 0..255 clamp mirrors the one-byte count arrays used elsewhere for items, and the wrap to zero on a negative total
  makes the store behave like a saturating counter.
- ?: the code path that actually adds stock (poaching) is not a direct call from any function in the image.

## State touched

- Reads: [g_PoachersDenStock](../globals/g_PoachersDenStock.md)
- Writes: [g_PoachersDenStock](../globals/g_PoachersDenStock.md)

## Referenced by

- Called by: [Shop_BuildItemList](Shop_BuildItemList.md)

## Notes

- V: the array is 261 bytes at 0x1411A7700; the item badge block starts 272 bytes after the array base, so only 11 unused
  bytes separate the two stores.

## Open questions

- ?: which routine or script adds den stock during play, given that the only direct caller always passes zero.
- ?: whether the add path enforces the same 261-id bound that this function enforces.
