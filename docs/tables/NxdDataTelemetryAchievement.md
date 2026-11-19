# NxdDataTelemetryAchievement

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 173
- **Rows:** 54 rows of 64 bytes, text in 7 languages
- **Keyed by:** one key: id (0..1049)
- **Row layout:** [NxdDataTelemetryAchievementRow](../structs/NxdDataTelemetryAchievementRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Achievement definitions for the platform (54): id strings, names, descriptions and parameters. Verdict: designer-data.

## Behavior

- V: 54 rows, one key id (0..1049); measured over every row of the stock file.
- V: the 53 text tables have the same columns, keys, row size and table id in all seven languages (offline decode of every file).

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 13 of 17 columns not decoded (see the row layout)
