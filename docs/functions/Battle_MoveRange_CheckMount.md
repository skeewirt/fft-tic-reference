# Battle_MoveRange_CheckMount

- **Address:** `0x14027C218`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void Battle_MoveRange_CheckMount(uint8 blockerIndex, int extraCost)`
- **Callers:** Battle_MoveRange_CheckStep
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

For a target tile holding a mountable ally: records in the tile's mark byte 3 the budget with which the unit could get onto the mount.

## Behavior

- V: nothing unless the target headroom is at least exit height + body and the budget left (source budget - extraCost - 1) is non-zero and not below the source's mark byte 3.
- V: scans heights from max(the mount's base, the target's enter height + 2 * depth) up to base + the mount's body: stops when either headroom is below height + body; a height above the exit height needs extraCost 0 and a climb within 2 * Jump; a height at or below needs a drop within 2 * Jump. The first height that passes stores the budget into mark byte 3 when larger.

## State touched

- Reads: [g_MoveBlockers](../globals/g_MoveBlockers.md), [MoveRangeScratch.body](../structs/MoveRangeScratch.md#body)
- Writes: [g_BattleRangeMarks](../globals/g_BattleRangeMarks.md)

## Referenced by

- Called by: [Battle_MoveRange_CheckStep](Battle_MoveRange_CheckStep.md)

## Notes

Battle_MoveRange_Commit lights a tile with mark byte 3 set when the acting unit can ride.

## Open questions

? Not covered by a capture (no chocobo ally).
