# WorldMapLocationsAndBattleEntry

- **Kind:** observed behaviour
- **Scope:** world map free roam, Locations list, travel to a battleground, battle deployment
- **Area:** [UI framework](../areas/ui-framework.md)
- **Affects:** [GUICore_GetFocus](../functions/GUICore_GetFocus.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

How a battle is entered from the world map, and which screens and memory fields show it, as seen live.

## Behavior

- V (live, 2026-11-05): the free-roam world map has no focused widget (focus empty, glove at the screen centre) and shows the footer 'Main Menu | Locations | Zoom Out | Move Cursor | Center on Ramza' plus the current objective text on worldmap_top_layer.uib ('Head to Dorter and find information on the Corpse Brigade's movements.'). A does nothing there unless the cursor is on a settlement.
- V (live): X opens the Locations list (worldmap_base_info.uib): tabs Settlements (Merchant City of Dorter, Magick City of Gariland, Eagrose Castle), Battlegrounds (The Siedge Weald, Mandalia Plain) and Miscellaneous; RB switches the tab. A on an entry closes the list and puts the map cursor on that location (focus worldmap_map_all.uib shows its name); a second A starts the walk there with no focus and no text.
- V (live): arriving at The Siedge Weald loaded the battle deployment screen (ffto_battle_sortie_ver02.uib, visible only then): footer 'Zoom | Select Tile | Previous Unit | Commence Battle', text 'Remaining: 3', 'Battle Members', 'Press [] to place a unit on this tile'. START opens 'Commence battle? Yes / No' (glove at about 959,923); A on Yes starts the battle.
- V (live): after Yes, while enemy and guest units took their turns, the memory state read as if nothing had started: focus still ffto_battle_sortie_ver02.uib, scene kind 'in-engine cutscene, event 31' with skip allowed 0, turn slot 0xFFFFFFFF, no text drawn; pad A / B / X / START, Esc, Enter, Space and hold Y / hold Space changed nothing, and window screenshots showed the battle running (a unit's movement range in red, a different unit each frame). When Ramza's turn came the fields caught up (focus ffto_battle_command.uib, turn slot 16, player_turn, menu row 0, the command menu drawn) with event 31 and the sortie screen still listed. The sortie screen stays loaded for the whole battle.
- V (live): the footer (ffto_footer_02.uib) tells the two phases apart: 'Zoom | Select Tile | Previous Unit | Commence Battle' on the deployment screen; during the enemy and guest turns it reads 'Pause Battle', 'Next', 'Status', 'View Battlefield', 'Center on Ramza', 'Change Combat Set' (the first label alternates between 'Pause Battle' and 'Change Display' every few seconds). The 'Next' in that footer is a permanent hint, not a message page.
- V (live): Esc opens ffto_pause.uib during this phase ('Esc resumes, hold Space skips the cutscene'); closing it brings up a ffto_battle_dialog.uib screen and a notice-dialog agent with no text drawn.

## Open questions

? Why the focus, event and turn fields keep the deployment and cutscene values during the opening enemy and guest turns. ? Whether any input shortens that wait (none of the tried keys did). ? Which battles let the player choose the party before Commence.
