# TextNodeDrawGate

- **Kind:** observed behaviour
- **Scope:** UI text nodes (GUITextNode_Draw)
- **Area:** [UI framework](../areas/ui-framework.md)
- **Affects:** [GUITextNode_Draw](../functions/GUITextNode_Draw.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

GUITextNode_Draw returns before drawing unless a byte at node +0xCC is non-zero, a byte at +0x91 is zero, the string size at +0xE8 is non-zero and a font-table / font-set lookup returns true. Draw is still called for a node that fails the gate, so a call is not evidence that text was drawn.

## Behavior

- V (decompile and disassembly of the entry, 2026-10-31): the four tests run in that order and a failure jumps to the end of the function before any glyph is emitted.
- V: the font test calls sub_1403DBA94(font table, node +0x12C); the string size is the qword at +0xE8, and the two bytes are +0xCC and +0x91 (decompile).

## Notes

V: the gate runs at the top of the function, so a closed gate also skips the palette upload and the batch flush the body would do.

## Open questions

? which writer clears +0xCC and sets +0xE8 on the banner's Title node.
