# UiScript_OpSetBlendFlag

- **Address:** `0x140328878`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned char *UiScript_OpSetBlendFlag(unsigned char *record)`
- **Callers:** UiScript_Run (through the 29-slot handler table)
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 14: sets the semi-transparency word passed to the following primitives.

## Behavior

- V: stores +3 in the word that the cell, rectangle and line queues test (zero clears their blend bit); UiScript_Run clears it to 0 at the start.
- V: returns the pointer after the record.

## Notes

The IDB declares an integer argument and return; the code uses the record pointer.

## Open questions

None recorded.
