# Boot_EnterState4

- **Address:** `0x1401E7C0C`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `__int64 Boot_EnterState4(int a1, int a2, int a3, int a4)`
- **Callers:** sub_1401E7EF8 (0x1401E8308)
- **Callees:** sub_1403CCA6C, Boot_SetState

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Enters boot state 4, first handing its four values to the render-command submitter and, when /return was given, storing 256 in a boot field.

## Behavior

- V: calls sub_1403CCA6C with the four arguments and a final 0.
- V: sub_1403CCA6C takes floats (its signature); its body queues render commands (RenderCommand_Allocate and RenderCommand_Submit appear in it); a fade or clear colour is likely but not read.
- V: when the byte g_UIStateFade+42 is 0 and the startup byte g_Application+1470 (/return) is non-zero, it stores 256 in the 16-bit field at g_UIStateFade+40 (low byte 0, next byte 1).
- V: then calls Boot_SetState with state 4.
- V: Boot_SetState's state-4 entry then overwrites that field with 255 at once, and no reader of a launcher mode byte was found; so the stored 256 has no lasting effect that was demonstrated.

## State touched

- Calls: [Boot_SetState](Boot_SetState.md)

## Referenced by

- Appears in flows: [LaunchSwitchesFromArgumentsToReaders](../flows/LaunchSwitchesFromArgumentsToReaders.md)

## Notes

The demonstrable effects of /return are only the skipped splash window and the unflipped 0x10000000 window-style toggle.

## Open questions

? what sub_1401E7EF8 is and when it runs.
