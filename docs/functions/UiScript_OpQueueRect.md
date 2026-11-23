# UiScript_OpQueueRect

- **Address:** `0x140329F4C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned char *UiScript_OpQueueRect(unsigned char *record)`
- **Callers:** UiScript_Run (through the 29-slot handler table)
- **Callees:** sub_14031E184

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 20: queues a rectangle from the record when no window animation is running.

## Behavior

- V: record: +2 x, +3 y, +4 width (0xFF means 374), +5 height; queued through sub_14031E184 one priority level below the current one, only while the animating byte is 0.
- V: returns the pointer after the record.
- ?: what the rectangle primitive does on screen.

## Open questions

None recorded.
