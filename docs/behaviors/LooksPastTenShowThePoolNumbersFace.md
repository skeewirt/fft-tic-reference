# LooksPastTenShowThePoolNumbersFace

- **Kind:** observed behaviour
- **Scope:** engine (battle portraits)
- **Area:** [Graphics](../areas/graphics.md)
- **Affects:** [TurnPanel_SetUnitPanel](../functions/TurnPanel_SetUnitPanel.md), [TurnPanel_SetTag](../functions/TurnPanel_SetTag.md), [sub_140214134](../functions/sub_140214134.md), [g_LookPoolFaceValue](../globals/g_LookPoolFaceValue.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A battle unit whose look took pool record 10 or higher shows the portrait of the sprite whose id equals its pool number, not its own: the face reads keep the pool number when it is 10 or more and pass it on as the face value.

## Behavior

- V: TurnPanel_SetUnitPanel takes the pool index from sub_14022AA88 into edi, tests it against 10 (0x14021508D) and only below 10 replaces it with g_LookPoolFaceValue[pool]; so a pool of 10 or more goes on as the face value itself; sub_14021FA50 does the same (the pool index, or the unit field, when the read is skipped).
- V (seen live 2026-11-20, random battle at Mandalia Plain, 11 enemy looks): the enemy of pool 10 (a Dryad, sprite 144) showed a young man's portrait in the unit panel and the Combat Timeline, and Ramza in pool 11 showed an old bearded man's portrait instead of his own; g_LookPoolFaceValue read 134..143 for pools 0..9, and the dword after it (dword_1437A5A08) read 144, pool 10's sprite, written over it.
- I: so a fix that only moves the table leaves these units on the faces of sprites 10 and up; the ten `< 10` tests must follow the new size.
- V (tested 2026-11-21, same 11-look battle, Ramza in pool 11): with the ten immediates raised from 10 to 12 in memory, the Dryad (pool 10) showed its own portrait in the unit panel and the Combat Timeline, and Ramza (pool 11) his own in his panel (face values read 144 and 1, already written past the table by the stock writer); dword_1437A5A08 had no write for 5 s and over an enemy phase.
- V: the queue (g_LookQueueCount, 0x141856720) is 0x208 bytes: the count at +0 and 16 entries of 32 bytes from +8; the next global, dword_141856928, follows at once. 35 instructions address it (LookQueue_Add 13, CharaPalette_ReloadForShape 14, the capture copy and restore of 0x208 bytes, and five stores or clears of the count); 18 other instructions have an operand in the same range that is not the queue: the end pointer of a loop over the 21 battle unit records (the table + 21 x 0x200 + a field).

## Open questions

None recorded.
