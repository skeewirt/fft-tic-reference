# StatusPanelLayoutsLanguage2

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x140808700`
- **Rows:** 8 rows of 8 bytes
- **Keyed by:** panel kind 0..7
- **Row layout:** [LayoutPointer](../structs/LayoutPointer.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Per status panel kind, its layout block, text language 2. Third of the four language copies behind StatusPanelLayoutsLanguage0.

## Behavior

- V: chosen when the language code is 2 (see StatusPanelLayoutsDefault)

## Notes

Our names. tags V.

## Open questions

- ?: layout block format
