# NxdDataScenarioId

- **Kind:** table
- **Area:** [Event system](../areas/event-system.md)
- **Storage:** NXD file
- **NXD table id:** 59
- **Rows:** 350 rows of 16 bytes
- **Keyed by:** one key: id (10..9991)
- **Row layout:** [NxdDataScenarioIdRow](../structs/NxdDataScenarioIdRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Scenario ids (350) with arrays of the event ids that belong to each. Verdict: designer-data.

## Behavior

- V: 350 rows, one key id (10..9991); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 2 of 3 columns not decoded (see the row layout)
