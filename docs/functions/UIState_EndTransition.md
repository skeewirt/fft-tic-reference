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

## Open questions

None recorded.
