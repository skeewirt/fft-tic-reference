# ClassicItemUi_OpIf

- **Address:** `0x14039AD90`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned char *ClassicItemUi_OpIf(unsigned char *record)`
- **Callers:** ClassicItemUsePage_Run (through the 25-slot handler table)
- **Callees:** the row callback, the handlers of the governed records

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 1 of the item page script: the conditional record.

## Behavior

- V: as UiScript_OpIf: +3 callback index, +4 governed record count, +5 immediate argument; run through the 25-slot item table (tbl_LegacyItemScriptOps) when the callback accepts, otherwise skipped by length.
- V: the row argument comes from the item page's own list globals and its row callback table (an array of callbacks indexed by +3).

## Open questions

None recorded.
