# NxdDataShopVoice

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 178
- **Rows:** 131 rows of 16 bytes
- **Keyed by:** two keys: id (1..355) x id2 (0..2)
- **Row layout:** [NxdDataShopVoiceRow](../structs/NxdDataShopVoiceRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Shop voice lines keyed by shop and line, each pointing at a packed audio entry. Verdict: designer-data.

## Behavior

- V: 131 rows, two keys id (1..355) x id2 (0..2); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 1 of 4 columns not decoded (see the row layout)
