# StatusPanelFrameLines

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** Executable
- **Address:** `0x140672450`
- **Rows:** 8 rows of 7 bytes
- **Keyed by:** line index 0..7
- **Row layout:** [StatusPanelFrameLine](../structs/StatusPanelFrameLine.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Eight one-pixel shaded border lines of the battle status panel (light and dark pairs). Verdict: designer-data.

## Behavior

- V: loop of 8 x 7 bytes in the reader; a text string follows at +0x38
- V: sub_14022AFEC (unit equipment / ability status panel constructor): writes eight flat-colour rectangle primitives from the rows

## Notes

Our names. Tags: V layout, I purpose.

## Open questions

- ?: whether the HD build still draws this legacy panel
