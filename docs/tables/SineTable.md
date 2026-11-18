# SineTable

- **Kind:** table
- **Area:** [Math](../areas/math.md)
- **Storage:** Executable
- **Address:** `0x14067A000`
- **Rows:** 4097 rows of 4 bytes
- **Keyed by:** angle 0..4095 (4096 per turn)
- **Row layout:** [TrigSample](../structs/TrigSample.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Shared sine lookup, same layout as the cosine table; 4097 samples and 8 bytes of padding up to the next object. Verdict: engine-data.

## Behavior

- V: seen: entry 0 = 0, entry 1024 = 4096, entry 3072 = -4096, entry 4096 = 0; 26 functions read it
- V: sub_14024E88C and 25 other functions: with the cosine table rotate a point; a zero result is replaced by 4096 before a divide in the unit sprite quad builder

## Notes

Our names. Tags: V layout, V meaning.

## Open questions

None recorded.
