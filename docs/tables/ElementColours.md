# ElementColours

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** Executable
- **Address:** `0x140683048`
- **Rows:** 9 rows of 3 bytes
- **Keyed by:** element slot 0..8
- **Read by:** [EffectFlash_Start](../functions/EffectFlash_Start.md)
- **Row layout:** [ElementColoursRow](../structs/ElementColoursRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

RGB tint per element for effect flashes. The element bit order that selects a row is the companion table ElementMaskOrder. Verdict: designer-data.

## Behavior

- V: EffectFlash_Start reads three bytes at 3 * slot and scales each by a blend weight from EffectBlendWeights
- I: slot 0 is no element (grey), then fire, water, earth, wind, holy, dark, ice, lightning in the order of ElementMaskOrder

## Notes

Our names. Tags: V layout, V reader, I element assignment from the colours.

## Open questions

None recorded.
