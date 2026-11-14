# BattleAction_GetRangeInfo

- **Address:** `0x140281C24`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int BattleAction_GetRangeInfo(const void *action, uint8_t *out_flags)`
- **Callers:** Battle_ResolveTargets, Battle_ResolveReaction
- **Callees:** AbilityAction_GetRecord, BattleRange_ApplyShape, sub_1402826B0, sub_140280170

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Chooses how an action acquires its range and area: the item path for the item-like command kinds and the ability record path otherwise, filling the caller flags and returning the range result.

## Behavior

- V: the action command byte is at +1 and is looked up in the command-kind table at 0x14067E010.
- V: the output byte is cleared before any work; it receives the record flags at +3, +4, +5 and +6 when the ability path is taken.
- V: for command kinds 0 and 6 and for an ability id below 0x170, the ability record is fetched through AbilityAction_GetRecord.
- V: command kinds flagged by the mask 0x506, or a combined flags byte with bit 0x20, skip the ability record and go to the item range path.
- V: the item path calls sub_140280170, which reads the weapon record of the item and returns the item range.
- V: the ability path calls BattleRange_ApplyShape and returns its result; -1 means nothing could be marked.
- V: when the record flags have bit 8 and the state word at 0x14186AF80 is zero, sub_1402826B0 is called before returning.
- I: the mask 0x506 covers the command kinds that carry an item or a throw rather than an ability row.
- ?: what sub_1402826B0 changes; it is called only on the flagged ability path.

## State touched

- Calls: [AbilityAction_GetRecord](AbilityAction_GetRecord.md), [BattleRange_ApplyShape](BattleRange_ApplyShape.md), [sub_140280170](sub_140280170.md)

## Referenced by

- Called by: [Battle_ResolveReaction](Battle_ResolveReaction.md)

## Notes

Whole function read (193 bytes). The command table index and the 0x170 test are its two sites of interest.

## Open questions

None recorded.
