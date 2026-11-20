# NxdDataMapVariationRandomBattle

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** NXD file
- **NXD table id:** 208
- **Rows:** 7 rows of 8 bytes
- **Keyed by:** one key: id (0..6)
- **Row layout:** [NxdDataMapVariationRandomBattleRow](../structs/NxdDataMapVariationRandomBattleRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Map variations for random battles (7). Verdict: designer-data.

## Behavior

- V: 7 rows, one key id (0..6); measured over every row of the stock file.
- I: the table role and the column roles are inferred from the table and column names and the measured value ranges; not traced to a reader, except where a column line says V.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

None recorded.
