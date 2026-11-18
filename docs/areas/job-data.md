# Job data

Job table accessors, job records, skillsets, learning and job icon paths.

Functions: 35, Structures: 15, Globals: 2, Registries: 1, Flows: 1, Observed behaviours: 27, Tables: 15.

## Functions (35)

| Name | Address | Purpose |
|---|---|---|
| [BattleUnit_BuildJobRecord](../functions/BattleUnit_BuildJobRecord.md) | `0x1400FCF80` | Builds the 148-byte job record of battle unit `slot` for the battle panels: its job, levels and JP, through JobRecord_FromJobId. |
| [GameState_ResetJobFlags](../functions/GameState_ResetJobFlags.md) | `0x14028433C` | New-game reset that initialises byte_1411A7490: 125 per-jobtype flags (at +21) to 1 and 21 per-generic-job flags (at +0) to (GeneralJob.Unknown78 == 0), then clears a block of party/story state. |
| [GuiImage_SetIconById](../functions/GuiImage_SetIconById.md) | `0x1402A8F40` | Binds an icon image, chosen by its Icon table key, to a UI image object; used by many screens that show job, command or ability icons. |
| [Icon_FormatPath](../functions/Icon_FormatPath.md) | `0x1400FC9A8` | Formats 'ui/ffto/icon/<IconFilePath>' (or the same path with a texture-parts URI prefix) from Icon row iconKey (table 118, cache qword_143CDA328). |
| [Job_BuildTabAbilityList](../functions/Job_BuildTabAbilityList.md) | `0x14028A400` | The tab-filtered ability list of a job's skillset (its JobTable row byte 0), or of `defaultSkillset` when no row holds that skillset. |
| [Job_GetJpForLevel](../functions/Job_GetJpForLevel.md) | `0x1402CC008` | Returns RequiredJobExp[level] of the GeneralJob row (table 189, cache qword_143CD9F00): u16 at row-data + 4 * level where the list offset is the dword at row +8. |
| [Job_HasMonsterPair](../functions/Job_HasMonsterPair.md) | `0x1402CBF60` | True when Job row +36 or +40 (Unknown10 / Unknown11) is nonzero: the job has a monster sprite/portrait pair. |
| [Job_IsChemistType](../functions/Job_IsChemistType.md) | `0x140270C58` | True when the Job row of the unit's job byte (unit+3) has jobtype +24 == 31. |
| [Job_IsHiddenFromTree](../functions/Job_IsHiddenFromTree.md) | `0x1402CBED4` | Returns 1 when the Job row (table 46, row = job id) has a nonzero HideJobTree byte at +60, else 0. |
| [Job_LearnAbilityByMenu](../functions/Job_LearnAbilityByMenu.md) | `0x14028936C` | Marks an ability as learned in the current party member's record when the player buys it in the job menu, then refreshes the hidden Onion Knight level and posts the learning notification. |
| [Job_LevelFromTotalJp](../functions/Job_LevelFromTotalJp.md) | `0x140278D5C` | Returns the job level (0..8) a total JP gives: how many of the 8 GeneralJob thresholds it reaches. |
| [JobAbilityList_Build](../functions/JobAbilityList_Build.md) | `0x1402867BC` | Builds the list of abilities shown for a job (skill-set abilities filtered by tab) for the job screen, learn menu and job-list availability tests. |
| [JobCommandTable_GetRow](../functions/JobCommandTable_GetRow.md) | `0x1400F84F4` | Returns the JobCommand-en row (table 41, cache qword_143CDA2E0). |
| [JobLearnList_ReadSelectedJp](../functions/JobLearnList_ReadSelectedJp.md) | `0x1402B9384` | The JP the Learn Abilities list shows: the selected party unit's JP in the job the Jobs screen has selected. |
| [JobList_BuildForPartyUnit](../functions/JobList_BuildForPartyUnit.md) | `0x14028662C` | Builds the job list of one party unit: points the bit reader at its unlock mask and calls JobList_Build with its job, marker and flags. |
| [JobRecord_FromJobId](../functions/JobRecord_FromJobId.md) | `0x1400FBB7C` | Builds the 148-byte job record used by the job tree and job-change screens from a job key and the unit's job arrays. |
| [JobScreen_BuildTabList](../functions/JobScreen_BuildTabList.md) | `0x140367A30` | Builds the list of one tab of the ability screen of the selected party unit into word_142E93E40: tab 1 = the secondary skillsets as (job, skillset) entries, tabs 2..5 = sub_14028A8B0's lists. |
| [JobScreen_FindJobOfSkillset](../functions/JobScreen_FindJobOfSkillset.md) | `0x140367888` | Finds which job a secondary skillset belongs to for the selected party unit: the first (job, skillset) pair of the unit's secondary list whose skillset matches, else the unit's own job; then hands (job, skillset) on. |
| [JobTable_GetNameText](../functions/JobTable_GetNameText.md) | `0x1400F4800` | Copies one of four Job-en string slots (+8, +12, +16, +20) into out, chosen by language (0/1) and variant (0/1), falling back to the other. |
| [JobTable_GetRow](../functions/JobTable_GetRow.md) | `0x1400F8574` | Returns the Job-en row for a job key (null if missing). |
| [Party_CountMasteredJobs](../functions/Party_CountMasteredJobs.md) | `0x140348828` | Counts the generic jobs whose every ability is learned and returns half of that count, capped at 7. |
| [Skillset_BuildAbilityList](../functions/Skillset_BuildAbilityList.md) | `0x140275980` | Builds the 24-entry ability list of a skillset into a shared static buffer, keeping only the ability classes the caller's mask allows. |
| [Skillset_BuildTabAbilityList](../functions/Skillset_BuildTabAbilityList.md) | `0x14028A370` | The 24 abilities of a skillset with every entry outside the tab's id window cleared. |
| [Skillset_GetAbility](../functions/Skillset_GetAbility.md) | `0x140275860` | Returns the ability id stored in one slot of a skillset, or 0 when the set or slot does not exist. |
| [sub_14028668C](../functions/sub_14028668C.md) | `0x14028668C` | Builds the job list of a unit given as a work record (C), not a party index: it points the bit reader at the work record's unlock mask and calls JobList_Build in mode 1, so the result holds only the jobs the unit has ... |
| [sub_140286A78](../functions/sub_140286A78.md) | `0x140286A78` | Collects the abilities of a party unit's current job into the list buffer used by the job screen, marking each entry that is available to the unit. |
| [sub_14028A8B0](../functions/sub_14028A8B0.md) | `0x14028A8B0` | Builds the ability list of a job-screen ability page for the selected party unit: the rows of the unit's own job plus the jobs 75..92, optionally sorted by a name-row order key. |
| [sub_1402C1628](../functions/sub_1402C1628.md) | `0x1402C1628` | Fills a unit's stat summary from a party record handed over in the same three copied parts as sub_1402C185C. |
| [sub_1402C185C](../functions/sub_1402C185C.md) | `0x1402C185C` | Builds a unit's detail panel (job line, icon, equipment, ability names) from a party record handed over in three copied parts. |
| [sub_140366FE0](../functions/sub_140366FE0.md) | `0x140366FE0` | The job screen's per-frame update: it tracks the selected unit and row, rebuilds the ability rows for the unit's job, handles input on the ability and equipment lists, and refreshes the detail panel. |
| [Unit_AwardJobJp](../functions/Unit_AwardJobJp.md) | `0x140283664` | Adds JP to one job of a battle unit: current JP and total JP (both capped at 9999), recomputes the job's level from the total and rebuilds the unit's unlock mask. |
| [Unit_CollectJobSkillsetPairs](../functions/Unit_CollectJobSkillsetPairs.md) | `0x14028A7C0` | Lists (job, skillset) pairs of the jobs a party unit can take as its secondary skill: 8-byte entries, 0xFFFF in the second word ends the list. |
| [Unit_SpendJp](../functions/Unit_SpendJp.md) | `0x1402B9AD0` | Subtracts the ability's JP cost from the unit's JP of the given job: *(u16 *)(g_PartyUnits[unit] + 2 * Job_IdToIndex(jobId) + 202) -= cost. |
| [UnitWork_FindJobBySkillset](../functions/UnitWork_FindJobBySkillset.md) | `0x14028AC50` | The first job of a work record's job list whose JobTable row holds `skillset`; the record's own job (+3) when none does. |
| [UnitWork_PackJobLevels](../functions/UnitWork_PackJobLevels.md) | `0x140278DA8` | Rebuilds the packed job-level nibbles of a save record from the unit total-JP array, two jobs per byte. |

