# SpriteTablesEndAtSprite169

- **Kind:** observed behaviour
- **Scope:** engine (sprite number tables)
- **Area:** [Graphics](../areas/graphics.md)
- **Affects:** [Unit_GetSpriteSetId](../functions/Unit_GetSpriteSetId.md), [CharaPalette_LoadClassic](../functions/CharaPalette_LoadClassic.md), [SpriteId_ToShape](../functions/SpriteId_ToShape.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The tables indexed by sprite number all have 170 rows (sprites 0 to 169); the unit queue and the face readers compare against fixed bounds, so a sprite number above 169 needs every table and every bound to grow.

## Behavior

- V (read in the database, 2026-11-08): the HD sheet table at 0x1407151F0 holds a signed 32-bit first-sheet number per sprite (-1 = none; the second sheet is the next number); sprites 155 to 158 are -1, sprite 159 is 1110, sprite 164 is 1120, sprite 169 is 1130.
- V: the classic file table at 0x140784690 and its twin at 0x140784BE0 hold a file number and a size per sprite (8 bytes a row); sprites 87 to 92 and 96 share one file, 93 has its own, 155 to 158 are empty, 159 to 162 are 880 to 883 (the Dark Knight and Onion Knight pair of the handheld edition), 164 to 169 are 885 to 890. The twin matches the first table in the rows read.
- V: the sprite attribute table at 0x140673300 has 4 bytes a row and its row 170 already holds other data, so a sprite above 169 reads the neighbouring table.
- V: three word tables hold the classic portrait code per sprite at 0x140680070, 0x140683A70 and 0x1406807C0 (211 entries); rows 164 to 169 are 0 and rows 203 to 209 hold 0x71 to 0x77. Two readers compare the index with 0xD3 and take a no-code path above it (0x14032AC18 in sub_14032AB3C, 0x1402C0848 in Unit_GetSpriteSetId).
- V: the unit queue builder sub_1403041A4 loads 0xAA at 0x140304207 and compares the sprite number with it (jump if less).
- I (not each re-read by us): the other fixed bounds are 0xA9 or 0xAA at the HD sheet readers (0x1400CE263, 0x140261714, 0x1402617A4, 0x1402618EC, 0x14026C335, 0x14026F006, 0x14026F02D).

## Open questions

None recorded.
