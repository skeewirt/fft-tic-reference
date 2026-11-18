# NxdDataConfigItemEnableDOF

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** NXD file
- **NXD table id:** 271
- **Rows:** 3 rows of 12 bytes
- **Keyed by:** one key: id (0..2)
- **Row layout:** [NxdDataConfigItemEnableDOFRow](../structs/NxdDataConfigItemEnableDOFRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Option values for the depth-of-field setting. Verdict: engine-data.

## Behavior

- V: 3 rows, one key id (0..2); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 2 of 3 columns not decoded (see the row layout)
