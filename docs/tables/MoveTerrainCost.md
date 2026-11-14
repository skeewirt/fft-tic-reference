# MoveTerrainCost

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** Executable (filled at run time)
- **Rows:** 64 entries of 1 byte
- **Held in:** [g_MoveTerrainCost](../globals/g_MoveTerrainCost.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Movement cost per terrain type for the unit being built (0xFF = cannot enter), copied by Battle_MoveRangeSetup from one of the six sets of g_MoveTerrainCostSets and adjusted for weather and abilities.

## Open questions

None recorded.
