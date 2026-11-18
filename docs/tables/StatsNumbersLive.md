# StatsNumbersLive

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1408E5A90`
- **Rows:** 8 rows of 32 bytes
- **Keyed by:** number field
- **Read by:** [StatsScreen_Task](../functions/StatsScreen_Task.md)
- **Row layout:** [UiNumberField](../structs/UiNumberField.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Eight stat number fields (At, Atmagic, Def, Defmgc, Ar, Armagic, Av, Avmagic) of a legacy screen. Verdict: designer-data.

## Behavior

- V: the screen task draws the eight numbers with a digit routine into a VRAM strip
- V: only the value pointers differ from exe.ui.stats_panel_numbers

## Notes

Our names. Tags: V.

## Open questions

None recorded.
