# PartyUnit_WriteBackToSave

- **Address:** `0x140285744`
- **Area:** [Unit data](../areas/unit-data.md)
- **Prototype:** `__int64 __fastcall PartyUnit_WriteBackToSave(int party_slot)`
- **Callers:** `sub_140285A6C`, `sub_14020806C` (save path), `sub_1402BBBCC`, `sub_14033359D`, `sub_140336095`, `sub_140337161`, `sub_1403371C2`, `sub_140338014`, `sub_140366A4C`, `sub_140368D1A`
- **Callees:** `Item_GetRecord`, `PartyUnit_FillFromWork`, `UnitWork_BuildFromSaveIndex`, `sub_1402BB31C`, `__security_check_cookie`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Writes one party unit's record back into its 600-byte save row. The five equipment words go to the save raw,
without a mask or flag test.

## Behavior

- V: It builds a work record from the save index (`UnitWork_BuildFromSaveIndex`) and fills the non-equipment
  fields from the party record.
- V: It writes the two hand words at record +0x54 and +0x56 to save +0x16/+0x14 and +0x1A/+0x18; the category
  19 (shield) item goes to the second word of each pair, the other item to the first (0x140285829..0x140285884).
- V: It writes +0x58, +0x5A and +0x5C to save +0x0E, +0x10 and +0x12 (0x140285890..0x1402858BF).
- V: The stores are whole-word copies: no 0x3FF mask and no bit-15 test. Before each pair it writes 0x00FF00FF
  to the two-word slot, so an empty half stays 0xFF.
- V: It calls `Item_GetRecord` with the raw word at 0x140285845 and 0x140285872. That accessor indexes the item
  table with the full 16-bit value, so a bit-15 word would read far past the table.
- V: The job: the save record is `g_UnitSaveData + 0x258 * (signed word at party +0x2C)`, and its job byte at +2 is
  the low byte of the party record's job word (a byte load from party +0x24 and a byte store to save +2, 0x1402857D3..0x1402857DB). A job
  change edits that party word (a u16 in `PartyUnit_FillFromWork`'s store at 0x140284AF1), so this store is where a changed
  job reaches the save record. Observed live 2026-11-04 (a data watch on the combat-set job byte saw this function copy
  the whole record); the three combat-set job bytes at party +462 / +550 / +638 are copied here and never read as a job.
- V: It ends with `PartyUnit_FillFromWork` to rebuild the party record from the save row.
- I: The commit handler strips the flags before this function runs; every other caller relies on the session
  having ended cleanly.

## State touched

- Calls: [Item_GetRecord](Item_GetRecord.md), [PartyUnit_FillFromWork](PartyUnit_FillFromWork.md)
- Reads: [g_PartyUnits](../globals/g_PartyUnits.md)
- Writes: [g_UnitSaveData](../globals/g_UnitSaveData.md)

## Referenced by

- Called by: [JobScreen_UpdateState](JobScreen_UpdateState.md), [sub_140285A6C](sub_140285A6C.md), [sub_1402BBBCC](sub_1402BBBCC.md), [sub_1403358FC](sub_1403358FC.md)
- Observed behaviours: [BattleLoadWritesThePartyBackToTheSaveRecords](../behaviors/BattleLoadWritesThePartyBackToTheSaveRecords.md), [CombatSetJobBytesAreOnlyCopied](../behaviors/CombatSetJobBytesAreOnlyCopied.md), [JobChangeReachesTheSaveRecordOnlyThroughWriteBack](../behaviors/JobChangeReachesTheSaveRecordOnlyThroughWriteBack.md), [PartyJobWordIsSixteenBits](../behaviors/PartyJobWordIsSixteenBits.md)

## Notes

V: stores the five party words raw at save +0x0E..+0x1A (0x140285829-0x1402858BF) and calls Item_GetRecord with the unmasked word at 0x140285845/0x140285872; a bit-15 word would index past the item table.

## Open questions

- ?: whether any caller can run with a bit-15 word still in the unit.
