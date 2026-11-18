# BattlePanelNumbersActor

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1408F71B0`
- **Rows:** 10 rows of 32 bytes
- **Keyed by:** number field 0..9
- **Read by:** [sub_140338A28](../functions/sub_140338A28.md)
- **Row layout:** [UiNumberField](../structs/UiNumberField.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Number fields of the battle unit panel, actor side (HP and MP with maxima, Wt, At, level, experience). Verdict: designer-data.

## Behavior

- V: sub_140338A28 (battle unit panel task): ten fields (hp, hpmax, mp, mpmax, wt, wtmax, at, atmax, level, exp) of the acting unit's panel
- V: ten records of 32 bytes (0x140) with readable tags; the twin table for the other side is at 0x1408F72F0

## Notes

Our names. Tags: V layout.

## Open questions

None recorded.
