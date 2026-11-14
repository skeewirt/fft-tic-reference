# g_MoveTerrainCostSets

- **Kind:** global
- **Address:** `0x14067F5B0`
- **Area:** [Battle](../areas/battle.md)
- **Type:** `uint8[6][64]`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Six constant cost sets by terrain type: walking, open (Fly / Teleport), float, water (two modes), one more water mode, lava walking. 0 = the weather cost, 0xFF = cannot enter.

## Referenced by

- Described by tables: [MoveTerrainCostSets](../tables/MoveTerrainCostSets.md)
- Read by: [Battle_MoveRangeSetup](../functions/Battle_MoveRangeSetup.md)

## Open questions

None recorded.
