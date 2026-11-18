# BattleStatusIconFlagMasks

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** Executable
- **Address:** `0x1406735D0`
- **Rows:** 40 rows of 4 bytes (42 to the next symbol)
- **Keyed by:** status id + 1 (row 0 unused; row s + 1 = status s)
- **Read by:** [BattleUnit_SetStatusVisual](../functions/BattleUnit_SetStatusVisual.md)
- **Row layout:** [StatusIconFlagMaskRow](../structs/StatusIconFlagMaskRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Per status id the bit mask that marks the status on the battle scene object (drawing side). Verdict: engine-data.

## Behavior

- V: BattleUnit_SetStatusVisual is called with status id + 1 (its callers pass the bit index + 1) and sets or clears the mask from this table, so row s + 1 belongs to status s
- V: Crystal (1), Chest (15), Chicken (21) and Toad (22) set sprite-change bits of the second word directly, so their masks are unused
- V: the tint flags SceneUnit_ApplyStatusTint tests: Stone (8) 0x20 grey; Vampire (13) 0x20000 grey + (3, -1, 8); Berserk (20) 0x4000 + 8 red; Poison (24) 0x400000 halved + 8 green; Regen (25) 0x20000000 + 8 blue; Oil (16) 0x800000 halved - 4; status 14 0x2000 halved - 8; Undead (3) 0x40000000 halved + (4, 0, 5); the first set in that order wins

## Notes

Our names. Tags: V layout, V reader, I mapping.

## Open questions

- ?: the tints not yet seen live (Poison green is the one most likely to be checked first)
