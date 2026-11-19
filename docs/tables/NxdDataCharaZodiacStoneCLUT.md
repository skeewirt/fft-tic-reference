# NxdDataCharaZodiacStoneCLUT

- **Kind:** table
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Storage:** NXD file
- **NXD table id:** 302
- **Rows:** 25 rows of 16 bytes
- **Keyed by:** one key: id (1..25)
- **Read by:** [SceneUnit_BuildPalette](../functions/SceneUnit_BuildPalette.md)
- **Row layout:** [NxdDataCharaZodiacStoneCLUTRow](../structs/NxdDataCharaZodiacStoneCLUTRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Palette byte blobs for the 25 zodiac stone looks. Verdict: engine-data.

## Behavior

- V: 25 rows, one key id (1..25); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 2 of 3 columns not decoded (see the row layout)
