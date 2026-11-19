# NxdDataWorldSituationBalloon

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 286
- **Rows:** 90 rows of 76 bytes
- **Keyed by:** two keys: id (0..30) x id2 (0..6)
- **Row layout:** [NxdDataWorldSituationBalloonRow](../structs/NxdDataWorldSituationBalloonRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

World situation balloons keyed by period and slot (90). Verdict: designer-data.

## Behavior

- V: 90 rows, two keys id (0..30) x id2 (0..6); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 22 of 23 columns not decoded (see the row layout)
