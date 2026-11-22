# DeploymentPortraitColumnBoxes

- **Kind:** observed behaviour
- **Scope:** engine (battle deployment UI)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [SortieScreen_BindBoxes](../functions/SortieScreen_BindBoxes.md), [SortieScreen_SetArea0Face](../functions/SortieScreen_SetArea0Face.md), [SortieScreen_SetArea1Face](../functions/SortieScreen_SetArea1Face.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The deployment screen's portrait column is a fixed set of named layout boxes, 5 for the first area and 4 for the second, bound by name and filled in placing order.

## Behavior

- V: ffto_battle_sortie_ver02.uib, component Team: layer LayerTeam01 (origin 0, -40) holds References T01_1..T01_5 at y 0, 100, 200, 300, 400; LayerTeam02 (origin 0, 550) holds T02_1..T02_4 at y 0..300. Each is a Reference to the Unit component (its layer holds IconLock, UnitFrame, Unit and UnitGlow).
- V: SortieScreen_BindBoxes binds the boxes by the name `T%02d_%d` (area, position) into the screen object (UIAddonFFTOBattleSortie2): area 1 from +0x310, area 2 from +0x328, 0x30 per box (node, Eye, Mouth).
- V: sub_1401F3858 walks the placed entries and gives each placed unit the next box of its area (SortieScreen_SetArea0Face / SortieScreen_SetArea1Face with its face), then hides the rest of each area's boxes (positions up to 4 / 3) with face -1. A unit placed past the boxes gets no face (the setters return for a position above 4 / 3).

## Open questions

None recorded.
