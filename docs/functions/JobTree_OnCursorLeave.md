# JobTree_OnCursorLeave

- **Address:** `0x1401346D4`
- **Area:** [Job tree](../areas/job-tree.md)
- **Prototype:** `void JobTree_OnCursorLeave(JobTreeAddon *addon, int jobIdx)`
- **Callers:** JobTree_OnEvent (event 20)
- **Callees:** JobTree_SetArrowState, JobTree_SetLabelState

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Cursor left panel `jobIdx`: puts its arrows and labels back to the resting (not on cursor) states.

## Behavior

- V: same loop as JobTree_OnCursorEnter but passes onCursor=0 to JobTree_SetArrowState and show=0 to JobTree_SetLabelState (labels hide when the cursor leaves).

## State touched

- Calls: [JobTree_SetArrowState](JobTree_SetArrowState.md), [JobTree_SetLabelState](JobTree_SetLabelState.md)
- Reads: [JobRecord.state](../structs/JobRecord.md#state)

## Referenced by

- Called by: [JobTree_OnEvent](JobTree_OnEvent.md)

## Open questions

None recorded.
