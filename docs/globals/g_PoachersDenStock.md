# g_PoachersDenStock

- **Kind:** global
- **Address:** `0x1411A7700`
- **Area:** [Items and shops](../areas/items.md)
- **Type:** `uint8[261]`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Poachers' Den stock: one count per item id 0..260 (PoachersDen_AddStock adds to it, clamped 0..255); the shop list builder Shop_BuildItemList lists the ids with stock when the shop id is 100 or above. Saved with the game.

## Behavior

- V: cleared by GameState_ResetParty at a new game.

## Referenced by

- Described by tables: [PoachersDenStock](../tables/PoachersDenStock.md)
- Observed behaviours: [ItemIdSpace](../behaviors/ItemIdSpace.md)
- Read by: [Battle_SnapshotLiveState](../functions/Battle_SnapshotLiveState.md), [PoachersDen_AddStock](../functions/PoachersDen_AddStock.md), [Shop_BuildItemList](../functions/Shop_BuildItemList.md), [sub_1401AEEF0](../functions/sub_1401AEEF0.md), [sub_1402CEEE8](../functions/sub_1402CEEE8.md)
- Written by: [Battle_SnapshotLiveState](../functions/Battle_SnapshotLiveState.md), [GameState_ResetParty](../functions/GameState_ResetParty.md), [PoachersDen_AddStock](../functions/PoachersDen_AddStock.md), [Save_BootClear](../functions/Save_BootClear.md)

## Notes

V: PoachersDen_AddStock clamps a count to 0..255 and is the only mutator of this store that game logic calls; its only direct caller is Shop_BuildItemList, which passes a delta of 0, so on that path the function only reads.

## Open questions

? the path that raises the den stock (poaching): no direct call to the mutator with a non-zero delta exists in the image.
