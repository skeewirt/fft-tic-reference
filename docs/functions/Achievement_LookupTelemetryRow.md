# Achievement_LookupTelemetryRow

- **Address:** `0x1400DEFAC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void Achievement_LookupTelemetryRow(void *achievement, ...)`
- **Callers:** not recorded
- **Callees:** NxdTable_GetRowById

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Looks up an achievement's telemetry row (part read).

## Behavior

- V: looks up the row of the TelemetryAchievement-en table (173, cached at qword_143CDA0B0) by Achievement telemetry_achievement (+4) and reads its +0x1C, string +0x2C, +0x38 and bytes +0x3C / +0x3D.

## State touched

- Calls: [NxdTable_GetRowById](NxdTable_GetRowById.md)

## Referenced by

- Observed behaviours: [AchievementClassesMatchByColumn](../behaviors/AchievementClassesMatchByColumn.md)

## Open questions

? what the function does with the telemetry row's fields.
