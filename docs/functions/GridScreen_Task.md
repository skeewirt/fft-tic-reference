# GridScreen_Task

- **Address:** `0x1402FC870`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GridScreen_Task(void)`
- **Callers:** not recorded
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Task of the legacy grid screen screen: a grid of five columns of unit portraits with a cursor and a help window.

## Behavior

- V: publishes the five menu nodes (0x1408EC6A0 for language 0, 0x1408EC860 otherwise) as the live menu tree (qword_140D40950).
- V: the cursor is two dwords (columns at 0x1408EC858, rows at 0x1408ECA18) that start at 2, 2 and are clamped to 0..4 by the pad; the unit at the cursor comes from a 5-wide table (0xFF = empty).
- I: the screen is the unit selection grid of the party; its availability flags come from GridAvailability_Reset.

## Referenced by

- Observed behaviours: [ScenarioRamzaRequiredRule](../behaviors/ScenarioRamzaRequiredRule.md), [TestBattleModeVariable510](../behaviors/TestBattleModeVariable510.md)
- Reads tables: [GridArrowCells](../tables/GridArrowCells.md), [GridMenuNodesDefault](../tables/GridMenuNodesDefault.md), [GridMenuNodesLanguage0](../tables/GridMenuNodesLanguage0.md)

## Notes

Only the table-facing parts were read (6307 bytes).

## Open questions

?: which game screen it is.
