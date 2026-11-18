# g_BattleMapId

- **Kind:** global
- **Address:** `0x140D3A838`
- **Area:** [Battle](../areas/battle.md)
- **Type:** `int`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

32-bit battle map id: set from scene variable 51 or from the signed event words 0x140D40924 / 0x140D40928, passed to the map task (BattleLoad_StepFresh, the load task) and copied whole by the battle capture; the battle save header keeps only its low byte

## Open questions

None recorded.
