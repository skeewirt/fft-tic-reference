# UiScript_OpDrawWindow

- **Address:** `0x140327DAC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned char *UiScript_OpDrawWindow(unsigned char *record)`
- **Callers:** UiScript_Run, UiScript_OpDrawWindowOpening (tail call), sub_14021C620
- **Callees:** sub_14031DA24 (cell queue), UiScript_OpFillTiles

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 0: draws a bordered window of a given size and fills its inside.

## Behavior

- V: record: +2 style (1, 2 or another value), +3 x, +4 y, +5 and +6 pixel width and height (tile count in the high nibble, remainder in the low nibble). With style 2 the rectangle is read from a global rectangle record (x, y, width, height) and copied to a shared rectangle for the fill.
- V: the frame is drawn 5 pixels left of and 9 above the origin; cells come from fixed texture positions that differ for style 1 and the other styles, with 16-pixel edge pieces repeated along the sides and a remainder piece.
- V: it queues the top edge and the side pieces, calls UiScript_OpFillTiles on a scratch record for the inside, then queues the lower edge pieces.
- V: stores the style and the sum of x and the packed width byte (+5; tile count in the high nibble, remainder in the low nibble; UiScript_OpScrollList uses it as the x of its up and down marks) in shared words and returns the pointer after the record.
- I: the lower edge is the second batch of cell calls (order of the calls).

## State touched

- Calls: [UiScript_OpFillTiles](UiScript_OpFillTiles.md)

## Referenced by

- Called by: [UiScript_OpDrawWindowOpening](UiScript_OpDrawWindowOpening.md)

## Notes

The item-page twin ClassicItemUi_OpDrawWindow has no style-2 rectangle case and draws without a tint.

## Open questions

?: the visual meaning of the styles.
