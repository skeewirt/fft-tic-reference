# EquipPanelPaletteCycle

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1408095D0`
- **Rows:** 19 rows of 4 bytes
- **Keyed by:** panel cell 0..18, phase 0/1
- **Row layout:** [PaletteCyclePair](../structs/PaletteCyclePair.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Two-phase palette ids of the 19 equipment panel cells (a blinking highlight). Verdict: designer-data.

## Behavior

- V: 19 cells x 2 words read with stride 4 (0x4C of the 0x52 bytes to the next symbol)
- V: sub_14022AFEC: each frame copies the 19 palette ids of the current phase (scene task value) into the cells

## Notes

Our names. Tags: V layout, I purpose.

## Open questions

- ?: what the blink marks
