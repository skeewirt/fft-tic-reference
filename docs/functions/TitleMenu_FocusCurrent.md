# TitleMenu_FocusCurrent

- **Address:** `0x1401C4318`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void TitleMenu_FocusCurrent(UIAddonFFTOTitle *addon)`
- **Callers:** not recorded
- **Callees:** GUICore_FocusNode

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Focuses the current row; with none, the first row of kind 2 (Continue) when a save exists, else of kind 0 (New Game).

## Behavior

- V: vtable slot 18; the default row is chosen by kind, as `TitleMenu_SelectKind` does.
- V: acts only when the widget is shown (+74) and the add-on is not showing (+42 == 0); with current < 0 it takes the first row of kind 2 (Continue) when +228 is set, else of kind 0 (New Game), stores it (or -1); then widget +616 = 1 (the focus sound is skipped once: event 19) and `GUICore_FocusNode(button)`, or `GUICore_FocusNode(0)` when there is no row.

## State touched

- Calls: [GUICore_FocusNode](GUICore_FocusNode.md)

## Referenced by

- Observed behaviours: [TitleMenuRowStorage](../behaviors/TitleMenuRowStorage.md)

## Open questions

None recorded.
