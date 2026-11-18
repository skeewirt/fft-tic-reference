# LegacyCursorRowsLangOther

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1408FB952`
- **Rows:** about 33 rows of 24 bytes
- **Keyed by:** row index
- **Read by:** [ClassicCursorRows_Select](../functions/ClassicCursorRows_Select.md)
- **Row layout:** [LegacyCursorRowsLangOtherRow](../structs/LegacyCursorRowsLangOtherRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Cursor row table of the same legacy menu for the languages other than 0; 30 bytes differ from the language 0 table. Verdict: designer-data.

## Behavior

- V: same reader; 0x37E bytes up to the next object
- V: ClassicCursorRows_Select (0x14036E28C): chosen for every language except 0; base 0x1408FB94E

## Notes

Our names. Tags: V reader, ? fields.

## Open questions

- ?: row count
