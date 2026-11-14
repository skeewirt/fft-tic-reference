# SceneVar_ResolveSlot

- **Address:** `0x140242984`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `uint32_t *SceneVar_ResolveSlot(int index)`
- **Callers:** SceneVar_Alu
- **Callees:** SceneTask_Terminate

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Maps an event variable index to the address of its dword in the second task group's variable store.

## Behavior

- V: the same mapping as EventVar_ResolveSlot (dwords 0-127, bits 128-863, nibbles 864-1023) on the store pointer `off_1407830D8`.
- V: an index of 1024 or more calls SceneTask_Terminate and returns null.

## State touched

- Calls: [SceneTask_Terminate](SceneTask_Terminate.md)

## Referenced by

- Called by: [SceneVar_Alu](SceneVar_Alu.md)

## Notes

See EventVar_ResolveSlot.

## Open questions

None recorded.
