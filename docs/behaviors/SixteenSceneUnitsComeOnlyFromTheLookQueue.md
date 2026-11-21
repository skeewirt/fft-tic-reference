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
- V: at build each scene unit's palette row is copied to row = its slot in CLUT bank 4 (sub_1402F7594), and that function treats a bank as 16 rows (the shown colours are bank 3: next line).
- V (palette banks by drawing slot, 2026-11-20): four banks of the palette manager use the scene unit's slot (+8) as the row: bank 3 the shown colours (UnitClut_TintRow, and sub_1402735F0), bank 4 a raw copy at build (SceneUnit_BuildFromQueueEntry), bank 7 the status label colours (ResultLabel_ShowNext, sub_140268350) and bank 10 the placement colours (SceneUnit_RunPlacement, sub_1402735F0). Each bank is 16 rows of 16 colours (2450 bytes); a row 16 would run past the bank into the next one's header.
- V: the palette image uploaded is 14 rows of 256 colours at video memory (0, 480) (ClutManager_Upload: x 0, y 480, width 256, height 14), one row per bank; the scene unit's CLUT word 0x78C0 | slot points at y 483 (bank 3), x = 16 x slot, so a slot of 16 or more points past the uploaded width (x 256 and on).
- V: sub_1402735F0 (event scripts' extra-page load, from EventScript_Run and sub_140272A04) writes a dword per drawing slot into xmmword_142E801A8 (16 dwords, cleared by EventScript_Run); no reader was found by address. Slots 16..20 would write dword_142E801E8 and dword_142E801EC (EventSprite_LoadTask), dword_142E801F0, dword_142E801F4 (the current effect, tested against -1 by HdLayer_BuildTextures) and dword_142E801F8.
- V (seen live 2026-11-20, one sample: random battle at Mandalia Plain, 13 drawn units, Ramza's turn): in the video page (g_SaveYoxPage, 1024 x 512 words) row 483 held data at x 0..191 (slots 0..11); x 256 and on held other data on every row 480..503; row 488 was empty from x 0 to 351 and row 508 from x 0 to 847.
- V (code, 2026-11-20): every caller that names a palette bank was read: the row copy sub_1402F7594 is called with banks 0 (MapBlock_RunCommand, sub_14024FBD8), 2 (sub_14020E4EC, sub_14026FEC8, BattleLoad_StepFresh, sub_14030476C), 3, 4, 5 and 6 (ItemSprite_LoadPalettes), 7, 10, 12 and 13 (EffectFile_UploadTexture); the fade ClutFade_SetTarget (bank = third argument) with banks 0, 3 and 7 by its wrappers, and by ClutManager_Update only for fades already set. No code names bank 8 or 9.
- I: since ClutManager_Upload rewrites rows 480..493 x 0..255 from the manager on every change, rows 488 and 489 hold only banks 8 and 9 (empty in the live sample): 32 free palette rows, enough for the 5 extra rows of each of the four slot banks (3, 4, 7, 10).
- V: the scene object list (g_SceneObjectList) is a linked list through the scene unit records themselves (next pointer at +0, slot at +8; SceneObject_FindBySlot, sub_140260AEC, SceneUnit_BuildFromQueueEntry inserts), so it has no capacity of its own; the 0x420 bytes after its head are other saved variables.
- V: two extra sprite pages serve all drawn units (the 2 x 31976-byte area 0x140CE3264..0x140CF2C34; SceneUnit_LoadExtraPage, sub_140273468); the owner byte is the slot | 0x80, so slots up to 127 fit; the count of 2 is shared and does not depend on the number of drawn units.

## Open questions

? whether a battle load can pass 16 queued entries: the units brought on later (Battle_AddJoinedUnit, ScenePreview_ShowEntry) clear the count and queue one, the entries queue one each (16 at most), but BattleLoad_StepFresh builds the roster team (Battle_BuildRosterTeam, up to 5 more) in state 8 after consuming the queue in state 7 with no count reset found; ? a chest and a picked-up crystal (by the code: the pickup takes the unit off through SceneObjects_StepStates, which releases it; not seen); ? what a reveal past 16 drawn units does (SceneUnit_BuildFromQueueEntry returns null: by the code the unit is on the field but not drawn; not tried).
