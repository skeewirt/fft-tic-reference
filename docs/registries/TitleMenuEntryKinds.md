# TitleMenuEntryKinds

- **Kind:** registry
- **Area:** [UI framework](../areas/ui-framework.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The six kinds of row of the Enhanced title menu: the kind byte stored in each row, the text id of its label (UI table, nxd id 19) and what choosing it does.

## Entries

| Id | Name | Value | Conf | Meaning |
|---|---|---|---|---|
| <a id="newgame"></a>0 | `NewGame` | `2215` | V | New Game. Always listed. Choosing it starts UI state 19 and agent state 2 (the play mode screen). |
| <a id="newgameplus"></a>1 | `NewGamePlus` | `2226` | V | New Game +. Listed when the game is cleared. Fade, agent state 0x201, only with no save request pending. |
| <a id="continue"></a>2 | `Continue` | `2223` | V | Continue. Listed when a save exists. UITitle_StartContinue. |
| <a id="loadgame"></a>3 | `LoadGame` | `2218` | V | Load Game. Always listed. UITitle_StartLoadGame. |
| <a id="musicplayer"></a>4 | `MusicPlayer` | `2224` | V | Music Player. Listed when the game is cleared. Fade, agent state 0x501. |
| <a id="selectversion"></a>5 | `SelectVersion` | `2217` | V | Select Version. Always listed. Fade, agent state 0x601. |

## Behavior

- V: any other kind byte gives text id 0 and `UITitle_OnMenuAction` does nothing for it.
- V: the strings were read in the stock English UI table.

## Notes

Written by TitleMenu_AddEntry, chosen by UITitle_OnMenuAction.

## Open questions

None recorded.
