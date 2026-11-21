# SixteenSceneUnitsComeOnlyFromTheLookQueue

- **Kind:** observed behaviour
- **Scope:** engine (battle unit drawing)
- **Area:** [Graphics](../areas/graphics.md)
- **Affects:** [SceneUnit_BuildFromQueueEntry](../functions/SceneUnit_BuildFromQueueEntry.md), [CharaPalette_ReloadForShape](../functions/CharaPalette_ReloadForShape.md), [LookPool_ResetForBattleLoad](../functions/LookPool_ResetForBattleLoad.md), [SceneUnits_SaveRestore](../functions/SceneUnits_SaveRestore.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A battle unit is drawn through one of 16 scene-unit records, and only SceneUnit_BuildFromQueueEntry creates them, from the 16-entry look queue; with all 16 in use the next unit gets no scene unit.

## Behavior

- V: the scene-unit records are 16 x 1352 bytes (in-use dword at 0x140D30030, g_SceneUnitSlots at +8); SceneUnit_BuildFromQueueEntry takes the requested record below 16 or the first free one and returns null when none is free.
- V: SceneUnit_BuildFromQueueEntry has one caller, CharaPalette_ReloadForShape, which runs from the battle load (BattleLoad_StepFresh), the mid-battle join (Battle_JoinUnitAndLoad), sub_14023A0B4 and sub_14030476C.
- V: five functions address the in-use dwords: LookPool_ResetForBattleLoad, SceneUnit_BuildFromQueueEntry, SceneUnits_SaveRestore, sub_1401D4544 and sub_14033D6B0.
- V: a scene unit is released only by SceneUnit_Release: from the event-script case that takes a unit off, from the deployment steps (a unit taken back off its cell), from SceneObjects_StepStates when a unit's state reaches 'gone', and from SceneUnits_ReleaseAll; the look pool record goes with it when no other drawn unit shares it.
- V (tested limit, random battle at Mandalia Plain with 12 entries sharing one look placed through a forced variable 57 of -7): 12 entries plus 4 placed party units used all 16 scene units (5 look pool records); placing a fifth party unit (the 17th unit) crashed the game: the deployment step (sub_1401F3128 at 0x1401F330F) reads the placed unit's scene object (state +0x18, then +0x148) and there was none.
- V: entries that start parked (presence 0x00 or a lost random bit) take no scene unit (seen live: random battle, 5 parked records, none had one); entries built hidden (0xC0) take one.
- V (seen live, Orbonne Monastery and Magick City of Gariland): a knocked-out unit keeps its scene unit and look pool record (4 enemies down at Orbonne, 12 of 16 still in use); a unit that turned into a crystal kept them too (Gariland, record 2: 11 of 16 still in use).
- V: the 16 records (0x140D30030..0x140D354B0) are followed at once by dword_140D354B0, the palette rows of sprites 155..158 (SceneUnit_TintOwnRow); six functions take the block's start or end as an address (LookPool_ResetForBattleLoad, SceneUnit_BuildFromQueueEntry, SceneUnits_SaveRestore, sub_1401D4544 and sub_14033D6B0 with a 0x5480-byte clear, SceneUnit_RunPlacement and sub_14026F698 through the next global).
- V: SceneUnits_SaveRestore copies exactly 0x5480 bytes (16 records) to and from a fixed place in the battle capture (+1200), next to the CLUT manager copy (0x86DC bytes).
- V: the look queue holds 16 entries of 32 bytes after its count (g_LookQueueCount, 0x141856720); LookQueue_Add writes at the current count before testing it against 16, so a 17th add writes a 17th entry over dword_141856928 and g_BattleEntrySource (0x141856930), and every later add rewrites that same place.
- V: each scene unit's palette row is row = its slot in CLUT bank 4 (sub_1402F7594), and that function treats a bank as 16 rows.

## Open questions

? a chest and a picked-up crystal (by the code: the pickup takes the unit off through SceneObjects_StepStates, which releases it; not seen); ? what a reveal past 16 drawn units does (SceneUnit_BuildFromQueueEntry returns null: by the code the unit is on the field but not drawn; not tried).
