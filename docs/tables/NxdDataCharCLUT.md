# NxdDataCharCLUT

- **Kind:** table
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Storage:** NXD file
- **NXD table id:** 210
- **Rows:** 16 rows of 24 bytes
- **Keyed by:** two keys: id (1..255) x id2 (0..3)
- **Read by:** [CharClut_ApplyToPalette](../functions/CharClut_ApplyToPalette.md)
- **Row layout:** [NxdDataCharCLUTRow](../structs/NxdDataCharCLUTRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Character palette (colour lookup) definitions: a byte blob of colours per palette id and variant, plus a skin colour link. Verdict: engine-data.

## Behavior

- V: 16 rows, two keys id (1..255) x id2 (0..3); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

None recorded.
