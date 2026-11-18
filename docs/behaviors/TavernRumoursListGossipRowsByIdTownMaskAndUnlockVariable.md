# TavernRumoursListGossipRowsByIdTownMaskAndUnlockVariable

- **Kind:** observed behaviour
- **Scope:** engine (tavern rumours)
- **Area:** [Event system](../areas/event-system.md)
- **Affects:** [TavernRumours_BuildList](../functions/TavernRumours_BuildList.md), [TavernRumour_IsAvailable](../functions/TavernRumour_IsAvailable.md), [g_RumourTownMasks](../globals/g_RumourTownMasks.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The tavern's Rumors list holds the nxd Gossip rows whose ids pass an availability test: ids 0..63 are walked; an id is listed when its Gossip row exists, its condition is met, and either its Gossip flag is set or the town's bit is set in a 64-entry mask table and event variable 721 + id is nonzero.

## Behavior

- V: the builder's loop bound is 64, the mask table holds 64 entries, the unlock variables are 721..784.
- V: the list entry is the Gossip key (a dword), so the widget reads the row's title and text by the full id.
- V: each listed id also takes a slot of the shared list of the tavern pages (g_ErrandBoardList, 128 words in this build), so at most that many rumours can be listed at once.
- V (seen live): stock Gossip has 23 rows; in Gariland early in Chapter 1 three were listed (ids 0, 1, 2).

## Notes

The replayable story event list (EventViewer_BuildList) is a different list: neither the tavern's Rumors nor the main menu's Chronicle > Events calls it.

## Open questions

? the town numbering behind the mask bits (15 bits for the settlements).
