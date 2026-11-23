# ClassicUi_OpQueueScreenRectOnce

- **Address:** `0x140391AA4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned char *ClassicUi_OpQueueScreenRectOnce(unsigned char *record)`
- **Callers:** ClassicUi_RunLayoutScript (through the 22-slot handler table)
- **Callees:** sub_14038F5FC

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 19 of the layout script table: the fixed screen rectangle once.

## Behavior

- V: while a flag byte is set it zeroes the y word of a fixed four-word rectangle, queues it through sub_14038F5FC at the incremented priority word (adding 2 to the priority word in all), and clears the flag; returns the pointer after the record.

## Open questions

?: why the priority word moves by two.
