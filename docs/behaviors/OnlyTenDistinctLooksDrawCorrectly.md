# OnlyTenDistinctLooksDrawCorrectly

- **Kind:** observed behaviour
- **Scope:** engine (battle unit looks, Enhanced)
- **Area:** [Graphics](../areas/graphics.md)
- **Affects:** [LookPool_ClaimForSprite](../functions/LookPool_ClaimForSprite.md), [SceneUnit_BuildFromQueueEntry](../functions/SceneUnit_BuildFromQueueEntry.md), [Battle_PlaceEntryUnits](../functions/Battle_PlaceEntryUnits.md), [EntryUnits_CheckLookBudget](../functions/EntryUnits_CheckLookBudget.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A battle can load up to 15 distinct looks (the look pool), but only the units whose look takes pool records 0..9 draw correctly; looks in records 10..14 draw as scrambled pieces, and a 16th distinct look crashes the game when it is placed at deployment. Stock battles stay at 10 or fewer.

## Behavior

- V: SceneUnit_BuildFromQueueEntry gives a high-res sheet entry only to pool records 0..9 (records 0..8 from one table, record 9 from another, records 10..14 none); records are claimed in load order (the battle's own units first, then the deployed party), one per distinct sprite byte.
- V (tested limit, random battle at Mandalia Plain, the battle's entries replaced at Battle_PlaceEntryUnits with distinct monster families and variable 57 forced to -7): with 10 enemy looks (records 0..9) and Ramza deployed alone (record 10), the enemies drew normally and Ramza drew as scrambled pieces; with 11 enemy looks and 4 party units (records 11..14) all four party units drew scrambled (judged by eye on the game window).
- V (tested limit): with 11 enemy looks and a fifth party unit (a 16th distinct look) the pool claim failed (15 of 15 records in use), the unit got no scene unit and the deployment step crashed at 0x1401F330F (the same null scene object as a 17th drawn unit).
- V (seen live, Orbonne Monastery, the first story battle): 11 units on the field, 9 distinct sprites among them and 10 pool records in use (one more for a hidden actor): exactly records 0..9.
- V: the battle's own units are held to 9 - variable 57 distinct sprites at load (EntryUnitsShareADistinctLookBudget); the deployed party and units revealed later are not checked, so it is the stock data that keeps a battle at 10 or fewer.

## Open questions

? what decides the scrambled image (the classic path without its texture, or a stale buffer); ? the battle portraits of records 10..14 (the face table has 10 entries; not judged in this test).
