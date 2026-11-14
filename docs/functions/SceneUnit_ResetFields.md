# SceneUnit_ResetFields

- **Address:** `0x140272E98`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t SceneUnit_ResetFields(int16_t slot, uint8_t mode_bits, uint8_t op4)`
- **Callers:** SceneUnit_ZeroPosAndReset (SceneUnit_ZeroPosAndReset).
- **Callees:** SceneObject_FindBySlot, SceneUnit_ReleasePartner

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Resets the state fields of one unit node and calls the partner release routine on it.

## Behavior

- V: finds the unit node for the slot with SceneObject_FindBySlot; when there is none it returns 0.
- V: sets the byte at node +168 to 1, the word at +294 to 0, and the byte at +293 to 0.
- V: sets the byte at +169 to: bits 0 and 1 from the low two bits of the r8 argument (operand 3 minus 1), bits 5 to 7 from bit 0 of the node byte at +138 (bit 5), and the low two bits of the op4 argument (bits 6 and 7).
- V: sets the dword at +68 and the dword at +72 to 0x2000, sets the dword at +164 to 0.
- V: calls SceneUnit_ReleasePartner on the node and returns 1.

## State touched

- Calls: [SceneObject_FindBySlot](SceneObject_FindBySlot.md), [SceneUnit_ReleasePartner](SceneUnit_ReleasePartner.md)

## Referenced by

- Called by: [SceneUnit_ZeroPosAndReset](SceneUnit_ZeroPosAndReset.md)
- Called by event opcodes: [0x70](../opcodes/README.md)

## Notes

The arguments come from registers: the slot in cx, the operand 3 minus 1 in r8 and the operand 4 byte in edx; the decompiler does not show the last two.

## Open questions

Meaning of the byte at +169 and of the fields set to 0x2000.
