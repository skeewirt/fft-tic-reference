# NxdDataTown

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 52
- **Rows:** 48 rows of 52 bytes, text in 7 languages
- **Keyed by:** one key: id (0..47)
- **Row layout:** [NxdDataTownRow](../structs/NxdDataTownRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Per town (48): description, place name link, condition and parameters. Verdict: designer-data.

## Behavior

- V: 48 rows, one key id (0..47); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.
- V: the 53 text tables have the same columns, keys, row size and table id in all seven languages (offline decode of every file).

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 13 of 17 columns not decoded (see the row layout); I: the other six languages share this layout (V by the offline decode in the title records); only the English file was extracted here
