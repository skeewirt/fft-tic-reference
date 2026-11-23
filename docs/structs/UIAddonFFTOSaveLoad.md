# UIAddonFFTOSaveLoad

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)
- **Size:** 1240 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The save/load screen's list add-on (1240 bytes, allocated in agent state 3 and constructed by `sub_140184C38` at 0x140184C38): a `UIAddonMenuBase` at +0 with a second `UIFFTOMenuFunctionBase` vtable at +48. It binds the list layout, keeps three vectors of pointers to 240-byte rows (all rows, auto rows and the visible rows), and owns the preview registration map and the helper widgets.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="vtable"></a>0x00 | vtable | `void *` | V | Primary vtable 0x14070DCE8. The base constructor `sub_14019CD74` runs first; the destructor puts the base vtables back. |
| <a id="menu_function_vtable"></a>0x30 | menu_function_vtable | `void *` | V | Second vtable 0x14070DC98 at +48 (the `UIFFTOMenuFunctionBase` part). The item fill, selection and page virtuals are reached through it. |
| <a id="widget"></a>0x40 | widget | `GUINode *` | V | The bound layout root, cached by `UIAddonFFTOSaveLoad_vfunc_4` from the first kind-1 component. `SaveLoadList_Refresh` looks the `ShowTextNone` state up on it. |
| <a id="header_node"></a>0x48 | header_node | `GUINode *` | V | The `Header` descendant, bound only when the tab at +432 is 1. Holds the filter buttons and the two page arrows. |
| <a id="filter_buttons"></a>0x50 | filter_buttons | `GUINode *[3]` | V | `TabButtonHeader00..02` at +80/+88/+96. `UIAddonFFTOSaveLoad_vfunc_4` gives them text ids 2561..2563, `UIAddonFFTOSaveLoad_vfunc_2` maps a click on one to +436, and `SaveLoadList_Refresh` applies the selected or normal state. |
| <a id="list_gadget"></a>0x68 | list_gadget | `UIListGadget` | V | The row list at +104, 328 bytes up to the tab field. Bound to the `SaveLoadList` node with part `data_list`; its cursor row is +96 inside the gadget (add-on +200). Used by `SaveLoadList_Refresh`, `sub_140187678` and the input virtual. |
| <a id="tab"></a>0x1B0 | tab | `int32` | V | V: main tab index, written by agent state 4 (`sub_1401838F0`) from the agent mode bits and read by `SaveLoadList_BuildEntries`, `SaveLoadList_Refresh`, `UIAddonFFTOSaveLoad_vfunc_4` and the input virtual. I: 0 is the save list, 1 the load list and 2 the New Game + source list (rests on the three open modes and on the selection handler's save branch on tab 0). |
| <a id="filter"></a>0x1B4 | filter | `int32` | V | Auto/manual filter: -1 = off, 0 = all rows, 1 = auto rows only, 2 = manual rows only. `SaveLoadList_Refresh` sets 0 on tab 1 and -1 elsewhere; the filter buttons (`UIAddonFFTOSaveLoad_vfunc_2`) and the input virtual's left/right paging set 0..2; `sub_140187678` applies it when it rebuilds the visible rows. |
| <a id="rows_allocator"></a>0x1B8 | rows_allocator | `void *` | V | Allocator for vector A. Set by the constructor, used when `SaveLoadList_BuildEntries` grows the pointer array. |
| <a id="rows_begin"></a>0x1C0 | rows_begin | `void **` | V | Vector A begin: every row `SaveLoadList_BuildEntries` builds (the tab-0 blank row, the tab-1 copies of vector B, and the manual rows). |
| <a id="rows_end"></a>0x1C8 | rows_end | `void **` | V | Vector A end. `sub_140186240` frees each row and moves this back to the begin pointer at the start of every rebuild. |
| <a id="rows_capacity"></a>0x1D0 | rows_capacity | `void **` | V | Vector A capacity. |
| <a id="auto_allocator"></a>0x1D8 | auto_allocator | `void *` | V | Allocator for vector B. Set by the constructor. |
| <a id="auto_begin"></a>0x1E0 | auto_begin | `void **` | V | Vector B begin: the auto rows `SaveLoadList_BuildAutoEntries` builds from the five resume descriptors. |
| <a id="auto_end"></a>0x1E8 | auto_end | `void **` | V | Vector B end. `SaveLoadList_ClearAutoEntries` frees each row and moves this back to the begin pointer. |
| <a id="auto_capacity"></a>0x1F0 | auto_capacity | `void **` | V | Vector B capacity. |
| <a id="visible_allocator"></a>0x1F8 | visible_allocator | `void *` | V | Allocator for vector C, the visible rows. Set by the constructor. |
| <a id="visible_begin"></a>0x200 | visible_begin | `void **` | V | Vector C begin: the rows currently shown to the player, rebuilt by `sub_140187678` from vector A through the +436 filter. The item callback, the selection virtual, the input guide and `SaveLoadList_Refresh`'s tail read it; it holds the same row pointers as vector A and does not own them. |
| <a id="visible_end"></a>0x208 | visible_end | `void **` | V | Vector C end. `sub_140186240` empties it at the start of every rebuild. |
| <a id="visible_capacity"></a>0x210 | visible_capacity | `void **` | V | Vector C capacity. |
| <a id="preview_map_allocator"></a>0x218 | preview_map_allocator | `void *` | V | First part of the map object at +536 (allocator). |
| <a id="preview_map_head"></a>0x220 | preview_map_head | `void *` | V | Head node of the map at +544. It maps each 32-byte preview record pointer to the value `SaveLoadList_FillItem` stores for it while registering the record. `sub_1401862BC` erases the node and `sub_140187678` clears the map. |
| <a id="preview_map_size"></a>0x228 | preview_map_size | `uint64` | V | Number of nodes in the preview map. |
| <a id="unknown_560"></a>0x230 | unknown_560 | `int32` | ? | Zeroed by the constructor and by the hide virtual (`0x140185404`); no other read or write was found in the list functions. |
| <a id="row_text_helper_a"></a>0x238 | row_text_helper_a | `uint8[104]` | V | 104-byte helper constructed by `sub_14028F46C` and destroyed by `sub_14028F528`. `SaveLoadList_FillItem` uses it for row text formatting. |
| <a id="row_text_helper_b"></a>0x2A0 | row_text_helper_b | `uint8[104]` | V | Second 104-byte helper of the same kind; used by `SaveLoadList_FillItem`. |
| <a id="row_text_helper_c"></a>0x308 | row_text_helper_c | `uint8[104]` | V | Third 104-byte helper of the same kind; used by `SaveLoadList_FillItem`. |
| <a id="page_left_button"></a>0x370 | page_left_button | `uint8[176]` | V | 176-byte icon-button helper constructed by `sub_14028BB54`; bound to the header's `PushLeft` node with icon 253, stepped by the input virtual when paging left. |
| <a id="page_right_button"></a>0x420 | page_right_button | `uint8[176]` | V | 176-byte icon-button helper of the same kind; bound to `PushRight` with icon 254, stepped by the input virtual when paging right. |
| <a id="hint_held"></a>0x4D0 | hint_held | `uint8` | V | Set by the input virtual while the guide/hint input is held and cleared when it is released; it locks the list input for the duration. Low byte of the word the constructor zeroes. |
| <a id="active_flag"></a>0x4D1 | active_flag | `uint8` | V | V: set to 1 by agent state 4 (seen in the code read here); I: states 6, 7, 9 and 10 also set it, when the list or a prompt is up, and cleared on exit. I: it marks the screen as active (rests on the set/clear pattern). No reader was found in the list functions, so the consumer is unknown. |

## Behavior

- V: the constructor `sub_140184C38` stores both vtables, zeroes the widget, the header node and the three filter buttons, constructs the gadget at +104, sets tab 0 and filter -1, sets all three vectors empty with the same allocator, builds the 48-byte map sentinel, constructs the five helper subobjects and zeroes the word at +1232.
- V: the destructor `sub_140184DB0` releases vector A's rows (`sub_140186240`), vector B's rows (`SaveLoadList_ClearAutoEntries`), the map (`sub_1401C896C`), the three 104-byte helpers, the two 176-byte helpers and the map object, then frees vector C's storage, vector B's storage and vector A's storage, and finally destroys the gadget at +104.
- V: `SaveLoadList_BuildEntries` owns vector A, `SaveLoadList_BuildAutoEntries` owns vector B, `sub_140187678` owns vector C and `SaveLoadList_Refresh` owns the presentation; `SaveLoadList_FillItem` is the row callback and indexes vector C.
- I: the three vectors are three layers of one list: B holds the auto rows, A holds every row the current tab can show (built from B and from the cache), and C holds the subset the player is shown after the +436 filter (rests on the three builders and on the item callback indexing C).
- V: the add-on does not own the 50-slot save image; the list rows are copies. The cache and the manager image are described by the `SaveManager` structure and the `g_SaveSlotCache` global.

## Referenced by

- Read by: [SaveLoadList_ClearAutoEntries](../functions/SaveLoadList_ClearAutoEntries.md), [SaveLoadList_Refresh](../functions/SaveLoadList_Refresh.md)
- Written by: [SaveLoadList_BuildAutoEntries](../functions/SaveLoadList_BuildAutoEntries.md), [SaveLoadList_ClearAutoEntries](../functions/SaveLoadList_ClearAutoEntries.md), [SaveLoadList_Refresh](../functions/SaveLoadList_Refresh.md)

## Notes

Read: the constructor `sub_140184C38`, the destructor `sub_140184DB0`, the add-on virtuals 2/4/12, `SaveLoadList_BuildEntries`, `SaveLoadList_BuildAutoEntries`, `SaveLoadList_Refresh`, `SaveLoadList_ClearAutoEntries` and `SaveLoadList_FillItem`. The field sizes are bounded by the next field or by the constructor's writes. Addresses are build-specific.

## Open questions

? what the +560 dword counts; ? who reads +1233; ? what the render handle stored per preview record refers to; ? whether the three 104-byte helpers have distinct roles beyond row text.
