# BTurn_PreviewAction

- **Address:** `0x14030FE60`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int BTurn_PreviewAction(UnitWorkRecord *unit, uint8_t *request, void *list, int flag)`
- **Callers:** Battle_TimelineBuildList, sub_14022EFF4
- **Callees:** BattleAction_ApplyRequest, TurnList_Build, sub_14030E2F0, sub_14002630C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Previews what a unit's pending action does to the turn order: applies the request in simulation mode, builds the timeline and puts the unit back as it was.

## Behavior

- V: saves the unit's 20-byte action block (+0x1A0), the bytes +0x18D, +0x1EF, +0x1B9 and +0x1BA, and the simulate mode (g_BattleSimulating), then sets the simulate mode to 2.
- V: calls BattleAction_ApplyRequest on the request; a result of 1 (or -1 when flag is 1) clears byte +0x18D.
- V: builds the turn list with TurnList_Build in mode 3 and, unless it returned -1, fixes it up with sub_14030E2F0 using the unit's bytes +0x1BC and +0x18D.
- V: restores the simulate mode, the four bytes and the action block; five status bytes are rebuilt as the OR of byte +0x57 + i and byte +0x1EF + i into +0x61 + i (the 0x61 is reached as +0x57 + 10 in a five-step loop) (what these two sources are was not read).
- I: the unit's ability word at +0x1A2 holds the previewed ability only while the simulation runs (the block copy is restored afterwards); the reading rests on the restore of the saved block +0x1A0..+0x1B3, which holds +0x1A2 (the word itself is not named in the body), not on a check of the word.

## State touched

- Calls: [BattleAction_ApplyRequest](BattleAction_ApplyRequest.md), [TurnList_Build](TurnList_Build.md)
- Reads: [UnitWorkRecord.action_request](../structs/UnitWorkRecord.md#action_request)
- Writes: [UnitWorkRecord.action_request](../structs/UnitWorkRecord.md#action_request)

## Referenced by

- Called by: [Battle_TimelineBuildList](Battle_TimelineBuildList.md)
- Observed behaviours: [StatusBitWritersAndTheRemovalPath](../behaviors/StatusBitWritersAndTheRemovalPath.md)

## Notes

The name is the IDB's (BTurn_PreviewAction); read 2026-11-10. 355 bytes, read whole. It recomputes +0x61 = +0x57 | +0x1EF after putting +0x1EF back (a five-byte loop from the +0x57 base: +10 and +408 from it).

## Open questions

? what bytes +0x57..+0x5B and +0x1EF..+0x1F3 are (the status OR at the end); what +0x1BC and +0x18D are.
