# LegacyMenuTaskSetups

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable
- **Address:** `0x140680230`
- **Rows:** 4 rows of 48 bytes
- **Keyed by:** menu state 0..3
- **Read by:** [LegacyMenuTasks_Run](../functions/LegacyMenuTasks_Run.md)
- **Row layout:** [LegacyMenuTaskSetupsRow](../structs/LegacyMenuTaskSetupsRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Per menu state, the three pane tasks of the legacy menu with their task ids and owner ids. Verdict: engine-data.

## Behavior

- V: LegacyMenuTasks_Run walks three panes, comparing a pane's expected owner id with the live owner and resetting the slot on a match

## Notes

Our names. Tags: V layout, I handler meaning.

## Open questions

None recorded.
