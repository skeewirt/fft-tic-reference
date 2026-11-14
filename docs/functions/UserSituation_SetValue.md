# UserSituation_SetValue

- **Address:** `0x1400FF660`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void UserSituation_SetValue(SituationStore *store, unsigned int id, int value)`
- **Callers:** EventScript_Run, sub_14019D548
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sets one situation counter and tells the registered listeners.

## Behavior

- V: writes the dword at +24 + 4 * id (or +104 + 4 * id when bit 0 of +16 is set), then calls the second virtual function of every listener on the list at qword_143CD9DE8 +24.
- V (read in the caller EventScript_Run, not in this body): event opcode 0xE9 calls it with an id and a value from the script; opcode 0xEA calls a twin (sub_1400FF6B8) that sets a flag byte (+72 / +152).

## State touched

- Writes: [g_UserSituation](../globals/g_UserSituation.md)

## Referenced by

- Observed behaviours: [TavernErrandsOpenAtSituationCounter450](../behaviors/TavernErrandsOpenAtSituationCounter450.md)

## Notes

Name is ours (was sub_1400FF660). Whole function read; the listener calls are indirect.

## Open questions

None recorded.
