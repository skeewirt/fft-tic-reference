# StatusPanelPaletteIds

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1408081B0`
- **Rows:** 22 rows of 2 bytes
- **Keyed by:** panel part
- **Row layout:** [PaletteIdWord](../structs/PaletteIdWord.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Palette ids of the battle status panel parts. Verdict: designer-data.

## Behavior

- V: 0x2C bytes to the next symbol
- V: Battle_UnitStatusFillAlt: reads words at +0 and at +0x10 + 2 x part

## Notes

Our names. Tags: V reader, I meaning.

## Open questions

- ?: which part takes which
