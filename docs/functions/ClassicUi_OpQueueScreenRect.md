# ClassicUi_OpQueueScreenRect

- **Address:** `0x140391B68`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned char *ClassicUi_OpQueueScreenRect(unsigned char *record)`
- **Callers:** ClassicUi_RunLayoutScript (through the 22-slot handler table)
- **Callees:** sub_14038F5FC

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 21 of the layout script table: the fixed screen rectangle.

## Behavior

- V: while the flag byte is 0: zeroes the fixed rectangle's y word and queues it through sub_14038F5FC one priority level above the priority word; returns the pointer after the record.

## Open questions

None recorded.
