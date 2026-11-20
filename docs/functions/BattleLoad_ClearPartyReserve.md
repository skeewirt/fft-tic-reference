# BattleLoad_ClearPartyReserve

- **Address:** `0x14033D7E4`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void BattleLoad_ClearPartyReserve(void)`
- **Callers:** BattleLoad_StepFresh
- **Callees:** Resource_GetSlotObject, SceneVar_Write

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Battle load step (state 1) that sets three script data pointers and writes scene variable 57 = 0.

## Behavior

- V: Resource_GetSlotObject(11); qword_140D409D0 and qword_140D409C0 = the slot object + 128 + its dwords at +4 and +8; qword_140D409A0 = qword_140D40A40; then a tail call SceneVar_Write(57, 0).
- V: BattleLoad_StepFresh calls it in state 1, before the entry units are built in state 5, so every fresh battle load starts with variable 57 = 0.

## State touched

- Calls: [Resource_GetSlotObject](Resource_GetSlotObject.md), [SceneVar_Write](SceneVar_Write.md)

## Notes

Named for its effect on the entry budget (EntryUnitsShareADistinctLookBudget).

## Open questions

None recorded.
