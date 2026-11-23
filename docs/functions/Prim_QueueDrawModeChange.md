# Prim_QueueDrawModeChange

- **Address:** `0x14031E238`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 __fastcall Prim_QueueDrawModeChange(int flagA, __int64 unused, int16_t mode, __int64 unused2, int bucket)`
- **Callers:** sub_14031E300, sub_14031E3AC, sub_14031E458, sub_140326D78, UiScript_OpSetDrawMode; a data reference
- **Callees:** sub_1402600BC

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Appends a draw-mode change record to a draw list bucket.

## Behavior

- V: takes a 32-byte record from the array at `*(qword_141874A18+192)` with counter `word_141876BE4` and fills it with `sub_1402600BC`: a command byte, kind 2, and a mode word made of `mode & 0x9FF` plus 0x400 when `flagA` is non-zero.
- V: links it at the front of bucket `bucket` and stores the tag word.

## Referenced by

- Called by: [UiScript_OpSetDrawMode](UiScript_OpSetDrawMode.md)

## Notes

Whole body and the helper `sub_1402600BC` read; 0x400 and 0x9FF are constants in that helper.

## Open questions

None.
