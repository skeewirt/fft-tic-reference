# SceneUnit_ReleasePartner

- **Address:** `0x1401FB398`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void SceneUnit_ReleasePartner(uint8_t *node)`
- **Callers:** SceneUnit_ResetFields (SceneUnit_ResetFields) and the callers listed in the decompiler (sub_1401FDD7C, sub_1401FE59C, sub_14020B6DC, sub_140268F68, sub_140272D70 and others).
- **Callees:** SceneObject_FindBySlot, sub_1401FAF54 (not read)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

When the unit node's low status bits equal 1, clears the unit's and its partner's status fields and calls the release routine for both.

## Behavior

- V: tests the low two bits of the byte at node +300; it does nothing unless they equal 1.
- V: reads the partner slot from the byte at node +320 and finds the partner node with SceneObject_FindBySlot.
- V: clears bit 1 of the dword at node +348, clears the low two bits of the byte at +300, sets the byte at +298 to 0 and the byte at +320 to 0.
- V: calls sub_1401FAF54 on the node found by the node's own slot byte at +8.
- V: when the partner node exists, clears the low two bits of the partner's byte at +300, sets the partner's byte at +320 to 0, and calls sub_1401FAF54 on the partner node found by the partner's slot byte at +8.

## State touched

- Calls: [SceneObject_FindBySlot](SceneObject_FindBySlot.md)

## Referenced by

- Called by: [EventBlock_ApplyOperands](EventBlock_ApplyOperands.md), [SceneUnit_ResetFields](SceneUnit_ResetFields.md)

## Notes

This is a partner-link release; the names of the two status fields are not decoded.

## Open questions

What sub_1401FAF54 does; the meaning of the status bits.
