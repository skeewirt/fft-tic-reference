# UiScript_OpQueueScreenRectOnce

- **Address:** `0x140329EFC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned char *UiScript_OpQueueScreenRectOnce(unsigned char *record)`
- **Callers:** UiScript_Run (through the 29-slot handler table)
- **Callees:** sub_14031E184

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 19: after a window animation, queues a fixed screen rectangle once and clears the animating byte.

## Behavior

- V: while the 'window animating' byte is set it zeroes the y word of a fixed four-word rectangle, queues it through sub_14031E184 one priority level above the current one, then clears the byte.
- V: returns the pointer after the record.
- ?: what the rectangle primitive does on screen.

## Open questions

None recorded.
