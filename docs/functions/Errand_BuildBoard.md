# Errand_BuildBoard

- **Address:** `0x1402ED078`
- **Area:** [Errands](../areas/errands.md)
- **Prototype:** `int64_t Errand_BuildBoard(void)`
- **Callers:** (the tavern errand screen; not traced here)
- **Callees:** Errand_LoadRecord, Errand_BuildBoardEntry, PreviewUnit_BuildRecord, sub_14019DC5C, sub_14019DCD4, sub_1402D541C, sub_1400F6C8C, sub_1401E8B7C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the list of errands the tavern board shows: one entry per errand record, marked as available, dispatched or returning,
with the preview of the units on a dispatched errand.

## Behavior

- V: starts a local array of 96 (state, active index) pairs, every state 4 ("not dispatched").
- V: walks the active errand slots (`g_ErrandActive`, 9-byte records, count `byte_140D407B2`): a slot whose errand number
  (record byte 1) is below 0x60 marks that errand state 2 (byte 0 bit 2 clear) or 3 (record byte 4 equal to
  `dword_140D493E8`; I: the errand returns in the current town), with the slot index.
- V: for every errand 0..95 (`cmp 60h` loop end): loads its record (Errand_LoadRecord), then either asks
  Errand_BuildBoardEntry (state 4; a zero answer skips the errand) or builds the unit previews of the dispatched slot (up to
  three units, record bytes 6..8; unit indices below 0x36 read the unit records, others use fixed fallback values).
- V: appends `errand - 0x3000` as a u16 to the board list at `dword_140D498F0` (range check at 0x100 bytes: at most 128
  entries) and reads the errand's 2-byte new-flag pair `byte_1411A7319[2 * errand]` for errands below 0x60 (the live copy of
  the save field ffto_world bar.mouke.menu_new: is_new, is_newarrival).
- V: hands the list to the UI and sets the screen state (sub_14019DCD4, sub_1402D541C, dword_140D49ABC = 9).

## State touched

- Calls: [Errand_LoadRecord](Errand_LoadRecord.md), [Errand_BuildBoardEntry](Errand_BuildBoardEntry.md), [PreviewUnit_BuildRecord](PreviewUnit_BuildRecord.md)

## Referenced by

- Called by: [Tavern_TopInput](Tavern_TopInput.md)
- Observed behaviours: [ErrandStateIsSpreadOverFiveStores](../behaviors/ErrandStateIsSpreadOverFiveStores.md)

## Notes

Limits of the errand count: the 96 compares here (0x1402ED103, 0x1402ED347, 0x1402ED43B)
and in sub_14036E5DC (0x14036EA2C, 0x14036EA79), the 96-pair local array, the 128-entry board list, and the per-errand save
fields (world mouke_delay[96], mouke_finishday[108], ffto_world bar.mouke.menu_new[96 x 2], active slots mouke_event[8] with
a u8 errand number).

The board list entry of an errand is
0xD000 + errand (the 11-bit id), and the new-flag read indexes with the errand's low byte.

The errand number in an active slot is a byte, so a save can name at most 256 errands.

## Open questions

? What the 108 entries of mouke_finishday hold beyond the 96 errands.
