# PartyUnit_FillFromWork

- **Address:** `0x140284A08`
- **Area:** [Unit data](../areas/unit-data.md)
- **Prototype:** `__int64 __fastcall PartyUnit_FillFromWork(__int64 work, __int16 *record_b, __int64 save_row)`
- **Callers:** `PartyUnit_ReloadEquipment`, `PartyUnit_WriteBackToSave`, `UnitWork_BuildForSlot`, `sub_14028B7D0`
- **Callees:** `sub_1402B8EBC`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the 640-byte party record B from a work record (the save row image) and the save row. The equipment words
at record B +0x54..+0x5C come from work +0x0E..+0x1A and are zeroed when the full 16-bit word is not a valid id.

## Behavior

- V: It writes record B +0x54 from work +0x14 or +0x16, +0x56 from work +0x18 or +0x1A, and +0x58/+0x5A/+0x5C
  from work +0x0E/+0x10/+0x12 (0x140284C19..0x140284C51). The choice within each hand pair is made by the
  equip-category check at 0x140284BFF..0x140284C13.
- V: It then walks the five output words at 0x140284C55 and calls `sub_1402B8EBC` on each. That callee accepts
  only 1..0xFD and 0x100..0x104; any other full word (including a bit-14 or bit-15 word) makes the caller write
  zero (0x140284C62).
- V: The save words are copied raw from the work record; the validity check is the only sanitizer.
- V: Earlier in the function it builds the non-equipment fields from the work and save records; that part was
  not traced in detail.
- I: This is where a flagged save word is dropped: it cannot survive the record-B rebuild, because the full
  word fails the id-range test and is replaced by zero.

## State touched

- Reads: [g_UnitSaveData](../globals/g_UnitSaveData.md)

## Referenced by

- Called by: [PartyUnit_ReloadEquipment](PartyUnit_ReloadEquipment.md), [PartyUnit_WriteBackToSave](PartyUnit_WriteBackToSave.md), [UnitWork_BuildForSlot](UnitWork_BuildForSlot.md)
- Observed behaviours: [CombatSetJobBytesAreOnlyCopied](../behaviors/CombatSetJobBytesAreOnlyCopied.md), [JobChangeReachesTheSaveRecordOnlyThroughWriteBack](../behaviors/JobChangeReachesTheSaveRecordOnlyThroughWriteBack.md), [PartyJobWordIsSixteenBits](../behaviors/PartyJobWordIsSixteenBits.md)

## Notes

V: copies the work record's equipment words to record B +0x54..+0x5C (0x140284C19-0x140284C51) and zeroes each word whose full 16-bit value fails sub_1402B8EBC (0x140284C59-0x140284C62).

## Open questions

- ?: the exact write order and the non-equipment fields; only the hand block and the sanitizer were read.
