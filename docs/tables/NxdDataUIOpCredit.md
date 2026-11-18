# NxdDataUIOpCredit

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 316
- **Rows:** 130 rows of 32 bytes
- **Keyed by:** two keys: id (0..1200) x id2 (0..7)
- **Row layout:** [NxdDataUIOpCreditRow](../structs/NxdDataUIOpCreditRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Opening credit rows keyed by credit and part. Verdict: designer-data.

## Behavior

- V: 130 rows, two keys id (0..1200) x id2 (0..7); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 6 of 8 columns not decoded (see the row layout)
