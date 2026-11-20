# NxdDataUIStatusEffect

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 57
- **Rows:** 45 rows of 36 bytes, text in 7 languages
- **Keyed by:** one key: id (1..1004)
- **Row layout:** [NxdDataUIStatusEffectRow](../structs/NxdDataUIStatusEffectRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Status effect names and captions (45) with a type. Verdict: designer-data.

## Behavior

- V: 45 rows, one key id (1..1004); measured over every row of the stock file.
- V: the 53 text tables have the same columns, keys, row size and table id in all seven languages (offline decode of every file).

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

None recorded.
