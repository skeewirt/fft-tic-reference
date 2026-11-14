# JobTree_OnCursorEnter

- **Address:** `0x140134594`
- **Area:** [Job tree](../areas/job-tree.md)
- **Prototype:** `void JobTree_OnCursorEnter(JobTreeAddon *addon, int jobIdx)`
- **Callers:** JobTree_OnEvent (event 19)
- **Callees:** JobTree_SetArrowState, JobTree_SetLabelState

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Cursor moved onto panel `jobIdx`: lights every arrow and label attached to it (its 6 requirement edges and its 6 dependent edges).

## Behavior

- V: guard jobIdx <= cap (0x13 in the game's code). Loops 6 slots of the panel's requirement table (record+0x88, 24 B each) and 6 of its dependents table (record+0x118); the code walks one pointer, addon + 456 x panel + 228, and reads 20 bytes before it and 124 after it (the record starts at addon + 72).
- V: met = required job's JobRecord.state == 0 (record+132) and edge level <= record+68 (the job's level). Each edge calls JobTree_SetArrowState(line, onCursor=1, met) and JobTree_SetLabelState(board, show=1, met).
- I: the Bard/Dancer pair (indices 17/18) is special-cased with addon+12240 (gender flag): only the visible one of the pair is processed.
- V: only 6 dependents are kept per job, so a job required by more than 6 others highlights only the first 6 of its outgoing arrows.

## State touched

- Calls: [JobTree_SetArrowState](JobTree_SetArrowState.md), [JobTree_SetLabelState](JobTree_SetLabelState.md)
- Reads: [JobRecord.state](../structs/JobRecord.md#state)

## Referenced by

- Called by: [JobTree_OnEvent](JobTree_OnEvent.md)
- Observed behaviours: [JobTreePanelLookups](../behaviors/JobTreePanelLookups.md)

## Notes

Mirror image of JobTree_OnCursorLeave. V: JobTree_OnEvent calls it on event 19 for a panel node, after storing the panel at addon+12232. I: event 19 is every cursor arrival on a panel, the pad's focus (GUICore_FocusNode) and the mouse's hover (event 12 focuses the hovered panel node).

## Open questions

None recorded.
