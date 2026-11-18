# BannerWords_FillQuads

- **Address:** `0x1402DF154`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int BannerWords_FillQuads(int banner, char *primitives)`
- **Callers:** not recorded
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills the gradient quads of one banner (a row of word cells) from the legacy banner tables.

## Behavior

- V: start = range table [banner] and count = range table [banner + 1] minus start; the range table (0x1406818F0) and the cell table (0x1408E3950, reached with a RIP-relative address, so it is not an immediate of the body) are copies of the stock banner tables.
- V: for each cell writes the four vertex positions (x from the cell x plus the origin, y, width, height), the texture u / v of the four corners and the four vertex colours taken from the first 16 bytes of the colour table (0x1408E42E4).
- V: for language 2 the cells are shifted by a few pixels (13, or an offset taken from the narrowest cell for one special cell).
- V: returns the number of cells.

## Notes

Read in full; the same job as the banner word drawer of the battle screens.

## Open questions

?: why language 2 needs the shift.
