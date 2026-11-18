# ClassicUi_OpWindowFrame

- **Address:** `0x140390294`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned char *ClassicUi_OpWindowFrame(unsigned char *record)`
- **Callers:** ClassicUi_RunLayoutScript, ClassicUi_OpAnimatedFrame
- **Callees:** sub_14038F3FC (queue one cell), ClassicUi_OpTileGrid

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Opcode 0: draws a bordered window of a given size at a position.

## Behavior

- V: arguments are the origin x (+3) and y (+4), the width in tiles and a remainder (+5) and the height (+6) packed as nibbles.
- V: draws the four corner / edge cells from fixed cell positions in the page texture, repeats edge cells along each side, then fills the inside through the tile grid handler on a scratch record.
- V: stores the window's right edge in a shared word for later records.

## State touched

- Calls: [ClassicUi_OpTileGrid](ClassicUi_OpTileGrid.md)

## Referenced by

- Called by: [ClassicUi_OpAnimatedFrame](ClassicUi_OpAnimatedFrame.md)

## Open questions

None recorded.
