# NxdDataCharaName

- **Kind:** table
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Storage:** NXD file
- **NXD table id:** 93
- **Rows:** 1024 rows of 24 bytes, text in 7 languages
- **Keyed by:** one key: id (0..1023)
- **Row layout:** [NxdDataCharaNameRow](../structs/NxdDataCharaNameRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Character names (1024 ids), a typed reference column and a generic-unit flag. Verdict: designer-data.

## Behavior

- V: 1024 rows, one key id (0..1023); measured over every row of the stock file.
- I: the table role and the column roles are inferred from the table and column names and the measured value ranges; not traced to a reader, except where a column line says V.
- V: the 53 text tables have the same columns, keys, row size and table id in all seven languages (offline decode of every file).

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? no reader found by table-id constant (readers may fetch it through a name or a runtime-computed id); ? 1 of 5 columns not decoded (see the row layout); I: the other six languages share this layout (V by the offline decode in the title records); only the English file was extracted here
