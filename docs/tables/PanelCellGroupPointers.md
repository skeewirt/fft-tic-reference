# PanelCellGroupPointers

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1408E54D0`
- **Rows:** 32 rows of 8 bytes
- **Keyed by:** language group x window mode
- **Read by:** [sub_1402DF374](../functions/sub_1402DF374.md)
- **Row layout:** [LayoutPointer](../structs/LayoutPointer.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Pointers to the sprite cell groups of the status window frame (four languages of eight modes). Verdict: pointer-table.

## Behavior

- V: 32 pointers = four groups of eight modes (language 0, other, 2, 3); most targets are shared with the status panel layout tables (StatusPanelLayouts*), which point at the same cell blocks
- V: the window builder selects eight pointers by language and indexes them by window mode
- V: several modes share a group (4/5, 6/7 and the matching pairs in the other languages)

## Notes

Our names. Tags: V.

## Open questions

None recorded.
