# SceneUnit_ZeroPosAndReset

- **Address:** `0x1402356B0`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t SceneUnit_ZeroPosAndReset(const uint8_t *operands)`
- **Callers:** EventScript_Run (opcode 0x70 case) and EventSubScript_RunTask (EventSubScript_RunTask).
- **Callees:** EventRef_ResolveSlot, SceneObject_FindBySlot, SceneUnit_AddPosition, ScenePreview_IndexOfSlot, SceneUnit_ResetFields

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Zeroes the three position words of the unit named by its operands and then calls the unit reset routine on it, with one preview-table byte set to 6 for the duration of that call.

## Behavior

- V: resolves the id at operand bytes 1 and 2 with EventRef_ResolveSlot, using the low byte of the id as the flag. When the result is 2000 it does nothing.
- V: reads the three 16-bit words at unit node +108, +110 and +112 and stores their negated values in a three-word buffer.
- V: calls SceneUnit_AddPosition with the slot and the buffer. That routine adds the three buffer words to the unit words at +108, +110 and +112 (16-bit wrap), so the position words become zero.
- V: calls ScenePreview_IndexOfSlot for the slot. When the index is 0 to 20 it saves the byte at unk_141853D23 plus 512 times the index, sets that byte to 6, and restores it after the next call. When the index is above 20 (including -1) the byte pointer is the address 67, which the code reads and writes.
- V: calls SceneUnit_ResetFields with the slot in the cx register (not set by the visible code after the preview lookup), operand 3 minus 1 in the r8 register and operand 4 in the edx register. It returns the result of SceneUnit_ResetFields, which is 1 when a unit node exists and 0 otherwise.
- V: the function does not wait.
- V: when the slot resolves but no unit node exists, the code reads the node's words through a zero pointer; no null test is made before the first read.

## State touched

- Calls: [EventRef_ResolveSlot](EventRef_ResolveSlot.md), [SceneObject_FindBySlot](SceneObject_FindBySlot.md), [SceneUnit_AddPosition](SceneUnit_AddPosition.md), [ScenePreview_IndexOfSlot](ScenePreview_IndexOfSlot.md), [SceneUnit_ResetFields](SceneUnit_ResetFields.md)

## Notes

The preview byte is at unk_141853D23 with 512-byte records; it is a per-unit byte of the preview table, meaning not decoded.

## Open questions

Whether the cx value passed to SceneUnit_ResetFields is the unit slot; what the preview byte set to 6 means; what happens for a slot with no node.
