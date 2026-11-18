# EventUnitNumbersA

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1408EACF0`
- **Rows:** 10 rows of 32 bytes
- **Keyed by:** number field
- **Read by:** [sub_1402F8684](../functions/sub_1402F8684.md)
- **Row layout:** [UiNumberField](../structs/UiNumberField.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Number fields (hp, hpmax, mp, mpmax, wt, wtmax, at, atmax, level, exp) of the legacy dialogue unit panel, first unit. Verdict: designer-data.

## Behavior

- V: one reader draws each number from its value pointer (the event unit preview words around 0x1407B071C)

## Notes

Our names. Tags: V.

## Open questions

None recorded.
