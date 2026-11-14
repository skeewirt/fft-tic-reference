# MoveTerrainCostSets

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** Executable (constant)
- **Rows:** 6 rows of 64 entries of 1 byte
- **Held in:** [g_MoveTerrainCostSets](../globals/g_MoveTerrainCostSets.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Six constant cost sets by terrain type: walking, open (Fly / Teleport), float, water (two modes), one more water mode, lava walking. 0 = the weather cost, 0xFF = cannot enter.

## Open questions

None recorded.
