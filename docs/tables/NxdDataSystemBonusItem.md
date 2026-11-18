# NxdDataSystemBonusItem

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 297
- **Rows:** 3 rows of 24 bytes, text in 7 languages
- **Keyed by:** one key: id (0..2)
- **Row layout:** [NxdDataSystemBonusItemRow](../structs/NxdDataSystemBonusItemRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Bonus item list (3): title, description and a typed reference. Verdict: designer-data.

## Behavior

- V: 3 rows, one key id (0..2); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.
- V: the 53 text tables have the same columns, keys, row size and table id in all seven languages (offline decode of every file).

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

I: the other six languages share this layout (V by the offline decode in the title records); only the English file was extracted here
