# ClassicUi_OpQueueRect

- **Address:** `0x140391B04`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned char *ClassicUi_OpQueueRect(unsigned char *record)`
- **Callers:** ClassicUi_RunLayoutScript (through the 22-slot handler table)
- **Callees:** sub_14038F5FC

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 20 of the layout script table: a rectangle from the record.

## Behavior

- V: record: +2 x, +3 y, +4 width (0xFF means 374), +5 height; while the flag byte is 0 it is queued through sub_14038F5FC one priority level below the priority word; returns the pointer after the record.

## Open questions

None recorded.
