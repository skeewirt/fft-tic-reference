# TitleAndSaveListScreens

- **Kind:** observed behaviour
- **Scope:** title screens, Continue / Load Game save list
- **Area:** [UI framework](../areas/ui-framework.md)
- **Affects:** [GUICore_GetFocus](../functions/GUICore_GetFocus.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The screens between launch and a loaded game, the keys they take, and how the save list is built, as seen live.

## Behavior

- V (live, 2026-11-05): after a launch the first focused screen is ffto_title_mode_select.uib (Enhanced / Classic); A on Start Game leads to the opening narration screens with no focused widget; the title menu (ffto_title_enhanced.uib: New Game, Continue, Load Game, Select Version, 50 px apart) appears by itself after about 33 s.
- V (live): the title takes the keyboard without a pad-mode switch: Space skips the narration (scene becomes title), Enter then shows the menu within about 3 s.
- V (live): the cursor starts on New Game (glove y 866; Continue 917, Load Game 965); Enter on New Game starts the first battle directly (no cutscene was seen).
- V (live): Continue and Load Game both open ffto_system_saveload.uib. Each entry shows Auto or the slot number, a timestamp, the map, a place label (Pre-battle, Mid-battle, World Map), level, difficulty and chapter. Tabs: Manual Saves, Autosaves, All (default).
- V (live): the list draws a window of five entries over a longer list (15 here: 10 manual, 5 auto) and scrolls; UP from the top wraps to the bottom; entries are 206 px apart. The list ignores input for about 2 s while it fades in, and fills in over a few reads (one entry first).
- V (live): manual saves are the slots 1 to 10 and never rotate; autosaves rotate and world map activity (entering a settlement, leaving a shop) writes new ones, pushing Mid-battle autosaves out; a Pre-battle autosave of 11-03 stayed through all runs.
- V (live, 2026-11-05): on the mode select screen the keyboard Enter on Start Game acts at once; the pad A is swallowed by the pad-mode switch (the first pad press only switches the input mode), so a pad press there costs a resend of about 5 s. The narration after it has no focused widget and reports a cinematic agent with skip allowed 0, but it IS skippable: Space then Enter skips it (the skip flag says nothing about keys). A key sent during the intro can be lost, so the press is repeated and varied by watching whether the state changed.
- V (live, watched with a state-change feed): Esc on the save list returns to the title menu with the glove still on Continue (y 916). For under a second the focus is empty, which looks like the narration but is not; an input sent then (Space + Enter) pressed Continue again and reopened the list. The game also falls back to the narration by itself after the menu has idled for about 40 s.
- V (live): E (keyboard) switches the save list tabs; after a switch the list refills over several reads, and a read taken right after the key can still show the old tab (wait for three equal reads).

## Notes

The opening logo videos were not observed.

## Open questions

? The opening videos and whether a key skips them. ? What Classic mode shows.
