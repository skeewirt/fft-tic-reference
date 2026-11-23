# BattleRange_ApplyShape

- **Address:** `0x14027FFE8`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int BattleRange_ApplyShape(const void *action)`
- **Callers:** sub_1400D94F8, sub_1401FAA24, sub_1402039C4, sub_140206F90, sub_140209738, BattleAction_GetRangeInfo
- **Callees:** memcpy, sub_140280850, sub_140280A98, Item_GetRecord, BattleRange_MarkArea, sub_14041FAE0

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Applies the range shape and the effect area of an action to the cursor mask: it resolves the action record or the item path, marks the reachable tiles and then hands the effect area to the area marker.

## Behavior

- V: the action block is copied to the stack and the acting slot must be 0x14 or below; the unit marker at +1 must not be 0xFF.
- V: for the item command kind it requires the action item byte at +0xB to be below 0x15 and reads the item record instead of an action row.
- V: the command kind comes from the table at 0x14067E010 and selects the range source in the same way as BattleRange_MarkRing.
- V: it calls sub_140280850 and sub_140280A98 to build the directional range and the area lists.
- V: BattleRange_MarkArea is called for the effect area of the resolved ability or item.
- V: when the ability id is 0x170 or above the function returns -1 and marks nothing; this is the battle_range_shape gate.
- V: the tile bits are set through 0x14041FAE0, the same mask helper the ring marker uses.
- I: the two range functions split the work: this one owns the shape and the area, the ring marker owns the outer boundary.
- ?: how the directional bits in the action block select between the single-tile and line shapes; that branch was not decoded.

## State touched

- Calls: [sub_140280850](sub_140280850.md), [Item_GetRecord](Item_GetRecord.md), [BattleRange_MarkArea](BattleRange_MarkArea.md)
- Reads: [g_CurrentActionBlock](../globals/g_CurrentActionBlock.md)

## Referenced by

- Appears in flows: [AbilityLifecycle](../flows/AbilityLifecycle.md), [BattleTimelineCameraFlow](../flows/BattleTimelineCameraFlow.md)
- Called by: [BattleAction_GetRangeInfo](BattleAction_GetRangeInfo.md), [Battle_TimelineFocusCamera](Battle_TimelineFocusCamera.md)

## Notes

Whole function read (389 bytes). The 0x170 return is the boundary the X3 in-game trace hit.

## Open questions

None recorded.
