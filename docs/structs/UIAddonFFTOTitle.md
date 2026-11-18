# UIAddonFFTOTitle

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)
- **Size:** 240 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The title menu screen object (240 bytes, `Mem_Alloc(240)` in UIAddonFFTOTitle_Create): base `UIAddonMenuBase`, primary vtable 0x14070A4B0 and a second vtable 0x14070A460 at +48 (the `UIFFTOMenuFunctionBase` part). Holds up to six rows of buttons.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="widget"></a>`0x18` | widget | `GUIWidget *` | V | The bound layout (ffto_title_enhanced.uib). |
| <a id="menu_function_vtable"></a>`0x30` | menu_function_vtable | `void *` | V | Second vtable 0x14070A460 (the `UIFFTOMenuFunctionBase` part). |
| <a id="title_node"></a>`0x40` | title_node | `GUINode *` | V | The `TitleEnhanced` node. |
| <a id="rows"></a>`0x48` | rows | `TitleRow[6]` | V | Six rows of 24 bytes: +0 button node, +8 its `Title` text node, +16 kind byte (memset of 0x90 bytes at +72). |
| <a id="row_count"></a>`0xD8` | row_count | `int32` | V | Number of rows in use (3 to 6 in practice, not checked against 6). |
| <a id="current_row"></a>`0xDC` | current_row | `int32` | V | Current row, -1 for none. |
| <a id="last_input_tick"></a>`0xE0` | last_input_tick | `uint32` | I | The `g_GUICore`+2096 tick of the last input (TitleMenu_StampInput); read by TitleMenu_IdleTimeout. |
| <a id="save_exists"></a>`0xE4` | save_exists | `uint8` | V | 'A save exists': the save manager reports a save or an AUTOENHANCED file exists. |
| <a id="game_cleared"></a>`0xE5` | game_cleared | `uint8` | I | 'Game cleared': copy of the byte at `g_SaveManager`+888 (inferred from what it gates). |
| <a id="idle_armed"></a>`0xE6` | idle_armed | `uint8` | V | 1 when the idle timeout is armed. |

## Behavior

- V: read in 0x1401CB9B4, 0x1401C3EB0, 0x1401C43B4, 0x1401C4318, 0x1401C41B0 and 0x1401C34B4.
- V: the base constructor is `sub_14019CD74`; the base vtable 0x14070CDD8 is put back by UIAddonFFTOTitle_Dtor (0x1401C3E64).

## Referenced by

- Observed behaviours: [TitleMenuRowStorage](../behaviors/TitleMenuRowStorage.md), [TitleMenuRows](../behaviors/TitleMenuRows.md)

## Notes

Functions: UIAddonFFTOTitle_Create, UITitleMenu_BindNodes, TitleMenu_Build, TitleMenu_AddEntry, UIAddonFFTOTitle_OnEvent.

## Open questions

None recorded.
