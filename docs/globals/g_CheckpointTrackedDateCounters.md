# g_CheckpointTrackedDateCounters

- **Kind:** global
- **Address:** `0x142E808DC`
- **Type:** `event system`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

uint8[64]: the checkpoint buffer's copy of the tracked date counters, written by the checkpoint writer (sub_1402CEEE8, four 16-byte stores from g_TrackedDateCounters) and read back by the checkpoint reader (sub_1402CF768, four 16-byte stores into g_TrackedDateCounters).

## Open questions

None recorded.
