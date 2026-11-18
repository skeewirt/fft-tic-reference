# MessageWindow_OpenMode2

- **Address:** `0x1402E0C2C`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `__int64 MessageWindow_OpenMode2(void)`
- **Callers:** not recorded
- **Callees:** sub_1402BA718, sub_1402DF374

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Opens the legacy unit info message window for the target unit with the hit chance (mode 2).

## Behavior

- V: starts task slot 12 (sub_1402BA718) when that slot does not carry tag 19, waits two frames, refreshes the preview buffers and clamps the predicted values against the action result block, writing them into the window widgets.
- V: calls the panel window builder with mode 2, the eight-row number table 0x1408E53D0 and the target preview buffer 0x14078DE70.

## State touched

- Calls: [sub_1402DF374](sub_1402DF374.md)

## Referenced by

- Reads tables: [UnitStatusNumbersMode2](../tables/UnitStatusNumbersMode2.md)

## Notes

Read in full; the clamp arithmetic is only summarised.

## Open questions

None recorded.
