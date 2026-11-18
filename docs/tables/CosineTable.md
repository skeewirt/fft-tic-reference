# CosineTable

- **Kind:** table
- **Area:** [Math](../areas/math.md)
- **Storage:** Executable
- **Address:** `0x140675FF0`
- **Rows:** 4097 rows of 4 bytes
- **Keyed by:** angle 0..4095 (4096 per turn)
- **Row layout:** [TrigSample](../structs/TrigSample.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Shared cosine lookup: 4097 signed 32-bit samples (the last repeats the first so an interpolation can read index + 1), then 12 bytes of padding up to the sine table. Verdict: engine-data.

## Behavior

- V: seen: entry 0 = 4096, entry 1024 = 0, entry 2048 = -4096, entry 4096 = 4096; 27 functions read it
- V: sub_140380FB8 (unit sprite quad builder) and the battle camera functions sub_1401F8A7C / sub_1401F8D90: index = angle & 0xFFF, product shifted right by 12
- V: about 25 more functions (legacy menu 3D layout, map transforms) read it the same way

## Notes

Our names. Tags: V layout, V meaning.

## Open questions

- ?: whether the 12 padding bytes are read by anything
