# CardSlot_IsValid

- **Address:** `0x140245C34`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `int32_t CardSlot_IsValid(int slot)`
- **Callers:** Game_MainLoop, SaveLoadList_BuildEntries, UIAddonFFTOSaveLoad_vfunc_4_0, sub_14021BD04
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Tests that a slot of the cache starts with the `SC` magic: returns 0 when valid, -1 otherwise.

## Behavior

- V (decompile): in ENHANCED mode (or when `dword_140D405B4 == 0`) the slot is `g_SaveSlotCache + 40164 * slot`; byte 0 must be 83 ('S') and byte 1 must be 67 ('C').
- V: with CLASSIC mode and the card layer on, slot 0 maps to `g_SaveAutoSlot` (0x142E75DF8), whose magic word this function sets to 17235 ('SC') itself; other slots shift down by one.

## Referenced by

- Called by: [Game_MainLoop](Game_MainLoop.md), [SaveLoadList_BuildEntries](SaveLoadList_BuildEntries.md), [sub_14021BD04](sub_14021BD04.md)

## Notes

Written in the 2026-10-29 integration pass from the J7, J8, J9 and W0 research reports; each address was re-checked against the decompile.

## Open questions

None recorded.
