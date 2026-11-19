# NxdDataSystemBonusEntitlement

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 293
- **Rows:** 31 rows of 20 bytes
- **Keyed by:** one key: id (1..31)
- **Row layout:** [NxdDataSystemBonusEntitlementRow](../structs/NxdDataSystemBonusEntitlementRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Bonus entitlements (31): download path link and parameters. Verdict: designer-data.

## Behavior

- V: 31 rows, one key id (1..31); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 4 of 5 columns not decoded (see the row layout)
