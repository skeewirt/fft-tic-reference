# TitleModeSelectButtons

- **Kind:** registry
- **Area:** [UI framework](../areas/ui-framework.md)
- **Resolved by:** [UILauncher_OnMenuAction](../functions/UILauncher_OnMenuAction.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The button ids of the mode select screen as `UILauncher_OnMenuAction` handles them.

## Entries

| Id | Name | Value | Conf | Meaning |
|---|---|---|---|---|
| <a id="enhanced start game"></a>110 | `Enhanced Start Game` |  | V | Starts Enhanced at once when `g_SaveManager`+890 allows it. |
| <a id="page"></a>111 | `page` |  | V | Opens a page. |
| <a id="classic start game"></a>112 | `Classic Start Game` |  | V | Starts Classic at once when `g_SaveManager`+889 allows it. |
| <a id="page"></a>113 | `page` |  | V | Opens a page. |
| <a id="quit"></a>114 | `quit` |  | V | Fades, then takes the quit path (`sub_1401D7DDC(qword_143CD9DD8, 5, 2)`; states 1 then 3). |
| <a id="button"></a>115 | `button` |  | ? | Handled; effect not read. |
| <a id="button"></a>116 | `button` |  | ? | Handled; effect not read. |

## Open questions

None recorded.
