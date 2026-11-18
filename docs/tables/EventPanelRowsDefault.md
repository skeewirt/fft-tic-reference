# EventPanelRowsDefault

- **Kind:** table
- **Area:** [Event system](../areas/event-system.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1407B4720`
- **Rows:** 14 rows of 56 bytes
- **Keyed by:** panel row number (the number stored in the 0x7D task block)
- **Read by:** [EventPanel_PickRow](../functions/EventPanel_PickRow.md)
- **Row layout:** [EventPanelRow](../structs/EventPanelRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Event panel rows used by the 0x7D event task, for every language except language 0. Verdict: designer-data.

## Behavior

- V: EventPanel_PickRow: row = table[56 x row number]; the first dword (kind) decides: 0 opens the row through the event window, 1 queues it with EventPanel_QueueAndWait
- V: single reader indexes 14 dwords (56 bytes) per row; 0x310 bytes up to the language 0 copy gives 14 rows

## Notes

Our names. Tags: V stride and reader, I count 14 (distance to the twin), ? field meaning.

## Open questions

- ?: what each of the 14 rows opens
