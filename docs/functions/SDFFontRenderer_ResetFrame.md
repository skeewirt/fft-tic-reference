# SDFFontRenderer_ResetFrame

- **Address:** `0x1403A9100`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 SDFFontRenderer_ResetFrame(__int64 renderer)`
- **Callers:** vftable 0x1407208E0 (data reference)
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Virtual slot that clears the per-frame emit counters so the next frame starts at quad / batch index 0.

## Behavior

- V: the qword at renderer + 9516 is set to 0 - an 8-byte store covering two adjacent dwords at +9516 and +9520 (quad counts; exact split not read).
- V: the qword at renderer + 7944 is set to 0 - the batch count (+7944, the count Flush sorts) and the dword at +7948 are cleared together.
- V: returns 0. No buffers are freed or cleared, only counters.
- V: only xref is the data reference at 0x1407208E0 (SDFFontRenderer vftable); no direct call sites.

## Notes

Counterpart of the emit counters used by SDFFontRenderer_EmitGlyph and consumed by SDFFontRenderer_Flush.

## Open questions

? which of +9516 / +9520 is the quad count and which the other counter. ? what +7948 is.
