# BattleSpriteFilesOtherLanguages

- **Kind:** table
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x140785760`
- **Rows:** 170 rows of 8 bytes
- **Keyed by:** unit sprite sheet id
- **Row layout:** [SectorAndSize](../structs/SectorAndSize.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Where each battle sprite sheet's data is, for text languages other than 0. Verdict: pointer-table.

## Behavior

- V: the 170 rows are {file number, size} pairs of numbers, not pointers; byte-identical to BattleSpriteFilesLanguage0
- V: 170 x 8 = 0x550 ends at 0x140785CB0, where the five-entry sheet 0x9A table for these languages starts (the symbol g_AbilityKind1_vbase at 0x140785CA8 is a virtual base, not a start)
- V: sub_140210AF0: as BattleSpriteFilesLanguage0, for languages other than 0

## Notes

Our names. Tags: V.

## Open questions

None recorded.
