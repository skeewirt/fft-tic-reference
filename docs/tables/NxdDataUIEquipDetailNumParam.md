# NxdDataUIEquipDetailNumParam

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** NXD file
- **NXD table id:** 198
- **Rows:** 9 rows of 12 bytes
- **Keyed by:** two keys: id (0..4) x id2 (0..1)
- **Read by:** [EquipDetail_Refresh](../functions/EquipDetail_Refresh.md)
- **Row layout:** [NxdDataUIEquipDetailNumParamRow](../structs/NxdDataUIEquipDetailNumParamRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Equipment detail number fields, keyed by field and variant. Verdict: engine-data.

## Behavior

- V: 9 rows, two keys id (0..4) x id2 (0..1); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 2 of 3 columns not decoded (see the row layout)
