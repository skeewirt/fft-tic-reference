# EventControl_CarryToNextEvent

- **Address:** `0x14021F14C`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void EventControl_CarryToNextEvent(void)`
- **Callers:** EventScript_Run
- **Callees:** sub_14021EE0C, GlobalWork_GetFastForwardMode, sub_140270BA4, sub_1401DB06C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

When an event script ends, saves whether auto-advance and fast-forward were on so a chained event can start with them.

## Behavior

- V: copies EventControl +47 (auto) into +48.
- V: sets EventControl +54 to 1 when the mode is 2 and the level is non-zero, else 0.
- V: when sub_140270BA4(current event number) is true it also writes the word +34 = 256, the word +49 = 0 and the byte +51 = 0.

## State touched

- Calls: [GlobalWork_GetFastForwardMode](GlobalWork_GetFastForwardMode.md)
- Reads: [EventControl.auto_mode](../structs/EventControl.md#auto_mode), [GlobalWork.ff_level](../structs/GlobalWork.md#ff_level)
- Writes: [EventControl.auto_carry](../structs/EventControl.md#auto_carry), [EventControl.ff_carry](../structs/EventControl.md#ff_carry)

## Open questions

? What sub_140270BA4 tests.
