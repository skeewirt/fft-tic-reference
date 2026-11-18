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
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

None recorded.
