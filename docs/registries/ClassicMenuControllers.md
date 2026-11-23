# ClassicMenuControllers

- **Kind:** registry
- **Area:** [UI framework](../areas/ui-framework.md)
- **Resolved by:** [ClassicMenu_RunScreenStack](../functions/ClassicMenu_RunScreenStack.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The per-screen controllers of the classic menu system: one contiguous array of input steps at 0x140681400, 55 filled slots (0 to 45 and 48 to 56; 46, 47 and 57 are null), with a further entry at index 58. The dispatcher calls the entry of the kind on top of the controller stack with that level's 92-byte record and does not bound-check the kind.

## Entries

| Id | Name | Value | Conf | Meaning |
|---|---|---|---|---|
| <a id="worldmap_screeninput"></a>0 | `WorldMap_ScreenInput` | `table index 0` | V | The world map: moves between locations, opens the town menu, rolls encounters. |
| <a id="classicmenu_hubstep"></a>1 | `ClassicMenu_HubStep` | `table index 1` | V | The controller under the other screens: after one closes, picks the next from flag bits of the state dword. |
| <a id="pagedtext_waitandclose"></a>2 | `PagedText_WaitAndClose` | `table index 2` | V | Runs the paged text widget until it ends, then closes. |
| <a id="helpmessage_wait"></a>3 | `HelpMessage_Wait` | `table index 3` | V | The help message screen: waits for the message window, then closes (opened by HelpMessage_Open). |
| <a id="sub_1403456d4"></a>4 | `sub_1403456D4` | `table index 4` | ? | A step documented as the scripted message window task. |
| <a id="tavern_topinput"></a>5 | `Tavern_TopInput` | `table index 5` | V | The tavern top screen. |
| <a id="tavern_rumorslistinput"></a>6 | `Tavern_RumorsListInput` | `table index 6` | I | The tavern rumor list. |
| <a id="errand_boardinput"></a>7 | `Errand_BoardInput` | `table index 7` | V | The tavern errand board. |
| <a id="tavern_rumortextwait"></a>8 | `Tavern_RumorTextWait` | `table index 8` | V | The rumor text page; rebuilds the rumor list at its end. |
| <a id="errand_boardconfirminput"></a>9 | `Errand_BoardConfirmInput` | `table index 9` | I | A confirm window of the errand screens; opens kind 10. |
| <a id="errand_confirmdialoginput"></a>10 | `Errand_ConfirmDialogInput` | `table index 10` | I | A confirm dialog pushed by index 9. |
| <a id="eventvareditor_listinput"></a>11 | `EventVarEditor_ListInput` | `table index 11` | V | The event variable editor list (ten variables a page). |
| <a id="errand_pickinput"></a>12 | `Errand_PickInput` | `table index 12` | I | An errand choice window; leads to the board painter. |
| <a id="errand_startconfirminput"></a>13 | `Errand_StartConfirmInput` | `table index 13` | V | The two-row confirm that calls Errand_Start. |
| <a id="errand_reportlistinput"></a>14 | `Errand_ReportListInput` | `table index 14` | I | The list of errands with a report ready. |
| <a id="uipage_choicepromptinput"></a>15 | `UiPage_ChoicePromptInput` | `table index 15` | I | A two-row prompt pushed by index 14. |
| <a id="errand_reportdialoguestep"></a>16 | `Errand_ReportDialogueStep` | `table index 16` | I | The errand report dialogue. |
| <a id="menuctl_entry17"></a>17 | `MenuCtl_Entry17` | `table index 17` | V | A jump to sub_140370D58. |
| <a id="errand_runninglistinput"></a>18 | `Errand_RunningListInput` | `table index 18` | I | The list of running errands. |
| <a id="errand_runningconfirminput"></a>19 | `Errand_RunningConfirmInput` | `table index 19` | I | The two-row confirm that marks a running errand. |
| <a id="bookprogress_resetconfirminput"></a>20 | `BookProgress_ResetConfirmInput` | `table index 20` | I | A question about a book's progress record. |
| <a id="sub_140372f9c"></a>21 | `sub_140372F9C` | `table index 21` | ? | An event script pass step. |
| <a id="menuctl_entry22"></a>22 | `MenuCtl_Entry22` | `table index 22` | ? | A two-row question with a fade; ends by opening kind 27. |
| <a id="sub_140373de8"></a>23 | `sub_140373DE8` | `table index 23` | ? | A text builder. |
| <a id="menuctl_entry24"></a>24 | `MenuCtl_Entry24` | `table index 24` | I | A list whose entries open kind 25. |
| <a id="menuctl_entry25"></a>25 | `MenuCtl_Entry25` | `table index 25` | I | The detail page with a picture of kind 24's entries. |
| <a id="menuctl_entry26"></a>26 | `MenuCtl_Entry26` | `table index 26` | I | A list whose entries open kind 27. |
| <a id="menuctl_entry27"></a>27 | `MenuCtl_Entry27` | `table index 27` | I | The detail page of kind 26's entries, with a picture dissolve and a book progress word. |
| <a id="menuctl_entry28"></a>28 | `MenuCtl_Entry28` | `table index 28` | I | A row menu that opens the event list, the tavern lists and three other lists. |
| <a id="eventviewer_listinput"></a>29 | `EventViewer_ListInput` | `table index 29` | V | The story event list. |
| <a id="eventviewer_entrypage"></a>30 | `EventViewer_EntryPage` | `table index 30` | V | The page of one story event. |
| <a id="sub_140375cd0"></a>31 | `sub_140375CD0` | `table index 31` | I | The second tavern list. |
| <a id="sub_140376040"></a>32 | `sub_140376040` | `table index 32` | I | The page of one entry of the second tavern list. |
| <a id="menuctl_entry33"></a>33 | `MenuCtl_Entry33` | `table index 33` | I | A list whose entries open kind 34. |
| <a id="menuctl_entry34"></a>34 | `MenuCtl_Entry34` | `table index 34` | I | The text page of kind 33's entries. |
| <a id="classicmenu_screenwipestep"></a>35 | `ClassicMenu_ScreenWipeStep` | `table index 35` | I | A frame-counted fade and slide of the picture layers. |
| <a id="errandunitpick_input"></a>36 | `ErrandUnitPick_Input` | `table index 36` | V | The unit picker of the errand board; starts the errand. |
| <a id="errand_statusmenuinput"></a>37 | `Errand_StatusMenuInput` | `table index 37` | I | A two-row menu that opens lists 38 and 41. |
| <a id="errand_progresslistinput"></a>38 | `Errand_ProgressListInput` | `table index 38` | I | A list whose entries open kind 39. |
| <a id="errand_unitlistinput"></a>39 | `Errand_UnitListInput` | `table index 39` | I | A list whose entries open kind 40. |
| <a id="errand_unitstatusinput"></a>40 | `Errand_UnitStatusInput` | `table index 40` | V | A unit's status page for a running errand. |
| <a id="errand_finishlistinput"></a>41 | `Errand_FinishListInput` | `table index 41` | I | A list whose entries open kind 42. |
| <a id="errand_finishdaypage"></a>42 | `Errand_FinishDayPage` | `table index 42` | I | The page of kind 41's entries, with the errand finish day. |
| <a id="menuctl_entry43"></a>43 | `MenuCtl_Entry43` | `table index 43` | I | A row menu opening lists 44, 45 and 33. |
| <a id="menuctl_entry44"></a>44 | `MenuCtl_Entry44` | `table index 44` | I | A list of 7 flagged entries. |
| <a id="menuctl_entry45"></a>45 | `MenuCtl_Entry45` | `table index 45` | I | A list of 8 flagged entries that starts an event. |
| <a id="eventvareditor_valueinput"></a>48 | `EventVarEditor_ValueInput` | `table index 48` | V | The number entry of the event variable editor. |
| <a id="screenreopen_step"></a>49 | `ScreenReopen_Step` | `table index 49` | V | Waits a few frames, then re-opens the screen of the kind in its first dword. |
| <a id="menuctl_entry50"></a>50 | `MenuCtl_Entry50` | `table index 50` | ? | A short step that closes itself once its window is done. |
| <a id="menuctl_entry51"></a>51 | `MenuCtl_Entry51` | `table index 51` | I | A paged text screen under a window with a pending close. |
| <a id="menuctl_entry52"></a>52 | `MenuCtl_Entry52` | `table index 52` | I | A yes or no step that applies a held number. |
| <a id="menuctl_entry53"></a>53 | `MenuCtl_Entry53` | `table index 53` | ? | Walks a chain of pages forward or back. |
| <a id="menuctl_entry54"></a>54 | `MenuCtl_Entry54` | `table index 54` | ? | A one-shot window controller. |
| <a id="errand_profitendstep"></a>55 | `Errand_ProfitEndStep` | `table index 55` | V | The errand end sequence with the profit notification. |
| <a id="statusglossary_input"></a>56 | `StatusGlossary_Input` | `table index 56` | I | A page of rows linked by direction, each with a help text. |
| <a id="sub_140376ca8"></a>58 | `sub_140376CA8` | `table index 58` | I | Takes a 92-byte record and pushes kind 33; the re-open tables have an index 58. Probably a controller that nothing pushes by an immediate. |

## Open questions

None recorded.
