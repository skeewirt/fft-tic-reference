# WorldMapBaseList_OnEvent

- **Address:** `0x14016029C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char WorldMapBaseList_OnEvent(_BYTE *self, _DWORD *node, _DWORD *event)`
- **Callers:** vtable 0x14070F5C8 slot 2
- **Callees:** UIAddon_OnEventBase, GUIComponentList_GetItemComponent, WorldMapBaseList_RecordAt, WorldMapBaseList_DrawRow, WorldMapLocationPanel_Fill, sub_1400F4BCC

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Vtable slot 2 of the Locations list addon (struct WorldMapBaseList): draws rows, fills the info panel when the cursor moves and tracks the hover flags.

## Behavior

- V: runs UIAddon_OnEventBase first.
- V: event 4: copies the hover byte +1854 to +1853 and clears +1854; event 0x1C: sets +1854 when the item under event[1] is a list button (kind 10).
- V: event 0x1E (draw a row): item = GUIComponentList_GetItemComponent(node, event[1]); for a list button, the data index is item +648 and WorldMapBaseList_DrawRow draws WorldMapBaseList_RecordAt(index).
- V: event 32 (the cursor moved to a list button node; index node +648): WorldMapLocationPanel_Fill with that record, then cue 0x5B when +1852 is set and neither busy byte is.

## State touched

- Calls: [UIAddon_OnEventBase](UIAddon_OnEventBase.md), [GUIComponentList_GetItemComponent](GUIComponentList_GetItemComponent.md), [WorldMapBaseList_RecordAt](WorldMapBaseList_RecordAt.md), [WorldMapBaseList_DrawRow](WorldMapBaseList_DrawRow.md), [WorldMapLocationPanel_Fill](WorldMapLocationPanel_Fill.md), [sub_1400F4BCC](sub_1400F4BCC.md)

## Open questions

None recorded.
