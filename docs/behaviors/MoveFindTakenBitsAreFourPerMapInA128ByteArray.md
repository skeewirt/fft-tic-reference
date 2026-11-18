# MoveFindTakenBitsAreFourPerMapInA128ByteArray

- **Kind:** observed behaviour
- **Scope:** engine (Move-Find state)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [MoveFind_ProbeTile](../functions/MoveFind_ProbeTile.md), [MoveFind_TakeItem](../functions/MoveFind_TakeItem.md), [SaveWork_PackFromLive](../functions/SaveWork_PackFromLive.md), [SaveWork_UnpackToLive](../functions/SaveWork_UnpackToLive.md), [Battle_SnapshotLiveState](../functions/Battle_SnapshotLiveState.md), [GameState_ResetParty](../functions/GameState_ResetParty.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Which hidden tiles of a map have been taken is kept as four bits per map, two maps per byte, in a 128-byte array indexed by scene variable 51 (the current map id): map ids 0..255 fit, and the bytes after the array belong to the Poachers' Den stock. The same 128 bytes are saved, restored, snapshotted and cleared by whole-array copies.

## Behavior

- V: the probe tests the bit 0x80 >> (tile slot + 4 x (id and 1)) of byte id / 2; the take sets the same bit. Neither compares the id with 256.
- V (census of every instruction addressing the array, 2026-11-15): nine functions touch it: the probe, the take, the save pack and unpack (whole-array 16-byte copies, 128 bytes), the battle snapshot capture and restore (both in one function, two copy runs), two further functions that copy the 128 bytes to and from another save structure, the party reset (clears the array byte by byte) and the function the database names Status_BuildFlagMasks, whose first statement clears the array with a 128-byte fill.
- V: the array begins at 0x1411A7680 and the Poachers' Den stock array begins at 0x1411A7700, directly behind it: an id of 256 or more makes the probe read, and a take write, bytes of that stock.
- V: the save pack puts the 128 bytes at a fixed offset (+34226) of the save work record, so a save carries bits for maps 0..255 only.
- I: a hidden tile on a map whose row is all zero (no item, no trap) is still tile slot 0 at (0, 0) on layer 0; the probe finds it and reads the taken bit for any unit standing there.

## Notes

The earlier count of seven functions was by cross-reference from IDA, which misses accesses through the image base (the probe and the party reset).

## Open questions

? whether any save layout the game reads carries more than these 128 bytes for this purpose.
