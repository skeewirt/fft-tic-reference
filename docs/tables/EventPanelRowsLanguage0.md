# EventPanelRowsLanguage0

- **Kind:** table
- **Area:** [Event system](../areas/event-system.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1407B4A30`
- **Rows:** 14 rows of 56 bytes
- **Keyed by:** panel row number
- **Read by:** [EventPanel_PickRow](../functions/EventPanel_PickRow.md)
- **Row layout:** [EventPanelRow](../structs/EventPanelRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Event panel rows for language 0. Verdict: designer-data.

## Behavior

- V: EventPanel_PickRow: used when the text language is 0
- V: language switch: v5 == 0 -> this table, otherwise the default table 0x1407B4720; same 14 rows

## Notes

Our names. Tags: V, I count.

## Open questions

- ?: how the rows differ from the default table in meaning
