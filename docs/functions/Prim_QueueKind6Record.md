# Prim_QueueKind6Record

- **Address:** `0x14031E0E8`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 __fastcall Prim_QueueKind6Record(const int16_t *rect, __int64 unused, int16_t value, int bucket)`
- **Callers:** UiScript_OpScrollList (two), sub_14037C8AC
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Appends a kind-6 record (command byte 0xF3, constant 576) built from a rectangle to a draw list bucket.

## Behavior

- V: takes a 32-byte record from the array at `*(qword_141874A18+176)` with counter `word_141876BE0`, sets kind word 6, byte +15 to 0xF3, copies two rect words to +20/+22 and the other two to +28/+30, stores 576 at +24 and `value` at +26.
- V: links it at the front of bucket `bucket` and stores the tag word.

## Referenced by

- Called by: [UiScript_OpScrollList](UiScript_OpScrollList.md)

## Notes

Whole body read.

## Open questions

What the kind-6 record does when drawn.
