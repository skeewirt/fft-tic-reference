# NxdDataUiJobAbilityHelp

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 303
- **Rows:** 35 rows of 12 bytes, text in 7 languages
- **Keyed by:** one key: id (0..34)
- **Row layout:** [NxdDataUiJobAbilityHelpRow](../structs/NxdDataUiJobAbilityHelpRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Job ability help texts (35). Verdict: text.

## Behavior

- V: 35 rows, one key id (0..34); measured over every row of the stock file.
- I: the table role and the column roles are inferred from the table and column names and the measured value ranges; not traced to a reader, except where a column line says V.
- V: the 53 text tables have the same columns, keys, row size and table id in all seven languages (offline decode of every file).

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? no reader found by table-id constant (readers may fetch it through a name or a runtime-computed id); I: the other six languages share this layout (V by the offline decode in the title records); only the English file was extracted here
