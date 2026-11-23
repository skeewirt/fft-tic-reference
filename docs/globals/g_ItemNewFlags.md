# g_ItemNewFlags

- **Kind:** global
- **Address:** `0x1411A7810`
- **Area:** [Items and shops](../areas/items.md)
- **Type:** `uint8[261][2]`
- **Points to / is a:** [ItemNewFlagBlock](../structs/ItemNewFlagBlock.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Two flag bytes per item id 0..260, set at a new game; I: the shop 'new item' badges (byte 1 cleared when the item is first sold, byte 0 when it is first obtained). The first 522 bytes of a 1007-byte block whose tail holds the four Poachers' Den (poach) arrays; g_InventoryCounts begins one byte after it.

## Behavior

- V: readers test the id against 0x104 (sub_140197BCC, sub_14036B2D0) or loop over ids 0..255 (sub_14028B510, sub_140344B68).

## Referenced by

- Described by tables: [ItemNewFlags](../tables/ItemNewFlags.md)
- Observed behaviours: [ItemIdSpace](../behaviors/ItemIdSpace.md)
- Read by: [Battle_SnapshotLiveState](../functions/Battle_SnapshotLiveState.md), [ShopEntry_Fill](../functions/ShopEntry_Fill.md), [sub_1401AEEF0](../functions/sub_1401AEEF0.md), [sub_14028B510](../functions/sub_14028B510.md), [sub_1402CEEE8](../functions/sub_1402CEEE8.md)
- Written by: [Battle_SnapshotLiveState](../functions/Battle_SnapshotLiveState.md), [GameState_ResetParty](../functions/GameState_ResetParty.md), [Game_MainLoop](../functions/Game_MainLoop.md), [sub_140197BCC](../functions/sub_140197BCC.md), [sub_14028B510](../functions/sub_14028B510.md)

## Notes

V: the 522 flag bytes are followed immediately by the poach arrays at +522, +619, +716 and +813; the last poach byte is +0x3EE and g_InventoryCounts begins at +0x3F0, one byte later.

## Open questions

None recorded.
