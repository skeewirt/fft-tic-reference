# GfxTextureWindowParams

- **Kind:** table
- **Area:** [Graphics](../areas/graphics.md)
- **Storage:** Executable
- **Address:** `0x140811C38`
- **Rows:** 4 words (head of a 2048-byte object)
- **Keyed by:** word 0..3
- **Row layout:** [TextureWindowWordRow](../structs/TextureWindowWordRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Texture window parameter words (mask x / y, offset x / y) of a draw mode command. Verdict: engine-data.

## Behavior

- V: sub_1402600BC builds the window command from the four words (x mask, y mask, x offset, y offset)
- ?: the 2040 bytes after the head hold words that look like RGB555 colours and have no reader found

## Notes

Our names. Tags: V head, ? rest.

## Open questions

- ?: what the other 2040 bytes are
