# EffectCb_ClearFlagAndWait

- **Address:** `0x14035E2D4`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `__int64 __fastcall EffectCb_ClearFlagAndWait(__int16 slot, int index, int, int)`
- **Callers:** reached only through tbl_EffectCallbacks (0x1406759C0, index 143)
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Effect callback (entry 143 of the effect callback table): on start it clears `byte_140D4003F`; while running it advances the word `word_142FEC530` from 1 to 2.

## Behavior

- V: the state byte is at `0x141D33136 + 312 * slot + index` (byte 38 + index of the slot's 312-byte script record).
- V: state 1: stores 0 in `byte_140D4003F`, sets the state byte to 2 and returns 2.
- V: state 2: when `word_142FEC530` equals 1 it stores 2 there; the state byte stays 2 and the function returns 2.
- V: state 3: sets the byte to 0 and returns 0. Any other state returns the byte.
- I: the state values are start / running / finish, as in the neighbouring callbacks.
- ?: what `word_142FEC530` and `byte_140D4003F` mean (only this function was read).

## Notes

V: whole body read. The name is ours; it describes what the two global writes look like.

## Open questions

?: who sets `word_142FEC530` to 1 and who reads the 2.
