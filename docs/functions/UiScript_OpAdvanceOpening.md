# UiScript_OpAdvanceOpening

- **Address:** `0x140329FEC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned char *UiScript_OpAdvanceOpening(unsigned char *record)`
- **Callers:** UiScript_Run (through the 29-slot handler table)
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 22: advances the window opening stage.

## Behavior

- V: increments the stage byte while it is below 4; the record is one byte, so it returns record + 1 (not the length byte).
- V: the stage byte is read by UiScript_OpDrawWindowOpening.

## Notes

The IDB declares an integer argument and return.

## Open questions

None recorded.
