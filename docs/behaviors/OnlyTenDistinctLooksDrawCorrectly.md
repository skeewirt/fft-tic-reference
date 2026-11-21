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
- V: the code addresses g_LookPoolFaceValue at exactly 19 places (no data pointer to it): 2 writes in sub_14026E838, the setup loop in sub_140210AF0 (count 10, cmp eax, 10 at 0x140210C96), 6 accesses in sub_140304BEC (the battle capture's copy, 40 bytes = 10 entries each way, called by Battle_SaveCapture and Battle_RestoreCapture) and 10 reads.
- V: each of the 10 reads tests the pool index against 10 first and keeps a default value when it is 10 or more: sub_1401F3858 (0x1401F38FC), sub_140214134 (0x140214162), TurnPanel_SetUnitPanel (0x14021508D), TurnPanel_SetTag (0x140215676), sub_14021FA50 (0x14021FD1B), sub_140221798 (0x14022196D), Battle_UnitStatusFillAlt (0x140229926), sub_1402DF374 (0x1402E0530), sub_140338A28 (0x14033977C, into g_DialogueFaceSlot0) and sub_1403980AC (0x140398DED, the same). So the portrait code never reads past the table: a unit of pools 10..14 gets the default instead of its face value, while the writes still overrun.
- V: the look pool records (g_LookPool, 15 x 0x32D6 = 0x2FA8A bytes) are addressed by exactly 22 instructions, none through a data pointer: the clear in sub_1401D4544, the capture copy in SceneUnits_SaveRestore, the restore in Battle_RestoreSceneVars, the claim loop in LookPool_ClaimForSprite (count 15 at 0x140269018, 0x14026904E, 0x140269068) and the record users (sub_140210AF0, SceneUnit_RunPlacement, SceneUnit_TintOwnRow, SceneUnit_SyncSpriteFromPool, SceneUnit_LoadExtraPage, SceneUnit_Release, sub_14026E838, LookPool_ResetForBattleLoad, CharaPalette_ReloadForShape, sub_140273468); three of them take the end of the table as a loop bound (0x140210C03, 0x14026F605, 0x14026FD3D), where byte_140D3002A and byte_140D3002B, separate globals, begin.

## Open questions

? what an overwritten dword_1437A5A08 or face-code entry 0..2 does on screen; ? which default face each of the 10 reads keeps for pools 10..14 (not seen live).
