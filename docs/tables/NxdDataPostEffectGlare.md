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
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 4 of 6 columns not decoded (see the row layout)
