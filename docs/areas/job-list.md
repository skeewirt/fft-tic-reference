# Job list and unlock

JobList_*, Job_*, Party_* and unlock/mask pages.

Functions: 21, Structures: 2.

## Functions (21)

| Name | Address | Purpose |
|---|---|---|
| [BitStream_ReadBits](../functions/BitStream_ReadBits.md) | `0x140360A74` | MSB-first bit reader over the stream at `qword_143C49BF8`; the bit cursor is `dword_140906AAC`. |
| [Job_IdToIndex](../functions/Job_IdToIndex.md) | `0x1402B8F18` | Maps a job key to its tree/unlock index. |
| [Job_IsLockedForParty](../functions/Job_IsLockedForParty.md) | `0x14028641C` | Returns 1 if NO party member has the job unlocked, else 0. |
| [JobChange_FillUnitEntry](../functions/JobChange_FillUnitEntry.md) | `0x14033751C` | Fills one 704-byte unit entry of the job-change screen: unit name, job list state, the current JobRecord/icon and the five equipped ability ids. |
| [JobChange_RunPreviewAnim](../functions/JobChange_RunPreviewAnim.md) | `0x140367F38` | Runs the job-change preview: builds scratch sprite/palette buffers and drives the change-animation node for the chosen job. |
| [JobChangeAddon_SetState](../functions/JobChangeAddon_SetState.md) | `0x14012FC6C` | Switches the job-change list addon (UIAddonFFTOUnitJobChange2) to a new mode and updates focus, tab bar, sprite requests and cursor for that mode. |
| [JobList_ApplyCellRecord](../functions/JobList_ApplyCellRecord.md) | `0x140131E4C` | Shows one job record in a job-change cell gadget: star, Active/Deactive/Black state, the unit sprite, the current-job mark and the job text. |
| [JobList_Build](../functions/JobList_Build.md) | `0x1402864AC` | Builds the runtime job list `g_RuntimeJobList` (uint16[], length `g_RuntimeJobListLen`). |
| [JobList_IsSelectedEntryUnflagged](../functions/JobList_IsSelectedEntryUnflagged.md) | `0x140367F00` | Tells whether the runtime-list entry under the list cursor lacks the 0x4000 flag (the 'current job' flag), when the list has two or more jobs. |
| [JobList_OnCursorChanged](../functions/JobList_OnCursorChanged.md) | `0x140131BF8` | Cursor-change handler of the job-change list (UIAddonFFTOUnitJobChange2). |
| [JobList_RecomputeAvailability](../functions/JobList_RecomputeAvailability.md) | `0x14028B6B0` | Recomputes the party-wide job-availability flags from each unit's job levels and the runtime job bits. |
| [JobList_SelectEntry](../functions/JobList_SelectEntry.md) | `0x14012F7F4` | Handler for screen message 128 (a tree panel was clicked): puts the job-change list cursor on cell `idx`, moves the highlight there and switches the list mode. |
| [JobList_StoreCell](../functions/JobList_StoreCell.md) | `0x14012EC5C` | Copies a 148-byte job record into cell `index` of the job-change list (addon+0x2280+148*index); `if (index >= 19) return` (cmp at 0x14012EC81). |
| [JobListScreen_GetCursorIndex](../functions/JobListScreen_GetCursorIndex.md) | `0x140116100` | Returns the job-change list's current cursor index through the holder object that owns the list addon. |
| [JobScreen_OpenJobPage](../functions/JobScreen_OpenJobPage.md) | `0x1402B9FB8` | Builds and shows the ability page of a job on the job screen: collects the unit's ability rows for the job and fills the page lists. |
| [JobScreen_ShowPopup](../functions/JobScreen_ShowPopup.md) | `0x1402BB5D4` | Thin wrapper that opens a message popup: forwards to sub_14031E94C, sets a screen flag and starts popup SoundCue_Play(a2 - 1). |
| [JobScreen_UpdateState](../functions/JobScreen_UpdateState.md) | `0x140368B4C` | Per-frame state machine of the job screen (states 1400..1412): reads the job-change list cursor, picks the job from g_RuntimeJobList, shows its ability page, runs the job change and the preview animation. |
| [Party_GetUnitJobId](../functions/Party_GetUnitJobId.md) | `0x1402863E4` | Returns the job id of a party member, normalising the generic-unit marker values. |
| [sub_1401321FC](../functions/sub_1401321FC.md) | `0x1401321FC` | Fills the "Level Requirements for <job>" window of the Change Job grid: one row per job the selected cell's job requires, with that job's icon and name, the required level and the unit's current level (or "Locked"). |
| [Unit_BuildJobUnlockMask](../functions/Unit_BuildJobUnlockMask.md) | `0x140348684` | Builds the 24-bit job-unlock mask for a unit. |
| [Unit_CollectJobSkillsets](../functions/Unit_CollectJobSkillsets.md) | `0x1402866E4` | Builds the secondary-skillset choice list of a party unit: the skillset byte of every job the unit can take, except its own job and three excluded ids, terminated by 0xFFFF. Returns the count. |

## Structures (2)

| Name | Size (bytes) | Summary |
|---|---|---|
| [AbilityListRow](../structs/AbilityListRow.md) | 8 | One 8-byte row of the job screen's ability page: word 0 job id, word 1 ability id with flag bits; the list ends with {0, 0xFFFF}. |
| [JobListWord](../structs/JobListWord.md) | 2 | One entry of g_RuntimeJobList: the job id in bits 0..9, bit 13 locked (not unlocked by any party member) and bit 14 current job. |
