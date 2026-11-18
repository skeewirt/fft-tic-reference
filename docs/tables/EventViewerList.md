# EventViewerList

- **Kind:** table
- **Area:** [Event system](../areas/event-system.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1407B81B0`
- **Rows:** 88 rows of 2 bytes
- **Keyed by:** event viewer entry
- **Read by:** [EventViewer_EntryPage](../functions/EventViewer_EntryPage.md)
- **Row layout:** [EventViewerEntry](../structs/EventViewerEntry.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Story event numbers of the scenes in the replay list. Verdict: designer-data.

## Behavior

- V: EventViewer_EntryPage writes word [entry] to event variable 39 when the entry is confirmed
- I: 88 words up to the window pattern tile table; the last two are zero

## Notes

Our names. Tags: V reader, I count.

## Open questions

None recorded.
