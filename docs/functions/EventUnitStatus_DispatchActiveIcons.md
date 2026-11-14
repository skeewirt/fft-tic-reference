# EventUnitStatus_DispatchActiveIcons

- **Address:** `0x140241080`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void *EventUnitStatus_DispatchActiveIcons(unsigned int slot, int mode)`
- **Callers:** EventScript_Run
- **Callees:** SceneCallback_Dispatch

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

For one preview unit of an event scene, sends the status icon updater a message for every status the unit currently has.

## Behavior

- V: points the scene callback slot (g_TextCommandSlot) at sub_1401FB064, the status icon updater.
- V: reads the effective set (unit +97) of the preview unit at slot (the 21-row table at 0x141853CE0) and loops over the ids 0..39 (a fixed bound of 40).
- V: for each id whose bit is set it calls SceneCallback_Dispatch with kind 3, argument id + 1, the given mode, the slot and 0.
- I: a slot above 20 makes the set pointer the bare offset 97 (a null-based read); the one caller (EventScript_Run) is expected to pass a valid slot.

## State touched

- Calls: [SceneCallback_Dispatch](SceneCallback_Dispatch.md)

## Notes

Name is ours. The unit row is reached through the address 0x141853D41 (the unit table at 0x141853CE0 plus 0x61), so the table address itself is not an operand. The mode is passed through to the icon updater (the status icon update takes on / off).

## Open questions

? the event opcode that calls it and the meaning of its mode values.
