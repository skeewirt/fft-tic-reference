# DebugSceneTablesShipStripped

- **Kind:** observed behaviour
- **Scope:** engine data (debug scene selection)
- **Area:** [Data access](../areas/data.md)
- **Affects:** [NxdDataDebugSceneSelect](../tables/NxdDataDebugSceneSelect.md), [NxdDataDebugMap](../tables/NxdDataDebugMap.md), [NxdDataDebugRefinedBgAnim](../tables/NxdDataDebugRefinedBgAnim.md), [NxdDataDebugRefinedBgTexture](../tables/NxdDataDebugRefinedBgTexture.md), [NxdDataDebugFIdSound](../tables/NxdDataDebugFIdSound.md), [NxdDataDebugGameFlowSettings](../tables/NxdDataDebugGameFlowSettings.md), [NxdDataDebugSceneSelectCategory](../tables/NxdDataDebugSceneSelectCategory.md), [NxdDataDebugFidG2D](../tables/NxdDataDebugFidG2D.md), [NxdDataDebugNovelPageDefine](../tables/NxdDataDebugNovelPageDefine.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The game data carries a set of debug scene-selection tables whose rows are stripped to a key and a flag: the scene picker, its map list, two background tables, a sound-id list, a graphics-id list, a game-flow table and a novel-page table. Only the picker's eight category names have text.

## Behavior

- V: row counts in the stock data: the scene picker table (58) 0 rows, the debug map table (78) 80 rows, the two refined background tables (79, 80) 0 rows, the sound-id list (89) 691 rows, the game-flow table (102) 0 rows, the category table (110) 8 rows, the graphics-id list (212) 1285 rows and the novel-page table (300) 0 rows.
- V: every row of the map, sound-id and graphics-id tables holds only its key and one constant flag (every comment and unnamed column is empty or 0).
- V: the eight category rows are named Invalid, Main Scenario, Subquests, For QA, Backup, EnvMapNum, EnvTest and QATest; categories 1 to 4 also carry a Japanese label before the English word (main scenario, sub event, for verification, for planner checks).
- I: no code reads these tables by their table id; the scene picker they belonged to is not reachable in this build.

## Open questions

? whether a reader fetches them through a computed table id.
