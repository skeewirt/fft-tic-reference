# LegacyMenu_InitWorld

- **Address:** `0x1402B2EB0`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 LegacyMenu_InitWorld(void)`
- **Callers:** the legacy menu start
- **Callees:** EventTasks_Init, Resource_GetSlotObject, EventVar_Write

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Initialises the legacy world menu: loads its text resource and picks the screen state block of the current text language.

## Behavior

- V: initialises the event tasks, loads resource slot 4, copies it into a work buffer and clears event variable 510.
- V: text language 0 selects the block at 0x14080CAB0, 3 the block at 0x14080D930, 2 the block at 0x14080E070 and every other value (1, default) the block at 0x14080D1F0; the choice becomes the active screen block.
- V: builds a pointer list into the work buffer, then writes event variables 511 = 0, 52 = 1, 53 = 0 and 54 = 1.

## State touched

- Calls: [EventTasks_Init](EventTasks_Init.md), [Resource_GetSlotObject](Resource_GetSlotObject.md), [EventVar_Write](EventVar_Write.md)

## Referenced by

- Called by: [OpeningTask_4](OpeningTask_4.md), [TitleScene_Task](TitleScene_Task.md)

## Notes

Name is ours.

## Open questions

None recorded.
