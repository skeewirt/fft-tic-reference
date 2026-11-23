# PackedBlock766_Load

- **Address:** `0x1403436C0`
- **Area:** [Resource](../areas/resource.md)
- **Prototype:** `int PackedBlock766_Load(int blockIndex)`
- **Callers:** sub_140247E8C, EventCmd_SetRecordOffset, sub_14033EC0C, sub_140344B68, Errand_ReportDialogueStep, sub_140371CAC, sub_140374484
- **Callees:** EventThread_PumpAudioWhileBusy, GameData_StartTrackedRead

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Starts loading one block of packed data file 766 into the shared block buffer.

## Behavior

- V: does nothing when the block is already the current one.
- V: waits for any read in progress, then takes start = table[index] and length = table[index + 1] - table[index] from the sector table at 0x140684CD0 and starts the read (length in 2048-byte sectors) into the block buffer.

## State touched

- Calls: [EventThread_PumpAudioWhileBusy](EventThread_PumpAudioWhileBusy.md), [GameData_StartTrackedRead](GameData_StartTrackedRead.md)

## Referenced by

- Called by: [Errand_ReportDialogueStep](Errand_ReportDialogueStep.md), [WorldMap_InitLocations](WorldMap_InitLocations.md)
- Reads tables: [RecordBlockSectors](../tables/RecordBlockSectors.md)

## Notes

Read in full (one small function).

## Open questions

?: what the blocks contain.
