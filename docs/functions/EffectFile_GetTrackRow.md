# EffectFile_GetTrackRow

- **Address:** `0x1402742CC`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void EffectFile_GetTrackRow(int effect, int *fileNumber, int *byteSize)`
- **Callers:** EventDataLoad_Poll (two calls)
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the two numbers that locate the data file of one battle effect: its file number in the game pack and its size in bytes.

## Behavior

- V: reads one 8-byte row (file number, size) at index effect from one of two 512-row tables in .rdata: dword_1406739C0 when the language flag at g_LanguageInfo + 8 is non-zero (or g_LanguageInfo is null), dword_1406749C0 otherwise.
- V: there is no bound check on the effect index; the tables hold 512 rows each (512 x 8 bytes; the second table starts that far after the first), so an index of 512 or more reads whatever follows the table.
- V (data): in the table used with the English pack, effect E (E at least 2) names the file called efc_eNNNdat_data in the pack file list (effect 260 = file 1133); rows 0 and 1 both point at file 901; the sizes are the stored size rounded up to 2048. The other table holds file number minus one in every non-empty row and the same sizes.
- V (data): 398 of the 512 rows are filled; a size of 0 marks an empty row (114 rows).
- V (2026-11-12): a leaf with no stack frame and no unwind entry: rcx = the effect, rdx and r8 the two out pointers; it writes [rdx] and [r8] and returns.
- V (data): row 511 is empty in both tables and no stock effect word selects it.

## Referenced by

- Observed behaviours: [BattleEffectsAreOneFilePerNumber](../behaviors/BattleEffectsAreOneFilePerNumber.md)

## Notes

Name is ours.

## Open questions

? which languages use the second table (it has the numbering of a pack whose list is one number lower).
