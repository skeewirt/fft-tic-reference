# JobTree_OnEvent

- **Address:** `0x140133DDC`
- **Area:** [Job tree](../areas/job-tree.md)
- **Prototype:** `char JobTree_OnEvent(JobTreeAddon *addon, GUINode *node, int *event)`
- **Callers:** UI system (vtable)
- **Callees:** JobTree_OnCursorEnter, JobTree_OnCursorLeave, GUICore_FocusNode

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

UI event handler of the tree addon (vtable slot 2).

## Behavior

- V: event 4 = copy the 'held' flag addon+12242 to addon+12241 and clear it; 0x10 = set addon+12242; 0xC on a panel node (node+544 == 18) = GUICore_FocusNode(node).
- I: event 12 is the mouse arriving over a panel (the pad focuses through JobTree_HandleInput); the focus then arrives as event 19 like the pad's.
- V: event 19 (cursor enter) on a panel node: addon+12232 = panel index (node+548); JobTree_OnCursorEnter(addon, index); then vtable slot 3 and sound id 17 (sub_1400F4BCC).
- V: event 20 (cursor leave) on a panel node: JobTree_OnCursorLeave(addon, index).

## State touched

- Calls: [JobTree_OnCursorEnter](JobTree_OnCursorEnter.md), [JobTree_OnCursorLeave](JobTree_OnCursorLeave.md), [GUICore_FocusNode](GUICore_FocusNode.md)
- Writes: [JobTreeAddon.selectedSlot](../structs/JobTreeAddon.md#selectedslot)

## Notes

Panel nodes carry kind 18 at node+544 and the job index at node+548 (set in JobTree_RefreshAddon).

## Open questions

None recorded.
