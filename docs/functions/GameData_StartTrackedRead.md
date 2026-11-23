# GameData_StartTrackedRead

- **Address:** `0x1403434D0`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `__int64 __fastcall GameData_StartTrackedRead(__int64 waitArg, unsigned int sector, unsigned int count, int blocks, void *dest)`
- **Callers:** ClassicMenu_LoadPageArtPack, PackedBlock766_Load, PackedBlock767_Load, WorldMap_InitLocations; a data reference
- **Callees:** EventThread_PumpAudioWhileBusy, GameData_ReadSectors

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Waits for any earlier tracked read, records the new request in a status block and starts the sector read.

## Behavior

- V: first calls `EventThread_PumpAudioWhileBusy`, which loops (service the audio queue, yield) while a pending-read word is non-zero.
- V: zeroes the status words, stores the sector, the block count and the destination in the block at 0x141856AB0..AD0, and calls `GameData_ReadSectors(sector, count, blocks << 11, dest)`.
- V: always returns 0.

## State touched

- Calls: [EventThread_PumpAudioWhileBusy](EventThread_PumpAudioWhileBusy.md), [GameData_ReadSectors](GameData_ReadSectors.md)

## Notes

Whole body read.

## Open questions

Names of the status block fields.
