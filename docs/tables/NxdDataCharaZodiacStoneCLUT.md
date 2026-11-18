# NxdDataCharaZodiacStoneCLUT

- **Kind:** table
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Storage:** NXD file
- **NXD table id:** 302
- **Rows:** 25 rows of 16 bytes
- **Keyed by:** one key: id (1..25)
- **Read by:** [SceneUnit_BuildPalette](../functions/SceneUnit_BuildPalette.md)
- **Row layout:** [NxdDataCharaZodiacStoneCLUTRow](../structs/NxdDataCharaZodiacStoneCLUTRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Palette byte blobs for the 25 zodiac stone looks. Verdict: engine-data.

## Behavior

- V: 25 rows, one key id (1..25); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

None recorded.
