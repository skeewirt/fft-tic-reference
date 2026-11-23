# StoryProgressEventVariable110DecidesWhichStoryBattleAWorldMapSiteLoads

- **Kind:** observed behaviour
- **Scope:** engine (story progress)
- **Area:** [Event system](../areas/event-system.md)
- **Affects:** [EventVar_Read](../functions/EventVar_Read.md), [EventVar_Write](../functions/EventVar_Write.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Event variable 110 holds the story's progress step. A save made after The Sand Rat's Sietch read 7 there; with 6 written back, walking onto Zeklaus Desert loaded The Sand Rat's Sietch again, as on the first visit.

## Behavior

- V: seen live 2026-11-22: on a Chapter 1 save made after The Sand Rat's Sietch (world-map objective 'Report back to Eagrose Castle'), event variable 110 read 7 and variable 111 read 3.
- V: seen live: with 6 written to variable 110 (EventVar_Write called on the game thread), a walk from Dorter to Zeklaus Desert loaded The Sand Rat's Sietch (entry key 386, its two deployment areas 260 / 261), title card, opening scene and deployment as on the first visit. Before the write, Ramza standing on Zeklaus Desert and A on the map gave a random encounter.
- V: seen live: the objective line on the world map kept 'Report back to Eagrose Castle' after the write and after the walk; it does not follow variable 110 at once.
- V: seen live: System Menu > Return to World Map from that battle kept variable 110 at 6, and A on the map loaded the battle again.
- I: variable 110 counts the story battles of Chapter 1 from Orbonne Monastery (The Sand Rat's Sietch is the sixth story battle and was loaded at 6); only the step before and after this one were seen.

## Notes

Seen on one save; which code compares variable 110 on arrival was not traced.

## Open questions

? the arrival check itself (which function reads variable 110 when a walk ends on a story site); ? when the objective line is rebuilt.
