# StatusPanelLayoutsDefault

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1408086C0`
- **Rows:** 8 rows of 8 bytes
- **Keyed by:** panel kind 0..7
- **Row layout:** [LayoutPointer](../structs/LayoutPointer.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Per status panel kind, its layout block, for text languages 1 and every language that has no table of its own. Second of the four language copies behind StatusPanelLayoutsLanguage0.

## Behavior

- V: the reader picks the table from the language code: 0 takes the table at 0x140808680, 3 the one at 0x140808740, 2 the one at 0x140808700, every other code this table
- V: all eight pointers differ from the language 0 table (the four copies share no pointer value in the same slot)

## Notes

Our names. This copy was found by the language switch of the reader; tags V.

## Open questions

- ?: layout block format
