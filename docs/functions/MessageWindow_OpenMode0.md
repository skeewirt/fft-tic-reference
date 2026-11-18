# MessageWindow_OpenMode0

- **Address:** `0x1402E092C`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `__int64 MessageWindow_OpenMode0(void)`
- **Callers:** not recorded
- **Callees:** sub_1402DE564, sub_1402DF374

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Opens the legacy unit info message window for the acting unit with level and experience (mode 0).

## Behavior

- V: refreshes the preview buffers (sub_1402DE564), sets a window flag word to 2 (3072 when a flag in the status page word is set) and clears two scene words.
- V: calls the panel window builder with the actor window record, mode 0, the ten-row number table 0x1408E5050 and the actor preview buffer 0x14078DE10.

## State touched

- Calls: [sub_1402DE564](sub_1402DE564.md), [sub_1402DF374](sub_1402DF374.md)

## Referenced by

- Reads tables: [UnitStatusNumbersMode0](../tables/UnitStatusNumbersMode0.md)

## Notes

Read in full.

## Open questions

None recorded.
