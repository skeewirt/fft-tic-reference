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
- I: column roles not marked V are inferred from names and measured ranges.
- V: the 53 text tables have the same columns, keys, row size and table id in all seven languages (offline decode of every file).

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 5 of 10 columns not decoded (see the row layout); I: the other six languages share this layout (V by the offline decode in the title records); only the English file was extracted here
