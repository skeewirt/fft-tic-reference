# EffectPaletteSeeds

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** Executable
- **Address:** `0x1406830A0`
- **Rows:** 6 rows of 3 bytes
- **Keyed by:** seed 0..5
- **Read by:** [EffectPalette_Step](../functions/EffectPalette_Step.md)
- **Row layout:** [EffectPaletteSeedsRow](../structs/EffectPaletteSeedsRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Six 5-bit RGB colours packed into the effect palette at the start of the palette effect. Verdict: designer-data.

## Behavior

- V: EffectPalette_Step packs the triples into 15-bit colours and writes them to the live palette twice (12 words)

## Notes

Our names. Tags: V layout, V reader.

## Open questions

None recorded.
