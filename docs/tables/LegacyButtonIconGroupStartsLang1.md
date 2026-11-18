# LegacyButtonIconGroupStartsLang1

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable
- **Address:** `0x140691D00`
- **Rows:** 15 rows of 1 byte
- **Keyed by:** icon group 0..13 (+1 for the end)
- **Read by:** [ButtonIcon_Draw](../functions/ButtonIcon_Draw.md)
- **Row layout:** [LegacyButtonIconGroupStartsRow](../structs/LegacyButtonIconGroupStartsRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Piece start indexes of the button icon groups for text languages 1, 2 and 3 (80 pieces; three identical copies at 0x140691D00, 0x140691CF0 and 0x140691A60). Verdict: designer-data.

## Behavior

- V: same reader and row shape as LegacyButtonIconGroupStartsLang0

## Notes

Our names. Companion of the group start table; tags V layout, V reader.

## Open questions

None recorded.
