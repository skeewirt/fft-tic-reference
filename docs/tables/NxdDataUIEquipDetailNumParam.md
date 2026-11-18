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
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 1 of 3 columns not decoded (see the row layout)
