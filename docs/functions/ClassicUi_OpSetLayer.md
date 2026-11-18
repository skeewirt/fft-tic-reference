# ClassicUi_OpSetLayer

- **Address:** `0x1403901C0`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned char *ClassicUi_OpSetLayer(unsigned char *record)`
- **Callers:** ClassicUi_RunLayoutScript
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Opcode 14: sets the layer word used by the following cells.

## Behavior

- V: stores byte +3 in the layer word and returns the next record.

## Open questions

None recorded.
