# SaveWork_PackFromParty

- **Address:** `0x14021B070`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `int64_t SaveWork_PackFromParty(int slot)`
- **Callers:** SaveSlot_WriteFromLive, sub_14021AEC0, sub_140246014, sub_1402BB6B0, sub_1402CEEE8 (5 callers)
- **Callees:** SaveWork_PackFromLive (tail jump)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Chooses the leader for the slot summary and packs the live state: the first party unit whose kind byte (+114) is 1..3, falling back to unit 0.

## Behavior

- V (decompile): clears `Src[257..272]` (the hero name, 16 bytes) and sets `Src[273] = 0xFE`.
- V: ends with a jump to SaveWork_PackFromLive(slot, job = the u16 at unit+36, level = the u16 at unit+0) at 0x14021B0E3: a TAIL JUMP, not a call; a hook that wants the packed copy must be a tail-jump hook.
- V: `Src` is the pointer to the work copy `g_SaveWorkCurrent`.

## State touched

- Calls: [SaveWork_PackFromLive](SaveWork_PackFromLive.md)
- Reads: [g_PartyCount](../globals/g_PartyCount.md), [g_PartyUnits](../globals/g_PartyUnits.md)

## Referenced by

- Called by: [SaveSlot_WriteFromLive](SaveSlot_WriteFromLive.md), [sub_14021AEC0](sub_14021AEC0.md), [sub_140246014](sub_140246014.md), [sub_1402CEEE8](sub_1402CEEE8.md)
- Observed behaviours: [CheckpointCopyHoldsTheLiveUnitRecords](../behaviors/CheckpointCopyHoldsTheLiveUnitRecords.md), [SaveCardJobIsTheLeadersPartyJobWordLowByte](../behaviors/SaveCardJobIsTheLeadersPartyJobWordLowByte.md)

## Notes

All five callers reach the one tail jump.

## Open questions

None recorded.