## Structures (15)

| Name | Size (bytes) | Summary |
|---|---|---|
| [AbilityEventPair](../structs/AbilityEventPair.md) | 4 | One row of the AbilityEventPairs table. |
| [CommandKindRow](../structs/CommandKindRow.md) | 1 | One byte per skillset id. |
| [JobChangeListAddon](../structs/JobChangeListAddon.md) | 19024 | The Change Job list screen object (the list addon, reached as [[[root]+0x10]+0x58]+0x78 and as field 15 of the screen object): 19 cell records of 148 bytes, 19 cell gadgets of 256 bytes, and the cursor state; every ar... |
| [JobMasteryIdRow](../structs/JobMasteryIdRow.md) | 4 | One job id. |
| [JobNeedLevelRow](../structs/JobNeedLevelRow.md) | 12 | The required job levels for one job index: 24 nibbles. |
| [JobTableRow](../structs/JobTableRow.md) | 49 | One 49-byte row of the stock job table: skillset, always-on abilities, equipment classes, growth constants, move, jump, evade, status and element sets and three look bytes. |
| [MonsterSkillsetRow](../structs/MonsterSkillsetRow.md) | 5 | One 5-byte monster skillset: one flag byte and four low ability id bytes. |
| [NxdDataEggRow](../structs/NxdDataEggRow.md) | 24 | One row of the nxd.egg table (data table). |
| [NxdDataGeneralJobRow](../structs/NxdDataGeneralJobRow.md) | 124 | One row of the nxd.general_job table (data table). |
| [NxdDataJobCommandRow](../structs/NxdDataJobCommandRow.md) | 36 | One row of the nxd.job_command table (English text table; the other languages share the layout). |
| [NxdDataJobRow](../structs/NxdDataJobRow.md) | 64 | One row of the nxd.job table (English text table; the other languages share the layout). |
| [NxdDataJobTypeRow](../structs/NxdDataJobTypeRow.md) | 16 | One row of the nxd.job_type table (data table). |
| [RuntimeJobListEntry](../structs/RuntimeJobListEntry.md) | 2 | One entry of the Change Job list as built by the game. |
| [SkillsetRow](../structs/SkillsetRow.md) | 25 | One 25-byte skillset: three bytes of ability bit-9 flags followed by 22 low ability id bytes. |
| [UnitJobFlagsBlock](../structs/UnitJobFlagsBlock.md) | 146 | The job flag block (g_UnitJobFlags). |

