# UnitPage_Task

- **Address:** `0x1402FAA28`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `_QWORD *UnitPage_Task(void)`
- **Callers:** not recorded
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Task of the legacy unit page: builds the cells and the fifteen number fields of the unit page.

## Behavior

- V: uses the 18-cell blocks at 0x1408EBF20 .. 0x1408EC1C0 (four languages) and the number field tables at 0x1408EC2A0 and 0x1408EC480 (two variants of fifteen rows, selected by the page mode).
- I: the page shows movement, jump, speed, weapon power, defence and the four evade values.

## Referenced by

- Reads tables: [StatsNumbersUnitA](../tables/StatsNumbersUnitA.md), [StatsNumbersUnitB](../tables/StatsNumbersUnitB.md)

## Notes

Only the table references were read (1439 bytes).

## Open questions

?: the page layout and update loop.
