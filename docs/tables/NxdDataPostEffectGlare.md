# NxdDataPostEffectGlare

- **Kind:** table
- **Area:** [Graphics](../areas/graphics.md)
- **Storage:** NXD file
- **NXD table id:** 256
- **Rows:** 19 rows of 24 bytes
- **Keyed by:** one key: id (1..19)
- **Read by:** [EventCharaSprite_SetTable256Entry](../functions/EventCharaSprite_SetTable256Entry.md)
- **Row layout:** [NxdDataPostEffectGlareRow](../structs/NxdDataPostEffectGlareRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Glare parameters (19). Verdict: engine-data.

## Behavior

- V: 19 rows, one key id (1..19); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 6 of 6 columns not decoded (see the row layout)
