# ItemOrder_Remove

- **Address:** `0x140285ED8`
- **Area:** [Items and shops](../areas/items.md)
- **Prototype:** `int ItemOrder_Remove(uint16_t id, uint16_t *orderList)`
- **Callers:** ItemOrder_SyncGroup, sub_140286070, sub_140286160 (three direct sites)
- **Callees:** None

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Removes one id from a saved order list by shifting the entries after it one place to the left. It is the removal half of the three synchronisers and does nothing else.

## Behavior

- V: takes the id in the first argument (ecx) and the list pointer in the second (rdx); it leaves the index where the removal started in eax, which the callers ignore.
- V: walks the list until it meets 255 (0xFF) or a value of 261 or above, the same two end conditions every order-list reader uses; the 261 bound is formed as 0xFF + 6, not an immediate.
- V: on the first entry equal to the id it copies the following entry over it, then repeats with the next pair, so the tail moves left by one and the terminator moves with it.
- V: if the id is not present the list is left untouched.
- V: it reads and writes only the caller's array; it uses no global and calls nothing.
- I: because the three synchronisers call it for every owned id that is no longer held, the list shrinks without ever being rewritten from scratch.
- ?: none.

## Referenced by

- Called by: [ItemOrder_SyncGroup](ItemOrder_SyncGroup.md), [sub_140286070](sub_140286070.md), [sub_140286160](sub_140286160.md)

## Notes

- V: whole body read; leaf.

## Open questions

None recorded.
