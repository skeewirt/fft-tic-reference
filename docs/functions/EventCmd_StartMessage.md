# EventCmd_StartMessage

- **Address:** `0x1402F1B2C`
- **Area:** [Event commands](../areas/event-commands.md)
- **Prototype:** `int64_t EventCmd_StartMessage(void)`
- **Callers:** Called through the command table (class 3) by EventCmd_Run
- **Callees:** EventTask_Start, `sub_1401DFED0`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The command handler (class 3) that opens a message window: it starts EventMessage_Scripted as the task in slot 14 and stores which message to show.

## Behavior

- V: reads byte 9 of the command register (the message number).
- V: when `qword_143CD9E28` has a non-zero field at +48 it hands the number to `sub_1401DFED0` instead of starting a task.
- V: otherwise it calls EventTask_Start(14, EventMessage_Scripted) and writes three fields of slot 14's task block: 9, the message reference `number + 0x8800` (text bank 17), and 0.
- V: then sets flag bit 4 in the command register flags and updates the command register's companion fields from the message number.
- I: `EventMessage_Scripted` reads the reference from the task block and looks the text up with EventText_FindMessage.

## State touched

- Calls: [EventTask_Start](EventTask_Start.md)

## Notes

Shows how the message task gets its message: the reference is placed in the task block before the task first runs.

## Open questions

What the value 9 in the task block means.
