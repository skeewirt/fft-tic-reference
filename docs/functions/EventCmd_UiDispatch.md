# EventCmd_UiDispatch

- **Address:** `0x1402B2098`
- **Area:** [Event commands](../areas/event-commands.md)
- **Prototype:** `void EventCmd_UiDispatch(int id)`
- **Callers:** sub_140210AF0, EventChannel_BindStepTask, sub_14024C068, sub_1402F109C, EventCmd_SetIdPrefixed, BattleLoad_StepFresh, sub_14030476C
- **Callees:** sub_1402BA8E8, sub_1401D80A8

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Event-command helper that forwards an id to the UI dispatcher with the prefixed-id kind 12: it stores the id, resolves the UI object and tail-jumps to the dispatcher.

## Behavior

- V: the argument is stored in the dword slot at 0x141856AA8.
- V: sub_1402BA8E8 converts the id into the UI message form and returns it in eax.
- V: the UI object at 0x143CD9DD8 is loaded and the dispatcher is entered with kind 12 and the converted id.
- V: the function tail-jumps, so the dispatcher result is its result.
- V: the seven callers are event command handlers and event scene tasks.
- I: kind 12 is the prefixed-id UI message class, because event command class 47 is tied to this helper.
- ?: what sub_1402BA8E8 adds to the id; the conversion was not decoded.

## State touched

- Calls: [sub_1401D80A8](sub_1401D80A8.md)

## Notes

Whole function read (39 bytes). The tail call is the only control transfer.

## Open questions

None recorded.
