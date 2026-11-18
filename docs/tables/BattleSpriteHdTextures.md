# BattleSpriteHdTextures

- **Kind:** table
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Storage:** Executable
- **Address:** `0x140714950`
- **Rows:** 170 rows of 4 bytes (172 to the next symbol)
- **Keyed by:** unit sprite sheet id (unit record +1)
- **Row layout:** [HdTextureId](../structs/HdTextureId.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Per battle sprite sheet, its HD texture id. Verdict: engine-data.

## Behavior

- V: 0x2B0 bytes = 172 entries to the next symbol; reader guard < 0xAA (170), so rows 0..169 are reachable
- V: the last two entries are zero padding, not sheets (seen in the data)
- V: sub_140210AF0 (battle sprite load step): for sheet < 0xAA at high graphics level, texture = table[sheet]

## Notes

Our names. Tags: V.

## Open questions

None recorded.
