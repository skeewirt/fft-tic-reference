# EventVar_ResolveSlot

- **Address:** `0x1402EC298`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `uint32_t *EventVar_ResolveSlot(int index)`
- **Callers:** EventVar_Alu
- **Callees:** EventTask_Terminate (error trap)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Maps an event variable index to the address of the dword in the store that holds it.

## Behavior

- V: indices 0-127 are whole dwords at `store + 4 * index`.
- V: indices 128-863 are single bits: dword `(index - 128) / 32` of a region at `store + 512`; the bit is `index & 31`.
- V: indices 864-1023 are 4-bit nibbles: dword `(index - 864) / 8` of a region at `store + 604`; the nibble is `index & 7`.
- V: an index of 1024 or more calls the error trap EventTask_Terminate and returns null.
- V: the store pointer is `off_14078DCE8`; the three regions total 604 + 80 = 684 bytes.

## State touched

- Calls: [EventTask_Terminate](EventTask_Terminate.md)

## Referenced by

- Called by: [EventVar_Alu](EventVar_Alu.md)
- Resolves registries: [EventVariables](../registries/EventVariables.md)

## Notes

Only the address is returned; EventVar_Alu works out the bit or nibble shift and mask from the index itself.

## Open questions

None recorded.
