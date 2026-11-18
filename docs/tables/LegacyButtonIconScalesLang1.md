# LegacyButtonIconScalesLang1

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable
- **Address:** `0x140691BB0`
- **Rows:** 80 rows of 4 bytes
- **Keyed by:** piece index 0..79
- **Read by:** [ButtonIcon_Draw](../functions/ButtonIcon_Draw.md)
- **Row layout:** [LegacyButtonIconScalesRow](../structs/LegacyButtonIconScalesRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Scale pair of each button icon piece for text languages 1, 2 and 3 (three identical copies); language 0 has its own with 81 rows (LegacyButtonIconScalesLang0). Verdict: designer-data.

## Behavior

- V: every value in the used rows is 4096 (1.0) except where a piece is stretched; the sign of the second word flips the piece

## Notes

Our names. Tags: V.

## Open questions

None recorded.
