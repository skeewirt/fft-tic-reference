# g_PoolFrameBuffers

- **Kind:** global
- **Address:** `0x1411A3788`
- **Type:** `void *[8]`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Frame buffer pointers of the look pool records from 9 up: sub_14026E838 stores 0x1437ADF4C + (pool - 7) * 0x8000 at entry pool - 7 (entries 2..7 for pools 9..14) and the 4 KB block base 0x1437B5F4C at entry 1 (qword_1411A3790); read by sub_14025ED60; dword_1411A37C8 follows at entry 8.

## Referenced by

- Observed behaviours: [ClassicLookDataHasEightBufferPlaces](../behaviors/ClassicLookDataHasEightBufferPlaces.md), [LookPoolOfFifteenIsWiredIntoFixedSlots](../behaviors/LookPoolOfFifteenIsWiredIntoFixedSlots.md)
- Written by: [sub_14026E838](../functions/sub_14026E838.md)

## Open questions

None recorded.
