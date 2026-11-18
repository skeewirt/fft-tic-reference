# ScenarioSetup

- **Kind:** table
- **Area:** [Event system](../areas/event-system.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1408ECAB0`
- **Rows:** 887 rows of 24 bytes
- **Keyed by:** scenario / event number (key u16 at +0; scene variable 39)
- **Read by:** [Scenario_CheckBattleRecord](../functions/Scenario_CheckBattleRecord.md)
- **Row layout:** [ScenarioSetupRow](../structs/ScenarioSetupRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Per story event / scenario: its scene setup record (map and battle settings). Verdict: designer-data.

## Behavior

- V: loop bound 0x377 = 887 and stride 24 in both readers (three loops, two immediates in ScenarioSetup_ApplyRecord: one bounds two loops)
- V: ScenarioSetup_ApplyRecord: builds the per-event word table g_BattleMapWords (indexed by the EVENT NUMBER) from the records up to the first record with event number 0 (bound 887)
- V: sub_14020DFA8: finds the current event's record and requires +0x14 == 0x80 before setting up the battle

## Notes

Our names. Tags: V layout of the copied fields, ? rest.

## Open questions

- ?: most field meanings
- ?: map field confirmation
