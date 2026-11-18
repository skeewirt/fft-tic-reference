# NxdDataUIPadGuide

- **Kind:** table
- **Area:** [Input](../areas/input.md)
- **Storage:** NXD file
- **NXD table id:** 278
- **Rows:** 15 rows of 44 bytes
- **Keyed by:** one key: id (0..14)
- **Row layout:** [NxdDataUIPadGuideRow](../structs/NxdDataUIPadGuideRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Pad guide layouts (15). Verdict: designer-data.

## Behavior

- V: 15 rows, one key id (0..14); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 10 of 11 columns not decoded (see the row layout)
