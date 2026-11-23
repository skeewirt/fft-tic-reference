# UiScript_OpDrawWindowOpening

- **Address:** `0x140328398`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned char *UiScript_OpDrawWindowOpening(unsigned char *record)`
- **Callers:** UiScript_Run (through the 29-slot handler table)
- **Callees:** sub_14031E184, UiScript_OpDrawWindow

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 18: draws a window that opens over a few redraws, then runs UiScript_OpDrawWindow on the same record.

## Behavior

- V: an opening stage byte counts 0..4; at 4 or more only the animating byte below is cleared.
- V: below 4 it scales the width (+5) and height (+6) by a percentage from a table of four 16-bit entries indexed by the stage (stages 0..3), centres the scaled box on the window box (+3, +4) and queues it through sub_14031E184 one priority level below the current one; for stages 0..2 it also clears a list-input word.
- V: sets the 'window animating' byte to 1 while the stage is below 4, else 0, then tail-calls UiScript_OpDrawWindow and returns its result.

## State touched

- Calls: [UiScript_OpDrawWindow](UiScript_OpDrawWindow.md)

## Notes

UiScript_OpAdvanceOpening raises the stage. Counterpart of ClassicUi_OpAnimatedFrame.

## Open questions

None recorded.
