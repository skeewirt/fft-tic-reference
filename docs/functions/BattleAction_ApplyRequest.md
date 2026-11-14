# BattleAction_ApplyRequest

- **Address:** `0x140281434`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int BattleAction_ApplyRequest(const void *request)`
- **Callers:** sub_140206CE8, sub_140282E38, BattleAction_BuildUnitRequest, sub_14030FE60, Battle_AITurnRun
- **Callees:** sub_140281488, sub_140279370

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Wrapper that takes a request whose first byte is a unit slot, points at that unit action block, and applies the request; on success in the normal battle state it also refreshes the unit action.

## Behavior

- V: the request first byte is the unit slot; the unit record is the 0x200-byte entry at 0x141853CE0 plus slot times 0x200 (base by lea, stride by shl 9).
- V: the unit action block is at unit +0x1A0 and is passed to sub_140281488 with a third argument of 1.
- V: when the apply returns 1 and the battle state word at 0x14186AF9C is zero, sub_140279370 is called with the unit and a zero argument.
- V: the result of the apply is returned unchanged; the refresh call does not change it.
- V: the routine does not validate the slot before indexing the unit table.
- V: the six callers are the command commit, the AI turn, the preview and the save/restore wrapper, so the request shape is shared by player and AI paths.
- I: the 1 passed to the apply means 'this is a request from the menu', because the AI passes 0 on its own path.
- ?: whether a slot outside the 21-entry unit table can reach here; the callers are expected to supply a live slot but this body does not test it.

## State touched

- Calls: [sub_140281488](sub_140281488.md)
- Writes: [UnitWorkRecord](../structs/UnitWorkRecord.md)

## Referenced by

- Called by: [BTurn_PreviewAction](BTurn_PreviewAction.md), [BattleAction_BuildUnitRequest](BattleAction_BuildUnitRequest.md)

## Notes

Whole function read (84 bytes). The call to sub_140281488 is the request-to-unit-block step of the item flow.

## Open questions

None recorded.
