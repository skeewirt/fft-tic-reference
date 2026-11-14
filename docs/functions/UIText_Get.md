# UIText_Get

- **Address:** `0x1403DBE88`
- **Area:** [Data access](../areas/data.md)
- **Prototype:** `char *__fastcall UIText_Get(unsigned int id)`
- **Callers:** 27 xrefs; named: GUITextNode_SetTextById, GUITextNode_UpdateLayout, JobList_StoreCell, JobRecord_FromJobId, JobTreePanel_FillTexts, Options_ApplyBlock
- **Callees:** UITable_GetRow

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the UI text string for an id from UI table 19, or a shared empty string when the row is missing.

## Behavior

- V: row = UITable_GetRow(19, id) (table 19 = UI text).
- V: found: returns row + *(int*)(row+4) + 4 (string stored at a dword offset in the row, relative to row+4 + offset; ie. offset base is row+4).
- V: missing: returns the global empty string Str.
- V: about 27 callers (JobTreePanel_FillTexts, GUITextNode_SetTextById, GUITextNode_UpdateLayout, JobList_StoreCell, JobRecord_FromJobId, Options_ApplyBlock and many sub_ UI screens). One xref is listed as DxgkInitialize, which is an IDA mislabel of a neighbouring address (I).

## State touched

- Calls: [UITable_GetRow](UITable_GetRow.md)

## Referenced by

- Called by: [BattleMsg_ResolveEntry](BattleMsg_ResolveEntry.md), [BattleMsg_TextFromDescriptor](BattleMsg_TextFromDescriptor.md), [GUITextNode_SetTextById](GUITextNode_SetTextById.md), [GUITextNode_UpdateLayout](GUITextNode_UpdateLayout.md), [JobRecord_FromJobId](JobRecord_FromJobId.md), [JobTreePanel_FillTexts](JobTreePanel_FillTexts.md), [SaveSlot_WriteFromLive](SaveSlot_WriteFromLive.md), [SaveSlots_StoreToFile](SaveSlots_StoreToFile.md), [sub_1401560D0](sub_1401560D0.md)

## Notes

Note the row-relative offset: the field is a dword at row+4, added to row+4 (V from the expression &Row[*((int*)Row+1)+4]; this reads as row + off + 4 where off = dword at row+4, i.e. the offset is relative to row+4 only if the stored value excludes the dword itself).

## Open questions

? whether the offset is relative to row+4 or to row. ? the compression / encoding of the text itself (decode path is the caller's).
