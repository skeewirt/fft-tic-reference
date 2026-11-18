# GridHelpRowsLanguage0

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1408F2000`
- **Rows:** 31 rows of 24 bytes
- **Keyed by:** cursor row
- **Read by:** [sub_1403015A4](../functions/sub_1403015A4.md)
- **Row layout:** [GridHelpRow](../structs/GridHelpRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Cursor rows of the grid screen text helper, language 0. Verdict: designer-data.

## Behavior

- V: the task reads the row of the cursor with stride 24 and starts the message task from its code word
- I: 31 rows after an 8-byte header by the size 0x2F0

## Notes

Our names. Tags: V stride, I count.

## Open questions

None recorded.
