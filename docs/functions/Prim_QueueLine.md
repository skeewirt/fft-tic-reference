# Prim_QueueLine

- **Address:** `0x14031D960`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 __fastcall Prim_QueueLine(const int16_t *rect, const uint8_t *rgb, char flag, int bucket)`
- **Callers:** UiScript_OpDrawLine, UiScript_OpDrawLineRel; a data reference
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Appends a coloured line primitive to a draw list bucket.

## Behavior

- V: takes the next 24-byte record from the array at `*(qword_141874A18+72)` using the counter `word_141876BFC`.
- V: stores the three colour bytes, bit 0x02 of the flag byte per `flag`, x0+128, y0, x1+128, y1 from the four input words, and a tag word from `word_14114A4E4`.
- V: links it at the front of the list in slot `bucket` of the table at `*qword_141874A18` (16 bytes per slot).

## Referenced by

- Called by: [UiScript_OpDrawLine](UiScript_OpDrawLine.md), [UiScript_OpDrawLineRel](UiScript_OpDrawLineRel.md)

## Notes

Whole body read.

## Open questions

What the tag word counts.
