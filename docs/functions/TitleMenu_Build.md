# TitleMenu_Build

- **Address:** `0x1401C34B4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void TitleMenu_Build(UIAgentFFTOTitle *agent)`
- **Callers:** UITitle_ShowMenu, UIAgentFFTOTitle_Update, UIAgentFFTOTitle_OnAddonEvent (twice), 0x1401C3494
- **Callees:** TitleMenu_AddEntry, TitleMenu_SelectKind, Str_Format, GUINode_ApplyStateAtFrame, sub_1400366B0

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills the title menu's rows according to the save state and the cleared flag, plays the matching layout state and shows the menu with the cursor on the row the agent asks for.

## Behavior

- V: count = 0. The flag 'a save exists' is true when the save manager reports a save or an `AUTOENHANCED` file exists; 'game cleared' is the byte at `g_SaveManager`+888.
- V: adds kind 0 (New Game) always, kind 1 (New Game +) if the game is cleared, kind 2 (Continue) if a save exists, kind 3 (Load Game) always, kind 4 (Music Player) if cleared, kind 5 (Select Version) always, each through `TitleMenu_AddEntry`.
- V: the six calls of `TitleMenu_AddEntry` are at 0x1401C3555 (kind 0), 0x1401C3564 (1), 0x1401C3573 (2), 0x1401C357D (3), 0x1401C358C (4) and 0x1401C3596 (5, the last).
- V: then plays the layout state `Menu<count>` (`Str_Format("Menu%d")`, `GUINode_ApplyStateAtFrame` on the TitleEnhanced node), arms the idle timeout (+230 = 1, +224 = now) and shows the add-on.
- V: puts the cursor back by the agent's byte +90 (1 selects kind 0, 2 selects kind 1, 3 selects kind 3, 5 selects kind 4, through `TitleMenu_SelectKind`) and shows the hand cursor.
- I: the menu has 3 to 6 rows: 4 for a game that is not cleared and has a save (New Game, Continue, Load Game, Select Version), 6 for a cleared game with a save. The add-on holds six rows and the layout file has the states Menu3 to Menu6 only.
- V: the add-on fields at +216 and above (count +216, current row +220, last input tick +224, flags +228 / +229 / +230) are read or written at 32 instructions in the title code: TitleMenu_Build (6), TitleMenu_AddEntry (2), TitleMenu_FocusCurrent (6), TitleMenu_SelectKind (2), TitleMenu_IdleTimeout (3), TitleMenu_StampInput (1), 0x1401C410C (1), UIAddonFFTOTitle_OnEvent (2), UITitleMenu_BindNodes (1), UIAddonFFTOTitle_Create (6), TitleMenu_MoveCursor (2, through the +48 part at its +168 / +172); none reads or writes +231..+239; 0x1401C410C is another function of the title code that touches these fields, not a callee of Build.
- V: the AddEntry calls are at 0x1401C3555 (New Game), 0x1401C3564 (New Game +), 0x1401C3573 (Continue), 0x1401C357D (Load Game), 0x1401C358C (Music Player), 0x1401C3596 (Select Version); `[g_SaveManager]` +888 is read by a byte load of +0x378 at 0x1401C3539.
- V: it does not reset the current row (+220); it focuses it through slot 18 before showing the add-on, arms the idle timeout, ends the UI fade state (UIState_EndTransition) and shows the hand cursor; it is the title agent's way back to its menu (from its sink on event 65537 and after the other title screens) and ends with the guide bar hidden.

## State touched

- Calls: [TitleMenu_AddEntry](TitleMenu_AddEntry.md), [TitleMenu_SelectKind](TitleMenu_SelectKind.md), [Str_Format](Str_Format.md), [GUINode_ApplyStateAtFrame](GUINode_ApplyStateAtFrame.md), [sub_1400366B0](sub_1400366B0.md)

## Referenced by

- Called by: [UIAgentFFTOTitle_OnAddonEvent](UIAgentFFTOTitle_OnAddonEvent.md), [UIAgentFFTOTitle_Update](UIAgentFFTOTitle_Update.md), [UITitle_ShowMenu](UITitle_ShowMenu.md)
- Observed behaviours: [TitleMenuRowStorage](../behaviors/TitleMenuRowStorage.md), [TitleMenuRows](../behaviors/TitleMenuRows.md)
- Reads file formats: [TitleMenuLayout](../formats/TitleMenuLayout.md)

## Notes

This name replaces an earlier one (`sub_1401C34B4`, a sheet that described it as a save list builder); the save probe it makes (`sub_1400366B0`) only decides whether Continue is offered. 'Game cleared' is an inference from what the byte gates (New Game +, Music Player).

## Open questions

? how the byte at `g_SaveManager`+888 gets set (only its readers were read).
