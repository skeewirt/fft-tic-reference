# ClassicUi_OpIf

- **Address:** `0x140390024`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned char *ClassicUi_OpIf(unsigned char *record)`
- **Callers:** ClassicUi_RunLayoutScript
- **Callees:** the condition functions set by the page

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Opcode 1: runs the next records only when a page condition holds, otherwise skips them.

## Behavior

- V: the condition is a function of the page's condition table (0x141D3B630) chosen by byte +3, called with the argument at +5 or, in a list page, the current list row plus the page's row offset.
- V: byte +4 is the number of following records governed by the condition; when it is true they are run through the handler table, otherwise their lengths are added to skip them.

## Open questions

None recorded.
