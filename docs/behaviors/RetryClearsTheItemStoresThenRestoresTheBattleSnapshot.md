# RetryClearsTheItemStoresThenRestoresTheBattleSnapshot

- **Kind:** observed behaviour
- **Scope:** Change Formation and Retry in a battle: where the party's item counts come from
- **Area:** [Save data](../areas/save-data.md)
- **Affects:** [GameState_ResetParty](../functions/GameState_ResetParty.md), [Battle_SnapshotLiveState](../functions/Battle_SnapshotLiveState.md), [Battle_RestoreSceneVars](../functions/Battle_RestoreSceneVars.md), [Inventory_AddCount](../functions/Inventory_AddCount.md), [g_InventoryCounts](../globals/g_InventoryCounts.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A Retry first clears the item stores with GameState_ResetParty and then writes them back from the battle snapshot taken when the battle began (Battle_SnapshotLiveState, direction 1). Only the entries the snapshot holds come back: the snapshot keeps 0x105 inventory counts, 0x105 Poachers' Den counts and the 0x105 new-flag pairs; anything past them in the live stores is left as the clear left it.

## Behavior

- V (seen live 2026-11-23, a random battle at Zeklaus Desert, System Menu > Retry > Change Formation and Retry; a data watch on two inventory counts): first GameState_ResetParty writes 0 (rip 0x14028456A, its clear loop); then Battle_SnapshotLiveState writes the count back from the snapshot (rip 0x140279CB0); then Inventory_AddCount (rip 0x14028482A) writes the same entry seven more times (the count did not change).
- V (seen live 2026-11-23): on this path the checkpoint restore sub_1402CF768 is not reached; the checkpoint writer sub_1402CEEE8 runs at the battle's start (with the battle snapshot written by Battle_SaveCapture).
- V: GameState_ResetParty clears g_InventoryCounts and g_PoachersDenStock (0x105 entries each), the move-find taken bits, sets every new-flag pair to 0x0101 and the gil to 7500 (EventVar_Write 44).

## Notes

Evidence: the live data watch of 2026-11-23 (rips above) and IDA decompiles of GameState_ResetParty and Battle_SnapshotLiveState.

## Open questions

? which caller runs GameState_ResetParty on the Retry path (the reset's callers are the title and opening tasks: the Retry seems to go through them); ? what the seven Inventory_AddCount calls add back (equipped items returned to the bag, likely).
