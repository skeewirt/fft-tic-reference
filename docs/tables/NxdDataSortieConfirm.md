# NxdDataSortieConfirm

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** NXD file
- **NXD table id:** 54
- **Rows:** 375 rows of 48 bytes
- **Keyed by:** one key: id (0..374)
- **Row layout:** [NxdDataSortieConfirmRow](../structs/NxdDataSortieConfirmRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Sortie confirmation screens (375): map link, UI text keys for event, max units and threat rating. Verdict: designer-data.

## Behavior

- V: 375 rows, one key id (0..374); measured over every row of the stock file.
- I: the table role and the column roles are inferred from the table and column names and the measured value ranges; not traced to a reader, except where a column line says V.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? no reader found by table-id constant (readers may fetch it through a name or a runtime-computed id); ? 7 of 12 columns not decoded (see the row layout)
