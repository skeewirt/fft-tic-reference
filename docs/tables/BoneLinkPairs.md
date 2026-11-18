# BoneLinkPairs

- **Kind:** table
- **Area:** [Graphics](../areas/graphics.md)
- **Storage:** Executable
- **Address:** `0x140720080`
- **Rows:** 33 rows of 16 bytes
- **Keyed by:** pair index 0..32
- **Read by:** [ModelSkeleton_BuildBoneLinks](../functions/ModelSkeleton_BuildBoneLinks.md)
- **Row layout:** [BoneLinkPairsRow](../structs/BoneLinkPairsRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The 33 bone name pairs that define the chains of a model skeleton (spine, neck, head, arms, hands, fingers, legs, toes, jaw, face, nose flap, forearm and shin extension bones, waist, tail segments). Verdict: engine-data.

## Behavior

- V: the builder compares every bone name of a loaded model with both names of all 33 pairs and keeps the bone indices; a pair becomes a link record only when both bones exist on the model
- V: the link record gets a flag byte that is set when the model bone name contains "spine"
- I: the sweep run of 344 pointers goes on behind slot 65 into 20 vtables of graphics classes; they are not part of this table

## Notes

Our names. Tags: V layout, V reader, I purpose.

## Open questions

- ?: what the link list is used for after it is built
- ?: meaning of the flag byte
