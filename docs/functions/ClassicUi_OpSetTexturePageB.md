# ClassicUi_OpSetTexturePageB

- **Address:** `0x140390A90`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned char *ClassicUi_OpSetTexturePageB(unsigned char *record)`
- **Callers:** ClassicUi_RunLayoutScript
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Opcode 10: as opcode 9 with a second set of arguments for an alternate display mode.

## Behavior

- V: a global mode byte chooses between the arguments at +2..+4 (as opcode 9) and the ones at +5..+7.

## Open questions

None recorded.
