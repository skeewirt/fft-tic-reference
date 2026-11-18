# g_BattleCaptureTrackedDateCounters

- **Kind:** global
- **Address:** `0x1408B885C`
- **Type:** `event system`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

uint8[64]: the battle capture buffer's copy of the tracked date counters (capture buffer 0x1408B8588 + 0x2D4): written by the errand-state copy (SaveWork_CopyErrandState, direction 0, called by Battle_SaveCapture), read back by the same function in direction 1 (Battle_RestoreCapture).

## Open questions

None recorded.
