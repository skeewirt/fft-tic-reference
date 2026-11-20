# LegacyMenuTasks_Run

- **Address:** `0x1402B4570`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void LegacyMenuTasks_Run(void)`
- **Callers:** started by the legacy menu start as a scene task
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Task body of the legacy menu panes: keeps three pane tasks in step with the menu state.

## Behavior

- V: picks a row of LegacyMenuTaskSetups by the menu state word (values above 3 use row 0).
- V: for each of the three panes compares the row's expected owner id with the live pane owner and sets one of two flag patterns in the pane's task slot depending on the match.
- V: never returns: it loops forever as a task and yields between passes.

## Referenced by

- Reads tables: [LegacyMenuTaskSetups](../tables/LegacyMenuTaskSetups.md)

## Notes

Name is ours.

## Open questions

None recorded.
