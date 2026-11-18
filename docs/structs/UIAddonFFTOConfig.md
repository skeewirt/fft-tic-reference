# UIAddonFFTOConfig

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)
- **Size:** 3416 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The General Options screen object (3416 bytes, `Mem_Alloc(3416)` in 0x140182478): base `UIAddonMenuBase`, vtable 0x14070DB30 with 18 entries (RTTI locator at 0x14070DB28).

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="addon_id"></a>`0x8` | addon_id | `int32` | V | The add-on id (listener id). |
| <a id="agent"></a>`0x10` | agent | `UIAgent *` | V | The owning agent. |
| <a id="widget"></a>`0x18` | widget | `GUIWidget *` | V | The bound layout. |
| <a id="sub_state"></a>`0x30` | sub_state | `int32` | V | 0 the list, 1 / 2 / 3 a confirm of its own is open, 4..6 a display change being applied, 7 waiting for a key, 8 / 9 a queued dialog. |
| <a id="mode"></a>`0x34` | mode | `uint8` | V | 1 = the mode select's General Options (tabs of ConfigCategory 11, 8, 10, 9; header UI text 2209 'General Options'; help text from ConfigItem +64); 0 = in game (categories 5, 3, 4, 0, 2, 1; header 2613 'Settings'; help text from ConfigItem +68). |
| <a id="changed_a"></a>`0x37` | changed_a | `uint8` | V | Changes not yet applied (with +56). |
| <a id="changed_b"></a>`0x38` | changed_b | `uint8` | V | Changes not yet applied (with +55). |
| <a id="restart_after_display_change"></a>`0x39` | restart_after_display_change | `uint8` | V | With it set the on-close handler restarts the boot sequence. |
| <a id="shown"></a>`0x3B` | shown | `uint8` | V | Set by the shown handler. |
| <a id="current_tab"></a>`0x54` | current_tab | `int32` | V | Current tab. |
| <a id="tab_count"></a>`0x58` | tab_count | `int32` | V | Tab count. |
| <a id="tab_categories"></a>`0x5C` | tab_categories | `int32[16]` | V | The tabs' ConfigCategory ids (up to +156). |
| <a id="row_count"></a>`0x9C` | row_count | `int32` | V | Row count of the current tab. |
| <a id="row_items"></a>`0xA0` | row_items | `int32[61]` | V | The rows' ConfigItem ids (61 slots, up to +404). |
| <a id="values"></a>`0x194` | values | `int32[61]` | V | The shown value per ConfigItem id. |
| <a id="game_values"></a>`0x288` | game_values | `int32[61]` | V | The game settings' values per id, refreshed every frame and compared with +404 to redraw rows changed elsewhere. |
| <a id="lb_rb_icons"></a>`0x570` | lb_rb_icons | `gadget` | V | The LB / RB icon gadgets (to +1568 and on). |
| <a id="row_list"></a>`0x6D0` | row_list | `UIListGadget` | V | The row list gadget (+1768 its list component, +1840 its cursor row). |
| <a id="value_list"></a>`0x818` | value_list | `SelectList gadget` | V | The value list gadget; +2192 it is open. |
| <a id="confirm_window"></a>`0x960` | confirm_window | `UIGadgetFFTOConfigConfirmWindow` | V | The confirm window gadget. |
| <a id="main_tab"></a>`0xB20` | main_tab | `MainTab gadget` | V | The MainTab gadget; +2880 the header text node, +2888 the sub-header node. |
| <a id="tab_buttons"></a>`0xBE0` | tab_buttons | `node[]` | V | The tab button nodes. |

## Behavior

- V: vtable entries: 0 deleting destructor 0x1401886CC (destructor body 0x140188700); 2 node event handler 0x14018A344; 3 may take input 0x1401D21D8; 4 node binding 0x140188878; 5 on close 0x140188FA4; 7 shown 0x14018A31C; 9 hidden 0x14018A33C (focus cleared); 12 input 0x1401892A8; 13 the rows' texts again 0x1401890E0; 14 per-frame update 0x140189D54.
- V: read in the constructor, 0x140188878, 0x14018EA74, 0x140189D54 and 0x1401892A8.

## Notes

Functions: UIAddonFFTOConfig_OnEvent, UIAddonFFTOConfig_OnInput, ConfigMenu_ShowTab.

## Open questions

None recorded.
