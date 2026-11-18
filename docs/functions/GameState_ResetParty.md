# GameState_ResetParty

- **Address:** `0x140284500`
- **Area:** [Unit data](../areas/unit-data.md)
- **Prototype:** `void GameState_ResetParty(int mode)`
- **Callers:** sub_14037FF14 (one direct site)
- **Callees:** sub_1402B32D4, sub_14027528C, sub_1402841D0, memset, sub_1402842CC, EventVar_Write, GameState_ResetJobFlags, sub_1402F0B68

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Resets the party-wide item state for a new game or a partial reset: the roster markers, the inventory counts, the Poachers' Den stock, the item badge block and the poach arrays, then the starting inventory and gil.

## Behavior

- V: the function takes one integer mode. Mode 0 calls sub_14027528C with 2; mode 2 calls sub_1402841D0 with 254; every other mode skips both calls.
- V: it writes a 0xFF byte into 54 records spaced 600 bytes apart starting at 0x1411A7D11 (the per-unit roster markers, byte +1 of each record).
- V: one bound register holding 261 (0x105) drives three separate clears: the 261 inventory counts at 0x1411A7C00, the 261 Poachers' Den stock bytes at 0x1411A7700, and the 261 two-byte badge pairs at 0x1411A7810.
- V: the badge pairs are filled with 0x0101, not zero, so a new game starts with both badge bytes set for every id.
- V: 128 bytes (0x80) at 0x1411A7680 are zeroed after the inventory and den clears and before the badge fill.
- V: the poach block after the badges is reset as well: the 97-byte count, order and sort arrays at 0x1411A7A1A, 0x1411A7A7B and 0x1411A7ADC are zeroed with three 97-byte memsets, and the 97 two-byte 'new' pairs at 0x1411A7B3D are filled with 0x0101.
- V: sub_1402842CC writes the starting inventory, then event variable 44 (gil) is set to 7500 (0x1D4C).
- V: GameState_ResetJobFlags runs near the end, and when the mode is 0 the function copies byte +0xC4 and the dwords +0x594/+0x598 of one scene record into globals before sub_1402F0B68 runs.
- I: the shared 261 bound and the 0x0101 fill rest on the item id space being one flat array of 261 entries at this point in development.

## State touched

- Calls: [EventVar_Write](EventVar_Write.md), [GameState_ResetJobFlags](GameState_ResetJobFlags.md)
- Writes: [g_InventoryCounts](../globals/g_InventoryCounts.md), [g_PoachersDenStock](../globals/g_PoachersDenStock.md), [g_ItemNewFlags](../globals/g_ItemNewFlags.md), [g_UnitSaveData](../globals/g_UnitSaveData.md), [g_PoachCount](../globals/g_PoachCount.md), [g_PoachOrder](../globals/g_PoachOrder.md), [g_PoachSort](../globals/g_PoachSort.md), [g_PoachNewFlags](../globals/g_PoachNewFlags.md)

## Referenced by

- Observed behaviours: [MoveFindTakenBitsAreFourPerMapInA128ByteArray](../behaviors/MoveFindTakenBitsAreFourPerMapInA128ByteArray.md)

## Notes

- V: the badge block and the poach arrays fill the 1007 written bytes from 0x1411A7810 up to the inventory at 0x1411A7C00; one byte between the last flag word and the inventory is not written.
- V: the same bound register is reused for the inventory and den loops, so both arrays are always the same length here.

## Open questions

- ?: what mode 1 means, since neither of the two mode branches runs for it.
- ?: the role of sub_14037FF14, the only direct caller.
- ?: the meaning of the 128 bytes at 0x1411A7680 (I: scene bits, written by sub_140271CA8).
