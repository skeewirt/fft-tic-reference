# EventPoseCodeFlags

- **Kind:** table
- **Area:** [Event system](../areas/event-system.md)
- **Storage:** Executable
- **Address:** `0x140682991`
- **Rows:** 83 rows of 1 bytes
- **Keyed by:** event pose code
- **Row layout:** [PoseCodeFlag](../structs/PoseCodeFlag.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Small per-code values read by an event unit block step. Verdict: engine-data.

## Behavior

- V: sub_140300D74 reads byte [code] for codes 63..82 (0x53 and above map to entry 63): only entries 63..82 are read, entries 0..62 are never read
- V: the chosen value is split by 60 into a quotient and a remainder for the frame timing
- I: 83 bytes up to g_StatusGuestMask

## Notes

Our names. Tags: V reader, I meaning.

## Open questions

- ?: meaning of the value
