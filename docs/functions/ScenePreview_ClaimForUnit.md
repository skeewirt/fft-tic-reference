# ScenePreview_ClaimForUnit

- **Address:** `0x1402731E8`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t ScenePreview_ClaimForUnit(int16_t key)`
- **Callers:** EventScript_Run (opcode 0x45 path, at the calls near 0x14023B208 to 0x14023CA9F); sub_1402029DC, EventSubScript_RunTask, EventUnitBlock_RunTask and sub_140269DC4 (helpers).
- **Callees:** SceneObject_FindBySlot (unit lookup), BattleUnit_RevealOnField

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

For one unit: sets its state words at +0x0E and +0x1F8 to 1 and claims its preview entry. Used by opcode 0x45 on the unit side.

## Behavior

- V: calls SceneObject_FindBySlot(key). If there is no unit node it returns 0.
- V: sets the words at node+0x0E and node+0x1F8 to 1.
- V: reads the node's sub-record pointer at +0x148. When it is nonzero, it reads the byte at sub-record +0x1BC (the preview index) and calls sub_1402718CC with that index.
- V: returns 1 when the node exists.
- V: BattleUnit_RevealOnField(index) puts the battle unit record on the field when it is off it (detail on its sheet); so this turns a unit that is already drawn but not placed (an entry built with presence 0xC0) into a unit on the field.

## State touched

- Calls: [SceneObject_FindBySlot](SceneObject_FindBySlot.md), [BattleUnit_RevealOnField](BattleUnit_RevealOnField.md)

## Referenced by

- Called by: [Battle_TurnStep](Battle_TurnStep.md), [EventSubScript_RunTask](EventSubScript_RunTask.md), [EventUnitBlock_RunTask](EventUnitBlock_RunTask.md)
- Called by event opcodes: [0x44](../opcodes/README.md), [0x45](../opcodes/README.md)
- Observed behaviours: [BattleUnitsAreFixedAtLoadAndRevealedLater](../behaviors/BattleUnitsAreFixedAtLoadAndRevealedLater.md)

## Notes

The brief calls this the release side of opcode 0x45; in the code it claims the entry (writes the slot into the owner byte), and the release is not in this function. Cross-check note: 0xC0 is an entry presence value (Battle_PlaceEntryUnits), not a constant of this body.

## Open questions

What word_14114B0B4 and byte_140D405A2 hold. The release path: one EventScript_Run case (at 0x14023BFA0) writes 0xFF to the record slot byte and a register value to +0x1B5; which opcode owns it is not confirmed.
