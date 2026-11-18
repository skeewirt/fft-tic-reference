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
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 20 of 23 columns not decoded (see the row layout)
