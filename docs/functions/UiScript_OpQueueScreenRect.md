# UiScript_OpQueueScreenRect

- **Address:** `0x140329FB0`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned char *UiScript_OpQueueScreenRect(unsigned char *record)`
- **Callers:** UiScript_Run (through the 29-slot handler table)
- **Callees:** sub_14031E184

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 21: queues the fixed screen rectangle of slot 19 while no window animation is running.

## Behavior

- V: while the animating byte is 0: zeroes the fixed rectangle's y word and queues it one priority level above the current one; it does not touch the byte.
- V: returns the pointer after the record.

## Open questions

None recorded.
