# SpriteDirectionTables

- **Kind:** table
- **Area:** [Graphics](../areas/graphics.md)
- **Storage:** Executable
- **Address:** `0x140672CE8`
- **Rows:** 184 bytes in six sub-tables
- **Keyed by:** facing 0..3, phase 0..15
- **Read by:** [SpriteRecord_Fill](../functions/SpriteRecord_Fill.md), [SpriteRecord_SetPaletteBits](../functions/SpriteRecord_SetPaletteBits.md)
- **Row layout:** [SpriteDirectionTablesRow](../structs/SpriteDirectionTablesRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Small per-facing tables read by the sprite record code: mirror flag words, frame flag masks, walk phase steps and palette base words. Verdict: engine-data.

## Behavior

- V: SpriteRecord_Fill and SpriteRecord_SetPaletteBits read the facing word (sprite facing modulo 4): bit 1 selects the mirrored sprite and the palette number is the request plus the palette base word
- V: the leading 16 bytes count 0..15 and have no reader of their own

## Notes

Our names. Tags: V block members, I some meanings.

## Open questions

- ?: exact meaning of the frame flag masks
- ?: the identity bytes have no reader
