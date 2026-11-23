# UIAgentSlots

- **Kind:** registry
- **Area:** [UI framework](../areas/ui-framework.md)
- **Resolved by:** [UIAgentManager_CreateAgents](../functions/UIAgentManager_CreateAgents.md)
- **Values stored in:** [UIAgentManager.agents_begin](../structs/UIAgentManager.md#agents_begin), [UIAgentManager.agents_end](../structs/UIAgentManager.md#agents_end)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The 54 UI agents the manager appends at construction, in slot order: six generic agents and 48 FFTO screens. The id is the agent vector index; the manager reads agents back by that index.

## Entries

| Id | Name | Value | Conf | Meaning |
|---|---|---|---|---|
| <a id="uiagentfade"></a>0 | `UIAgentFade` | `vtable 0x140713158; base ctor 0x1401D14F4; 88 bytes` | I | Full-screen fade overlay used by UI transitions; one of the six generic agents. |
| <a id="uiagentcursor"></a>1 | `UIAgentCursor` | `vtable 0x140713078; base ctor 0x1401D14F4; 136 bytes` | I | The finger cursor and its request stack; one of the six generic agents. |
| <a id="uiagentsoundvisualizer"></a>2 | `UIAgentSoundVisualizer` | `vtable 0x140712F98; base ctor 0x1401D14F4; 80 bytes` | I | The sound visualizer overlay; one of the six generic agents. |
| <a id="uiagentfftostartup"></a>3 | `UIAgentFFTOStartup` | `vtable 0x14070ADD0; base ctor 0x1401D14F4; 72 bytes` | V | The startup screen; the IDB comment names slot 3 Startup. |
| <a id="uiagentfftostartupconfig"></a>4 | `UIAgentFFTOStartupConfig` | `vtable 0x14070AD68; base ctor 0x1401D14F4; 128 bytes` | I | The first-start configuration screen. |
| <a id="uiagentfftolauncher"></a>5 | `UIAgentFFTOLauncher` | `vtable 0x14070AC08; base ctor 0x1401D14F4; 88 bytes` | V | The launcher and mode select (Enhanced or Classic); the IDB comment names slot 5 Launcher. |
| <a id="uiagentfftotitle"></a>6 | `UIAgentFFTOTitle` | `vtable 0x14070A5B0; ctor 0x1401C2AE4; 1448 bytes` | V | The title screens; owns the menu, play mode and saving addons. The IDB comment names slot 6 Title. |
| <a id="uiagentfftobgmmode"></a>7 | `UIAgentFFTOBGMMode` | `vtable 0x14070A2A8; base ctor 0x1401D14F4; 72 bytes` | I | The BGM mode: the music player reached from the title. |
| <a id="uiagentfftobattlemain"></a>8 | `UIAgentFFTOBattleMain` | `vtable 0x140712DD8; base ctor 0x1401D14F4; 96 bytes` | I | The battle main HUD. |
| <a id="uiagentfftobattlemenuwindows"></a>9 | `UIAgentFFTOBattleMenuWindows` | `vtable 0x140712D88; base ctor 0x1401D14F4; 120 bytes` | I | The battle menu windows: the command and ability pages. |
| <a id="uiagentfftobattlesystemmenu"></a>10 | `UIAgentFFTOBattleSystemMenu` | `vtable 0x140712D38; base ctor 0x1401D14F4; 80 bytes` | I | The battle system menu (the pause menu in battle). |
| <a id="uiagentfftounit"></a>11 | `UIAgentFFTOUnit` | `vtable 0x1407123F8; ctor 0x140113830; 216 bytes` | V | The unit screen: a party member's detail, with a job list and a command list. |
| <a id="uiagentfftocommonparts"></a>12 | `UIAgentFFTOCommonParts` | `vtable 0x1407113E0; base ctor 0x1401D14F4; 88 bytes` | I | The common parts shared by the FFTO screens. |
| <a id="uiagentfftoevent"></a>13 | `UIAgentFFTOEvent` | `vtable 0x140711260; base ctor 0x1401D14F4; 192 bytes` | I | The event scenes: dialogue and event UI. |
| <a id="uiagentfftoheaderfooter"></a>14 | `UIAgentFFTOHeaderFooter` | `vtable 0x140710C58; base ctor 0x1401D14F4; 80 bytes` | I | The header and footer overlay used by the FFTO screens. |
| <a id="uiagentfftomainmenuparts"></a>15 | `UIAgentFFTOMainMenuParts` | `vtable 0x140711478; base ctor 0x1401D14F4; 88 bytes` | I | The shared parts of the main menu. |
| <a id="uiagentnoticedialog"></a>16 | `UIAgentNoticeDialog` | `vtable 0x140711430; base ctor 0x1401D14F4; 104 bytes` | I | The generic notice and confirm dialog; one of the six generic agents. |
| <a id="uiagentloading"></a>17 | `UIAgentLoading` | `vtable 0x1407107A0; base ctor 0x1401D14F4; 72 bytes` | I | The generic loading screen; one of the six generic agents. |
| <a id="uiagentfftobattlescreen"></a>18 | `UIAgentFFTOBattleScreen` | `vtable 0x140710750; ctor 0x14013EE98; 624 bytes` | V | The battle screen agent: the battlefield HUD. |
| <a id="uiagentannounce"></a>19 | `UIAgentAnnounce` | `vtable 0x14070FF00; ctor 0x140151678; 2704 bytes` | V | The announcements (on-screen notices); one of the six generic agents. The IDB comment names slot 19 Announce. |
| <a id="uiagentfftoworldmap"></a>20 | `UIAgentFFTOWorldMap` | `vtable 0x14070FCC8; ctor 0x140156E78; 248 bytes` | V | The world map. |
| <a id="uiagentfftobravestory"></a>21 | `UIAgentFFTOBraveStory` | `vtable 0x14070EFF8; base ctor 0x1401D14F4; 176 bytes` | I | The Brave Story top screen. |
| <a id="uiagentfftobravestorybooks"></a>22 | `UIAgentFFTOBraveStoryBooks` | `vtable 0x14070EEA8 (a second vtable 0x14070EE88 is stored at +64); base ctor 0x1401D14F4; 96 bytes` | I | The Brave Story books list. |
| <a id="uiagentfftobravestoryzodiacstone"></a>23 | `UIAgentFFTOBraveStoryZodiacStone` | `vtable 0x14070EB10; base ctor 0x1401D14F4; 104 bytes` | I | The Brave Story Zodiac Stone page. |
| <a id="uiagentfftobravestorycollection"></a>24 | `UIAgentFFTOBraveStoryCollection` | `vtable 0x14070ED50; base ctor 0x1401D14F4; 152 bytes` | I | The Brave Story collection page. |
| <a id="uiagentfftobravestoryworkhistory"></a>25 | `UIAgentFFTOBraveStoryWorkHistory` | `vtable 0x14070E998; base ctor 0x1401D14F4; 120 bytes` | I | The Brave Story work history page. |
| <a id="uiagentfftojournal"></a>26 | `UIAgentFFTOJournal` | `vtable 0x14070EC70; base ctor 0x1401D14F4; 128 bytes` | V | The journal screen; its vtable carries JournalScreen_OnAction. |
| <a id="uiagentfftobravestoryglossary"></a>27 | `UIAgentFFTOBraveStoryGlossary` | `vtable 0x14070E8B8; base ctor 0x1401D14F4; 80 bytes` | I | The Brave Story glossary page. |
| <a id="uiagentfftobravestoryworldsituation"></a>28 | `UIAgentFFTOBraveStoryWorldSituation` | `vtable 0x14070E6F0; base ctor 0x1401D14F4; 80 bytes` | I | The Brave Story world situation page. |
| <a id="uiagentfftobravestorytrophy"></a>29 | `UIAgentFFTOBraveStoryTrophy` | `vtable 0x14070E530; base ctor 0x1401D14F4; 80 bytes` | I | The Brave Story trophy page. |
| <a id="uiagentfftobravestorydarlavon"></a>30 | `UIAgentFFTOBraveStoryDarlavon` | `vtable 0x14070E3D0; base ctor 0x1401D14F4; 80 bytes` | I | The Brave Story Darlavon page. |
| <a id="uiagentfftonovel"></a>31 | `UIAgentFFTONovel` | `vtable 0x14070E1B0; base ctor 0x1401D14F4; 80 bytes` | V | The novel reader; its code shows the novel's pages (NovelReader_ShowPage). |
| <a id="uiagentfftosubtitles"></a>32 | `UIAgentFFTOSubtitles` | `vtable 0x14070E078; base ctor 0x1401D14F4; 80 bytes` | I | The subtitle overlay. |
| <a id="uiagentfftoguide"></a>33 | `UIAgentFFTOGuide` | `vtable 0x14070BED8; base ctor 0x1401D14F4; 168 bytes` | I | The guide overlay (help tips). |
| <a id="uiagentfftoclassicsubtitles"></a>34 | `UIAgentFFTOClassicSubtitles` | `vtable 0x14070D8E0; base ctor 0x1401D14F4; 80 bytes` | I | The Classic mode subtitles. |
| <a id="uiagentfftoclassicband"></a>35 | `UIAgentFFTOClassicBand` | `vtable 0x14070D738; base ctor 0x1401D14F4; 96 bytes` | I | The Classic mode title band. |
| <a id="uiagentfftoclassicloading"></a>36 | `UIAgentFFTOClassicLoading` | `vtable 0x14070D578; base ctor 0x1401D14F4; 72 bytes` | I | The Classic mode loading screen. |
| <a id="uiagentfftosystem"></a>37 | `UIAgentFFTOSystem` | `vtable 0x14070DF00; ctor 0x140181C94; 1472 bytes` | V | The System menu. |
| <a id="uiagentfftosaveload"></a>38 | `UIAgentFFTOSaveLoad` | `vtable 0x14070DE48; ctor 0x140182B38; 1592 bytes` | V | The save and load screen. |
| <a id="uiagentfftoendslate"></a>39 | `UIAgentFFTOEndSlate` | `vtable 0x14070D5C0; base ctor 0x1401D14F4; 72 bytes` | V | The end slate: the chapter or task end card (EventEndSlate_ShowTask). |
| <a id="uiagentfftoshop"></a>40 | `UIAgentFFTOShop` | `vtable 0x14070D380; base ctor 0x1401D14F4; 144 bytes` | I | The shop screen. |
| <a id="uiagentfftobar"></a>41 | `UIAgentFFTOBar` | `vtable 0x14070CD20; base ctor 0x1401D14F4; 160 bytes` | V | The tavern top menu; its vtable carries TavernMenu_OnCommand. |
| <a id="uiagentfftoemploy"></a>42 | `UIAgentFFTOEmploy` | `vtable 0x14070BCF0; base ctor 0x1401D14F4; 128 bytes` | I | The employ (recruit) screen. |
| <a id="uiagentfftopoach"></a>43 | `UIAgentFFTOPoach` | `vtable 0x14070B7D0; base ctor 0x1401D14F4; 168 bytes` | V | The Poachers' Den screen; its code builds the poach list (PoachList_Build). |
| <a id="uiagentfftoitem"></a>44 | `UIAgentFFTOItem` | `vtable 0x14070BD58; base ctor 0x1401D14F4; 80 bytes` | I | The item screen. |
| <a id="uiagentfftofullscreenradialblur"></a>45 | `UIAgentFFTOFullScreenRadialBlur` | `vtable 0x140710918; base ctor 0x1401D14F4; 80 bytes` | I | The full-screen radial blur effect. |
| <a id="uiagentfftosituationsubtitles"></a>46 | `UIAgentFFTOSituationSubtitles` | `vtable 0x140710FA0; base ctor 0x1401D14F4; 80 bytes` | I | The situation subtitles overlay. |
| <a id="uiagentfftobattlecontinuous"></a>47 | `UIAgentFFTOBattleContinuous` | `vtable 0x14070FFE0; base ctor 0x1401D14F4; 120 bytes` | I | The continuous-battle screen agent; the role beyond the name was not read (?). |
| <a id="uiagentfftotextinput"></a>48 | `UIAgentFFTOTextInput` | `vtable 0x14070AEB0; ctor 0x1401B43DC; 1328 bytes` | I | The text input screen (name entry). |
| <a id="uiagentfftochapterpicture"></a>49 | `UIAgentFFTOChapterPicture` | `vtable 0x140710EC0; base ctor 0x1401D14F4; 88 bytes` | I | The chapter picture card. |
| <a id="uiagentfftocredit"></a>50 | `UIAgentFFTOCredit` | `vtable 0x14070A770; base ctor 0x1401D14F4; 104 bytes` | I | The credits screen. |
| <a id="uiagentfftoopcredit"></a>51 | `UIAgentFFTOOpCredit` | `vtable 0x14070A690; base ctor 0x1401D14F4; 80 bytes` | V | The opening credits; the IDB comment names slot 51 OpCredit. |
| <a id="uiagentfftoendingsave"></a>52 | `UIAgentFFTOEndingSave` | `vtable 0x14070DAE0; base ctor 0x1401D14F4; 72 bytes` | I | The ending save prompt. |
| <a id="uiagentfftosubquest"></a>53 | `UIAgentFFTOSubquest` | `vtable 0x140710CA8; base ctor 0x1401D14F4; 80 bytes` | I | The subquest screen. |

## Behavior

- V: the manager appends one agent per `Mem_Alloc` in this order; the vector index is the slot id (54 allocations and 54 appends).
- V: the IDB comment on `UIAgentManager_CreateAgents` names slots 3 Startup, 5 Launcher, 6 Title, 19 Announce and 51 OpCredit; each one matches the class in that position.
- V: eight slots are built by a named constructor (6, 11, 18, 19, 20, 37, 38, 48); the other 46 call the base agent constructor and store their vtable inline.
- V: the 54 entries are contiguous and no vtable repeats; the manager constructor starts the vector empty, and every slot's object is allocated and constructed here.
- V: the agent vector's allocator is at +8 and its begin, end and capacity at +16, +24 and +32; after the last append the dword at +176 is set to 1.
- V: agents are read back by slot. `TavernMenu_OnCommand` reads the pointer at `begin + 88`, which is slot 11 (the Unit agent), and the System struct page records `begin + 37 * 8`.
- V: the six agents with no FFTO prefix (Fade, Cursor, SoundVisualizer, NoticeDialog, Loading, Announce) are generic UI agents; the other 48 are FFTO screen agents.
- I: the role lines are the class names read as plain descriptions; where the code was read further, the entry names it (Bar, Journal, Poach, Novel, EndSlate).
- ?: the role of UIAgentFFTOBattleContinuous beyond its name, and the meaning of the manager's +176 flag.

## Referenced by

- Appears in flows: [UIAgentLifecycle](../flows/UIAgentLifecycle.md)

## Notes

This is a code table, not game content. Entries tagged I carry a role read from the class name; their vtable, constructor and size values are decoded from the allocation code. The class names are the vtables, the constructor addresses are the factories, and the size is the allocation. Every slot was read in `UIAgentManager_CreateAgents`; the eight named constructors were read separately to confirm the vtable each one stores. Agent fields are not described here.

## Open questions

? the role of UIAgentFFTOBattleContinuous beyond its name. ? whether the slot id is ever used for anything other than indexing the agent vector.
