# UnitWork_BuildFromSave

- **Address:** `0x140275B84`
- **Area:** [Unit data](../areas/unit-data.md)
- **Prototype:** `int UnitWork_BuildFromSave(uint8_t *work, uint8_t *save, int slot)`
- **Callers:** sub_140275C70 (build by save index), sub_14028B7D0, SceneUnit_FillSpriteRecord
- **Callees:** sub_140278DA8, Unit_BuildJobUnlockMask, UnitWork_CopySaveFields, UnitWork_ApplyJobRow, sub_140276DF4, sub_140276EBC, sub_14027788C, sub_1402760E8

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the 512-byte unit work record C from a save unit record A. It first refreshes the unit's unlock mask inside the save record, then copies and completes the work record.

## Behavior

- V: returns -1 when the save slot is empty (A+1 = 0xFF).
- V: calls sub_140278DA8 on the second JP array (A+174) with the job levels (A+116) before anything else.
- V: recomputes the job unlock mask with Unit_BuildJobUnlockMask(levels A+116, flags A+4, learned bits A+50, story stage A+289) and stores its three bytes at A+47 (high), A+48, A+49 (low).
- V: clears a set of work fields (words/bytes around C+65, C+396, C+436..443, C+492, C+500), stores the third argument at C+2, then calls UnitWork_CopySaveFields, UnitWork_ApplyJobRow(work, 0) and four more fill helpers.
- V: the value stored at C+2 is overwritten by UnitWork_CopySaveFields with A+1.
- V: returns 0 on success.

## State touched

- Calls: [Unit_BuildJobUnlockMask](Unit_BuildJobUnlockMask.md), [UnitWork_CopySaveFields](UnitWork_CopySaveFields.md), [UnitWork_ApplyJobRow](UnitWork_ApplyJobRow.md)

## Referenced by

- Called by: [SceneUnit_FillSpriteRecord](SceneUnit_FillSpriteRecord.md)

## Notes

Side effect worth knowing: the save record's unlock mask is rewritten every time a work record is built, so a save needs no manual unlock bits.

## Open questions

Roles of the four trailing helper calls.
