# StatusPanelLayoutsLanguage3

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x140808740`
- **Rows:** 8 rows of 8 bytes
- **Keyed by:** panel kind 0..7
- **Row layout:** [LayoutPointer](../structs/LayoutPointer.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Per status panel kind, its layout block, text language 3. Fourth of the four language copies behind StatusPanelLayoutsLanguage0.

## Behavior

- V: chosen when the language code is 3 (see StatusPanelLayoutsDefault)
- V: the eight pointers are followed by two data words that are not pointers

## Notes

Our names. tags V.

## Open questions

- ?: layout block format
