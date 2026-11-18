# NxdDataUIButtonGuide

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** NXD file
- **NXD table id:** 33
- **Rows:** 1152 rows of 40 bytes
- **Keyed by:** two keys: id (0..23011) x id2 (0..10)
- **Row layout:** [NxdDataUIButtonGuideRow](../structs/NxdDataUIButtonGuideRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Button guide footer layouts keyed by screen and slot (1152). Verdict: designer-data.

## Behavior

- V: 1152 rows, two keys id (0..23011) x id2 (0..10); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 12 of 13 columns not decoded (see the row layout)
