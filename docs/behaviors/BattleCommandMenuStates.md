# BattleCommandMenuStates

- **Kind:** observed behaviour
- **Scope:** battle, own turn: command menu, Abilities list, Move tile selection, target selection, facing prompt
- **Area:** [UI framework](../areas/ui-framework.md)
- **Affects:** [GUICore_GetFocus](../functions/GUICore_GetFocus.md), [GUICore_FindWidgetByKey](../functions/GUICore_FindWidgetByKey.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

How to tell the screens of an own battle turn apart and which row the command menu cursor is on, from game state only: the glove position, the focused widget and the text of the instruction-message widget.

## Behavior

- V (live, 2026-11-05): the main command menu is up while the radio-menu entry count at UIAddonFFTOBattleCommand +856 is above 0 (5 entries: Move, Abilities, Wait, Status, Auto-Battle); the count stays 5 while the Abilities list is open and is 0 on tile, target and facing screens.
- V (live): the finger cursor (glove, node CursorRef) sits at x 1158 for the main column with y 760, 814, 871, 928, 983 for rows 0 to 4 (about 55.8 apart, +-2 from the bob); in the Abilities list it sits at x 1278 with y 759 for the first entry (Attack), 814 for the next.
- V (live): the selected (+1120) and hover (+1124) row fields read -1 until the cursor first moves, and read -1 again after returning from any sub-screen, while the glove stays on the row the sub-screen was opened from. They are therefore not a reliable row; the glove y is.
- V (live): the cursor is remembered across cancels: B from the facing prompt returns to row 2 (Wait), B from tile selection returns to row 0, B from the Abilities list returns to row 1, B from target selection returns to the Abilities list on its first entry.
- V (live): the Abilities list is drawn inside the command widget (ffto_battle_command.uib stays the focused widget, glove x 1278); Attack opens target selection; the job command (Martial Arts for a Monk with nothing learnt) did nothing on A.
- V (live): tile selection, target selection and the facing prompt have no focused widget (empty focus), no glove, the same set of visible screens and the same agents; they differ only by the text of the Title node under TextBoardInstructionMessage in ffto_battle_menu_instruction_message_02.uib, which is drawn (draw gate set) only while a prompt is up: 'Select a tile and press [A] to move.', 'Select a target and press [A] to confirm.', 'Select a facing direction and press [A] to confirm.' ([A] stands for button-glyph characters in the private-use area).
- V (live): the node's text stays set after the prompt is gone; only the draw gate (node +204 != 0 and +145 == 0) says it is shown.
- V (live): A on Wait opens the facing prompt; A there ends the turn and writes the battle autosave; B returns to the menu. A on Status (row 3) opens ffto_status_ver03.uib and B returns to the menu with the glove on row 3.
- V (live, 2026-11-05): the battle map is 13 x 13 here (bytes at 0x140C6AD6A / 0x140C6AD6B); the 8-byte tile records at 0x140D8DCB0 are row-major (index = y * 13 + x), flag byte +5. In Move tile selection bit 0x20 marks the lit tiles the unit can stop on (3 tiles for a boxed-in Chemist, matching the screen) and bit 0x40 marked the three allies it could pass; units cannot pass enemies. A on an unlit tile shows ffto_common_error.uib with 'Select a tile within movement range.' and changes nothing. A on a lit tile moves the unit (+79/+80 of its unit record change), returns to the command menu with the cursor on Abilities.
- V (live): the cursor starts on the unit's own tile and moves one tile per pad direction press, relative to the camera. RB / LB rotate the camera by quarter turns, so UP / RIGHT are not fixed compass directions (seen: RIGHT = +x with UP = +y, then RIGHT = +y with UP = -x after RB). The tile table gives each tile's height (record byte +2, byte +3 = half step) and the HUD node TextHeight shows the height of the tile under the cursor, so one press plus the table tells the current mapping.
- I: the cursor's own tile and the camera rotation were not found in memory (not in the tile table; the camera manager at 0x143CDA758 and 512 KB of globals from 0x143C80000 showed no change under RB). The debugger does not need them: it measures the mapping from the heights.
- V (live, 2026-11-05): an attack is four steps: Abilities, Attack, target tile, then a preview screen (no prompt line; footer Cancel / Confirm / Move Viewpoint) where A executes it and B returns to target selection with the cursor still on the chosen tile. A on a target out of range shows an error and stays. While the target prompt is up the tile table at 0x140D8DCB0 still holds the last Move range, so the attack range lives elsewhere (not found). The menu returns about 3 s after Confirm; the target can counter.
- V (live): the battle can show modal tutorial / message pages (a KO turning into a chest; Next then Done) that hold the turn until A is pressed per page, and the Game Over screen (ffto_battle_gameover_02.uib) whose entries Retry, Load, Return to World Map, Return to Title Screen appear after a first pad press shows the glove.
- V (owner, 2026-11-05): in target selection the game marks tiles yellow (in range and targetable, empty or occupied), white (outside the x/y range) and red with a slash (inside the x/y range but out of vertical reach); a normal sword attack reaches the four tiles around the unit. The tile table at 0x140D8DCB0 keeps the Move range while targeting; the marks are in the range-mark array (next record).
- V (live, 2026-11-05): the yellow (targetable) tiles are the records whose byte 0 is non-zero in the range-mark array at 0x1418004E0 (512 records of 5 bytes, index = x + y * width + layer * 256, layer = the acting unit's z bit, unit +81 >> 7), written by BattleRange_MarkRing (via sub_14027F974 for ability ranges, sub_14027F5B4 / sub_14027FD2C / sub_14027F270 for the other command kinds). Brice at (6,1) with a sword: byte 0 set at (6,0), (5,1), (6,2), clear at (7,1) (too high), matching the screen.

## Notes

The debugger reads the prompt by a scoped text scan (0.45 s once, then the single node by address). The game's own state variable that selects the prompt was not looked for; this is an observation, not the engine's rule.

## Open questions

? The engine field behind the prompt (a UI state or the battle action mode). ? Meaning of range-mark bytes 1 to 4 and of values above 1 in byte 0. ? Whether Move shows a different prompt when the unit has no reachable tile. ? Where the cursor tile and the camera rotation live. ? The job command's ability list for a unit that has learnt abilities.
