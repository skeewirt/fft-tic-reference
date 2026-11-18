# PopupBounceCurve

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** Executable
- **Address:** `0x1406725F0`
- **Rows:** 13 rows of 2 bytes
- **Keyed by:** animation frame 0..12
- **Row layout:** [PopupBounceStep](../structs/PopupBounceStep.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Arc of offsets for a bouncing pop-up over 13 frames. Verdict: engine-data.

## Behavior

- V: 13 symmetric values, then a 0 pair; frame 11 resets to 0 in sub_14022A19C
- V: Battle_UnitStatusFillAlt and sub_14022A19C: add table[frame] (plus 0xF0 in one mode) to a primitive word

## Notes

Our names. Tags: V layout, I meaning.

## Open questions

- ?: whether the value is a y position or a texture v offset