## Globals (2)

| Name | Address | Type | Summary |
|---|---|---|---|
| [g_JobTable](../globals/g_JobTable.md) | `0x140785E30` | `uint8[174][49]` | The stock job table: 174 rows of 49 bytes. |
| [g_UnitJobFlags](../globals/g_UnitJobFlags.md) | `0x1411A7490` | `uint8[146]` | The job flag block: 21 per-job new flags then 125 per-job-type disable flags (see UnitJobFlagsBlock); saved in the save file. |

## Registries (1)

| Name | Summary |
|---|---|
| [JobIdSpace](../registries/JobIdSpace.md) | What a job id (the byte in save record +2 and work record +3) means to the code, and the job index the per-job arrays use for it. |

## Flows (1)

| Name | Summary |
|---|---|
| [ScriptedBattleUnitsFromEntries](../flows/ScriptedBattleUnitsFromEntries.md) | How a scripted battle gets its units: the battle key picks 16 entries, the OverrideEntryData rows of the key overwrite them in place, and battle unit i is built from entry i with row i. |

## Observed behaviours (27)

| Name | Scope | Summary |
|---|---|---|
| [BattleAbilityListReadsLearnedBitsThroughAPointerPastTheGroup](../behaviors/BattleAbilityListReadsLearnedBitsThroughAPointerPastTheGroup.md) | engine (battle ability list) | The battle's usable-ability list builder reads the three learned bytes of a job group from a battle record with the group number in one address register and the record pointer plus twice the group in the other, so for... |
| [BattleActionJpFormulaAndSpillover](../behaviors/BattleActionJpFormulaAndSpillover.md) | engine (battle JP award) | JP for an action is 8 + 2 x the job level of the acting unit's current job + the unit's level / 4, scaled by an event percentage and by JP Boost; every other unit of the battle gets a quarter of that base amount in th... |
| [BattleCommandHeaderTakesTheUnitsJobByte](../behaviors/BattleCommandHeaderTakesTheUnitsJobByte.md) | engine (battle Abilities list) | The header of the battle Abilities list (the job name and icon above the commands) is a job record built by sub_140335140: for the unit's own job command it takes the battle unit's job byte (+3); for a secondary comma... |
| [BattleJpGoesToTheJobOfTheUnitsByteNotItsClass](../behaviors/BattleJpGoesToTheJobOfTheUnitsByteNotItsClass.md) | engine (battle JP award and learning) | The battle JP award reads the acting unit's job byte, runs it through Job_IdToIndex and adds the JP to that job's slot: a job id wider than the byte cannot be held in it. |
| [BattlePanelsNameTheJobByte](../behaviors/BattlePanelsNameTheJobByte.md) | engine (battle unit panels) | The battle's unit panels and command screens name a unit's job from its job byte (+3) or from the first listed job whose row holds a skillset, never from a party word. |
| [BattleRosterCopiesCarryTheBattleSlotAt44](../behaviors/BattleRosterCopiesCarryTheBattleSlotAt44.md) | engine (battle party records) | In battle the party records are copies of battle unit records: PartyUnit_FillFromWorkRecord fills the battle roster records from the battle unit table, writing the unit's battle slot at +44 and its save slot at +0x1E,... |
| [CombatSetJobBytesAreOnlyCopied](../behaviors/CombatSetJobBytesAreOnlyCopied.md) | engine (party and save records) | The three combat-set job bytes of a unit record (party record +462, +550, +638; save record +380, +468, +556) are never read as a job by the status, equipment or combat-set screens: every access seen is a whole-record... |
| [JobArrayAccessesPutTheRecordPointerInTheIndexRegister](../behaviors/JobArrayAccessesPutTheRecordPointerInTheIndexRegister.md) | engine (per-unit job arrays) | Nine accesses of the per-unit job arrays are written with the byte offset in the register that stands first in the address and the pointer into the record in the register that stands second, so the record pointer is n... |
| [JobArraysInThePartyRecordHoldStockIndicesOnly](../behaviors/JobArraysInThePartyRecordHoldStockIndicesOnly.md) | engine (party record) | In the 640-byte party record the per-job arrays are sized for the stock job indices, so an access with a larger index leaves its own array and, from a certain index, the record. |
| [JobCardComesFromTheJobTypeRow](../behaviors/JobCardComesFromTheJobTypeRow.md) | engine (job card art on the Status screen) | The job card (the large faded painting behind the right half of the Status panel) is chosen by the job's JobType row, not by the job row's TexturePartsIndex (that is the small job icon): Job row +24 names a JobType ro... |
| [JobChangeReachesTheSaveRecordOnlyThroughWriteBack](../behaviors/JobChangeReachesTheSaveRecordOnlyThroughWriteBack.md) | engine (Jobs screen, party and save records) | Changing a unit's job on the Jobs screen changes the save record's job byte (+2) in exactly one place: PartyUnit_WriteBackToSave copies the low byte of the party record's job word (+0x24) into it. |
| [JobLearnedBitsPointerIsBuiltFromTheUnitRecord](../behaviors/JobLearnedBitsPointerIsBuiltFromTheUnitRecord.md) | engine | The readers of a job's learned bits compute a pointer into the unit record (unit record + 123 + 3 * job index) and hand it to the bit reader, which reads 24 bits = 3 bytes. |
| [JobLevelZeroDrawsDashesAndGreysChangeJob](../behaviors/JobLevelZeroDrawsDashesAndGreysChangeJob.md) | engine (Change Job grid and job popup) | A job whose level reads as 0 draws 'Lv. |
| [JobListBuilderCallersHold24Words](../behaviors/JobListBuilderCallersHold24Words.md) | engine (job list consumers) | JobList_BuildForPartyUnit is called by seven functions and each hands over a buffer sized for the stock list (24 words, 48 bytes); only the Jobs screen's own call uses the 48-word g_RuntimeJobList. |
| [JobListEntryWordMeaning](../behaviors/JobListEntryWordMeaning.md) | engine (runtime job list) | How JobList_Build fills an entry and what the readers do with its three parts: the id is the low 13 bits the mask keeps, bit 13 means locked for the whole party, and bit 14 means the unit's own job in mode 2 and 'unlo... |
| [JobTreePanelCountLimits](../behaviors/JobTreePanelCountLimits.md) | engine (Job Tree) | What bounds the number of Job Tree panels: the immediate widths of the count and cap compares, the render slots 80 + panel and the per-panel arrow capacity. |
| [NewUnitsGetStartingJpInEveryJob](../behaviors/NewUnitsGetStartingJpInEveryJob.md) | engine (starting JP of a new unit) | A new unit (a spawn: battle entries, the New Game party, recruits built by Unit_BuildFromRecord) gets starting JP in every job by the game's own rule for stock jobs (Unit_InitJobJp: the curve's value at the level plus... |
| [PartyJobWordIsSixteenBits](../behaviors/PartyJobWordIsSixteenBits.md) | engine (party and save records, Jobs screen) | The party record's 16-bit job word (+0x24) carries a job id above 255 through the Jobs screen, the status header and the skillset lookup; only the save record's byte (+2) cannot. |
| [PartyWriteBackCopiesSecondarySetAndReactionLowByteInOneLoop](../behaviors/PartyWriteBackCopiesSecondarySetAndReactionLowByteInOneLoop.md) | engine (party record to save record) | PartyUnit_WriteBackToSave copies two bytes in one two-pass loop: the low byte of the party record's secondary command word into save +7, then the low byte of the equipped reaction word into save +8; the reaction's hig... |
| [PassiveListsJoinTheCurrentAndStockJobs](../behaviors/PassiveListsJoinTheCurrentAndStockJobs.md) | engine | The reaction, support and movement lists of the Status screen join the rows of the unit's current job and of the stock jobs 75..92 only. |
| [PreviewBuildersReadPartyRecordCopies](../behaviors/PreviewBuildersReadPartyRecordCopies.md) | engine (party and save records) | The unit detail and summary builders (sub_1402C185C, sub_1402C1628) read a party record copied in three parts (header from +34, middle from +48, block from +112); the header names the save slot (header + 10 = +44), an... |
| [RuntimeJobListCanLiveInAnyBlockWithinReach](../behaviors/RuntimeJobListCanLiveInAnyBlockWithinReach.md) | engine (runtime job list) | Every reference to g_RuntimeJobList is a 32-bit displacement (four rip-relative `lea`, six reads through the image base plus a sign-extended index), the list is in the zero-filled tail of the data section and no data ... |
| [RuntimeJobListIs48WordsFollowedByAnotherGlobal](../behaviors/RuntimeJobListIs48WordsFollowedByAnotherGlobal.md) | engine (runtime job list) | g_RuntimeJobList is 96 bytes (48 words) and the next object in memory is g_UIChosenItemId, so the list cannot grow in place; the length is a signed 16-bit word kept at another address. |
| [SecondarySkillsetListsTakeEveryUnlockedJob](../behaviors/SecondarySkillsetListsTakeEveryUnlockedJob.md) | engine (secondary skillset lists) | Both secondary-skillset collectors build the unit's job list into a 24-word stack buffer, and write into lists that hold 145 entries: the three lists the game builds them into (g_MenuList, g_JobAbilityPairList, JobScr... |
| [SpawnedUnitsCarryAOneByteJob](../behaviors/SpawnedUnitsCarryAOneByteJob.md) | engine (spawn records, scripted battle entries) | A spawned unit's job is one byte of its spawn record (+10), copied into the work record's job byte; the scripted-battle table OverrideEntryData has a 32-bit MainJob column, but the copy keeps only its low byte. |
| [StockJobRowData](../behaviors/StockJobRowData.md) | stock job-related table rows | Facts about the stock job rows of job.en, generaljob and jobtype: unused rows still carry numbers, the generic jobs map to texture part indices, and Ramza's jobs share the Squire's job type. |
| [UnlockMaskStreamRunsIntoLearnedBitsPastIndex23](../behaviors/UnlockMaskStreamRunsIntoLearnedBitsPastIndex23.md) | engine (per-unit job state) | The unit's unlock mask is 3 bytes (24 bits) read through a bit stream, and the learned-ability bits follow it directly in the same record, so a bit read at a job index of 24 or more lands in the learned bits of the fi... |

