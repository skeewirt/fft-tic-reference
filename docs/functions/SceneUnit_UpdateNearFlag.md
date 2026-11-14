# SceneUnit_UpdateNearFlag

- **Address:** `0x140273838`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void SceneUnit_UpdateNearFlag(int16_t slot)`
- **Callers:** EventObject_MoveWorker (EventObject_MoveWorker).
- **Callees:** SceneObject_FindBySlot, sub_140262808 (not read)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sets or clears one flag byte of a unit node by comparing two values from sub_140262808, only when the global mode dword_140782A94 equals 386.

## Behavior

- V: does nothing unless dword_140782A94 equals 386.
- V: finds the unit node for the slot with SceneObject_FindBySlot.
- V: builds three 16-bit sums from words of three node fields and a comparison value v2 (the sum of three words at +74, +90 and +106); calls sub_140262808 with a pointer to the three sums and the flag 0, and again with the flag 1.
- V: sets the byte at node +138 to 1 when the flag-1 result is non-zero, is at least v2, and either the flag-0 result is below v2 or the distance from v2 to the flag-1 result is below the distance from v2 to the flag-0 result; otherwise it sets it to 0.
- I: the three sums are taken from the words at node +76, +92 and +108 and at +80, +96 and +112; the field offsets were derived from the struct layout of the list node.

## State touched

- Calls: [SceneObject_FindBySlot](SceneObject_FindBySlot.md)

## Notes

Not called by opcode 0x70 (the earlier sheet listed it as a callee); the caller is EventObject_MoveWorker.

## Open questions

What sub_140262808 returns; the meaning of byte +138.
