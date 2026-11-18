# MessageWindowTagCellsDefault

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1407B29E0`
- **Rows:** 20 rows of 12 bytes
- **Keyed by:** window kind 5..9 x 4 cells
- **Read by:** [MsgWindow_BuildFrame](../functions/MsgWindow_BuildFrame.md)
- **Row layout:** [UiSpriteCell](../structs/UiSpriteCell.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Message window decoration cells, default (language 1) variant. Verdict: designer-data.

## Behavior

- V: 0xF0 = 20 x 12
- V: sub_14022BFEC / sub_1402E2C54 (default language)

## Notes

Our names. Tags: V layout.

## Open questions

- ?: window kinds
