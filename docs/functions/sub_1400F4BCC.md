# sub_1400F4BCC

- **Address:** `0x1400F4BCC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `_DWORD *sub_1400F4BCC(__int64 unused, unsigned int soundKey)`
- **Callers:** about 290 sites, among them JobTree_OnEvent, JobTree_HandleInput, sub_140130DF0, sub_140131068, sub_140131688, sub_140131734, sub_1400F4D38, sub_14012E82C
- **Callees:** UITable_GetRowByKey, EventSoundEntry_Append, SoundCue_Play, sub_1401D964C, sub_1401D80A8

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Plays a UI sound cue: looks key soundKey up in UI table 0x45 and starts the sound the row names, dispatching on the row's type word.

## Behavior

- V: row = UITable_GetRowByKey(0x45, soundKey); returns the (null) row when missing and does nothing.
- V: switch on the u16 at row+8: 0x66 -> SoundCue_Play(row[3] - 1); 0x15E -> EventSoundEntry_Append(qword_143CD9DD8, row[3]); 0x17E -> sub_1401D964C(qword_143CD9DD8 + 1384, row[3]); 0x180 -> sub_1401D80A8(qword_143CD9DD8, 10, row[3] + 1); any other type value does nothing. row[3] is the dword at row+12 (the sound / entry id).
- V: a1 is ignored (callers pass a leftover register). The function has about 290 callers: every screen's confirm / cancel / cursor-move cue goes through it.
- V: Job Tree / job-list uses: ids 14 (0xE, confirm-like), 15 (0xF, cancel), 17 (0x11, cursor enter in JobTree_OnEvent), 0xE6 (230, refused action).

## State touched

- Calls: [UITable_GetRowByKey](UITable_GetRowByKey.md), [EventSoundEntry_Append](EventSoundEntry_Append.md), [SoundCue_Play](SoundCue_Play.md), [sub_1401D80A8](sub_1401D80A8.md)

## Referenced by

- Called by: [BattleCommand_BuildScreen](BattleCommand_BuildScreen.md), [Battle_CommandTask](Battle_CommandTask.md), [Battle_InitScene](Battle_InitScene.md), [Battle_TimelineFocusCamera](Battle_TimelineFocusCamera.md), [BgmMode_OnTabButton](BgmMode_OnTabButton.md), [BgmMode_ToggleTitleLanguage](BgmMode_ToggleTitleLanguage.md), [EventControl_PausedTick](EventControl_PausedTick.md), [EventPreviewUnits_RunFrames](EventPreviewUnits_RunFrames.md), [JobList_SelectEntry](JobList_SelectEntry.md), [JobTree_HandleInput](JobTree_HandleInput.md), [JournalReplay_StartEvent](JournalReplay_StartEvent.md), [JournalReplay_StartMovie](JournalReplay_StartMovie.md), [MovieControl_PausedTick](MovieControl_PausedTick.md), [UIAddonFFTOTitle_OnEvent](UIAddonFFTOTitle_OnEvent.md), [Unit_SpendJp](Unit_SpendJp.md), [WorldMapRouteGrow_OnState](WorldMapRouteGrow_OnState.md), [sub_1400F4D38](sub_1400F4D38.md), [sub_140107914](sub_140107914.md), [sub_140130DF0](sub_140130DF0.md), [sub_140131068](sub_140131068.md), [sub_140131688](sub_140131688.md), [sub_140131734](sub_140131734.md), [sub_14016E60C](sub_14016E60C.md), [sub_140183C38](sub_140183C38.md), [sub_140183DD4](sub_140183DD4.md), [sub_1401A161C](sub_1401A161C.md), [sub_1401EA2F0](sub_1401EA2F0.md), [sub_140214404](sub_140214404.md), [sub_140214610](sub_140214610.md), [sub_1402722D8](sub_1402722D8.md), [sub_1402C6514](sub_1402C6514.md), [sub_1402C72B8](sub_1402C72B8.md)

## Notes

Proposed name UISound_Play (medium confidence; kept as sub_ because the table 0x45 columns and the four handler types are not decoded). Counterpart that stops / sets state is sub_1400F4C54.

## Open questions

? what the four type words 0x66 / 0x15E / 0x17E / 0x180 name (sound effect banks?). ? table 0x45 column layout. ? the meaning of ids 14 / 15 / 17 / 230 (judged from use only).
