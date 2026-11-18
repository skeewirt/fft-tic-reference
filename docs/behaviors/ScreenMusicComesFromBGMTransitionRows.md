# ScreenMusicComesFromBGMTransitionRows

- **Kind:** observed behaviour
- **Scope:** engine (music)
- **Area:** [Event system](../areas/event-system.md)
- **Affects:** [sub_1401D9174](../functions/sub_1401D9174.md), [UITitle_ShowPlayMode](../functions/UITitle_ShowPlayMode.md), [Tavern_HasNewEntries](../functions/Tavern_HasNewEntries.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Screens such as the title's play-mode page, the save and load list and the tavern start their music through sub_1401D9174 with a BGMTransition row number: the row names a SoundEnhanced row, whose Unknown10 is the music id bound to slot 1 and loaded.

## Behavior

- V (seen live): opening the save and load list from the main menu ran BGMTransition row 8 (SoundEnhanced row 190, music id 41): id 41 was bound to slot 1 and track 40 was loaded.
- V (seen live): with SoundEnhanced row 190's Unknown10 changed to 300, the same screen bound id 300 and loaded track 299 (music_00299.sab).
- V (seen live): the world map's music on a load (id 27, slot 1) does not come from SoundEnhanced row 176 (also 27): changing that row left it unchanged.

## Notes

Seen 2026-11-16 on the Steam PC build.

## Open questions

? where the world map takes its music id from.
