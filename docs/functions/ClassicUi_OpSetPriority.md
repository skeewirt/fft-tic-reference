# ClassicUi_OpSetPriority

- **Address:** `0x140390B88`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned char *ClassicUi_OpSetPriority(unsigned char *record)`
- **Callers:** ClassicUi_RunLayoutScript
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Opcode 15: sets the draw priority word unless a plate is being built.

## Behavior

- V: stores byte +3 in the priority word when the plate flag is 0.

## Open questions

None recorded.
