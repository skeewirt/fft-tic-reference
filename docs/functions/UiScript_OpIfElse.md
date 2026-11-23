# UiScript_OpIfElse

- **Address:** `0x140327A04`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned char *UiScript_OpIfElse(unsigned char *record)`
- **Callers:** UiScript_Run (through the 29-slot handler table)
- **Callees:** the row callback, the handlers of the run records

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 2: as slot 1 with an else branch.

## Behavior

- V: record: +3 callback index, +4 count of then records, +5 count of else records (they follow in that order), +6 immediate argument; the argument rule is the one of slot 1.
- V: callback true: runs the then records and skips the else records; false: skips the then records and runs the else records. Skipping steps one record length per record, headers included; ?: whether scripts nest conditional records.
- V: returns the pointer after both branches.

## Open questions

None recorded.
