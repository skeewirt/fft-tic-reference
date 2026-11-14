# UITable_GetRow

- **Address:** `0x1403DBD60`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char *UITable_GetRow(int tableId, unsigned int row)`
- **Callers:** GUITextNode_Layout, GUITextNode_SetRenderScale
- **Callees:** sub_1403D325C, sub_1403D3A10, sub_1403D3BE4

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the in-memory row of an nxd table by table id and row index (null when the table or row is missing).

## Behavior

- V: tables live under qword_143CD9CD0; id 27 is used for the UIFontType rows by GUITextNode_Layout (V, GUITextNode_Layout / GUITextNode_FinishLine: the row dwords are Unknown8 (+8, the baseline term), UnknownC (+12, the per-glyph multiplier), Unknown10 (+16, its alternative when GUIFontTable+40 is set) and Unknown14 (+20, the size multiplier)).
- V: the registry it searches through NxdRegistry_Find is the table list built from root.nxl by NxdRegistry_LoadRootNxl; the table state must be 2 or 3 (loaded) or the call returns null.

## Referenced by

- Called by: [EventSubquestPanel_Run](EventSubquestPanel_Run.md), [GUIFontTable_Load](GUIFontTable_Load.md), [GUITextNode_Draw](GUITextNode_Draw.md), [GUITextNode_FinishLine](GUITextNode_FinishLine.md), [GUITextNode_HandleTag](GUITextNode_HandleTag.md), [GUITextNode_PlaceIcon](GUITextNode_PlaceIcon.md), [Input_UpdateActionRow](Input_UpdateActionRow.md), [UIText_Get](UIText_Get.md), [sub_1400F69BC](sub_1400F69BC.md)

## Notes

sub_1403DBC74 is the keyed variant used by the job tree (table 0xBD = job-need rows).

Registry details (hash map, table object layout, 246 tables) are on the NxdRegistry_LoadRootNxl and NxdRegistry_Find pages.

## Open questions

None recorded.
