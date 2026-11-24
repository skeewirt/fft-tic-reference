# WorldMapBaseList

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)
- **Size:** 1856 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The Locations list addon of the world map (X on the map): addon +80 of the world map agent, made once by WorldMapAgent_CreateAddons from UI addon row 133. Seen live, its three tabs read Settlements / Battlegrounds / Miscellaneous.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="vtable"></a>`0x0` | vtable | `void*` | V | 0x14070F5C8: slot 0 WorldMapBaseList_DeletingDestruct, 2 WorldMapBaseList_OnEvent, 3 WorldMapBaseList_CanTakeInput, 4 WorldMapLocationPanel_Init (binds the nodes), 25 WorldMapBaseList_ClearRecords. |
| <a id="widget"></a>`0x18` | widget | `void*` | V | The addon's widget. |
| <a id="busy_a"></a>`0x2A` | busy_a | `u8` | V | Nonzero blocks input (CanTakeInput) and the cursor sound. |
| <a id="busy_b"></a>`0x2B` | busy_b | `u8` | V | As +42. |
| <a id="vtable2"></a>`0x30` | vtable2 | `void*` | V | Second base, vtable 0x14070F578. |
| <a id="base_info"></a>`0x158` | base_info | `node*` | V | The BaseInfo node; plays its 'TownInfo' / 'FieldInfo' states (SelectTab). |
| <a id="list_node"></a>`0x160` | list_node | `node*` | V | The inner list node; plays 'Default' / 'NoItem' by the record count. |
| <a id="tab_labels"></a>`0x168` | tab_labels | `node*[3]` | V | The three tab label components selected by SelectTab. |
| <a id="town_info"></a>`0x180` | town_info | `node*` | V | The TownInfo panel (tab 0). |
| <a id="field_info"></a>`0x2C8` | field_info | `node*` | V | The FieldInfo panel (tab 2). |
| <a id="list_gadget"></a>`0x2D0` | list_gadget | `UIListGadget` | V | The list gadget; +744 its list component (+648 = row count), +816 the cursor. |
| <a id="guide_l"></a>`0x418` | guide_l | `part` | V | Button guide part (left). |
| <a id="guide_r"></a>`0x4C8` | guide_r | `part` | V | Button guide part (right). |
| <a id="radio_menu"></a>`0x578` | radio_menu | `UIGadgetFFTORadioButtonMenu` | V | The tab bar's radio menu (mouse clicks). |
| <a id="records"></a>`0x6A0` | records | `vector[3]` | V | One vector of 64-byte location records per tab t at +1696 + 32 t (allocator +0, begin +8, end +16). Record: +51 marker (3 Next, 2 midway point), +52 location id, +62 facility flag, +63 current-location flag. |
| <a id="unknown_1792"></a>`0x700` | unknown_1792 | `qword[6]` | ? | Six qwords +1792..+1832, only cleared at construction in the code read. |
| <a id="tab"></a>`0x730` | tab | `i32` | V | Current tab; -1 at construction, above 2 = none. Seen live: 0xFFFFFFFF before the first open, then the opening tab. |
| <a id="location"></a>`0x734` | location | `i32` | V | Current location; the cursor opens on its record. |
| <a id="unknown_1848"></a>`0x738` | unknown_1848 | `i32` | ? | Only set to -1 at construction in the code read. |
| <a id="row_sound"></a>`0x73C` | row_sound | `u8` | V | Play cue 0x5B when the cursor moves; off while SelectTab moves the cursor. |
| <a id="hover_prev"></a>`0x73D` | hover_prev | `u8` | V | Hover flag copied at event 4. |
| <a id="hover"></a>`0x73E` | hover | `u8` | V | Set at event 0x1C on a list button. |

## Behavior

- V (seen live): the row count read at the list component (+744, +648) was 3 on Battlegrounds with 9 visible slots (gadget +1036); Down on the last row wraps to row 0.

## Open questions

None recorded.
