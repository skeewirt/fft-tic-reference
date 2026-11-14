# EnhancedDrawsHdSheetsWithTheClassicFilePalette

- **Kind:** observed behaviour
- **Scope:** engine (unit sprites)
- **Area:** [Graphics](../areas/graphics.md)
- **Affects:** [CharaPalette_LoadClassic](../functions/CharaPalette_LoadClassic.md), [GameData_ReadSectors](../functions/GameData_ReadSectors.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

In the enhanced build a unit's HD sprite sheet is drawn with the palette taken from the classic sprite file named in the classic file table, so the colours follow that file, not the sheet.

## Behavior

- I (reported from play, 3 runs): a job given its own HD sheet while its classic row pointed at another job's file was drawn in the other job's colours; swapping the two sheets between jobs moved the shape and left the colours with the job.
- V (read in the database): the classic file is read by a call to GameData_ReadSectors at 0x14026E7C1 in CharaPalette_LoadClassic, and the battle loader makes a second such call at 0x14026FE7B.
- I: at both calls the table is the classic table or its twin and the sprite number is in a register.
- I: only the first 0x200 bytes of the classic file (the palettes) are used by the enhanced build.

## Open questions

None recorded.
