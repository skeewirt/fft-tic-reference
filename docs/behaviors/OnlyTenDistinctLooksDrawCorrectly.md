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
- V (cause of the scrambled image): SceneUnit_BuildFromQueueEntry gives pools 9..14 one sheet word, 17, and sub_140260CF0 draws word 17 from HD sheet group 13, which holds pool 9's sheet (entry dword_142E7FEE0), whenever that entry is set; so a unit of pools 10..14 is cut out of pool 9's sheet at its own frame rectangles. The classic data of pools 9..14 is uploaded to buffers 2..7 (sub_14026E838) and the classic quad takes buffer pool - 7, so the low-resolution path has each of the 15 looks (I: drawn correctly with HD off; not tried).
- V: sub_14026E838 stores each pool's sprite byte into g_LookPoolFaceValue[pool] (10 dwords at 0x1437A59E0); pools 10..14 write past it: pool 10 into dword_1437A5A08 (a step value of sub_140315B10, which sets it to 0x8000 and adds it each frame), pool 11 into 0x1437A5A0C, pools 12..14 into the first three dwords of the 99-entry table at xmmword_1437A5A10 that the dialogue code reads by face code (sub_1402F8684, sub_140338A28, sub_1402FF81C).

## Open questions

? the battle portraits of records 10..14 (not judged in the test); ? what an overwritten dword_1437A5A08 or face-code entry 0..2 does on screen.
