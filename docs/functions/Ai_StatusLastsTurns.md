# Ai_StatusLastsTurns

- **Address:** `0x14038BAB4`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int Ai_StatusLastsTurns(int turns, UnitWorkRecord *unit, int status)`
- **Callers:** sub_14031FD40, sub_140388ABC, sub_14038B34C, sub_14038BB68, sub_14038E07C
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Tells the battle AI whether a unit has a status and will still have it after the given number of its turns.

## Behavior

- V: returns 0 when the status bit is not set in the unit effective set (+97, byte status / 8, bit 0x80 >> (status % 8)).
- V: for status 5 (Jumping) it returns 0 when turns is greater than the unit charge counter (+0x18D).
- V: for a status of 24 or more (the timed statuses) that is not in the innate group a (+87) it returns 0 when turns is greater than the countdown byte (unit + 78 + status, the byte at +102 + (status - 24)); an innate status never expires.
- V: otherwise it returns 1 (statuses below 24 other than Jumping are permanent until removed).

## State touched

- Reads: [UnitWorkRecord.status_effective](../structs/UnitWorkRecord.md#status_effective), [UnitWorkRecord.status_countdown](../structs/UnitWorkRecord.md#status_countdown), [UnitWorkRecord.charge_counter](../structs/UnitWorkRecord.md#charge_counter)

## Referenced by

- Observed behaviours: [StatusesAreFortyBitSetsInEightRegions](../behaviors/StatusesAreFortyBitSetsInEightRegions.md)

## Notes

Name is ours. The countdown index assumes the 24..39 window; a status id outside it reads past the 16 countdown bytes.

## Open questions

? the AI decisions that use it (all callers are in the AI range).
