# JobCommandTable_GetRow

- **Address:** `0x1400F84F4`
- **Area:** [Job data](../areas/job-data.md)
- **Prototype:** `char *JobCommandTable_GetRow(unsigned int commandId)`
- **Callers:** sub_1400F7334, sub_1400FB8E4, sub_1400FBF9C, sub_140109134, sub_140109F0C, sub_140113F40, sub_140129260, sub_14012F138, sub_1401560D0, sub_140214FB4, sub_1402A20A4, sub_1402A9220
- **Callees:** sub_1403D325C, sub_1403D3AE8, sub_1403D2FD8

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the JobCommand-en row (table 41, cache qword_143CDA2E0).

## Behavior

- V: row +4 icon (drawn only when 1..24, sub_1400FBF9C), +8 Name, +20 group number (sub_1400F7334 compares), +28 flag, +32 extra_text (sub_140129260).

## Referenced by

- Called by: [JobCommand_SameGroup](JobCommand_SameGroup.md), [TurnPanel_SetUnitPanel](TurnPanel_SetUnitPanel.md), [sub_1401560D0](sub_1401560D0.md), [sub_1402A20A4](sub_1402A20A4.md)
- Observed behaviours: [SkillsetIdsPastTheByte](../behaviors/SkillsetIdsPastTheByte.md), [SkillsetNamesAndHelpAreKeyedBySetId](../behaviors/SkillsetNamesAndHelpAreKeyedBySetId.md)
- Reads tables: [JobCommand](../tables/JobCommand.md)

## Notes

The command's ability list is not in this row (nor in any nxd table).

## Open questions

Where the skillset membership lives.
