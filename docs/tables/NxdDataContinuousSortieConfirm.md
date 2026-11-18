# NxdDataContinuousSortieConfirm

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** NXD file
- **NXD table id:** 230
- **Rows:** 27 rows of 108 bytes
- **Keyed by:** two keys: id (0..25) x id2 (0..1)
- **Read by:** [SaveLoadList_FillItem](../functions/SaveLoadList_FillItem.md)
- **Row layout:** [NxdDataContinuousSortieConfirmRow](../structs/NxdDataContinuousSortieConfirmRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Sortie confirmation parameters for chained battles, keyed by battle and part. Verdict: designer-data.

## Behavior

- V: 27 rows, two keys id (0..25) x id2 (0..1); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 21 of 22 columns not decoded (see the row layout)
