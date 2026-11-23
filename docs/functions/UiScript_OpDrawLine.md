# UiScript_OpDrawLine

- **Address:** `0x140327C3C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned char *UiScript_OpDrawLine(unsigned char *record)`
- **Callers:** UiScript_Run (through the 29-slot handler table)
- **Callees:** Prim_QueueLine

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 7: queues a line between two points.

## Behavior

- V: record: +2 x0, +3 y0, +4 x1, +5 y1, +6..+8 the colour bytes; no list-row offset is applied.
- V: calls Prim_QueueLine (the line queue, which adds 128 to both x values) with the blend flag and priority words and returns the pointer after the record.

## State touched

- Calls: [Prim_QueueLine](Prim_QueueLine.md)

## Open questions

None recorded.
