# SceneGroup_ResolveId

- **Address:** `0x140240888`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int SceneGroup_ResolveId(uint16_t *id, int32_t *groupMode)`
- **Callers:** EventScript_Run (opcode 0x81 through the call at 0x14023D716, and opcode 0x80 through the call at 0x14023D79C); SceneGroup_SetFlag04 (opcodes 0x6C and 0x6D); sub_140241CB0 (opcode 0x83 body); sub_140240D5C, sub_140240F34, sub_1402416C8, sub_140241DF8, sub_140241EC4 and sub_140241FF0 (helper bodies that are called from EventScript_Run).
- **Callees:** EventRef_ResolveSlot (the id resolver)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Reads an operand id and decides whether it names one unit or a group: ids 1 to 255 are resolved to a unit id, and ids 0 and 256 and up select a group mode for SceneUnit_TestGroupMember.

## Behavior

- V: if *id is 0 it writes 1 to *groupMode, leaves *id unchanged and returns 1.
- V: if *id is 256 or more it writes *id - 254 to *groupMode (so ids 256, 257, 258 and 259 give modes 2, 3, 4 and 5), leaves *id unchanged and returns 1. Larger ids give larger modes, which the group test treats as no match.
- V: for ids 1 to 255 it calls EventRef_ResolveSlot with the id, stores the result in *id as a 16-bit value and writes 0 to *groupMode. It returns 0 when the result is 2000 (0x7D0, no unit) and 1 otherwise.
- V: how ids 1 to 255 map to slots (including the special ids 100 to 105) is described in EventRef_ResolveSlot.

## State touched

- Calls: [EventRef_ResolveSlot](EventRef_ResolveSlot.md)

## Referenced by

- Called by: [EventUnitStatus_RunMembers](EventUnitStatus_RunMembers.md), [SceneGroup_SetFlag04](SceneGroup_SetFlag04.md), [ScenePlacement_WriteGroup](ScenePlacement_WriteGroup.md), [ScenePlacement_WritePair](ScenePlacement_WritePair.md), [SceneUnit_ApplyModeAndAction](SceneUnit_ApplyModeAndAction.md)
- Called by event opcodes: [0x2C](../opcodes/README.md)

## Notes

The id values 0 and 256 and up are group selectors; the operand itself never names a group by byte, only through this 16-bit range.

## Open questions

What the 16 records scanned for id 104 and the unit data behind ids 105 and above hold; see EventRef_ResolveSlot.
