# LookPool_ClaimForSprite

- **Address:** `0x140268FF4`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `uint16_t LookPool_ClaimForSprite(int16_t sprite)`
- **Callers:** sub_14026EB74, sub_14026A048
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Finds or claims the look pool record for a sprite number and returns its index, or 0xFFFF when all 15 records are in use.

## Behavior

- V: walks the 15 records of 0x32D6 bytes at 0x140D005A0 and returns the index of the first one whose byte +1 equals the argument, after storing the low byte of the argument into its byte +0.
- V: when none matches it takes the first record whose byte +0 is zero, stores the low byte of the argument in +0 and +1 and returns its index.
- V: returns 0xFFFF when no record is free.

## Referenced by

- Called by: [sub_14026EB74](sub_14026EB74.md)
- Observed behaviours: [LookPoolOfFifteenIsWiredIntoFixedSlots](../behaviors/LookPoolOfFifteenIsWiredIntoFixedSlots.md), [LookSlotsAlreadyInTheGame](../behaviors/LookSlotsAlreadyInTheGame.md), [PoolRecordKeepsItsSpriteAcrossTheReset](../behaviors/PoolRecordKeepsItsSpriteAcrossTheReset.md)

## Notes

Structure: LookPoolRecord. Both stores and the comparison are single bytes. The name is ours (IDB: sub_140268FF4).

## Open questions

? the purpose of the second caller sub_14026A048.