## Tables (15)

| Name | Storage | NXD table id | Rows | Summary |
|---|---|---|---|---|
| [AbilityEventPairs](../tables/AbilityEventPairs.md) | Executable |  | 15 rows of 4 bytes | Pairs (key, event variable) that mark achievements when the job screen learns something; the object starts 0x30 earlier and also holds an unreferenced 16-byte list and a vtable. |
| [CommandKind](../tables/CommandKind.md) | Executable |  | 256 rows of 1 byte | The command kind of each skillset id: the battle range and action builders switch on it to decide how the skillset acts. |
| [Job](../tables/Job.md) | NXD file | 46 |  | The job rows (the Job-en table), read through JobTable_GetRow. |
| [JobCommand](../tables/JobCommand.md) | NXD file | 41 |  | The job command rows (the JobCommand-en table), read through JobCommandTable_GetRow. |
| [JobMasteryIds](../tables/JobMasteryIds.md) | Executable |  | 2 rows of 4 bytes | The two jobs whose full mastery gates job index 20 (Knight and Black Mage by id). |
| [JobNeedLevelRows](../tables/JobNeedLevelRows.md) | Executable |  | 22 rows of 12 bytes | Prerequisite job levels of each unlockable job. |
| [JobTable](../tables/JobTable.md) | Executable |  | 174 rows of 49 bytes | The stock job table: per job the skillset, always-on abilities, equipment classes, stat growth, base move / jump / evade, status and element sets and the look bytes of marker-130 units. |
| [NxdDataEgg](../tables/NxdDataEgg.md) | NXD file | 310 | 49 rows of 24 bytes | Per egg (a job grouping): three job ids and a parameter. |
| [NxdDataGeneralJob](../tables/NxdDataGeneralJob.md) | NXD file | 189 | 21 rows of 124 bytes | Per general job (21): arrays of required jobs, levels, positions and experience, and tree placement parameters. |
| [NxdDataJobType](../tables/NxdDataJobType.md) | NXD file | 200 | 124 rows of 16 bytes | Per job look type (124): male and female icon ids. |
| [RuntimeJobList](../tables/RuntimeJobList.md) | Executable (filled at run time) |  | 48 rows of 2 bytes | The Change Job list the game builds each time the job screen fills; the list length is a separate int16 at 0x143C510D8. |
| [SkillsetTable](../tables/SkillsetTable.md) | Executable |  | 176 rows of 25 bytes | Ability slots of the stock skillsets. |
| [SkillsetTableMonster](../tables/SkillsetTableMonster.md) | Executable |  | 48 rows of 5 bytes | Monster skillsets: four ability slots per set. |
| [SkillsetTableSpecial](../tables/SkillsetTableSpecial.md) | Executable |  | 3 rows of 25 bytes | Three further skillsets in the same layout as SkillsetTable, selected by Skillset_GetAbility for the ids above the monster range. |
| [UnitJobFlags](../tables/UnitJobFlags.md) | Executable (filled at run time) |  | 1 block of 146 bytes (21 + 125 flag bytes) | The job flag block: 21 per-job "new" flags and 125 per-job-type disable flags. |
