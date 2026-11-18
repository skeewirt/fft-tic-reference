# BannerWordColours

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1408073F4`
- **Rows:** 4 rows of 4 bytes
- **Keyed by:** quad corner 0..3
- **Read by:** [BannerWord_Draw](../functions/BannerWord_Draw.md)
- **Row layout:** [CornerColour](../structs/CornerColour.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Corner colours of the banner word gradient. Verdict: designer-data.

## Behavior

- V: four 4-byte groups, read field by field
- V: sub_140227AD8: writes the four corner colours of every banner quad

## Notes

Our names. Tags: V.

## Open questions

- ?: earlier research took bytes +8/+9 as a unit-record copy; in this reader they are a primitive's corner colour
