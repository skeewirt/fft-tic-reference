# MoveFindItems

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** Executable (initialised data, written at run time)
- **Address:** `0x140783840`
- **Rows:** 128 rows of 24 bytes
- **Keyed by:** battle map id
- **Read by:** [Map_LoadBattleData](../functions/Map_LoadBattleData.md), [MoveFind_ProbeTile](../functions/MoveFind_ProbeTile.md), [MoveFind_TakeItem](../functions/MoveFind_TakeItem.md), [MoveFind_ApplyTrap](../functions/MoveFind_ApplyTrap.md)
- **Row layout:** [MoveFindRow](../structs/MoveFindRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Move-Find Item and trap data: per map, up to four hidden tiles with a trap kind and a common and a rare item. Verdict: designer-data.

## Behavior

- V: 128 rows x 24 bytes = 0xC00 to the next symbol; row copied whole by the loader; taken bits at 0x1411A7680 indexed by scene variable 51 (2 maps per byte, 4 bits per map)
- V: sub_140251584 (map loader): copies the 24-byte row of the map into 0x140D8DC90
- V: sub_140271D80: finds the hidden tile under a unit (x, y, layer), reports item if its taken bit is clear and the trap kind 0..3 if 0x10 is clear
- V: sub_140271CA8: rolls rare vs common item and sets the taken bit
- V: sub_14030C39C: applies the trap: kind 0 sets an action-result flag with value 256 (I: Degenerator, level down), kind 1 inflicts status 39 Doom (Death Trap), kind 2 inflicts status 35 Sleep (Sleeping Gas), kind 3 deals max HP / 5 damage (Steel Needle)

## Notes

Our names. Tags: V.

## Open questions

- ?: kind 0's effect field (+0x1D0 = 256) mapped to Degenerator by elimination only
- ?: the support condition behind the +25 points
