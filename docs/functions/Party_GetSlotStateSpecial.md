# Party_GetSlotStateSpecial

- **Address:** `0x140289320`
- **Area:** [Unit data](../areas/unit-data.md)
- **Prototype:** `int Party_GetSlotStateSpecial(int party_slot)`
- **Callers:** sub_14028916C, sub_1403666CC, sub_140366ABC, sub_140366FE0
- **Callees:** Party_GetSlotState

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Wrapper around the party slot check that replaces the usable result with the special-job code for jobs 161 and 164.

## Behavior

- V: a slot of 0x38 or above, or a negative slot, returns -1 without calling the inner check.
- V: it calls Party_GetSlotState and passes every result other than 1 straight through.
- V: for a usable slot it reads the job word at +0x24 and returns -6 when the job is 0xA1 or 0xA4 (the second reached as 0xA1+3).
- V: every other usable slot keeps the value 1.
- V: the function does not write anything; it is a pure filter over the inner result.
- I: 0xA1 and 0xA4 are the two jobs whose party records cannot be used in the normal unit list, which is why the caller needs a distinct code.
- ?: whether the caller treats -6 as hidden or as unusable; the four call sites were not compared.

## State touched

- Calls: [Party_GetSlotState](Party_GetSlotState.md)
- Reads: [g_PartyUnits](../globals/g_PartyUnits.md)

## Notes

Whole function read (76 bytes).

## Open questions

None recorded.
