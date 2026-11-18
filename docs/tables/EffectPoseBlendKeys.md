# EffectPoseBlendKeys

- **Kind:** table
- **Area:** [Graphics](../areas/graphics.md)
- **Storage:** Executable
- **Address:** `0x1407238B0`
- **Rows:** 10 blocks of 16 bytes
- **Keyed by:** block 0..9
- **Row layout:** [FixedRampBlockRow](../structs/FixedRampBlockRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Ten blocks of 16-bit fixed point (4096 = 1.0) ramp values copied by a sprite effect update. Verdict: engine-data.

## Behavior

- V: the update copies the blocks into local arrays before using them as key values

## Notes

Our names. Tags: V copy, I meaning.

## Open questions

- ?: what the ramps scale
