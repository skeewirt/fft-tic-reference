# NxdDataUICreditLineArt

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 304
- **Rows:** 19 rows of 8 bytes
- **Keyed by:** one key: id (0..18)
- **Row layout:** [NxdDataUICreditLineArtRow](../structs/NxdDataUICreditLineArtRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Credit line art UI names (19). Verdict: engine-data.

## Behavior

- V: 19 rows, one key id (0..18); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 1 of 2 columns not decoded (see the row layout)
