# EventCmd_ShowMessage

- **Address:** `0x1402F2000`
- **Area:** [Event commands](../areas/event-commands.md)
- **Prototype:** `void *EventCmd_ShowMessage(void)`
- **Callers:** EventCmd_Run through the class table, class 13
- **Callees:** EventTask_Start, sub_1401DFED0; EventMessage_Scripted is passed as the entry function and is not called here

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Class 13: shows a scripted event message. With an object active it passes the message index to the object's message routine; otherwise it starts the scripted message task in slot 14.

## Behavior

- V: argument layout: byte 9 is the message index (kept as v0); bytes 10 and 11 are not read.
- V: when the dword at offset 48 of the object at qword_143CD9E28 is nonzero, it calls sub_1401DFED0 with the object and v0 and returns that result.
- V: otherwise it calls EventTask_Start with slot 14 and the entry EventMessage_Scripted.
- V: after the start, it writes 0 to the 64-bit entry at index 3586 of the table at off_14078D5D8 (byte offset 0x7010), 9 to index 3584 (0x7000), and v0 + 0x8800 to index 3585 (0x7008).
- V: it sets bit 2 (4, continue) of the status word and writes v0 as a 16-bit word at offset 4 of xmmword_141862450 (the second command register).
- V: in the no-object branch the return value is the result of EventTask_Start (the address of unk_143791D70).

## State touched

- Calls: [EventTask_Start](EventTask_Start.md), [EventMessage_Scripted](EventMessage_Scripted.md)

## Notes

The message task is the one in the first task table. sub_1401DFED0 is the object's own message path and was not traced. The IDA name of this handler is still EventCmd_ShowMessage; no rename was made.

## Open questions

What the message index means to EventMessage_Scripted; what the entries at indices 3584 to 3586 and the base 0x8800 mean.
