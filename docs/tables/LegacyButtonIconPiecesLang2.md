# LegacyButtonIconPiecesLang2

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable
- **Address:** `0x140692740`
- **Rows:** 80 rows of 12 bytes
- **Keyed by:** piece index 0..79
- **Read by:** [ButtonIcon_Draw](../functions/ButtonIcon_Draw.md)
- **Row layout:** [LegacyButtonIconPiecesRow](../structs/LegacyButtonIconPiecesRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Texture rectangle and draw offset of each button icon piece, text language 2. The four languages differ in offsets, not in shape. Verdict: designer-data.

## Behavior

- V: ButtonIcon_Draw adds the offsets to the icon position and sizes the piece by its scale pair

## Notes

Our names. Tags: V.

## Open questions

None recorded.
