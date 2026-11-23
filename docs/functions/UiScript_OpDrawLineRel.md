# UiScript_OpDrawLineRel

- **Address:** `0x140327C94`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned char *UiScript_OpDrawLineRel(unsigned char *record)`
- **Callers:** UiScript_Run (through the 29-slot handler table)
- **Callees:** Prim_QueueLine

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 28: queues a line from a point by an offset.

## Behavior

- V: record: +2 x0, +3 y0, +4 dx, +5 dy, +6..+8 colour; the end point is (x0 + dx, y0 + dy).
- V: otherwise as UiScript_OpDrawLine; returns the pointer after the record.

## State touched

- Calls: [Prim_QueueLine](Prim_QueueLine.md)

## Open questions

None recorded.
