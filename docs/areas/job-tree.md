# Job tree

The Job Tree screen: JobTree_* and JobRecord_* pages.

Functions: 45, Structures: 4, Flows: 1, Observed behaviours: 7.

## Functions (45)

| Name | Address | Purpose |
|---|---|---|
| [JobRecord_FillIconAndGenericFlag](../functions/JobRecord_FillIconAndGenericFlag.md) | `0x1400FBEB8` | Looks up the Job row, then the JobType table (id 0xC8) row, and stores an icon id (male/female) at out[0]; out[4] = 'not a generic job' flag. |
| [JobScreen_BuildAbilityTabList](../functions/JobScreen_BuildAbilityTabList.md) | `0x14028A770` | Builds the ability list of one tab for the party member the job screen has selected, then hands it to the job screen list builder. |
| [JobScreen_BuildLearnableList](../functions/JobScreen_BuildLearnableList.md) | `0x14028ACD8` | Builds the ability list a job page shows with the learned flags applied, using the unit learned-bit reader and the job tab builder. |
| [JobScreen_BuildLearnList](../functions/JobScreen_BuildLearnList.md) | `0x1402B9598` | Builds the Learn page of the job screen: the job ability list, the JP cost and the learn action for the selected party unit. |
| [JobScreen_FillUnitRows](../functions/JobScreen_FillUnitRows.md) | `0x1402B90D4` | Fills the job menu rows for the selected party unit: the static job record, the level and JP readers and the availability flags. |
| [JobScreen_RefreshLearnList](../functions/JobScreen_RefreshLearnList.md) | `0x1402B9C20` | Refreshes the Learn page list after the job screen state changes, rebuilding the ability rows from the job list without spending JP. |
| [JobTree_Create](../functions/JobTree_Create.md) | `0x140113970` | Factory that allocates a UIAddonFFTOUnitJobTree and runs JobTree_Ctor (call at 0x140113E28). |
| [JobTree_Ctor](../functions/JobTree_Ctor.md) | `0x140133368` | Constructor for UIAddonFFTOUnitJobTree (RTTI). |
| [JobTree_Dtor](../functions/JobTree_Dtor.md) | `0x140133574` | Destructor body of UIAddonFFTOUnitJobTree (called through wrapper sub_14013349C, vtable slot 0). |
| [JobTree_FillJobRecords](../functions/JobTree_FillJobRecords.md) | `0x140368424` | Walks `g_RuntimeJobList` and, per list position, builds the 148-byte job record plus the sprite record, then hands them to the job-change list (sub_14012EC5C) and the tree (JobTree_SetPanelRecord). |
| [JobTree_HandleInput](../functions/JobTree_HandleInput.md) | `0x140133FA4` | Per-frame pad input for the tree: confirm, back and 8-way cursor movement over the panel grid. |
| [JobTree_NodeStem](../functions/JobTree_NodeStem.md) | `0x140134980` | Tree index -> UIB node-name stem. |
| [JobTree_OnCursorEnter](../functions/JobTree_OnCursorEnter.md) | `0x140134594` | Cursor moved onto panel `jobIdx`: lights every arrow and label attached to it (its 6 requirement edges and its 6 dependent edges). |
| [JobTree_OnCursorLeave](../functions/JobTree_OnCursorLeave.md) | `0x1401346D4` | Cursor left panel `jobIdx`: puts its arrows and labels back to the resting (not on cursor) states. |
| [JobTree_OnEvent](../functions/JobTree_OnEvent.md) | `0x140133DDC` | UI event handler of the tree addon (vtable slot 2). |
| [JobTree_OnFocusChange](../functions/JobTree_OnFocusChange.md) | `0x140133F30` | Focus change handler (vtable slot 27): when the tree gains the input focus (id 1409) it puts the cursor back on the remembered panel; when it loses it, it tells its parent. |
| [JobTree_RefreshAddon](../functions/JobTree_RefreshAddon.md) | `0x1401335F4` | UIAddonFFTOUnitJobTree vtable slot 4. |
| [JobTree_ReleaseCharaSlots](../functions/JobTree_ReleaseCharaSlots.md) | `0x140133EB8` | Releases the unit-preview render slots used by the tree panels (CharaRender slot ids 80..98). |
| [JobTree_SetArrowState](../functions/JobTree_SetArrowState.md) | `0x1401347DC` | Sets the look of one requirement arrow: activates exactly one of the named states Lock / Unlock / LockOnCursor / UnlockOnCursor on the line node. |
| [JobTree_SetLabelState](../functions/JobTree_SetLabelState.md) | `0x1401348B0` | Sets one level-label board: activates exactly one of the named states Hide / ShowLock / ShowUnlock. |
| [JobTree_SetPanelRecord](../functions/JobTree_SetPanelRecord.md) | `0x14013420C` | Stores a job record into the tree panel slot and sets the panel's Lock/Unlock/LvNum UI states. |
| [sub_140130DF0](../functions/sub_140130DF0.md) | `0x140130DF0` | Input handler of the job-list panel for mode 2 (the main cell grid): confirm / cancel / detail buttons and cursor movement across the 19 cells. |
| [sub_140131068](../functions/sub_140131068.md) | `0x140131068` | Input handler of the job-list panel for mode 3 (the job action / confirmation list at p+5296..p+5320): confirm / cancel / list movement. |
| [sub_140131688](../functions/sub_140131688.md) | `0x140131688` | Handles the info / help button (action 0x7E = 126) in the job-list panel: shows a message popup for the cursor cell or emits an addon event. |
| [sub_140131734](../functions/sub_140131734.md) | `0x140131734` | Handles action 0x8E (142) on a cell that has the flag byte at [148 * cell + p + 8974]: shows the info popup 37 when the cell state is 2, else sets out[0] = 1410 and plays the refusal sound. |
| [sub_1401319FC](../functions/sub_1401319FC.md) | `0x1401319FC` | Plays the Show / Hide animation of the sub-widget at p+4912 (the tab strip at p+4896) and, when showing, initialises its cursor. |
| [sub_140132B34](../functions/sub_140132B34.md) | `0x140132B34` | Copies the current cell's data into a 124-byte preview record and calls sub_1402A7474 (update the detail view for that cell). |
| [sub_140132CF4](../functions/sub_140132CF4.md) | `0x140132CF4` | Posts command 123 to the addon's owner with argument 1024 or 1025 depending on sub_1400FCE48 (busy gate). |
| [sub_140132D6C](../functions/sub_140132D6C.md) | `0x140132D6C` | Refreshes the sprite palette state of all 19 cells after the cursor / mode changed. |
| [sub_140132DC8](../functions/sub_140132DC8.md) | `0x140132DC8` | Clears the 'tinted' flag of a cell's chara sprite: restores palette bits and re-requests the render slot. |
| [sub_140132E1C](../functions/sub_140132E1C.md) | `0x140132E1C` | Applies the 'unavailable / dimmed' palette to a cell's chara sprite (palette bit group 6) when the cell is the cursor cell with state 0 or sub_140132D48 says so, and marks the cell tinted. |
| [sub_1401332A0](../functions/sub_1401332A0.md) | `0x1401332A0` | Sets the visibility byte (+144) of the first kind-13 part of every one of the 19 cell nodes and of one extra node. |
| [sub_140133DB8](../functions/sub_140133DB8.md) | `0x140133DB8` | UnitJobTree addon vtable slot 7: posts command 126 to the addon owner. |
| [sub_14028A474](../functions/sub_14028A474.md) | `0x14028A474` | Builds a list of the first 24 ability slots of a party unit's job, tagging each id with display bits, in 9 modes selected by a6. |
| [sub_1402A20A4](../functions/sub_1402A20A4.md) | `0x1402A20A4` | Sets the description text of the job command detail window: the second description once its condition holds. |
| [sub_140366ABC](../functions/sub_140366ABC.md) | `0x140366ABC` | Job screen routine that fills the help panel and the ability list for the selected job, then handles the page input. |
| [sub_140367AA0](../functions/sub_140367AA0.md) | `0x140367AA0` | Builds the job screen's ability page from one 4-byte ability menu entry: it maps the job, prices the ability, lays out the tab rows and passes the ability id to the page builder. |
| [sub_140392620](../functions/sub_140392620.md) | `0x140392620` | Builds the ability-token list for a job in a job-tree screen, restricted to an id window chosen by a3, tagging each id. |
| [sub_140392800](../functions/sub_140392800.md) | `0x140392800` | Job screen reader: it returns the JP the party has in one job and copies the job id into the screen state. |
| [sub_14039284C](../functions/sub_14039284C.md) | `0x14039284C` | Job screen reader: it stores a second value of the same job state block, next to sub_140392800. |
| [sub_140392884](../functions/sub_140392884.md) | `0x140392884` | Job screen reader: it writes the third word of the job state block after mapping the job id. |
| [sub_1403928D4](../functions/sub_1403928D4.md) | `0x1403928D4` | Job screen reader: it converts the party's JP into a job level through Job_GetJpForLevel and stores it. |
| [sub_14039297C](../functions/sub_14039297C.md) | `0x14039297C` | Job screen task: it runs the job page's input loop and calls the four job-state readers to refresh the page. |
| [UIGadgetFFTOJobDetailWindow_SetJob](../functions/UIGadgetFFTOJobDetailWindow_SetJob.md) | `0x1402A7474` | Fills the job detail window for one job record: the name / level texts, the job icon, the Show / Hide / ShowNext states and the up to four innate ability slots (Sp0..Sp3, with Good / Bad colouring: Bad for an ability ... |
| [UIGadgetFFTOJobDetailWindowWithButton_SetJobArgs](../functions/UIGadgetFFTOJobDetailWindowWithButton_SetJobArgs.md) | `0x1402A7C38` | Slot 8 of the 'with button' job detail window (called from UIGadgetFFTOJobDetailWindow_SetJob through virtual +64): resets the text argument list at w+1168, pushes the job id and a flag, refreshes the text and refits ... |

## Structures (4)

| Name | Size (bytes) | Summary |
|---|---|---|
| [JobRecord](../structs/JobRecord.md) | 148 | Only the listed offsets are verified; the rest of the 148 bytes is copied wholesale. |
| [JobTreeAddon](../structs/JobTreeAddon.md) | 13312 | STOCK layout (20 panels). |
| [JobTreeNavRecord](../structs/JobTreeNavRecord.md) | 32 | The 32-byte cursor neighbour record inside a Job Tree panel record (panel +0x1A8): for each of the eight pad directions two candidate neighbour panels, each with a flag byte. |
| [JobTreePanel](../structs/JobTreePanel.md) | 456 | Stride 456 bytes (stock: 20 panels). |

## Flows (1)

| Name | Summary |
|---|---|
| [JobScreenFrame](../flows/JobScreenFrame.md) | How the Job Tree gets input and a chance to run code each frame: the party-menu scene's frame function runs the current screen's update through a function table, the job screen's update runs the screen dispatch, and t... |

## Observed behaviours (7)

| Name | Scope | Summary |
|---|---|---|
| [JobAndAbilityDisplayFlagColumns](../behaviors/JobAndAbilityDisplayFlagColumns.md) | engine (job and ability windows) | Small flag columns of the Job, Ability and JobCommand tables that only change how a window draws. |
| [JobTreeCursorNeighbourTable](../behaviors/JobTreeCursorNeighbourTable.md) | engine (Job Tree) | The Job Tree pad cursor does not search the screen for the nearest panel: each job row of the GeneralJob table names, for each of eight pad directions, up to two panels to move to. |
| [JobTreeHoverFade](../behaviors/JobTreeHoverFade.md) | the focused Job Tree panel while its UnitJob CursorOver state plays | Focusing a panel plays the UnitJob component's CursorOver state at 60 Hz: the ring (UnitSelect) opacity 0 -> 1, the sprite (Unit) scale 1.125 -> 1.2 and the name tag fade in over frames 0 - 6 with the curves of the UI... |
| [JobTreeLockState](../behaviors/JobTreeLockState.md) | every Job Tree panel, for the viewed unit | A panel is in one of three states: Unlock (the viewed unit has the job), LockReleased (it does not, but another party member does: shaded) or LockUnreleased (nobody in the party has it: black silhouette). |
| [JobTreePanelLookups](../behaviors/JobTreePanelLookups.md) | the per-panel lookups, the pad step and the scrolling root of the Job Tree | The tree is built for panel numbers 0..19. |
| [JobTreePanelSprite](../behaviors/JobTreePanelSprite.md) | the unit sprite of every Job Tree panel | Each panel shows the viewed unit as that job: the generic sheet of the unit's gender for the 20 tree jobs, the unit's own sprite for its own special job (Ramza's Squire panel). |
| [JobTreeViewControl](../behaviors/JobTreeViewControl.md) | what a smooth stick scroll and a zoom of the Job Tree can use | The tree root is one node; its position (scroll) and scale are plain integer / float fields whose change reaches every panel, arrow, label and the finger cursor's target in the same UI pass. |
