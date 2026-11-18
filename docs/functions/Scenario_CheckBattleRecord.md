# Scenario_CheckBattleRecord

- **Address:** `0x14020DFA8`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void Scenario_CheckBattleRecord(void)`
- **Callers:** sub_140210AF0
- **Callees:** sub_140207880

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Finds the scenario setup record of the current event and lets the battle set-up continue only for a battle record.

## Behavior

- V: linear search of up to 887 records (24 bytes) of the scenario setup table (0x1408ECAB0) by the 16-bit event number; 0 ends the search.
- V: a record whose byte +0x14 is not 0x80, or no record, sets the battle state to 59.
- V: otherwise links two entries for the current slot into a list and advances a counter; at 30 the state is set to 59 too.

## Referenced by

- Observed behaviours: [ScenarioSetupRecordFeedsTheBattleSceneVariables](../behaviors/ScenarioSetupRecordFeedsTheBattleSceneVariables.md), [ScenarioWordLinksRecordsByATenBitKeyAndLivesInTheBattleCapture](../behaviors/ScenarioWordLinksRecordsByATenBitKeyAndLivesInTheBattleCapture.md)
- Reads tables: [ScenarioSetup](../tables/ScenarioSetup.md)

## Notes

Read: the search and the state checks; the list entries are not identified.

## Open questions

?: what battle state 59 is; what the linked entries are.
