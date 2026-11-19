# UnitWork_BuildFromGuestOrPartyRecord

- **Address:** `0x1402766C8`
- **Area:** [Unit data](../areas/unit-data.md)
- **Prototype:** `int UnitWork_BuildFromGuestOrPartyRecord(uint8_t *work, const uint8_t *entry)`
- **Callers:** Unit_ApplySpawnRecord
- **Callees:** sub_1402752E0, UnitWork_BuildFromSaveIndex

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Finds the save record a spawn entry names and builds the work record from it.

## Behavior

- V: entry +1 bit 3 set: searches the save records 50..53 (the guest range of g_UnitSaveData) for a used record (+1 not 0xFF) whose byte +0 equals entry +0; otherwise sub_1402752E0(entry +0) picks the index.
- V: returns -1 when no record is found; else calls UnitWork_BuildFromSaveIndex(work, index, dword_1437414A0), sets work +6 = (work +6 & 0xEE) | (entry +1 & 0x11), work +5 and work +494 = entry +24, and returns 0.

## State touched

- Reads: [g_UnitSaveData](../globals/g_UnitSaveData.md)

## Referenced by

- Called by: [Unit_ApplySpawnRecord](Unit_ApplySpawnRecord.md)

## Open questions

? what dword_1437414A0 selects.
