# UiCoreNameKeys

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable
- **Address:** `0x1406F6100`
- **Rows:** 43 rows of 8 bytes
- **Keyed by:** slot of the UI name table 0..42
- **Read by:** [UiNames_InstallCoreNames](../functions/UiNames_InstallCoreNames.md)
- **Row layout:** [StringPointerRow](../structs/StringPointerRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The 43 fixed names the UI system registers first: widget events (Show, Hide, Enable, Disable, FocusIn, FocusOut, CursorOver, CursorOut, Click, Check, Open, Close, gauge and scroll events, In / Out), widget part names (Title, Button, List, Bar, Base, Knob, Collision01) and component marks. Verdict: text.

## Behavior

- V: UiNames_InstallCoreNames interns name n into slot n of the UI name table (16-byte slots from +4584); the loop ends at the end of this table (43 entries)

## Notes

Our names. Tags: V layout, V reader, I name roles.

## Open questions

- ?: which UI event runs for each name
