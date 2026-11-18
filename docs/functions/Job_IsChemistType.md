# Job_IsChemistType

- **Address:** `0x140270C58`
- **Area:** [Job data](../areas/job-data.md)
- **Prototype:** `bool Job_IsChemistType(const uint8_t *unit)`
- **Callers:** sub_140271AC0, sub_140271CA8
- **Callees:** (inlined Job getter)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

True when the Job row of the unit's job byte (unit+3) has jobtype +24 == 31.

## Behavior

- V: hard-coded jobtype 31 (Chemist).

## Referenced by

- Called by: [MoveFind_TakeItem](MoveFind_TakeItem.md), [sub_140271AC0](sub_140271AC0.md)

## Notes

Engine hard-code that depends on the stock jobtype numbering.

## Open questions

None recorded.
