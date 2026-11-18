# LegacyMenu_PickLocation

- **Address:** `0x1402B28B0`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 LegacyMenu_PickLocation(void)`
- **Callers:** the legacy menu tasks
- **Callees:** EventVar_Write, EventTask_Terminate

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Confirms the highlighted location of the legacy location menu.

## Behavior

- V: reads the location id from the live list at the cursor index (+608 of the screen block) or, with a pending selection object, from that object.
- V: when the entry is selectable, writes the id to event variable 51, sets bit 14 of a shared flag word (a bit-test-and-set, value 0x4000), clears the next two task slots and, when no pending selection object exists, sets the menu result code to 1; otherwise the result code becomes 5.
- V: ends the calling task.

## State touched

- Calls: [EventVar_Write](EventVar_Write.md), [EventTask_Terminate](EventTask_Terminate.md)

## Notes

Name is ours.

## Open questions

None recorded.
