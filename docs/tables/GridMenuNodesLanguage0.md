# GridMenuNodesLanguage0

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1408EC6A0`
- **Rows:** 5 rows of 88 bytes
- **Keyed by:** menu node number
- **Read by:** [GridScreen_Task](../functions/GridScreen_Task.md)
- **Row layout:** [LegacyMenuNode](../structs/LegacyMenuNode.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Legacy menu nodes of the grid screen, language 0. Verdict: designer-data.

## Behavior

- V: GridScreen_Task publishes the array as the live menu tree (qword_140D40950)
- I: five nodes by the size 0x1B8

## Notes

Our names. Tags: V reader, I count.

## Open questions

None recorded.
