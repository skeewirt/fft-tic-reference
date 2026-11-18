# ScreenTaskSets

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable
- **Address:** `0x140681650`
- **Rows:** 9 rows of 64 bytes
- **Keyed by:** screen set number
- **Read by:** [ScreenTaskSet_Run](../functions/ScreenTaskSet_Run.md)
- **Row layout:** [ScreenTaskSetRow](../structs/ScreenTaskSetRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The window tasks started together for each legacy screen set (four handlers, their slot numbers, their expected tags). Verdict: code-table.

## Behavior

- V: ScreenTaskSet_Run: row = set number x 64; handlers at +0, slots at +32, tags at +48
- I: nine rows by the gap to the next object

## Notes

Our names. Tags: V layout, I count.

## Open questions

None recorded.
