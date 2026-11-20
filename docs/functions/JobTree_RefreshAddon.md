# JobTree_RefreshAddon

- **Address:** `0x1401335F4`
- **Area:** [Job tree](../areas/job-tree.md)
- **Prototype:** `int64_t JobTree_RefreshAddon(JobTreeAddon *addon)`
- **Callers:** addon vtable
- **Callees:** JobTree_NodeStem, GUINode_FindDescendant, sub_140409134, sub_1403DBC74, Str_Format, UIName_Key

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

UIAddonFFTOUnitJobTree vtable slot 4. Builds the tree: finds the 'JobTree' root, looks up one panel node per job BY NAME, finds each node's 'Unit' gadget and text children, and wires Line* connector nodes.

## Behavior

- V: runs at BOOT (title screen), not when the tree opens (exec breakpoint fires about 5 s after launch).
- V: stock panel loop bound is 20 (the immediate at 0x140133944).
- V: node name = sub_140134980(table, i): job index -> stem ('Squire'..'Mime'); the index past the stock 20 falls to the default Str1.
- V: stores node at addon+72+456*i, Unit gadget at +8, name gadget at +16, title at +24.
- V: requirement lines come from GeneralJob rows (nxd table 189): node names 'Line%sLv%02d' / 'Line%s%s'; missing line nodes are null-checked.
- V: the name format is chosen by the requirement's position code, not by which node exists: code 5 or 6 -> 'Line<required>Lv<level>' (one node shared by every requirement on that job at that level: the stock Squire / Chemist two-branch arrows), any other code -> 'Line<required><job>'. Codes 3, 5 and 6 all select the B label board.
- V: second loop (jobs 0..n-1): for each job reads its GeneralJob row; per requirement j < min(6, count): required job, level and position code. Stores the arrow node at panel record +0x88+24*j (line), the label board at +0x90, required job at +0x98, level at +0x9C.
- V: position code -> board name: 1 -> TextBoardJobLvL, 2 -> R, 3/5/6 -> B, 4 -> T. The board is looked up BY NAME on the REQUIRED job's panel node, so every requirement pointing at the same side of the same panel resolves to the same board (the last text written wins).
- V: the board's 'LvMaster'/'LvNum' states are started and its 'Title' text receives the level number: the requirement's level, the i16 at row + [row+0x18] + j*2 (rdi = the GeneralJob row, r12 = j; 0x140133C5B).
- V: sharing one board is how the stock tree labels arrows that leave one side at one level: Squire's B board shows one 'Lv. 2' for both Chemist and Knight; seen live 2026-11-12 (three Lv. 2 arrows under Squire, one label).
- V (stock uib, offline): the boards are References to the 40 x 20 component TextBoardJobLv at scale 1.2, pivot = centre, in UnitJob's LayerRoot (origin (0, 8)): centres relative to the panel node L (-54, 90), R (116, 90), T (32, -38), B (32, 136), the disc centre being (31, 88). Every one of the 30 stock arrows leaves its side on the centre lane (L / R at y 87..90, B at x 26..36), so each board sits on its side's centre lane just outside the panel box.
- V: the same pass records the reverse edge in the required job's dependents table (record +0x118, 6 entries x {line, board, child job, level}); more than 6 dependents are dropped.
- V: the loop tail copies the job's 8-direction navigation pairs (cursor grid) from the GeneralJob row into the panel record at +0x1A8: per direction, candidate 0 takes the low byte of the dword at row +0x28 + 4 * direction and the flag byte at row +0x68 + direction, candidate 1 the low byte of the dword at row +0x48 + 4 * direction and the flag byte at row +0x70 + direction (columns cursor_<direction>, cursor_<direction>_2, cursor_<direction>_primary_only, cursor_<direction>_2_primary_only); record byte 4 * direction + 2 * candidate = panel index (0..19, 20 = none), the next byte = the flag. See behavior JobTreeCursorNeighbourTable.

## State touched

- Calls: [JobTree_NodeStem](JobTree_NodeStem.md), [GUINode_FindDescendant](GUINode_FindDescendant.md), [Str_Format](Str_Format.md), [UIName_Key](UIName_Key.md)
- Reads: [g_UINameTable](../globals/g_UINameTable.md)

## Referenced by

- Observed behaviours: [JobTreeCursorNeighbourTable](../behaviors/JobTreeCursorNeighbourTable.md), [JobTreePanelCountLimits](../behaviors/JobTreePanelCountLimits.md), [JobTreePanelLookups](../behaviors/JobTreePanelLookups.md)

## Notes

The panel record offsets (+0x88, +0x90, +0x98, +0x9C, +0x118, +0x1A8) are reached through a running pointer into the 456-byte record, so they appear only as sums in the body. Panel stride is 456 bytes; the addon is 0x2FD8 bytes in stock (allocated in JobTree_Create). Limits in this function: 6 requirements per job, 6 dependents per job, 4 label boards per panel (one per side).

## Open questions

Requirement arrows are authored nodes: a job with no Line* node draws no arrow.
