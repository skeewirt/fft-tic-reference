# GfxPacket_QueueRect

- **Address:** `0x140395698`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 __fastcall GfxPacket_QueueRect(RECT16 *rect, int, __int16 value, int slot)`
- **Callers:** ClassicItemUi_OpScrollList (two calls)
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Takes the next 32-byte packet from the draw packet pool, fills it with a rectangle and a value and links it at the head of an ordering list.

## Behavior

- V: the pool is at `*(qword_141D3B798 + 176)`; the next packet is `pool + 32 * word_141D3B820`, and `word_141D3B820` is incremented (no bound check).
- V: fills the packet: type word at +10 = 6, rect x and y at +20 and +22, 256 at +24, rect width and height at +28 and +30, `value` at +26, byte 0xF3 at +15, and the current `word_14114A4E4` at +8.
- V: links it at the head of list `slot`: the list head table is `*qword_141D3B798` and each head is 16 bytes apart; the packet's first qword takes the old head and the head points at the packet.
- V: returns `word_14114A4E4` (zero-extended). The second argument is not used.
- I: this is a draw-order list with one list per depth slot and the packet is a rectangle copy or fill (rests on the head-of-list push and the rectangle fields; the type 6 is not decoded).

## Referenced by

- Called by: [ClassicItemUi_OpScrollList](ClassicItemUi_OpScrollList.md)

## Notes

V: whole body read. The name is ours.

## Open questions

?: the packet type 6 and byte 0xF3, and what `word_14114A4E4` holds.
