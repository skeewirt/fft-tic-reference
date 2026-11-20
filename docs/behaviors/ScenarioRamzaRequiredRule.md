# ScenarioRamzaRequiredRule

- **Kind:** observed behaviour
- **Scope:** engine (deployment screen, scene variable 511)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [ScenarioSetup_ApplyRecord](../functions/ScenarioSetup_ApplyRecord.md), [GridScreen_Task](../functions/GridScreen_Task.md), [DeploymentGrid_CommenceCheck](../functions/DeploymentGrid_CommenceCheck.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A scenario setup record with a deployment area and the Ramza flag set makes the deployment screen place party member 0 first and refuse to start the battle without that member.

## Behavior

- V: ScenarioSetup_ApplyRecord copies the record's byte +17 to scene variable 511 only when the area at +9 is non-zero. Stock: 0 on 363 rows, 1 on 350; 23 rows hold 1 with no area and never apply it (M).
- V: GridScreen_Task, with variable 511 non-zero, fills the first open cell of the deployment grid with party member 0.
- V: taking that member off the grid while variable 511 is 1 starts a message task (sub_14023286C) instead of removing it.
- V: DeploymentGrid_CommenceCheck returns 2 when variable 511 is non-zero and no placed unit is party member 0.

## Open questions

None recorded.
