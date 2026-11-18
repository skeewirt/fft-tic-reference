# SpriteShapeHdTexture

- **Kind:** table
- **Area:** [Graphics](../areas/graphics.md)
- **Storage:** Executable
- **Address:** `0x140714C00`
- **Rows:** 82 rows of 4 bytes (84 to the next symbol)
- **Keyed by:** sprite shape 0..81
- **Read by:** [SpriteShape_ToHdTexture](../functions/SpriteShape_ToHdTexture.md)
- **Row layout:** [TextureIdRow](../structs/TextureIdRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

HD texture id per sprite shape (effect and scene sprites), -1 for none. Verdict: engine-data.

## Behavior

- V: the shape number 205 is first replaced by 76
- V: shapes 84..89, 104, 105 and 106..111 return fixed ids from 822 to 829 by compare chains; the rest return -1
- V: seen live 2026-11-15: the battle sprites of the story characters (shape 0 is Ramza) take their HD texture from this table: a row naming the texture of another shape drew his battle sprite with wrong art, and one id in every row drew Ramza and the guest blurred, while the generic job units (shapes above 81) did not change; the screen-chip builder that places a unit chip calls the same function

## Notes

Our names. Tags: V.

## Open questions

- ?: shapes above 81 are handled in code
