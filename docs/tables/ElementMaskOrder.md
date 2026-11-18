# ElementMaskOrder

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** Executable
- **Address:** `0x140683068`
- **Rows:** 9 rows of 1 byte
- **Keyed by:** element slot 0..8
- **Read by:** [EffectFlash_Start](../functions/EffectFlash_Start.md)
- **Row layout:** [ElementMaskOrderRow](../structs/ElementMaskOrderRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The element bit mask of each element slot of ElementColours: 0 (none), then the bits 0x80, 0x04, 0x08, 0x10, 0x02, 0x01, 0x20, 0x40. Verdict: engine-data.

## Behavior

- V: EffectFlash_Start tests the effect element mask against each entry in order and uses the position of the first match as the colour slot

## Notes

Our names. Companion of ElementColours (found beside the table at 0x140683048); tags V layout, V meaning.

## Open questions

None recorded.
