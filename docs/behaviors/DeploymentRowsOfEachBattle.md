# DeploymentRowsOfEachBattle

- **Kind:** observed behaviour
- **Scope:** engine (battle deployment)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [ScenarioSetup_ApplyRecord](../functions/ScenarioSetup_ApplyRecord.md), [WorldEncounter_StartBattle](../functions/WorldEncounter_StartBattle.md), [Deployment_SelectArea](../functions/Deployment_SelectArea.md), [Deployment_PrepareCandidates](../functions/Deployment_PrepareCandidates.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Where a battle's deployment rows come from: a story battle's scenario setup records name one or two rows, a random battle's encounter row names one per arrival road; a row's own map byte is not always the battle's map, and two pairs of battles share a row.

## Behavior

- V: Deployment_SelectArea(n) reads scene variable 53 + n as the row of the 12-byte placement table (0x1407AE2D0) and returns its count byte (+8); scene variable 52 is the number of areas.
- V: a story battle: ScenarioSetup_ApplyRecord writes the record's bytes +9 / +11 to variables 53 / 54 and their count to 52; the records of one battle's events carry the same rows (Siedge Weald: events 30, 31, 32, row 258). 494 records name a row; grouped by their rows they make 90 battles, 33 of them with two areas.
- V: a random battle: WorldEncounter_StartBattle writes variable 52 = 1 and 53 = 0x200 + the encounter row's byte 1; the 19 battlegrounds have three encounter rows each (one per arrival road; road 0 = unused), each naming its row (Mandalia Plain: 552, 553, 554; seen live: 554; The Siedge Weald: 519, 520).
- V (data): a placement row's byte +9 is a map id (Deployment_PrepareCandidates matches it in one mode), but it is not always the map the battle runs on: row 232 (byte +9 = 116, a map with no place name) is the first area of event 445, whose scenario record names map 50 (Mullonde Cathedral).
- V (data): row 324 is the second area of both Mullonde Cathedral battles (events 443 / 444 and event 445), and row 527 is both the Zeklaus Desert story battle's row (events 525..528) and one of the Zeklaus Desert random battle's rows.

## Open questions

None recorded.
