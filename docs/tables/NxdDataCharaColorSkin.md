# NxdDataCharaColorSkin

- **Kind:** table
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Storage:** NXD file
- **NXD table id:** 276
- **Rows:** 5 rows of 12 bytes
- **Keyed by:** two keys: id (0..1) x id2 (0..3)
- **Row layout:** [NxdDataCharaColorSkinRow](../structs/NxdDataCharaColorSkinRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Skin colour variants gated by a story-progress condition (UserSituation link). Verdict: designer-data.

## Behavior

- V: 5 rows, two keys id (0..1) x id2 (0..3); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 2 of 3 columns not decoded (see the row layout)
