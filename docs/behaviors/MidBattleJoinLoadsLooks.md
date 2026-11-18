# MidBattleJoinLoadsLooks

- **Kind:** observed behaviour
- **Scope:** engine (battle join)
- **Area:** [Graphics](../areas/graphics.md)
- **Affects:** [Battle_JoinUnitAndLoad](../functions/Battle_JoinUnitAndLoad.md), [CharaPalette_ReloadForShape](../functions/CharaPalette_ReloadForShape.md), [g_LookLoaderState](../globals/g_LookLoaderState.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A unit that joins mid-battle is queued by Battle_AddJoinedUnit and loaded by running the look loader once per frame until it returns 0; the loader's file reads are synchronous.

## Behavior

- V: the loader's step machine (g_LookLoaderState: pass, step, entry index; buffer 0x140CE3250) returns 0 once the entry index reaches g_LookQueueCount, 1 or 2 otherwise; its files are read with GameData_ReadSectors, which is synchronous (MemFile_Read clears the pending flag the high dword of qword_141856AB0 itself).
- V: load step 2 stores a queue word above 170 back as 1 (stock clamp) and tests the word against byte +1 of all 15 look pool records, claimed or not (the loop over 0x140D005A1 in steps of 0x32D6); when one matches it reads no classic file, and the scene unit is built from whatever data the record its build uses holds.

## Open questions

None recorded.
