# BattleRange_MarkRing

- **Address:** `0x14027FE20`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int BattleRange_MarkRing(const void *action)`
- **Callers:** sub_14020A7F0, sub_14020AD64, sub_14020C5C0, BattleAction_BuildUnitRequest, sub_14030D0E4, sub_14030D1CC, sub_140389D84, sub_14038C47C
- **Callees:** memcpy, sub_14027F5B4, sub_14041FAE0, sub_14027F270, sub_14027FD2C, Item_GetRecord, AbilityAction_GetRecord, sub_14027F974

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Marks the outer ring of tiles an action can reach, from the twenty-byte action block, and returns the range value the range display uses.

## Behavior

- V: it copies the twenty-byte action block into a stack buffer and takes the acting unit slot from its first byte.
- V: a slot above 0x14, or a unit whose marker byte +1 is 0xFF, makes it return without marking.
- V: the command byte at action +1 is looked up in the command-kind table at 0x14067E010 and the switch selects the range source for that kind.
- V: for the item and throw kinds the range comes from the item record and Item_GetRecord, not from an action row.
- V: for the ability kinds it reads the action record through AbilityAction_GetRecord and copies the range, area and vertical fields into the ring buffers.
- V: sub_14027F270 supplies the tile set, sub_14027FD2C and sub_14027F974 the inner and outer expansions, and 0x14041FAE0 sets the tiles in the cursor mask.
- V: the ability id is compared with the 0x170 boundary at the gate named battle_ring_range.
- I: this is the ring preview only; the filled effect area is produced by the companion BattleRange_ApplyShape and BattleRange_MarkArea.
- ?: whether the return value is a radius, a tile count or a status; the callers use it as a small range value but the unit is not proven.

## State touched

- Calls: [sub_14027F270](sub_14027F270.md), [Item_GetRecord](Item_GetRecord.md), [AbilityAction_GetRecord](AbilityAction_GetRecord.md), [sub_14027F974](sub_14027F974.md)
- Reads: [g_CurrentActionBlock](../globals/g_CurrentActionBlock.md)

## Referenced by

- Called by: [BattleAction_BuildUnitRequest](BattleAction_BuildUnitRequest.md)

## Notes

Whole function read (454 bytes); the eight call sites are the AI, preview and command paths.

## Open questions

None recorded.
