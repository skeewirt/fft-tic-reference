# UnitStatusNumbersMode0

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1408E5050`
- **Rows:** 10 rows of 32 bytes
- **Keyed by:** number field
- **Read by:** [MessageWindow_OpenMode0](../functions/MessageWindow_OpenMode0.md)
- **Row layout:** [UiNumberField](../structs/UiNumberField.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Number fields of the legacy unit info message window, actor with level and experience. Verdict: designer-data.

## Behavior

- V: MessageWindow_OpenMode0 passes the table and the actor preview buffer (0x14078DE10) to the panel window builder
- V: labels hp, hpmax, mp, mpmax, wt, wtmax, at, atmax, level, exp

## Notes

Our names. Tags: V.

## Open questions

None recorded.
