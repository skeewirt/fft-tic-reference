# EventThread_PumpAudioWhileBusy

- **Address:** `0x140343564`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `__int64 __fastcall EventThread_PumpAudioWhileBusy(__int64 arg)`
- **Callers:** EventCmd_SetBackdrop, EventCmd_SetRecordOffset, WorldMap_InitLocations, Tavern_HasNewEntries, ClassicMenu_LoadPageArtPack, PackedBlock766_Load, PackedBlock767_Load, sub_1402473EC, sub_1402482F8, sub_1402D4A3C, sub_1402F109C, GameData_StartTrackedRead, sub_140372EF0, sub_1403769CC, sub_140378FA4, sub_1403793DC; also referenced from a data table at 0x143D3E740
- **Callees:** sub_14033FE00, EventThread_Yield

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Loops, one frame at a time, until the high dword of `qword_141856AB0` (0x141856AB4) is zero; each pass services the audio command queue and hands the baton back to the scheduler.

## Behavior

- V: while the dword at 0x141856AB4 is non-zero it calls `sub_14033FE00` (the audio command queue servicer) with no argument (the argument seen in the pseudocode is a call-site artifact) and then `EventThread_Yield(1)`; this function's own argument is therefore unused.
- V: the return value is the result of the last `EventThread_Yield` call (undefined when the loop body never runs).
- I: the dword at 0x141856AB4 is a busy count of a block load in progress (rests on the callers: the event command that selects a data block, the packed-block loaders and the world-map and tavern set-up code all call this right after starting a load).

## State touched

- Calls: [sub_14033FE00](sub_14033FE00.md), [EventThread_Yield](EventThread_Yield.md)

## Referenced by

- Called by: [ClassicMenu_LoadPageArtPack](ClassicMenu_LoadPageArtPack.md), [EventCmd_SetBackdrop](EventCmd_SetBackdrop.md), [EventCmd_SetRecordOffset](EventCmd_SetRecordOffset.md), [GameData_StartTrackedRead](GameData_StartTrackedRead.md), [PackedBlock766_Load](PackedBlock766_Load.md), [PackedBlock767_Load](PackedBlock767_Load.md)

## Notes

V: whole body read (35 bytes). The name is ours. I: the load-wait role rests only on the callers.

## Open questions

?: which code writes the high dword of qword_141856AB0 and what it counts.
