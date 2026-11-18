# EventIdRowOfTheCurrentEventIsReadWithoutANullTestWhenSkipping

- **Kind:** observed behaviour
- **Scope:** engine (event script load, EventId table)
- **Area:** [Event system](../areas/event-system.md)
- **Affects:** [EventScript_LoadCurrent](../functions/EventScript_LoadCurrent.md), [EventScript_Run](../functions/EventScript_Run.md), [sub_14020261C](../functions/sub_14020261C.md), [SaveSlot_WriteFromLive](../functions/SaveSlot_WriteFromLive.md), [Battle_SaveCapture](../functions/Battle_SaveCapture.md), [Battle_RestoreSceneVars](../functions/Battle_RestoreSceneVars.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

When the current event changes and skipping is enabled, EventScript_LoadCurrent looks up the EventId row (data table 156) of the event number and reads its byte +32 without testing the lookup result: an event number with no EventId row makes it read through a null pointer. The other readers of that table test for null.

## Behavior

- V: EventScript_LoadCurrent compares scene variable 39 with the last loaded event; when they differ, the skip-flags word is not 1 and skipping is enabled, it takes the table (registry id 156), asks NxdTable_GetRowById for the event number, uses the default row for a negative entry, and otherwise sets the row pointer to null when the table or the row is missing, then reads byte +32 of it.
- V: EventScript_Run (the dword at +28), sub_140254ABC (byte +39) and sub_14020261C (byte +37) read the same table for the current event and skip the read when the row is missing.
- V: the event number is kept as a dword in the battle capture (Battle_SaveCapture stores scene variable 39 and the applier's resume key; Battle_RestoreSceneVars puts both back), the world save copies the whole scene variable store, and SaveSlot_WriteFromLive stores variable 39 as a 16-bit word at +284 of the slot record.
- V: the other readers of variable 39 found (21 functions that load the index 39 directly) compare it with fixed event numbers or pass it on as a lookup key; none indexes an array by it except the per-event word table.

## Notes

I: byte +32 of the EventId row decides whether the skip check goes on to the fixed list of event numbers at 0x1407142E0 (read only as far as the branch).

## Open questions

? readers of variable 39 that load the index from another register were not part of the scan.
