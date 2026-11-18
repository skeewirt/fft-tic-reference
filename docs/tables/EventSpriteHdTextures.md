# EventSpriteHdTextures

- **Kind:** table
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Storage:** Executable
- **Address:** `0x140714490`
- **Rows:** 144 rows of 4 bytes
- **Keyed by:** event sprite number (evtchr)
- **Read by:** [EventSprite_LoadTask](../functions/EventSprite_LoadTask.md)
- **Row layout:** [HdTextureId](../structs/HdTextureId.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Per event character sprite, its HD texture id. Verdict: engine-data.

## Behavior

- V: 0x240 bytes = 144 entries to the next symbol
- V: EventSprite_LoadTask (opcode 0x58 task): at high graphics level, stores table[n] and table[n] + 140 for display side 0 or 1

## Notes

Our names. Tags: V.

## Open questions

- ?: what the + 140 texture is
