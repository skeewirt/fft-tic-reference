# SaveLoadList_BuildEntries

- **Address:** `0x140185D1C`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `int64_t SaveLoadList_BuildEntries(int64_t addon)`
- **Callers:** sub_140187BD4
- **Callees:** CardSlot_IsValid, sub_140186240, sub_140186390, memset, sub_140011750

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the ENHANCED save/load list: one 240-byte entry per cache slot whose magic is `SC`, then sorts the entry vector.

## Behavior

- V: loops the 50 slots over the cache (level byte at cache + 0x113), skips slots failing CardSlot_IsValid, and per slot fills +0 slot, +4 language, +8 level, +12 mainProgress, +16 difficulty, +20 pos, +24 situation, +28 nextEventId, +32 timestamp, +40..+167 the four sprite records, +232 auto-slot flag, +236 cleared, +237 NG+.
- V: ends with a tail `jmp sub_1401CCE78` (0x14018621B) that sorts the vector.
- V: no job byte or job text is read (the list shows no class).

## State touched

- Calls: [CardSlot_IsValid](CardSlot_IsValid.md)

## Notes

Written in the 2026-10-29 integration pass from the J7, J8, J9 and W0 research reports; each address was re-checked against the decompile.

## Open questions

None recorded.
