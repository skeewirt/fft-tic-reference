# NxdDataCollection

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 121
- **Rows:** 43 rows of 44 bytes, text in 7 languages
- **Keyed by:** one key: id (0..42)
- **Row layout:** [NxdDataCollectionRow](../structs/NxdDataCollectionRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Collection entries (43): name, description and numeric parameters. Verdict: designer-data.

## Behavior

- V: 43 rows, one key id (0..42); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.
- V: the 53 text tables have the same columns, keys, row size and table id in all seven languages (offline decode of every file).

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 7 of 11 columns not decoded (see the row layout); I: the other six languages share this layout (V by the offline decode in the title records); only the English file was extracted here
