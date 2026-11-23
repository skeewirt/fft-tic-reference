# UIState_EndTransition

- **Address:** `0x1401DDA5C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UIState_EndTransition(int state)`
- **Callers:** TitleMenu_Build
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Ends the UI fade state given (fade +24 = 0).

## Behavior

- I: used by TitleMenu_Build after the menu is shown.

## Referenced by

- Called by: [Boot_Update](Boot_Update.md), [OpeningScene_Start](OpeningScene_Start.md), [OpeningTask_10](OpeningTask_10.md), [TitleScene_Task](TitleScene_Task.md), [TitleScene_Update](TitleScene_Update.md), [UISaveLoad_StateEnter](UISaveLoad_StateEnter.md)

## Open questions

None recorded.
