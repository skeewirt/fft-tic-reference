# EventUnitStatus_SaveAndHide

- **Address:** `0x140241128`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int64 EventUnitStatus_SaveAndHide(int slot)`
- **Callers:** EventUnitBlock_RunTask (2), EventScript_Run (2), EventUnitStatus_RunMembers
- **Callees:** SceneVar_Read, sub_14030CFB8

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

For an event scene, saves the status state of a unit into the event unit store and clears the statuses the scene must not show.

## Behavior

- V: returns 0 at once when the store marks the slot as done (store byte +924 + slot); otherwise copies +0x57, +0x1EF and +0x61 (five bytes each; the applied set is addressed as an offset from the store, 5 * (99 - slot)), the 16 countdown bytes, the charge counter +0x18D, the KO counter +0x07, the HP word +0x30 and +5 into the store (qword_142FF8268).
- V: the pending remove +0x1E0 becomes +0x61 & a five-byte mask: byte_1406720EC when SceneVar 509 is 0, else byte_1406720B8 for some units (+0x12, the marker, the job) and byte_1406720F4 for the others; the same bytes go into two store areas; two flag bits of the store word +1008 follow.
- V: when the remove holds Charmed (byte 4 bit 0x20) +5 takes +0x1EE; then sub_14030CFB8 removes the pending set from +0x61 and +0x57 (not +0x1EF), through the scene callback slot when dword_140D40948 is set; marks the slot done and returns 1.
- I: sub_14024138C is the restore: it writes +0x57, +0x1EF, +0x61 and the countdowns back from the store.

## State touched

- Calls: [SceneVar_Read](SceneVar_Read.md), [sub_14030CFB8](sub_14030CFB8.md)
- Reads: [UnitWorkRecord.status_effective](../structs/UnitWorkRecord.md#status_effective), [UnitWorkRecord.applied_status](../structs/UnitWorkRecord.md#applied_status), [UnitWorkRecord.innate_status_a](../structs/UnitWorkRecord.md#innate_status_a), [UnitWorkRecord.status_countdown](../structs/UnitWorkRecord.md#status_countdown)
- Writes: [UnitWorkRecord.pending_status_remove](../structs/UnitWorkRecord.md#pending_status_remove)

## Referenced by

- Observed behaviours: [StatusBitWritersAndTheRemovalPath](../behaviors/StatusBitWritersAndTheRemovalPath.md)

## Notes

Name is ours. The removal here works on +0x61 and +0x57 and never on +0x1EF; the restore puts +0x61 back whole.

## Open questions

? what the three masks hold per scene kind.
