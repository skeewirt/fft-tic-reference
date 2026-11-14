# TabBar_SetTable

- **Address:** `0x1402A9730`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 TabBar_SetTable(TabBar *t, unsigned int tableKey)`
- **Callers:** sub_14012FC6C, sub_1402A9540
- **Callees:** UITable_GetRowByKey, UIName_Key, GUINode_FindPartByName, Str_Format, GUINode_FindState, GUINode_PlayState, GUINode_StopState, sub_1403D8D1C, sub_1402A9944

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sets up a row of up to four tab / button nodes from a row of UI table 139: one title text id per tab, the count and a 'focusable' byte; then picks the layout state ButtonNN for the count and selects tab 0.

## Behavior

- V: does the set-up only when the key differs from the stored dword at t+416: t+416 = key, t+424 = 0 (count).
- V: row = UITable_GetRowByKey(0x8B (139), key). count = row byte +12 when the row dword +12 is below 4, else 4; the u32 title ids are at row + *(int)(row+8) + 4*i. For i < count (stops early on a 0 id or a missing node): the tab node t+24+8*i is searched for a part named 'Title' (GUINode_FindPartByName on node+272); if it is kind 3 (text) its text id (+248) is set to the row id and its dirty byte (+316) set; t+424 += 1. t+425 = row byte +16.
- V: when the node t+16 (the bar root) exists and count > 1: for n = 2..count the state 'Button%02u' on t+16 is PLAYED for n == count and STOPPED for the others (the layout of the bar for that number of tabs).
- V: finishes with a tail call sub_1402A9944(t, 0): select tab 0 (done every call, also when the key was unchanged).

## State touched

- Calls: [UITable_GetRowByKey](UITable_GetRowByKey.md), [UIName_Key](UIName_Key.md), [GUINode_FindPartByName](GUINode_FindPartByName.md), [Str_Format](Str_Format.md), [GUINode_FindState](GUINode_FindState.md), [GUINode_PlayState](GUINode_PlayState.md), [GUINode_StopState](GUINode_StopState.md)
- Reads: [g_UINameTable](../globals/g_UINameTable.md)

## Referenced by

- Called by: [JobChangeAddon_SetState](JobChangeAddon_SetState.md)

## Notes

Name proposed (IDB: sub_1402A9730). I: the table is the tab-title table of the job-change window (the labels of the four tabs); not checked against the nxd table 139 data.

## Open questions

? the nxd table 139 columns (row +8 offset, +12 count, +16 byte). ? meaning of the byte at +425 (see TabBar_Select).
