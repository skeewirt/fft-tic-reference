# LegacyButtonIconGroupStartsLang0

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable
- **Address:** `0x140691A50`
- **Rows:** 15 rows of 1 byte
- **Keyed by:** icon group 0..13 (+1 for the end)
- **Read by:** [ButtonIcon_Draw](../functions/ButtonIcon_Draw.md)
- **Row layout:** [LegacyButtonIconGroupStartsRow](../structs/LegacyButtonIconGroupStartsRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Cumulative piece start index of each button icon group for text language 0; language 1 (default), 2 and 3 share another list (LegacyButtonIconGroupStartsLang1). Verdict: designer-data.

## Behavior

- V: ButtonIcon_Draw reads start[group] and start[group + 1] and draws that many pieces from the piece table of the same language

## Notes

Our names. Tags: V.

## Open questions

None recorded.
