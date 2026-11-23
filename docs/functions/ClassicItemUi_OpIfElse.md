# ClassicItemUi_OpIfElse

- **Address:** `0x14039AE40`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned char *ClassicItemUi_OpIfElse(unsigned char *record)`
- **Callers:** ClassicItemUsePage_Run (through the 25-slot handler table)
- **Callees:** the row callback, the handlers of the run records

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 2 of the item page script: the conditional record with an else branch.

## Behavior

- V: as UiScript_OpIfElse: +3 callback index, +4 then count, +5 else count, +6 immediate argument; the branch records are run through the 25-slot item table or skipped by length.
- V: the row argument comes from the item page's own list globals and its row callback table (an array of callbacks indexed by +3).

## Open questions

None recorded.
