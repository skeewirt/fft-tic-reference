# g_MoveTerrainCost

- **Kind:** global
- **Address:** `0x141882700`
- **Area:** [Battle](../areas/battle.md)
- **Type:** `uint8[64]`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Movement cost per terrain type for the unit being built (0xFF = cannot enter), copied by Battle_MoveRangeSetup from one of the six sets of g_MoveTerrainCostSets and adjusted for weather and abilities.

## Referenced by

- Described by tables: [MoveTerrainCost](../tables/MoveTerrainCost.md)
- Read by: [Battle_MoveRange_CheckStep](../functions/Battle_MoveRange_CheckStep.md)
- Written by: [Battle_MoveRangeSetup](../functions/Battle_MoveRangeSetup.md)

## Open questions

None recorded.
