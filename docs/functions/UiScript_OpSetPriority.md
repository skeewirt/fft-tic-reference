# UiScript_OpSetPriority

- **Address:** `0x14032890C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned char *UiScript_OpSetPriority(unsigned char *record)`
- **Callers:** UiScript_Run (through the 29-slot handler table)
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 15: sets the draw priority word.

## Behavior

- V: stores +3 in the priority word that every queue call receives as its ordering index; UiScript_Run clears it to 0 at the start.
- V: returns the pointer after the record.

## Notes

Same role as ClassicUi_OpSetPriority (which skips it while a plate is built). The IDB declares an integer argument and return.

## Open questions

None recorded.
