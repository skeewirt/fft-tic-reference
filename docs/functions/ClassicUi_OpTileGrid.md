# ClassicUi_OpTileGrid

- **Address:** `0x140390800`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned char *ClassicUi_OpTileGrid(unsigned char *record)`
- **Callers:** ClassicUi_RunLayoutScript, ClassicUi_OpWindowFrame
- **Callees:** sub_14038F3FC

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Opcode 17: fills a rectangle with 8 x 8 tiles.

## Behavior

- V: arguments are the origin (+3, +4), the tile columns in the high nibble of +5 and the remainder width in its low nibble, and the rows in the high nibble of +6 and the remainder height in its low nibble.
- V: queues one tile per 16 pixels, then a partial last column and a partial last row.

## Referenced by

- Called by: [ClassicUi_OpWindowFrame](ClassicUi_OpWindowFrame.md)

## Open questions

None recorded.
