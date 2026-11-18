# PlaceNameOfABattleComesFromTheMapRowOfTheLoadedId

- **Kind:** observed behaviour
- **Scope:** engine (battle title card, pause menu, save list)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [SaveHeader_FillBattleFields](../functions/SaveHeader_FillBattleFields.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The title card, the objective header of the pause menu and the place label of the save list all show the place name belonging to the loaded map id's Map row, and a mid-battle autosave resumes the battle on the saved id.

## Behavior

- V (seen live, id 120 with a Map row equal to map 84's): the title card read 'Balias Tor' (map 84's name); the pause menu's objective header read 'Balias Tor' above 'Defeat all enemies!'; the save list labelled the Pre-battle and Mid-battle autosaves 'Balias Tor'.
- V (seen live): after loading the Mid-battle autosave the battle resumed on the same terrain with the saved unit whose turn it was (slot 17 of the party), the word at 0x140D4012C read 0x78 (120), and the pause menu was usable.
- V (seen live): a pause-menu 'Return to World Map' after the resume went to the world map normally; a victory returns to the world map after the victory page and the closing balloons.

## Open questions

None recorded.
