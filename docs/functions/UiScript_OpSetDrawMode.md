# UiScript_OpSetDrawMode

- **Address:** `0x14032888C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned char *UiScript_OpSetDrawMode(unsigned char *record)`
- **Callers:** UiScript_Run (through the 29-slot handler table)
- **Callees:** Prim_QueueDrawModeChange (mode primitive queue)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 24: queues a draw-mode change: a blend mode from +2 and 3.

## Behavior

- V: queues a mode primitive whose value is (32 * (+2 and 3)) | 4, with the current priority, through Prim_QueueDrawModeChange (the extra register arguments pass through unchanged and the callee does not use them). I: the | 4 is a fixed page base.
- V: returns the pointer after the record.
- I: the IDB signature (four arguments) over-declares; the handler takes the record pointer only.

## State touched

- Calls: [Prim_QueueDrawModeChange](Prim_QueueDrawModeChange.md)

## Notes

Item-page twin ClassicItemUi_OpSetDrawMode builds the same entry inline.

## Open questions

None recorded.
