# EventSlot_LoadTrack

- **Address:** `0x1402B1D58`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int EventSlot_LoadTrack(int track, unsigned slot)`
- **Callers:** Music_StartSceneTracks, Scene_StartMusic, sub_1401D7DDC, sub_1401D9174, sub_1402C538C, sub_1402D50E4, sub_1402F2500, sub_14033FE00, sub_140345FE4 (also reached through the text-command slot pointer)
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Loads a music track number into an event music slot when that slot is free.

## Behavior

- V: returns 0 and changes nothing when qword_1418623F8[slot] is already set.
- V: otherwise dword_142E7FB08[slot] = track, qword_1418623F8[slot] = the address of the shared record unk_14185A2E0, qword_1418623C0[slot] = 0, and it returns the slot.

## Notes

Slot count: the arrays are indexed 1 and 2 by every caller read; EventSlots_ResetAll clears both.

## Open questions

? what the shared record unk_14185A2E0 holds.
