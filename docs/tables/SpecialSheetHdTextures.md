# SpecialSheetHdTextures

- **Kind:** table
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Storage:** Executable
- **Address:** `0x14071500C`
- **Rows:** 119 rows of 4 bytes (121 to the next symbol)
- **Keyed by:** ability presentation byte (exe.ability.anim +1)
- **Row layout:** [HdTextureId](../structs/HdTextureId.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

HD texture ids for the per-ability sheets of sprite sheet 0x9A. Verdict: engine-data.

## Behavior

- V: 0x1E4 bytes = 121 entries to the next symbol; the reader tests the presentation byte minus 115 against 3 as a signed value, so rows 0..118 are reachable
- V: the last two entries are zero padding (seen in the data)
- V: sub_140210AF0: for sprite sheet 0x9A only, the sheet file and its HD texture are chosen by the ability presentation byte (115..119 for the file)

## Notes

Our names. Tags: V layout, I meaning.

## Open questions

- ?: which unit uses sheet 0x9A
