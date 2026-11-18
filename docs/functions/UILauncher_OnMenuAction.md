# UILauncher_OnMenuAction

- **Address:** `0x1401B924C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UILauncher_OnMenuAction(UIAgent *agent, int button)`
- **Callers:** not recorded
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The mode select screen's button handler.

## Behavior

- V: buttons 110 (Enhanced Start Game) and 112 (Classic Start Game) start a mode at once when the flags at `g_SaveManager`+890 / +889 allow it; 111 and 113 open pages; 114 fades and then takes the quit path (`sub_1401D7DDC(qword_143CD9DD8, 5, 2)`, states 1 then 3); 115 and 116 are further buttons.

## Referenced by

- Resolves registries: [TitleModeSelectButtons](../registries/TitleModeSelectButtons.md)

## Notes

Registry: TitleModeSelectButtons.

## Open questions

None recorded.
