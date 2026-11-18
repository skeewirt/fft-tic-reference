# NxdDataBattle

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** NXD file
- **NXD table id:** 83
- **Rows:** 713 rows of 4 bytes
- **Keyed by:** one key: id (0..743)
- **Row layout:** [NxdDataBattleRow](../structs/NxdDataBattleRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Index of battle ids: the rows carry no data column besides the DLC gate; other tables key off these ids. Verdict: engine-data.

## Behavior

- V: 713 rows, one key id (0..743); measured over every row of the stock file.
- I: the table role and the column roles are inferred from the table and column names and the measured value ranges; not traced to a reader, except where a column line says V.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? no reader found by table-id constant (readers may fetch it through a name or a runtime-computed id)
