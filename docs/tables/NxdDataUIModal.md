# NxdDataUIModal

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** NXD file
- **NXD table id:** 333
- **Rows:** 27 rows of 24 bytes
- **Keyed by:** one key: id (1..27)
- **Row layout:** [NxdDataUIModalRow](../structs/NxdDataUIModalRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Modal window definitions (27). Verdict: designer-data.

## Behavior

- V: 27 rows, one key id (1..27); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 3 of 5 columns not decoded (see the row layout)
