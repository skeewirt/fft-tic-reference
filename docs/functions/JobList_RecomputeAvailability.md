# JobList_RecomputeAvailability

- **Address:** `0x14028B6B0`
- **Area:** [Job list and unlock](../areas/job-list.md)
- **Prototype:** `void JobList_RecomputeAvailability(void)`
- **Callers:** sub_1402C53F0, sub_14033FB00 (deferred callback)
- **Callees:** sub_1400F8574, sub_1402CBED4, BitStream_ReadBits

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Recomputes the party-wide job-availability flags from each unit's job levels and the runtime job bits.

## Behavior

- V: walks 50 x 600-byte unit save records starting at unk_1411A7D12, skipping records whose byte-1 is 0xFF.
- V: derives the unit's job id from byte-2 (128/129 -> 74, 130 -> byte 0, else the byte), looks up its Job row, and when the row id (+24) is 1..124 and byte_1411A7490[id+21] is set, clears that flag.
- V: for records where sub_1402CBED4(byte0) == 0 and (uint8)(byte+5 + 80) > 0x2F, loops job indices i = 0..20 but breaks at i == 20; for each Job row (74+i) whose id is >= 125 or has the flag set, resets the bit reader to record+45 and reads i bits then one bit; a set bit clears flag[id+21] for id < 125.
- V: the record pointer used here starts 2 bytes into the 600-byte save record, so the reader base +45 is save-record +47, the stored unlock mask: the same MSB-first bits JobList_Build uses.

## State touched

- Calls: [BitStream_ReadBits](BitStream_ReadBits.md)
- Writes: [g_BitReaderPtr](../globals/g_BitReaderPtr.md), [g_BitReaderReset](../globals/g_BitReaderReset.md)

## Referenced by

- Observed behaviours: [AJobTypeAbove124HasCardsButNoPartyFlag](../behaviors/AJobTypeAbove124HasCardsButNoPartyFlag.md), [UnlockMaskStreamRunsIntoLearnedBitsPastIndex23](../behaviors/UnlockMaskStreamRunsIntoLearnedBitsPastIndex23.md)
- Reads tables: [UnitJobFlags](../tables/UnitJobFlags.md), [UnitSaveSlots](../tables/UnitSaveSlots.md)

## Notes

The loop's `if (i == 20) break` means index 20 is never considered.

Per-job bits are addressed by job index (Job_IdToIndex), not job id.

## Open questions

Whether the i == 20 skip is an off-by-one or deliberate (only 20 stock tree jobs).
