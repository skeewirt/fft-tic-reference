# NxdDataCharaControlId

- **Kind:** table
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Storage:** NXD file
- **NXD table id:** 218
- **Rows:** 87 rows of 12 bytes
- **Keyed by:** one key: id (0..1006)
- **Read by:** [OverrideEntry_FillUnitEntry](../functions/OverrideEntry_FillUnitEntry.md)
- **Row layout:** [NxdDataCharaControlIdRow](../structs/NxdDataCharaControlIdRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Maps character control ids (up to 1006) to a character number. Verdict: engine-data.

## Behavior

- V: 87 rows, one key id (0..1006); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 3 of 3 columns not decoded (see the row layout)
