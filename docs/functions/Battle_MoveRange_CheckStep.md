# Battle_MoveRange_CheckStep

- **Address:** `0x14027BD0C`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int Battle_MoveRange_CheckStep(int variant, int extraCost)`
- **Callers:** Battle_MoveRange_Expand, Battle_MoveRange_ExpandJump
- **Callees:** Battle_MoveRange_CeilingAbove, Battle_MoveRange_CheckMount

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Tests one target of a step or jump (variant bit 0 = map layer, variant >= 2 = onto the unit standing there) and, when the unit can get there with a better budget, stores the budget and flags the tile as frontier.

## Behavior

- V: ground variants need tile flag 0x10 (standable); unit variants need 0x28, take the unit's top as the height, call Battle_MoveRange_CheckMount when the flag has 0x20 and then stop unless it has 0x08.
- V: ground: enter height = height * 2 + slope * corner value of the edge entered; the far edge the same with the other shift; a positive rise far - enter on a tile with flag 0x40 is refused (no walking up a steep tile).
- V: headroom: refused when the lowest underside above the enter height (Battle_MoveRange_CeilingAbove on the target) is below exit height + body, when the source headroom is below enter height + body, or when the target one is below enter height + body. Body = scratch byte 0x14188261B (6 half-steps, 4 as Toad or Chicken, 8 with the float ability, +2 per rider).
- V: ground: the compared level is enter height + 2 * the target's depth. Level <= exit height is a drop of exit - level; a higher level is a climb and is refused when extraCost is not 0 (no jumping upward across a gap).
- V: refused when the drop or climb is above 2 * Jump (scratch byte 0x141882602).
- V: budget left = source budget - terrain cost of the target (g_MoveTerrainCost by tile byte +0 low 6 bits) - extraCost; unit variants use cost 1. Refused when below 1, when below the target's stored budget, or when equal and the path's largest climb (kept in mark byte 4; 0 in Fly mode) is not smaller.
- V: stores budget and climb byte; when the budget is above 1 sets tile flag 0x01 and raises the pending byte.
- V: return codes 1..17 name the refusing test; 0 = stored.

## State touched

- Calls: [Battle_MoveRange_CeilingAbove](Battle_MoveRange_CeilingAbove.md), [Battle_MoveRange_CheckMount](Battle_MoveRange_CheckMount.md)
- Reads: [g_MoveTileFlags](../globals/g_MoveTileFlags.md), [g_MoveTerrainCost](../globals/g_MoveTerrainCost.md), [g_MoveBlockers](../globals/g_MoveBlockers.md), [MoveRangeScratch.body](../structs/MoveRangeScratch.md#body), [MoveRangeScratch.jump_limit](../structs/MoveRangeScratch.md#jump_limit), [BattleTileRecord.surface](../structs/BattleTileRecord.md#surface)
- Writes: [g_BattleRangeMarks](../globals/g_BattleRangeMarks.md), [g_MoveTileFlags](../globals/g_MoveTileFlags.md)

## Referenced by

- Called by: [Battle_MoveRange_Expand](Battle_MoveRange_Expand.md), [Battle_MoveRange_ExpandJump](Battle_MoveRange_ExpandJump.md)
- Observed behaviours: [MoveRangeRules](../behaviors/MoveRangeRules.md)

## Notes

A terrain cost of 0xFF makes the budget negative, which is how forbidden terrain is refused. Captures: height limit exact to the half-step on both sides, water cost 2, extra cost per jumped tile, no upward jump, enemies block (no 0x10 on their tiles), allies passable.

## Open questions

? The depth is added to the target but to the source only with a water ability; not exercised by the captures (their water is depth 1 next to depth 1 or out of reach).
