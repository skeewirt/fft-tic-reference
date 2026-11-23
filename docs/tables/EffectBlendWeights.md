# EffectBlendWeights

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** Executable
- **Address:** `0x14071E7C0`
- **Rows:** 5 rows of 7 bytes
- **Keyed by:** blend row 0..4
- **Read by:** [EffectFlash_Start](../functions/EffectFlash_Start.md)
- **Row layout:** [EffectBlendWeightsRow](../structs/EffectBlendWeightsRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Four ramps of seven 0..255 blend weights for the flash effect and a fifth row listing five palette slots. Verdict: designer-data.

## Behavior

- V: the flash multiplies each colour channel by weight * element colour >> 8
- V: row 4 (10, 11, 12, 13, 14, 0, 0) is read at offset 28 by the palette routine EffectSequence_SpawnGroup3Cluster

## Notes

Our names. Tags: V layout, V reader.

## Open questions

None recorded.
