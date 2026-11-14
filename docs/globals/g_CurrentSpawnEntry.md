# g_CurrentSpawnEntry

- **Kind:** global
- **Address:** `0x1411A3868`
- **Area:** [Unit data](../areas/unit-data.md)
- **Type:** `unit data`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Pointer to the spawn entry being built: set by Battle_PlaceEntryUnits and sub_1402841D0 before each Unit_BuildFromRecord; Unit_ApplySpawnRecord copies its bytes +33..+39 into unit +407..+413, and Battle_PlaceEntryUnits reads bytes +25..+32 back after the build

## Referenced by

- Written by: [Battle_PlaceEntryUnits](../functions/Battle_PlaceEntryUnits.md)

## Open questions

None recorded.
