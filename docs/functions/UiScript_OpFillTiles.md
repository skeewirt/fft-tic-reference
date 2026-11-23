# UiScript_OpFillTiles

- **Address:** `0x140328490`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned char *UiScript_OpFillTiles(unsigned char *record)`
- **Callers:** UiScript_Run (handler table), UiScript_OpDrawWindow
- **Callees:** sub_14031DA24

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 17: fills a rectangle with 16-pixel tiles of one texture cell.

## Behavior

- V: record: +2 style, +3 x, +4 y, +5 and +6 width and height as tile count (high nibble) and remainder (low nibble); with style 2 the rectangle comes from the shared rectangle words filled by UiScript_OpDrawWindow.
- V: queues one cell per 16 x 16 tile from a fixed texture position, a remainder column (width = the remainder) at the left of each row and a remainder row after the full rows, with the window tint pointer and the default palette word.
- V: returns the pointer after the record.

## Referenced by

- Called by: [UiScript_OpDrawWindow](UiScript_OpDrawWindow.md)

## Notes

Same role as ClassicUi_OpTileGrid of the 22-slot table. The IDB return type is a byte pointer.

## Open questions

None recorded.
