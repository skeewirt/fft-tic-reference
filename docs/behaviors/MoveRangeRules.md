# MoveRangeRules

- **Kind:** observed behaviour
- **Scope:** battle: the tiles lit when the Move command opens (and the same builder for the AI and for another unit's range)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [Battle_MoveRange_Build](../functions/Battle_MoveRange_Build.md), [Battle_MoveRangeSetup](../functions/Battle_MoveRangeSetup.md), [Battle_MoveRange_InitTiles](../functions/Battle_MoveRange_InitTiles.md), [Battle_MoveRange_Expand](../functions/Battle_MoveRange_Expand.md), [Battle_MoveRange_ExpandJump](../functions/Battle_MoveRange_ExpandJump.md), [Battle_MoveRange_CheckSource](../functions/Battle_MoveRange_CheckSource.md), [Battle_MoveRange_CheckStep](../functions/Battle_MoveRange_CheckStep.md), [Battle_MoveRange_GapBlocked](../functions/Battle_MoveRange_GapBlocked.md), [Battle_MoveRange_CeilingAbove](../functions/Battle_MoveRange_CeilingAbove.md), [Battle_MoveRange_Commit](../functions/Battle_MoveRange_Commit.md), [MoveRangeScratch](../structs/MoveRangeScratch.md), [MoveBlockerRecord](../structs/MoveBlockerRecord.md), [BattleTileRecord](../structs/BattleTileRecord.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Which tiles a unit can stop on: a budget of Move + 1 spreads from its tile by steps and straight jumps under height, headroom, terrain-cost and occupancy rules; a final pass keeps the tiles it may stop on. Checked against eight ranges captured live: identical.

## Behavior

- V: budget: the start tile holds Move + 1 (Move capped at 124). Entering a tile leaves budget - cost(terrain of the entered tile) - the number of tiles jumped over. A tile is reached with a budget of 1 or more and can be left only with 2 or more. A better budget replaces a worse one; at equal budget the path with the smaller largest climb wins.
- V: terrain cost (tile byte +0, low 6 bits), walking set: 1; 2 for terrains 14, 15, 16, 17 and 45; the weather cost (1..3, Battle_MoveRange_WeatherCost) for 9, 10, 11, 26 and 36; no entry for 18, 25, 28 and 63. The water sets cost 1 on the water terrains; the lava set also enters 18; the Fly / Teleport / float sets cost 1 everywhere except 63.
- V: heights are half-steps: an edge of a tile is at 2 * height (byte +2) + slope (byte +3, low 5 bits) * k, k = two bits of the corner byte +4 for that edge (shift 0 = the +x edge, 2 = -x, 4 = -y, 6 = +y).
- V: a step compares the edge left with the edge entered plus 2 * the entered tile's water depth; the difference, up or down, must not exceed 2 * Jump (Jump capped at 7; 31 for Fly or unit +0x9C bit 0x02).
- V: headroom: the unit's body (6 half-steps; 4 Toad / Chicken; 8 with the float flag) must fit under the lowest underside above it at both ends of the step; an underside is 2 * (height - thickness) + the slope term of the other layer's tile, thickness = tile byte +5 low 5 bits.
- V: slopes: a tile whose slope exceeds the unit's Jump, or is 3 or more on a one-axis slope (corner byte & 5 equal to 1 or 4), can be entered or left only downhill.
- V: horizontal jump: in a straight line over 1 .. Jump / 2 tiles (Jump 3 -> 1 tile), never onto a higher level, each tile passed costs 1 extra; a column in the gap blocks when its tile or an enemy on it overlaps the unit's body at the height it leaves from, or lies entirely above that height. Fly and Teleport do not jump.
- V: other units: an enemy's tile is not standable, so it cannot be entered or crossed (it blocks a jump too); an ally's tile can be crossed but not stopped on; KO and Jumping units are not obstacles but nobody stops on their tile; Crystal and Chest units are ignored (their tile can be stopped on).
- V: mounts: a tile holding an ally of job 94..96 without a status of group 10 and with no rider is lit for a unit that can ride (unit +0x06 bit 0x80 or 0x40, not Toad / Chicken, unit +0x65 bit 0x20 clear).
- V: water: depth 1..3 tiles are standable for a walker; depth 4+ only with flags 0x80 / 0x40; stopping needs depth <= 2 (3 with any of flags 0xD0); unit +0x9D bit 0x10 keeps the unit out of water altogether.
- V: stop conditions besides the budget: slope <= 3 (<= 2 on a one-axis slope), tile byte +6 bits 0x80 and 0x02 clear, terrain not 28, terrain 18 only with flags 0x20 / 0x08, never the start tile.
- V: Teleport (unit +0x9D bit 0x04 or 0x08, not as Toad / Chicken): every tile gets budget 1, so every tile that passes the stop conditions is lit. Fly (unit +0x9E bit 0x04, not as Toad / Chicken): open cost set, Jump 31, no climb bookkeeping; enemy tiles get the 'step onto' flag.
- V: the result is written to tile byte +5 bit 0x20 only when the battle manager's marking state (dword +6536) is 15; other callers write the same set to a state bit of the marking table and leave the tile bits as they were.
- V (captures, 8 of 8 exact on both layers): Orbonne (Ramza, Move 5 Jump 3, three turns) and Gariland (five units, Move 3..5 Jump 3). Removing any one of these rules breaks at least one capture: the horizontal jump and its length, the gap test, water cost 2, the extra cost per jumped tile, no upward jump, the height limit (exact to the half-step, both directions), slope-aware edge heights, enemies block, allies cannot be stopped on, KO tiles cannot be stopped on, tile byte +6 bits 0x03 not standable.
- ?: not exercised by any capture (code only): headroom under a second layer, steep-slope refusal, forbidden terrains, depth 3+ water, the weather cost, Fly / Teleport / float and the water and lava abilities, Toad / Chicken, mounts and riders, the 16-entry blocker limit.

## Notes

Detail and evidence: the function sheets linked from this page.

## Open questions

? Captures that would settle the code-only rules: a two-layer map (a bridge) with a unit under and on the bridge; a unit next to deep water (depth 3 and 4); a steep roof or stair of slope 3+; a unit with Fly, Teleport, Float or a water ability; a mounted chocobo; rain or a storm on a swamp map (weather cost); a battle with more than 16 other units.
