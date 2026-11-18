# BattleSpriteFilesLanguage0

- **Kind:** table
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x140785210`
- **Rows:** 170 rows of 8 bytes
- **Keyed by:** unit sprite sheet id (unit record +1)
- **Row layout:** [SectorAndSize](../structs/SectorAndSize.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Where each battle sprite sheet's data is, for text language 0. Verdict: pointer-table.

## Behavior

- V: the 170 rows are {file number, size} pairs of numbers, not pointers; only 11 rows are filled (sheet ids 136..153), every filled size is 32768
- V: the table is byte-identical to the other-language table BattleSpriteFilesOtherLanguages
- V: the five-entry table of sheet 0x9A behind the other-language copy is a separate object (the table ends at 0x140785CB0)
- V: 0x550 = 170 x 8 to 0x140785760 (the other-language copy); HD texture guard < 0xAA agrees
- V: sub_140210AF0 (battle sprite load step): reads the sheet's data when the language is 0 (0x140785760 otherwise)

## Notes

Our names. Tags: V.

## Open questions

- ?: the five-entry table at 0x1407851E8 just before it (sheet 0x9A files by ability presentation byte 115..119) is a separate table
