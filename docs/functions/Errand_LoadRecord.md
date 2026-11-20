# Errand_LoadRecord

- **Address:** `0x1402CCDC4`
- **Area:** [Errands](../areas/errands.md)
- **Prototype:** `void Errand_LoadRecord(uint16_t *out, int errandIndex)`
- **Callers:** Errand_IsAvailable, Errand_ComputeRewards, `sub_1402ED078`, `sub_1402ED7E0`, `sub_1402EDF58`, `sub_1402EE1C8`, `sub_14036CC50`, `sub_14036E5DC`, `sub_14037131C`, `sub_140377E9C`
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Copies one 23-byte errand (dispatch) definition out of the executable's errand data block into 23 16-bit words, resolving the two fee fields.

## Behavior

- V: the block starts with an offset table; the first offset locates the array of 23-byte records (96 records, one per errand).
- V: each byte of record `errandIndex` is widened to a 16-bit word in out[0..22].
- V: out[4] and out[5] are then replaced by entries of the 16-bit price table whose offset is the block's second offset (fee components).
- I: the 96 records match the 96 errand flags (event variables 864..959).
- V: used by Errand_IsAvailable, Errand_ComputeRewards, the board builders and several UI and start functions.
- V: over all its callers (the shared record g_ErrandRow and the three functions that load into a buffer of their own: Errand_IsAvailable, sub_1402EDF58, sub_14036E5DC) words 0, 1, 2, 4..12, 16, 17, 19, 21 and 22 are read; words 3, 13, 14, 15, 18 and 20 are read by no function.

## Referenced by

- Called by: [Errand_BuildBoard](Errand_BuildBoard.md), [Errand_ComputeRewards](Errand_ComputeRewards.md), [Errand_IsAvailable](Errand_IsAvailable.md), [Errand_Recall](Errand_Recall.md), [Errand_SelectBoardEntry](Errand_SelectBoardEntry.md), [sub_14036E5DC](sub_14036E5DC.md)
- Observed behaviours: [ErrandStateIsSpreadOverFiveStores](../behaviors/ErrandStateIsSpreadOverFiveStores.md)
- Reads tables: [ErrandBlob](../tables/ErrandBlob.md)

## Notes

Its three blob operands are at 0x1402CCDC4, 0x1402CCDCB and 0x1402CCDF8; the header offsets it reads are data in the table.

Field meanings by word: 0 category, 1 type, 2 errand number, 4 and 5 fee components, 6 base day count, 9 JP tier, 10 treasure pool, 11 bonus roll, 12 gil tier, 16 town, 17 condition flags, 19 featured-unit selector, 21 story threshold, 22 reference errand.

## Open questions

? what the six unread words (3, 13, 14, 15, 18, 20) were for; word 7 is read (the most days a dispatch may take).
