# DeploymentPortraitColumnBoxes

- **Kind:** observed behaviour
- **Scope:** engine (battle deployment UI)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [SortieScreen_BindBoxes](../functions/SortieScreen_BindBoxes.md), [SortieScreen_SetArea0Face](../functions/SortieScreen_SetArea0Face.md), [SortieScreen_SetArea1Face](../functions/SortieScreen_SetArea1Face.md), [SortieScreen_ShowAreaBoxes](../functions/SortieScreen_ShowAreaBoxes.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The deployment screen's portrait column is a fixed set of named layout boxes, 5 for the first area and 4 for the second, bound by name and filled in placing order.

## Behavior

- V: ffto_battle_sortie_ver02.uib, component Team: layer LayerTeam01 (origin 0, -40) holds References T01_1..T01_5 at y 0, 100, 200, 300, 400; LayerTeam02 (origin 0, 550) holds T02_1..T02_4 at y 0..300. Each is a Reference to the Unit component (its layer holds IconLock, UnitFrame, Unit and UnitGlow).
- V: SortieScreen_BindBoxes binds the boxes by the name `T%02d_%d` (area, position) into the screen object (UIAddonFFTOBattleSortie2): area 1 from +0x310, area 2 from +0x328, 0x30 per box (node, Eye, Mouth).
- V: sub_1401F3858 walks the placed entries and gives each placed unit the next box of its area (SortieScreen_SetArea0Face / SortieScreen_SetArea1Face with its face), then hides the rest of each area's boxes (positions up to 4 / 3) with face -1. A unit placed past the boxes gets no face (the setters return for a position above 4 / 3).
- V: how many boxes show is a Team state per count: SortieScreen_ShowAreaBoxes plays 'Team01_<n>' (n 1..5) and 'Team02_<n>' (n 1..4), each switching the box parts' visibility; a face of -1 only hides the face, the empty frame stays (seen live: before any placement the allowed boxes show as empty frames).
- V (seen live, tested limit): the box pointers SortieScreen_BindBoxes stores come from GUINode_FindDescendant, which returns the referenced component; the visibility a state animates is the enabled byte (+144) of the Reference part in the screen's own tree (GUINode_FindPartByName(component + 272, name)). Writing +144 of a box's Reference part in memory hid and showed that box; a layout part that no state names stays as written.
- V (layout file, Team component): Team01_n moves LayerTeam02 to (0, 50 + 100 n) and shows T01_1..T01_n, so the second area's column starts right below the first area's last row; Team02_n shows T02_1..T02_n without moving anything; ShowTeam02 / HideTeam02 show or hide LayerTeam02.
- M (seen live 2026-11-22, Sand Rat's Sietch with 4 + 3): the screen has room for about 5 rows of boxes in all: with 4 rows in the first area, the second area's second row met the footer and its third lay below the screen; no position track names a box, so a box's place (GUINode +0x38 / +0x3C) can be set without a state undoing it.

## Open questions

None recorded.
