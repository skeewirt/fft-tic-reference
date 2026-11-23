# ClassicItemUi_OpDrawWindowOpening

- **Address:** `0x14039B81C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned char *ClassicItemUi_OpDrawWindowOpening(unsigned char *record)`
- **Callers:** ClassicItemUsePage_Run (through the 25-slot handler table)
- **Callees:** sub_140395734, ClassicItemUi_OpDrawWindow

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 18 of the item page script: the opening window.

## Behavior

- V: as UiScript_OpDrawWindowOpening (same record layout and result), over the draw globals of the item pages; the differences are listed below.
- V: same stage test, percentage scaling table and animating byte; the scaled box goes through sub_140395734 and the record is then run through ClassicItemUi_OpDrawWindow.

## State touched

- Calls: [ClassicItemUi_OpDrawWindow](ClassicItemUi_OpDrawWindow.md)

## Open questions

None recorded.
