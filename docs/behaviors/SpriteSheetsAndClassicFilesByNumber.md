# SpriteSheetsAndClassicFilesByNumber

- **Kind:** observed behaviour
- **Scope:** engine (asset loading)
- **Area:** [Data access](../areas/data.md)
- **Affects:** [sub_1403D2450](../functions/sub_1403D2450.md), [GameData_ReadSectors](../functions/GameData_ReadSectors.md), [CharaPalette_LoadClassic](../functions/CharaPalette_LoadClassic.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

HD sprite sheets are read by number and the loader accepts any number; classic sprite files are read by name only.

## Behavior

- I: the sheet loader entries 0x1403D2450 (load), 0x1403D25D8 (decode) and 0x1403D25A4 (unload) accept any number, so a file named tex_<N>.bin under system/ffto/g2d is served for N above 2449, past the game's own table of contents.
- I: classic files are mapped only by names already in the game's file list, so a name at an empty number is ignored (see EnhancedDrawsHdSheetsWithTheClassicFilePalette).
- V (read in the database): the first-sheet row of sprite 164 is 1120, so the sprite tables hold the entry numbers of the game's own g2d container directly (its table has 2450 entries, see sprites.md).

## Open questions

None recorded.
