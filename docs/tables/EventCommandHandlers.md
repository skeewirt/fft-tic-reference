# EventCommandHandlers

- **Kind:** table
- **Area:** [Event system](../areas/event-system.md)
- **Storage:** Executable
- **Address:** `0x140681DE0`
- **Rows:** 54 rows of 8 bytes
- **Keyed by:** event command id
- **Read by:** [EventCmd_Run](../functions/EventCmd_Run.md)
- **Row layout:** [FunctionPointerRow](../structs/FunctionPointerRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Handler registry read by EventCmd_Run: one function pointer per event command.

## Behavior

- V: the handlers are code; the opcode semantics are in the opcode records.

## Notes

Our names. Tags per member and behaviour line; read statically in the decompilation of the Enhanced executable.

## Open questions

None recorded.
