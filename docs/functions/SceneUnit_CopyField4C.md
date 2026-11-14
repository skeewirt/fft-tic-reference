# SceneUnit_CopyField4C

- **Address:** `0x14022697C`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void SceneUnit_CopyField4C(int64_t key, uint16_t *out)`
- **Callers:** sub_140240D5C (opcode 0x53 body, at 0x140240E16 and 0x140240E21); sub_140241FF0 (opcode 0x69 body, at 0x140242073); a data reference at 0x143D37E64.
- **Callees:** SceneObject_FindBySlot (unit lookup)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Copies three 16-bit words from a unit node into a caller buffer, used by the opcode 0x53 and 0x69 bodies.

## Behavior

- V: calls SceneObject_FindBySlot(key) to get the unit node. If there is none, it returns without writing anything.
- V: if there is a node, it copies the word at node+0x4C to out[0], the word at node+0x4E to out[1] and the word at node+0x50 to out[2].
- V: it returns nothing; the return register holds a leftover value that the callers do not use.

## State touched

- Calls: [SceneObject_FindBySlot](SceneObject_FindBySlot.md)

## Referenced by

- Called by: [ScenePlacement_WriteGroup](ScenePlacement_WriteGroup.md), [ScenePlacement_WritePair](ScenePlacement_WritePair.md)

## Notes

The function is a plain copy; its name says what it reads, not what the caller does with it.

## Open questions

What the three words at node+0x4C are in the game. The callers' use of them is only read from the opcode records.
