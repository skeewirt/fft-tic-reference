# MessageWindow_OpenMode3

- **Address:** `0x1402E098C`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `__int64 MessageWindow_OpenMode3(void)`
- **Callers:** not recorded
- **Callees:** sub_1402DE564, sub_1402DF374

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Opens the legacy unit info message window for the target unit with level and experience (mode 3).

## Behavior

- V: refreshes the preview buffers, sets the same window flag word as mode 0 and calls the panel window builder with mode 3, the ten-row number table 0x1408E5190 and the target preview buffer 0x14078DE70.

## State touched

- Calls: [sub_1402DE564](sub_1402DE564.md), [sub_1402DF374](sub_1402DF374.md)

## Referenced by

- Reads tables: [UnitStatusNumbersMode3](../tables/UnitStatusNumbersMode3.md)

## Notes

Read in full.

## Open questions

None recorded.
