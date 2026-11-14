# ResourceHandle_LoadNow

- **Address:** `0x14009627C`
- **Area:** [Resource](../areas/resource.md)
- **Prototype:** `int ResourceHandle_LoadNow(ResourceHandle *h)`
- **Callers:** Resource_AcquireHandle (the file-open path), sub_1400915C0, sub_1400919A8, sub_140091D64, sub_140093610
- **Callees:** sub_140096328, vtable slots 7, 8, 13, ResourceHandle_FinishLoad

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Drives one handle's load to the end: steps the read until state 3, calls the loaded callback (slot 8), records the status, calls the ready callback (slot 13) and finishes.

## Behavior

- V: sub_140096328 creates the reader when missing and moves state 0 to 2; flag 0x800 is set.
- V: loops vtable +56 (read step) until state (+84) is 3, then calls vtable +64 (slot 8: NxdHandle_OnLoaded for nxd handles); a negative step result ends the loop with that error in +76.
- V: +80 = 1 on success, 2 on failure; then vtable +104 (slot 13: NxdHandle_OnReady) and ResourceHandle_FinishLoad(h, result).

## State touched

- Calls: [ResourceHandle_FinishLoad](ResourceHandle_FinishLoad.md), [ResourceHandle_ReadData](ResourceHandle_ReadData.md), [NxdHandle_OnLoaded](NxdHandle_OnLoaded.md), [NxdHandle_OnReady](NxdHandle_OnReady.md)

## Referenced by

- Called by: [Resource_AcquireHandle](Resource_AcquireHandle.md)

## Notes

The order that matters: the buffer is complete when slot 8 runs, and the rows are bound inside slot 8, before the table is marked ready in slot 13.

## Open questions

None recorded.
