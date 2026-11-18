# UnitStatusNumbersMode1

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1408E52D0`
- **Rows:** 8 rows of 32 bytes
- **Keyed by:** number field
- **Read by:** [MessageWindow_OpenMode1](../functions/MessageWindow_OpenMode1.md)
- **Row layout:** [UiNumberField](../structs/UiNumberField.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Number fields of the legacy unit info message window, actor with hit chance. Verdict: designer-data.

## Behavior

- V: the opener passes the table and the actor preview buffer
- V: labels hp, hpmax, mp, mpmax, wt, wtmax, pt, hit

## Notes

Our names. Tags: V.

## Open questions

None recorded.
