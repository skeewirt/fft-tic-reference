# UiScript_OpSetTint

- **Address:** `0x1403288C8`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned char *UiScript_OpSetTint(unsigned char *record)`
- **Callers:** UiScript_Run (through the 29-slot handler table)
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 11: sets the tint colour of the following cells.

## Behavior

- V: flag clear: three colour bytes +2..+4; flag set (the alternate-value flag of UiScript_Run): +5..+7; stored as the shared tint record (a word and a byte).
- V: returns the pointer after the record.

## Notes

The state reset sets a neutral tint before each script.

## Open questions

None recorded.
