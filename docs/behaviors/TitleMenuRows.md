# TitleMenuRows

- **Kind:** observed behaviour
- **Scope:** which rows the Enhanced title menu shows and how they are laid out
- **Area:** [UI framework](../areas/ui-framework.md)
- **Affects:** [TitleMenu_Build](../functions/TitleMenu_Build.md), [TitleMenu_AddEntry](../functions/TitleMenu_AddEntry.md), [UIAddonFFTOTitle](../structs/UIAddonFFTOTitle.md), [TitleMenuLayout](../formats/TitleMenuLayout.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The Enhanced title menu shows 3 to 6 rows chosen by the save state and the cleared flag; the layout file has a state for each count.

## Behavior

- I: the menu has 3 to 6 rows: 4 for a game that is not cleared with a save (New Game, Continue, Load Game, Select Version), 6 for a cleared game with a save. The add-on holds six rows and the layout file has the states Menu3 to Menu6 only.
- V: `g_UIStateFade` (0x143CD9E00) holds the fade timer (+16, the title's actions wait for it to reach 0 or less) and the requested state (+24); the title writes states 6 and 19.
- V: `g_SaveManager` (0x143CD9EE0) +888 gates New Game + and Music Player (I: game cleared); +889 / +890 let the mode select start Classic / Enhanced at once.

## Open questions

None recorded.
