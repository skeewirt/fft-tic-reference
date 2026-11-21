# TwentyOneUnitsNeedSixPerSlotStoresWidened

- **Kind:** observed behaviour
- **Scope:** engine (battle units, drawing, AI, Enhanced HD)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [ClutBank_CopyRow](../functions/ClutBank_CopyRow.md), [ClutFade_UnitSlot](../functions/ClutFade_UnitSlot.md), [ClutFade_SetTarget](../functions/ClutFade_SetTarget.md), [UnitClut_TintRow](../functions/UnitClut_TintRow.md), [CharaRender_LoadMapLights](../functions/CharaRender_LoadMapLights.md), [CharaRender_UnitLight](../functions/CharaRender_UnitLight.md), [CharaRender_UnitFlash](../functions/CharaRender_UnitFlash.md), [CharaRenderer_Init](../functions/CharaRenderer_Init.md), [SceneUnit_BuildFromQueueEntry](../functions/SceneUnit_BuildFromQueueEntry.md), [sub_14026E838](../functions/sub_14026E838.md), [g_ClutManager](../globals/g_ClutManager.md), [g_LookPoolFaceValue](../globals/g_LookPoolFaceValue.md), [g_AiCommandTable](../globals/g_AiCommandTable.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A battle can hold all 21 battle unit records on the field with 21 distinct looks once six stores sized for 16 drawing slots, 15 looks or 16 AI numbers are widened: the scene units, the look pool (and its face values), the AI's per-number tables, the per-slot palette rows, the HD sheet groups, and the HD character renderer's per-slot light block.

## Behavior

- V: the HD character renderer's per-slot block ([g_CharaRenderer + 0x242A0], 1104 bytes, built by CharaRenderer_Init) is: +0 16 x 20 bytes of the map's light sources (CharaRender_LoadMapLights, not per slot), +320 the map number, +324 / +325 two bytes, +328 16 x 40 bytes per drawing slot (CharaRender_UnitLight; SceneUnit_BuildFromQueueEntry sets the slot's factor at record +24 to 1.0), +968 16 x 8 bytes per drawing slot (CharaRender_UnitFlash), +1096 / +1097 two bytes. Every access is the block pointer plus a fixed field offset (the 8-byte array and the two bytes: 30 operands in 12 functions); the helpers take a slot of 16 or more as slot 0, the HD draw (sub_140415BF4, sub_140415CFC, HdLayer_ResolveQuadTexture) indexes by the draw record's slot with no clamp.
- V: ClutFade_UnitSlot takes 16 and up as every slot; four callers ask for every slot with exactly 16.
- V: ClutManager_Update fades a palette bank row by row when the bank's first flag byte is 0, and the whole bank (all 256 colours) whenever row 0's header has a fade running when it is not 0; the battle's palette reset (sub_1402F79F8) sets the byte to 1 for every bank and clears it for banks 2, 3, 4 and 7 only.
- V: three more readers of the renderer's per-slot 8-byte entries clamp the slot without a branch (slot & -(slot < 16): the highlight flash setter sub_14027073C, DoScreenSave, and sub_140260CF0 with its limit in a register, 12 + 4), so a slot of 16 or more shares slot 0's entry.
- V: palette banks 8 and 9 of g_ClutManager are named by no caller and are uploaded with the other 12 rows (image rows 488 and 489 in video memory and in the g_SaveYoxPage shadow the HD textures are built from), so they hold 32 free rows.
- V (tested 2026-11-21, random battle at Mandalia Plain, the battle's entries replaced with 16 distinct monster families, variable 57 forced to -7, 5 party units: 21 units on the field, 21 distinct looks, 21 drawing slots): with the scene units, the look pool, the face values and the AI's four per-number tables moved in memory to 21 entries, the per-slot rows of banks 3, 4, 7 and 10 for slots 16..20 sent to banks 8 / 9 (the row copy, the fade target, UnitClut_TintRow's four operands, the CLUT word, the header test of SceneObjects_StepStates), ClutFade_UnitSlot's every-slot callers given 127 and its loop 21, the renderer's per-slot block laid out for 21 slots (the 8-byte array 200 bytes later, the two bytes 240 later, 1344 bytes, the helpers' clamp 21), sub_14026E838's classic copy and frame pointer store kept inside its 8 buffers, and the HD sheet groups of WordSeventeensArithmeticReachesNewSheetGroups: all 21 units were placed and drawn with their own sprites, palettes and portraits, lit by the map's light like the others; the AI moved the enemies and a party unit with AI number 19 on Auto-battle; no fault was recorded.
- V (seen live, same setup, before each fix): the units of drawing slots 16.. drew brighter than the others, not darkened by the map's light (the block not laid out; seen by eye on the game window); with ClutFade_UnitSlot's 16 read as one slot their deployment fade stayed on (a pale glow); and with banks 8 / 9 left in whole-bank mode, the active unit's pulse on bank 8 row 0 made every unit of slots 16..20 flash with it (seen by eye on the game window; bank 8's rows then all held, row 0's counter running).
- V (seen live after the fix): banks 8 and 9 in row mode after the reset, only the active unit's row fading.

## Open questions

? a mid-battle resume with more than 16 units (the battle capture copies 16 scene units, 15 look records, 10 face values and the AI block's stock part); ? the classic (low-resolution) path for looks past 15; ? event scripts' per-slot extra-page table (16 dwords at xmmword_142E801A8) for slots past 15.
