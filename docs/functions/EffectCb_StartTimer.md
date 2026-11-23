# EffectCb_StartTimer

- **Address:** `0x14035E33C`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `__int64 __fastcall EffectCb_StartTimer(__int16 slot, int index, int, int)`
- **Callers:** reached only through tbl_EffectCallbacks (0x1406759C0, index 148)
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Effect callback (entry 148 of the effect callback table): on start it sets one global from the script record and the block at `qword_1411A3818`, zeroes a second and stores 150 in a third.

## Behavior

- V: the record is `word_141D33110[156 * slot]` (312 bytes); the state byte is at record byte 38 + index.
- V: state 1: stores `*(u16*)(qword_1411A3818 + 2) - record_word[22]` in `dword_140D8ECB4` (record word 22 is the u16 at record byte 44), zeroes `dword_140DDEFC0`, stores 150 in `word_14114A108`, sets the byte to 2 and returns 2.
- V: state 3: sets the byte to 0 and returns 0. States 0 and 2 return the byte unchanged.
- ?: what the three globals mean.

## Notes

V: whole body read. The name is ours. I: the 150 is a frame count (rests only on it being stored as a 16-bit value; not checked).

## Open questions

?: the effect that uses callback 148 and the readers of `dword_140D8ECB4` and `word_14114A108`.
