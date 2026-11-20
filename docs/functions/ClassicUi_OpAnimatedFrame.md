# ClassicUi_OpAnimatedFrame

- **Address:** `0x140390744`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned char *ClassicUi_OpAnimatedFrame(unsigned char *record)`
- **Callers:** ClassicUi_RunLayoutScript
- **Callees:** ClassicUi_OpWindowFrame, sub_14038F5FC

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Opcode 18: a window frame that grows open over the first 8 page redraws.

## Behavior

- V: while the page redraw counter is below 8 it scales the width by an 8-entry percentage table (0x14071F1D0) and queues a growing plate before drawing the frame; later redraws draw the frame at full size.
- V: then runs the window frame handler on the same record.

## State touched

- Calls: [ClassicUi_OpWindowFrame](ClassicUi_OpWindowFrame.md)

## Notes

Read: the counter test and the plate; the table values are listed with LegacyCursorPositions.

## Open questions

None recorded.
