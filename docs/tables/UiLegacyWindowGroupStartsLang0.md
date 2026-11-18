# UiLegacyWindowGroupStartsLang0

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable
- **Address:** `0x140813E80`
- **Rows:** 12 rows of 1 byte (+4 padding)
- **Keyed by:** group 0..11
- **Row layout:** [WindowGroupStartRow](../structs/WindowGroupStartRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Cumulative start indexes of 12 cell groups of a legacy list window, text language 0. Verdict: designer-data.

## Behavior

- V: the first byte of the head is always 0; the reader adds the group size to find the next start

## Notes

Our names. Tags: V head, ? cells.

## Open questions

- ?: cell record count per language
