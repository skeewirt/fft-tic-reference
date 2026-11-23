# LegacyMenuRowIcons

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable
- **Address:** `0x140692F20`
- **Rows:** 16 rows of 1 bytes
- **Keyed by:** menu row 0..15
- **Row layout:** [LegacyMenuRowIconsRow](../structs/LegacyMenuRowIconsRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A run of 16 consecutive row codes followed by a table of 88 u16 cell ids: menu row decoration data of the legacy menus. Verdict: designer-data.

## Behavior

- V: 0xC0 = 16 + 176 bytes; the byte part is the identity run 0x11..0x20; the word part starts at 0x140692F30
- V: Errand_ReportDialogueStep and sub_140374484: read byte [row] and pass it to sub_1403436C0
- V: sub_14037C2EC reads the 88 u16 cell ids that follow (from +0x10) through sub_14031EB60

## Notes

Our names. Tags: V layout, ? meaning.

## Open questions

- ?: what the 88 cell ids draw
- ?: which legacy menu rows use the 16 codes
