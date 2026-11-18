# MessageWindowTagCellsLanguage2

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1407B28F0`
- **Rows:** 20 rows of 12 bytes
- **Keyed by:** window kind 5..9 x 4 cells
- **Read by:** [MsgWindow_BuildFrame](../functions/MsgWindow_BuildFrame.md)
- **Row layout:** [UiSpriteCell](../structs/UiSpriteCell.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Sprite cells (4 per window kind 5..9) decorating message windows, language 2 variant. Verdict: designer-data.

## Behavior

- V: 0xF0 = 20 x 12; language switch 0 -> 0x1407B2AD0, 2 -> this, 3 -> 0x1407B2BC0, other -> 0x1407B29E0
- V: sub_14022BFEC (message window build) and its twin sub_1402E2C54: for window kinds 5..9 place four cells from (kind - 5) x 4

## Notes

Our names. Tags: V layout, ? kinds.

## Open questions

- ?: what the five window kinds are in game
