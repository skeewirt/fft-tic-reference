# Battle_MoveRange_CeilingAbove

- **Address:** `0x14027C348`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `uint8 Battle_MoveRange_CeilingAbove(int x, int y, uint8 edgeShift, uint8 above)`
- **Callers:** Battle_MoveRange_CheckSource, Battle_MoveRange_CheckStep, sub_14027D0FC, sub_14027D2F8
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The lowest underside, over both map layers of one column, that lies above a given height on one edge; 127 when there is none.

## Behavior

- V: for layer 0 and layer 1 of (x, y), skipping records with byte +6 bit 0x01: underside = 2 * (height - thickness) + slope * ((corner byte >> edgeShift) & 3), thickness = tile byte +5 low 5 bits; keeps the smallest value above the given height.
- I: this is the bridge rule: a unit under a layer-1 tile needs its body to fit below that tile's underside, and a unit on it has nothing above.

## State touched

- Reads: [g_BattleTileTable](../globals/g_BattleTileTable.md), [BattleTileRecord.flags5](../structs/BattleTileRecord.md#flags5), [BattleTileRecord.corners](../structs/BattleTileRecord.md#corners)

## Referenced by

- Called by: [Battle_MoveRange_CheckSource](Battle_MoveRange_CheckSource.md), [Battle_MoveRange_CheckStep](Battle_MoveRange_CheckStep.md)
- Observed behaviours: [MoveRangeRules](../behaviors/MoveRangeRules.md)

## Open questions

? Not exercised by the captures: both maps have every layer-1 record flagged unusable (byte +6 = 1) and thickness 0.
