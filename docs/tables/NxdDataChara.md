# NxdDataChara

- **Kind:** table
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Storage:** NXD file
- **NXD table id:** 274
- **Rows:** 131 rows of 8 bytes
- **Keyed by:** one key: id (0..130)
- **Row layout:** [NxdDataCharaRow](../structs/NxdDataCharaRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Index of 131 character ids with one flag column. Verdict: engine-data.

## Behavior

- V: 131 rows, one key id (0..130); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 1 of 2 columns not decoded (see the row layout)
