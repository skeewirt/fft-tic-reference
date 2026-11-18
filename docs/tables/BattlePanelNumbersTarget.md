# BattlePanelNumbersTarget

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1408F72F0`
- **Rows:** 10 rows of 32 bytes
- **Keyed by:** number field 0..9
- **Read by:** [sub_140338A28](../functions/sub_140338A28.md)
- **Row layout:** [UiNumberField](../structs/UiNumberField.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Number fields of the battle unit panel, target side. Verdict: designer-data.

## Behavior

- V: sub_140338A28 (battle unit panel task): the same ten fields for the second unit of the panel
- V: ten records of 32 bytes (0x140); value pointers differ from the actor table

## Notes

Our names. Tags: V layout.

## Open questions

None recorded.
