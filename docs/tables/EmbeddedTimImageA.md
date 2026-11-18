# EmbeddedTimImageA

- **Kind:** table
- **Area:** [Resource](../areas/resource.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1407BDC70`
- **Rows:** 1 block of 2368 bytes
- **Keyed by:** single image
- **Read by:** [sub_140344B68](../functions/sub_140344B68.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A 4-bit image with its 16-colour palette in the legacy container format (magic 0x10, flags, palette block, image block), read by the world map code. Verdict: engine-data.

## Behavior

- V: sub_140344B68 passes the address of the flags word (base + 4) to TimImage_Parse
- V: the palette block length is 0x2C: 12 header bytes and 16 colours; its VRAM position is (0, 487)
- I: total length 0x940 bytes up to the next table

## Notes

Our names. Found beside the table at 0x1407BDC74; tags V container, I use.

## Open questions

None recorded.
