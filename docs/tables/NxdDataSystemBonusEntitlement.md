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
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 2 of 5 columns not decoded (see the row layout)
