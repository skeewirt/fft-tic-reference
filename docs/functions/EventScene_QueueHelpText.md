# EventScene_QueueHelpText

- **Address:** `0x1402C08C0`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void EventScene_QueueHelpText(void)`
- **Callers:** none found
- **Callees:** memcpy, sub_1400FBB40, sub_1401D78C0, sub_1401E37D4, sub_1400F71E8, Unit_GetSpriteSetId, sub_1402C3570, sub_14021E7FC, EventTask_Start, EventTask_Terminate, sub_14041FAE0

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Prepares a unit preview scene task: it builds the preview sprite record for the selected party unit, queues the shared help-text id as render command 12 and starts the event task.

## Behavior

- V: the selected party slot is the signed word at 0x141811428; the unit pointer is g_PartyUnits[slot] and its job word is at +0x126.
- V: Unit_GetSpriteSetId is called on that job and the result feeds PreviewUnit_BuildSpriteRecord.
- V: the help slot at 0x1418736B4 is sign-extended and written to the render command block at 0x14078D5D8 + 0x800, with command 0x12 and a zero word after it.
- V: the command block is then handed to sub_1402BA698, the render queue.
- V: EventTask_Start creates the scene task and EventTask_Terminate ends it when the preview cannot be built.
- V: the render command uses the S3 text slot.
- V: the function has no direct caller; the event scene state machine reaches it by a stored pointer.
- I: this is the help-panel preview task, because the queued command is the shared help text id rather than a dialogue line.
- ?: what sub_1402C3570 creates before the task starts; it is not tied to a named object here.

## State touched

- Calls: [Unit_GetSpriteSetId](Unit_GetSpriteSetId.md), [EventTask_Start](EventTask_Start.md), [EventTask_Terminate](EventTask_Terminate.md)
- Reads: [g_PartyUnits](../globals/g_PartyUnits.md), [g_SelectedUnitIndex](../globals/g_SelectedUnitIndex.md), [g_HelpIdSlot](../globals/g_HelpIdSlot.md)

## Notes

Whole function read (697 bytes). The missing direct caller is a fact; the dispatch route is inferred.

## Open questions

None recorded.
