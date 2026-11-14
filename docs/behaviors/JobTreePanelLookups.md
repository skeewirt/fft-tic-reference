# JobTreePanelLookups

- **Kind:** observed behaviour
- **Scope:** the per-panel lookups, the pad step and the scrolling root of the Job Tree
- **Area:** [Job tree](../areas/job-tree.md)
- **Affects:** [JobTree_RefreshAddon](../functions/JobTree_RefreshAddon.md), [JobTree_NodeStem](../functions/JobTree_NodeStem.md), [JobTree_SetPanelRecord](../functions/JobTree_SetPanelRecord.md), [JobTree_FillJobRecords](../functions/JobTree_FillJobRecords.md), [JobTree_HandleInput](../functions/JobTree_HandleInput.md), [JobList_SelectEntry](../functions/JobList_SelectEntry.md), [UITable_GetRowByKey](../functions/UITable_GetRowByKey.md), [GUICore_FocusNode](../functions/GUICore_FocusNode.md), [Input_TestAction](../functions/Input_TestAction.md), [GUINode_SetPosition](../functions/GUINode_SetPosition.md), [JobTree_OnCursorEnter](../functions/JobTree_OnCursorEnter.md), [JobTree_OnFocusChange](../functions/JobTree_OnFocusChange.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The tree is built for panel numbers 0..19. Four per-panel lookups drive it: the node stem (JobTree_NodeStem), the GeneralJob row (requirement and pad-navigation neighbours), the record slot (JobTree_SetPanelRecord) and the click target (JobList_SelectEntry). The pad step moves the focus by the GeneralJob neighbour rows; the whole tree is one root node.

## Behavior

- V: the stem of panel p comes from JobTree_NodeStem at four call sites of JobTree_RefreshAddon (the panel loop and the three arrow-name builds); it answers the empty string for p >= 20, and the function writes only rax and edx while its callers keep rcx / ecx across it (the level of an arrow name is read back from ecx after the call).
- V: the requirement of panel p is the GeneralJob row with KEY p (one UITable_GetRowByKey(0xBD, p) call in JobTree_RefreshAddon). The same row supplies the 14 pad-navigation neighbours (unknown30..64), where 20 means none.
- V: JobTree_SetPanelRecord(tree, rec, pos) stores the record in panel pos (+1 for jobs 92 / 93) when pos is within the addon's panel count; the fill loop passes the LIST POSITION.
- V: a click on panel p sends the list entry p - 1 (p >= 18) as screen message 128 to JobList_SelectEntry.
- V: the position code of a requirement row is the EXIT side of the arrow from the required panel (1 left, 2 right, 3 bottom, 4 top; V against the 19 stock rows, where code 3 pairs with an arrow entering the target from above).
- V: the 21-entry table of 512-byte entries in JobTree_FillJobRecords (loop bound 21) is g_PreviewUnitTable, indexed by a party unit's save index, not by panel.
- V: a required panel has room for 6 dependents (record +0x118): a seventh dependent on one required job gets its arrow drawn but no lit state.
- V (executable bytes at the 17 one-byte count and cap sites of the tree, 2026-11-08): every one is a compare with a sign-extended 8-bit immediate, so the tree holds at most 127 panels; a byte of 0x80 and above would compare as a negative number (the signed panel loops would stop after one pass, the unsigned caps would bound nothing).
- V: a requirement id in a GeneralJob row read by the tree is a tree index (the requirement source and requirement.jobIndex compares are capped at the panel count - 1).
- V (layout file): the floor behind the panels is the BG reference of the JobTree component (base fill Rect03 2100 x 1100, the tiled stone image BGStone/Image01, the edge fades Rect00 / Rect01, all with pivot mode 0); it is part of the tree root, so it scrolls with the panels.
- V: the pad direction is read by JobTree_HandleInput as the four bytes at qword_143CD9EE8 + 13648 (down, left, up, right), else the four at + 13652 in the same order; up wins over down, right over left; the game numbers the eight directions clockwise from RIGHT (live 2026-11-08: pad right reads 0, down 2, left 4, up 6), -1 none.
- V: the game's own tests run before the step, in this order: Input_TestAction(0, 0, 26) or the held flag (confirm), then Input_TestAction(0, 0, 27) (cancel). With selector 0 Input_TestAction only reads a table, so asking it twice in a frame changes nothing.
- V: the stock step starts at the panel under the cursor (addon field 12232) when it is a panel, else at the remembered panel (12236) when it is below the panel count, and skips the Bard / Dancer panel the gender flag hides.
- V: the target is focused with GUICore_FocusNode(addon + 72 + 456 x panel); the focus arrives as event 19 and lights the panel's arrows through JobTree_OnCursorEnter.
- V (live, 2026-11-08): the ffto_job_tree.uib widget is one root node (1920 x 1080, no parent, at (0, 0)); GUINode_SetPosition on it moved the whole tree and back exactly; the footer (another widget) stayed.
- I: the root is found from a panel node by following the parent pointer (+0x18) to the node with no parent; a panel's place in root coordinates is the sum of the local positions (+56 / +60) below the root.
- V: JobTree_OnFocusChange with focus 1409 (the tree gains the input focus: the screen opens, or the player comes back from the job list) refocuses the remembered panel.

## Open questions

None recorded.
